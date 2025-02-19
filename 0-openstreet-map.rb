# frozen_string_literal: true

require 'langchain'
require 'openai'

require 'httparty'
require 'json'

# Define the Overpass API endpoint
OVERPASS_URL = 'https://overpass-api.de/api/interpreter'

class OpenStreetMapOverPassTool
  extend Langchain::ToolDefinition

  define_function :search_restaurants,
                  description: 'Search for restaurants in a given city with optional cuisine filters' do
    property :city, type: 'string', description: 'The city name to search for restaurants', required: true
    # property :cuisines, type: 'array', description: 'Optional array of cuisines to filter restaurants by',
    #                     required: false
  end

  def initialize; end

  def search_restaurants(city:, cuisines: [])
    cuisine_filter = cuisines.map { |cuisine| "node['cuisine'='#{cuisine}'](area.searchArea);" }.join("\n")

    query = <<~QUERY
      [out:json];
      area[name="#{city}"]->.searchArea;
      (
        node["amenity"="restaurant"](area.searchArea);
        way["amenity"="restaurant"](area.searchArea);
        relation["amenity"="restaurant"](area.searchArea);
        #{cuisine_filter}
      );
      out center;
    QUERY

    response = HTTParty.get(OVERPASS_URL, query: { data: query })
    data = JSON.parse(response.body)

    restaurants = data['elements'].map do |element|
      element['tags']&.fetch('name', 'Unknown Restaurant')
    end

    tool_response(content: restaurants.join(', '))
  end
end

llm = Langchain::LLM::OpenAI.new(
  api_key: ENV['OPENAI_API_KEY'],
  default_options: { temperature: 0.7, chat_model: 'gpt-4o' }
)

assistant = Langchain::Assistant.new(
  llm: llm,
  instructions: "You're a helpful AI assistant that can search for restaurants",
  tools: [OpenStreetMapOverPassTool.new]
)
assistant.add_message_and_run!(content: 'What are some Mexican resturants in Houston?')

pp assistant.messages
# Check the response in the last message in the conversation
# assistant.messages.last
