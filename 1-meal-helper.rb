# frozen_string_literal: true

require 'langchain'
require 'openai'

require 'httparty'
require 'json'
require 'readline'

# Define the Overpass API endpoint
OVERPASS_URL = 'https://overpass-api.de/api/interpreter'

class MealDBTool
  extend Langchain::ToolDefinition

  define_function :list_categories,
                  description: 'List all meal categories from the MealDB API'

  define_function :search_meals,
                  description: 'Search for meals by name and optional category using the MealDB API, returns meal ID and name' do
    property :meal_name, type: 'string',
                         description: 'The name of the meal to search for (search using only one word if no results)', required: true
    # property :category, type: 'string', description: 'Optional category to filter meals by', required: false
  end
  def initialize; end

  define_function :lookup_meal_by_id,
                  description: 'Lookup a meal by its ID using the MealDB API' do
    property :meal_id, type: 'string', description: 'The ID of the meal to look up', required: true
  end

  def list_categories
    response = HTTParty.get('https://www.themealdb.com/api/json/v1/1/categories.php')
    data = JSON.parse(response.body)

    categories = data['categories'].map do |category|
      category['strCategory']
    end

    tool_response(content: categories.join(', '))
  end

  def search_meals(meal_name:, category: nil)
    url = "https://www.themealdb.com/api/json/v1/1/search.php?s=#{meal_name}"
    url += "&c=#{category}" if category
    response = HTTParty.get(url)
    data = JSON.parse(response.body)

    meals = data['meals']&.map do |meal|
      "#{meal['idMeal']}|#{meal['strMeal']}"
    end
    puts 'MEALS', meals

    tool_response(content: meals ? meals.join(', ') : 'No meals found')
  end

  def lookup_meal_by_id(meal_id:)
    response = HTTParty.get("https://www.themealdb.com/api/json/v1/1/lookup.php?i=#{meal_id}")
    data = JSON.parse(response.body)

    meal = data['meals']&.first
    if meal
      meal_details = "Name: #{meal['strMeal']}, Category: #{meal['strCategory']}, Area: #{meal['strArea']}, Instructions: #{meal['strInstructions']}"
      tool_response(content: meal_details)
    else
      tool_response(content: 'No meal found with the given ID')
    end
  end
end

llm = Langchain::LLM::OpenAI.new(
  api_key: ENV['OPENAI_API_KEY'],
  default_options: { temperature: 0.7, chat_model: 'gpt-4o' }
)

assistant = Langchain::Assistant.new(
  llm: llm,
  instructions: "You're a helpful AI assistant that can search for meal recipies, if you cant find a recipe improvise!",
  tools: [MealDBTool.new]
)
DONE = %w[done end eof exit].freeze

puts 'Welcome to your Meal DB helper!'

# assistant.add_message_and_run!(content: 'Find a Thai Curry recipe')

# pp assistant.messages
def prompt_for_message
  puts "(multiline input; type 'end' on its own line when done. or exit to exit)"

  user_message = Reline.readmultiline('Question: ', true) do |multiline_input|
    last = multiline_input.split.last
    DONE.include?(last)
  end

  return :noop unless user_message

  lines = user_message.split("\n")
  if lines.size > 1 && DONE.include?(lines.last)
    # remove the "done" from the message
    user_message = lines[0..-2].join("\n")
  end

  return :exit if DONE.include?(user_message.downcase)

  user_message
end

begin
  loop do
    user_message = prompt_for_message

    case user_message
    when :noop
      next
    when :exit
      break
    end

    assistant.add_message_and_run content: user_message, auto_tool_execution: true
    puts assistant.messages.last.content
  end
rescue Interrupt
  exit 0
end
