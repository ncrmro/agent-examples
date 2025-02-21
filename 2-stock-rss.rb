# frozen_string_literal: true

require 'langchain'
require 'openai'
require 'rss'
require 'open-uri'
url = 'https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=100003114'
URI.open(url) do |rss|
  feed = RSS::Parser.parse(rss)
  puts "Title: #{feed.channel.title}"
  feed.items.each do |item|
    puts "Item: #{item.title}"
  end
end

class RssFeedTool
  extend Langchain::ToolDefinition
  define_function :get_news,
                  description: 'Aggregate news item titles from multiple RSS feeds'

  def initialize; end

  def get_news
    urls = [
      'https://feeds.content.dowjones.io/public/rss/mw_realtimeheadlines',
      'https://feeds.content.dowjones.io/public/rss/mw_bulletins',
      'https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=100003114'
    ]

    titles = []

    urls.each do |url|
      URI.open(url) do |rss|
        feed = RSS::Parser.parse(rss)
        feed.items.each do |item|
          titles << item.title
        end
      end
    end

    tool_response(content: titles.join(', '))
  end
end

llm = Langchain::LLM::OpenAI.new(
  api_key: ENV['OPENAI_API_KEY'],
  default_options: { temperature: 0.7, chat_model: 'gpt-4o' }
)

assistant = Langchain::Assistant.new(
  llm: llm,
  instructions: 'You are an expert stock analyst.',
  tools: [RssFeedTool.new]
)
assistant.add_message_and_run!(content: 'What are three stocks or options you would purchase today?')

pp assistant.messages
