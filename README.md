# Agent Examples
For the next seven days, my goal is to build an Assistant that utilizes an interesting tool.

## Day 2 [The Meal DB](https://www.themealdb.com/api.php)

The Meal DB is a pretty inflexible API allowing you to search the title of a recipe, category, or single ingredient.

The assistant works pretty well even when it initially doesn't find results. After giving it a hint, if no results are found, try searching one word at a time.

From the initial search, we return only the ID and meal name separated by a pipe and then a comma between meals, keeping the token count low.

The assistant can then pull the rest of the recipe once it finds a good match. Allowing it to specify a category did have it try and make multiple searches but ultimately confused it more.

* Chicken Fried Steak or cornbread didn't return anything from the database.
* Generic queries like "I need to do something with this shrimp" or "my kids want pancakes."

Lastly, I updated its prompt instructing it to improvise a recipe if none was found.
```
[#<Langchain::Assistant::Messages::OpenAIMessage:0x00007fa9a6f620f0
  @content="You're a helpful AI assistant that can search for meal recipies",
  @image_url=nil,
  @role="system",
  @tool_call_id=nil,
  @tool_calls=[]>,
 #<Langchain::Assistant::Messages::OpenAIMessage:0x00007fa9a6f61b00 @content="Find a Thai Curry recipe", @image_url=nil, @role="user", @tool_call_id=nil, @tool_calls=[]>,
 #<Langchain::Assistant::Messages::OpenAIMessage:0x00007fa9a632f3c8
  @content="",
  @image_url=nil,
  @role="assistant",
  @tool_call_id=nil,
  @tool_calls=
   [{"id" => "call_qkqowgIYFIpP9tfXOwNdO7ag",
     "type" => "function",
     "function" => {"name" => "meal_db_tool__search_meals", "arguments" => "{\"meal_name\":\"Thai Curry\"}"}}]>,
 #<Langchain::Assistant::Messages::OpenAIMessage:0x00007fa9a6326e08
  @content="No meals found",
  @image_url=nil,
  @role="tool",
  @tool_call_id="call_qkqowgIYFIpP9tfXOwNdO7ag",
  @tool_calls=[]>,
 #<Langchain::Assistant::Messages::OpenAIMessage:0x00007fa9a6363da8
  @content="",
  @image_url=nil,
  @role="assistant",
  @tool_call_id=nil,
  @tool_calls=
   [{"id" => "call_6Wruj8CVvvXt38k57ub0MhL8", "type" => "function", "function" => {"name" => "meal_db_tool__search_meals", "arguments" => "{\"meal_name\":\"Curry\"}"}}]>,
 #<Langchain::Assistant::Messages::OpenAIMessage:0x00007fa9c27db270
  @content="52814|Thai Green Curry, 52868|Kidney Bean Curry, 52820|Katsu Chicken curry, 52827|Massaman Beef curry, 52851|Nutty Chicken Curry",
  @image_url=nil,
  @role="tool",
  @tool_call_id="call_6Wruj8CVvvXt38k57ub0MhL8",
  @tool_calls=[]>,
 #<Langchain::Assistant::Messages::OpenAIMessage:0x00007fa9a6c74898
  @content="",
  @image_url=nil,
  @role="assistant",
  @tool_call_id=nil,
  @tool_calls=
   [{"id" => "call_VfwCOpa3vsGPDtAZ6BTYgsSe", "type" => "function", "function" => {"name" => "meal_db_tool__lookup_meal_by_id", "arguments" => "{\"meal_id\":\"52814\"}"}}]>,
 #<Langchain::Assistant::Messages::OpenAIMessage:0x00007fa9a6cf97a0
  @content=
   "Name: Thai Green Curry, Category: Chicken, Area: Thai, Instructions: Put the potatoes in a pan of boiling water and cook for 5 minutes. Throw in the beans and cook for a further 3 minutes, by which time both should be just tender but not too soft. Drain and put to one side.\r\n" +
   "In a wok or large frying pan, heat the oil until very hot, then drop in the garlic and cook until golden, this should take only a few seconds. Don’t let it go very dark or it will spoil the taste. Spoon in the curry paste and stir it around for a few seconds to begin to cook the spices and release all the flavours. Next, pour in the coconut milk and let it come to a bubble.\r\n" +
   "Stir in the fish sauce and sugar, then the pieces of chicken. Turn the heat down to a simmer and cook, covered, for about 8 minutes until the chicken is cooked.\r\n" +
   "Tip in the potatoes and beans and let them warm through in the hot coconut milk, then add a lovely citrussy flavour by stirring in the shredded lime leaves (or lime zest). The basil leaves go in next, but only leave them briefly on the heat or they will quickly lose their brightness. Scatter with the lime garnish and serve immediately with boiled rice.",
  @image_url=nil,
  @role="tool",
  @tool_call_id="call_VfwCOpa3vsGPDtAZ6BTYgsSe",
  @tool_calls=[]>,
 #<Langchain::Assistant::Messages::OpenAIMessage:0x00007fa9a6f66a10
  @content=
   "Here's a recipe for Thai Green Curry:\n" +
   "\n" +
   "**Ingredients:**\n" +
   "- Potatoes\n" +
   "- Green beans\n" +
   "- Oil\n" +
   "- Garlic\n" +
   "- Green curry paste\n" +
   "- Coconut milk\n" +
   "- Fish sauce\n" +
   "- Sugar\n" +
   "- Chicken pieces\n" +
   "- Lime leaves (or lime zest)\n" +
   "- Basil leaves\n" +
   "- Lime for garnish\n" +
   "\n" +
   "**Instructions:**\n" +
   "\n" +
   "1. **Cook the Vegetables:**\n" +
   "   - Put the potatoes in a pan of boiling water and cook for 5 minutes.\n" +
   "   - Add the beans and cook for a further 3 minutes until both are just tender. Drain and set aside.\n" +
   "\n" +
   "2. **Prepare the Curry:**\n" +
   "   - In a wok or large frying pan, heat the oil until very hot.\n" +
   "   - Add the garlic and cook until golden, being careful not to let it go too dark.\n" +
   "   - Add the curry paste and stir for a few seconds to release the flavors.\n" +
   "\n" +
   "3. **Simmer the Curry:**\n" +
   "   - Pour in the coconut milk and let it come to a bubble.\n" +
   "   - Stir in the fish sauce and sugar, then add the chicken pieces.\n" +
   "   - Turn the heat down to a simmer and cook, covered, for about 8 minutes until the chicken is cooked.\n" +
   "\n" +
   "4. **Add Vegetables and Flavorings:**\n" +
   "   - Add the potatoes and beans, warming them through in the hot coconut milk.\n" +
   "   - Stir in the shredded lime leaves (or lime zest) for a citrussy flavor.\n" +
   "   - Add the basil leaves briefly to maintain their brightness.\n" +
   "\n" +
   "5. **Serve:**\n" +
   "   - Garnish with lime and serve immediately with boiled rice.\n" +
   "\n" +
   "Enjoy your delicious Thai Green Curry!",
  @image_url=nil,
  @role="assistant",
  @tool_call_id=nil,
  @tool_calls=[]>]
```
```
```

## Day 1 [Open Street Map Restaurant Finder](0-openstreet-map.rb)

This assistant uses the Open Street Map [OverPass API](https://wiki.openstreetmap.org/wiki/Overpass_API) to search for restaurants of various cuisines in a city.

Initially, I attempted to create a single OverPass Query to search for multiple cuisines, but the langchain ended up making three separate tool calls to the Overpass API (which was good enough at 11:30 at night.

> User: What are some Mexican, Chinese or Mediterrian resturants in Houston?' 

```markdown
Agent Response

Here are some restaurants in Houston that serve Mexican, Chinese, or Mediterranean cuisine:

### Mexican Restaurants
1. La Tapatia
2. Las Haciendas
3. Escalante's Mexican Grille
4. Guadalajara
5. Tacos A Go Go
6. Sierra Madre Taco Co.
7. El Palenque
8. Skeeter's
9. Tacos La Bala
10. 100% Taquito

### Chinese Restaurants
1. Hunan River Bistro
2. D Wok Express
3. Chinese Buffet
4. Fat Bao
5. Spicy Tu Jiazu
6. China Stix
7. Moody Towers Dining Commons
8. Los Chinos Rico
9. Vstar
10. Hin's Garden

### Mediterranean Restaurants
1. Fadi's Mediterranean Grill
2. CAVA
3. Dimassi's Mediterranean Buffet
4. Mary'z
5. Aladdin
6. Busy Boy
7. Kenz Mediterranean Cafe
8. Zabak's Mediterranean Cafe
9. Island Grill
10. Barbar Mediterranean Grill

Feel free to ask if you need more information or additional options!
```
```
