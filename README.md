# Agent Examples
For the next seven days, my goal is to build an Assistant that utilizes an interesting tool.

I'm pasting the whoe message history

## Day 3 [Choosing Stocks or Options off RSS feeds](2-stock-rss.rb)

RSS feeds are kind of dying but I did manage to get a pretty simple agent that would pick some
intersting stocks to look at (THIS IS NOT INVESTMENT ADVICE)

This could be taken pretty far but again its 11:30pm as I finish this.

Note it called the RSS tool three times expecting diffrent results.


```
Agent Instructinos: You are an expert stock analyst.
User: What are three stocks or options you would purchase today?
Agent:
   Based on the recent news and developments, here are three stocks to consider purchasing today:
   
   1. **Rivian (RIVN)**: Rivian has recently hit a milestone, leading to a jump in its stock. Additionally, Rivian beat Wall Street's fourth-quarter expectations, which could indicate strong underlying performance.
   
   2. **Alibaba (BABA)**: Alibaba shares soared 11% in Hong Kong after stellar earnings, suggesting a recovery in China's e-commerce sector. Additionally, GameStop CEO Ryan Cohen increased his personal stake in Alibaba to $1 billion, which may reflect confidence in Alibaba's growth prospects.
   
   3. **Duolingo (DUOL)**: Duolingo was recently started at a "buy" with a $222 price target at Seaport. This indicates positive analyst sentiment and potential for growth.
   
   These stocks reflect a mix of positive earnings news, strategic investments, and analyst upgrades, making them attractive options to consider.
```


<details>
<summary>Full Messages including tool calls</summary>

```
[#<Langchain::Assistant::Messages::OpenAIMessage:0x00007ff3aabaf1f8
  @content="You are an expert stock analyst.",
  @image_url=nil,
  @role="system",
  @tool_call_id=nil,
  @tool_calls=[]>,
 #<Langchain::Assistant::Messages::OpenAIMessage:0x00007ff3aabaf1a8
  @content="What are three stocks or options you would purchase today?",
  @image_url=nil,
  @role="user",
  @tool_call_id=nil,
  @tool_calls=[]>,
 #<Langchain::Assistant::Messages::OpenAIMessage:0x00007ff3aaba0608
  @content="",
  @image_url=nil,
  @role="assistant",
  @tool_call_id=nil,
  @tool_calls=
   [{"id" => "call_383TkKscqziJZtRxBSn8yg65", "type" => "function", "function" => {"name" => "rss_feed_tool__get_news", "arguments" => "{}"}},
    {"id" => "call_BrLIlVfBMwF95VIfp1QyaH7W", "type" => "function", "function" => {"name" => "rss_feed_tool__get_news", "arguments" => "{}"}},
    {"id" => "call_3OM2XkSi1HWrJeVU7C0pXmqN", "type" => "function", "function" => {"name" => "rss_feed_tool__get_news", "arguments" => "{}"}}]>,
 #<Langchain::Assistant::Messages::OpenAIMessage:0x00007ff3a97acbd8
  @content=
   "Swiss National Bank cuts interest rates by a half point to 0.5%, Dollar jumps 0.5% to 0.8890 francs, Germany flash manufacturing PMI rises to 4-month high of 43.2, Germany flash services PMI falls to 9-month low of 49.4, Powell says labor market not a source of significant inflation pressure, Fed’s Powell says rate cut ‘on the table’ as soon as September, Final S&P U.S. manufacturing index is 52.2 in February vs. initial 51.5, Duolingo started at buy with $222 price target at Seaport, Housing starts fall 14.8% in January after revised 3.3% gain in December, Building permits fall 1.5% in January, The stock market’s previous breakneck pace is slowing down. What's next?, Stocks feel pressure after Walmart's guidance renews worries about U.S. consumer, Electric-truck maker Rivian hits a milestone, and its stock jumps, Dow ends down 450 points as Walmart’s tepid outlook weighs on U.S. stocks, Dow losing over 500 points in final hour of trade as Walmart drags market down, Walmart is the Dow’s worst performer today. Analysts aren’t nervous., The Chips Act may be dead. That’s another big hurdle for semiconductor stocks., Wall Street wants to know if DOGE-led job cuts will tip U.S. into recession, There are growing signs that the labor market is slowing, Fed’s Bostic says, Satya Nadella says he’s not an economist — and proved it with this misconception, Meta approves plan for bigger executive bonuses following 5% layoffs, Amazon surpasses Walmart in revenue for the first time, Rivian beats Wall Street's fourth-quarter expectations, but expects lower deliveries in 2025, Walmart, Palantir and inflation concerns: What investors think was behind Thursday's sell-off, Alibaba shares soar 11% in Hong Kong after stellar earnings as China's e-commerce sector recovers, China backs Trump's Ukraine peace bid at G20 as U.S. allies rally behind Zelenskyy, Block shares fall on profit, revenue miss, Japan's inflation rate climbs to a 2-year high of 4% in January, supporting rate hike calls from BOJ members, Hong Kong shares hit three-year high as investors weigh Japan inflation data, Trump tariff threats, DOGE cuts nearly half of unit overseeing autonomous vehicles safety, report says, How Walmart won over wealthy shoppers, Trump says his administration will check Fort Knox 'to make sure the gold is there', Kontoor Brands CEO describes growth plans for new acquisition , MLB, ESPN opt out of TV deal for 2026-28 seasons, JPMorgan's top biopharma picks for 2025, Josh Brown says Palantir is now trapped in a 'no-man's land' after stock momentum breaks, Judge rules against union bid to block mass federal layoffs by Trump, Walmart shares drop as retailer says profit growth will slow, Texas Roadhouse gets off to slower current quarter start. But nothing it can't handle, New York Gov. Hochul won't remove Mayor Eric Adams 'at this time', Crypto firms ask Congress to roll back IRS rules for DeFi: CNBC Crypto World, How do I pay my taxes with a credit card?, Moscow loathed the U.S. for years as its economy paid a high price for war — now, it’s doing a U-turn, GameStop CEO Ryan Cohen hikes his personal stake in Alibaba to $1 billion, WSJ says, U.S. says it will drop immigration case against SpaceX, Senate confirms Kash Patel as FBI director, Friday’s big stock stories: What’s likely to move the market in the next trading session, Sen. Elizabeth Warren: DOGE's FDIC firings put banking system at risk, Palantir drops for a second day as cult stock loses momentum, Amazon to gain creative control of James Bond franchise from Broccoli family",
  @image_url=nil,
  @role="tool",
  @tool_call_id="call_383TkKscqziJZtRxBSn8yg65",
  @tool_calls=[]>,
 #<Langchain::Assistant::Messages::OpenAIMessage:0x00007ff3a975a478
  @content=
   "Swiss National Bank cuts interest rates by a half point to 0.5%, Dollar jumps 0.5% to 0.8890 francs, Germany flash manufacturing PMI rises to 4-month high of 43.2, Germany flash services PMI falls to 9-month low of 49.4, Powell says labor market not a source of significant inflation pressure, Fed’s Powell says rate cut ‘on the table’ as soon as September, Final S&P U.S. manufacturing index is 52.2 in February vs. initial 51.5, Duolingo started at buy with $222 price target at Seaport, Housing starts fall 14.8% in January after revised 3.3% gain in December, Building permits fall 1.5% in January, The stock market’s previous breakneck pace is slowing down. What's next?, Stocks feel pressure after Walmart's guidance renews worries about U.S. consumer, Electric-truck maker Rivian hits a milestone, and its stock jumps, Dow ends down 450 points as Walmart’s tepid outlook weighs on U.S. stocks, Dow losing over 500 points in final hour of trade as Walmart drags market down, Walmart is the Dow’s worst performer today. Analysts aren’t nervous., The Chips Act may be dead. That’s another big hurdle for semiconductor stocks., Wall Street wants to know if DOGE-led job cuts will tip U.S. into recession, There are growing signs that the labor market is slowing, Fed’s Bostic says, Satya Nadella says he’s not an economist — and proved it with this misconception, Meta approves plan for bigger executive bonuses following 5% layoffs, Amazon surpasses Walmart in revenue for the first time, Rivian beats Wall Street's fourth-quarter expectations, but expects lower deliveries in 2025, Walmart, Palantir and inflation concerns: What investors think was behind Thursday's sell-off, Alibaba shares soar 11% in Hong Kong after stellar earnings as China's e-commerce sector recovers, China backs Trump's Ukraine peace bid at G20 as U.S. allies rally behind Zelenskyy, Block shares fall on profit, revenue miss, Japan's inflation rate climbs to a 2-year high of 4% in January, supporting rate hike calls from BOJ members, Hong Kong shares hit three-year high as investors weigh Japan inflation data, Trump tariff threats, DOGE cuts nearly half of unit overseeing autonomous vehicles safety, report says, How Walmart won over wealthy shoppers, Trump says his administration will check Fort Knox 'to make sure the gold is there', Kontoor Brands CEO describes growth plans for new acquisition , MLB, ESPN opt out of TV deal for 2026-28 seasons, JPMorgan's top biopharma picks for 2025, Josh Brown says Palantir is now trapped in a 'no-man's land' after stock momentum breaks, Judge rules against union bid to block mass federal layoffs by Trump, Walmart shares drop as retailer says profit growth will slow, Texas Roadhouse gets off to slower current quarter start. But nothing it can't handle, New York Gov. Hochul won't remove Mayor Eric Adams 'at this time', Crypto firms ask Congress to roll back IRS rules for DeFi: CNBC Crypto World, How do I pay my taxes with a credit card?, Moscow loathed the U.S. for years as its economy paid a high price for war — now, it’s doing a U-turn, GameStop CEO Ryan Cohen hikes his personal stake in Alibaba to $1 billion, WSJ says, U.S. says it will drop immigration case against SpaceX, Senate confirms Kash Patel as FBI director, Friday’s big stock stories: What’s likely to move the market in the next trading session, Sen. Elizabeth Warren: DOGE's FDIC firings put banking system at risk, Palantir drops for a second day as cult stock loses momentum, Amazon to gain creative control of James Bond franchise from Broccoli family",
  @image_url=nil,
  @role="tool",
  @tool_call_id="call_BrLIlVfBMwF95VIfp1QyaH7W",
  @tool_calls=[]>,
 #<Langchain::Assistant::Messages::OpenAIMessage:0x00007ff3a9859ba8
  @content=
   "Swiss National Bank cuts interest rates by a half point to 0.5%, Dollar jumps 0.5% to 0.8890 francs, Germany flash manufacturing PMI rises to 4-month high of 43.2, Germany flash services PMI falls to 9-month low of 49.4, Powell says labor market not a source of significant inflation pressure, Fed’s Powell says rate cut ‘on the table’ as soon as September, Final S&P U.S. manufacturing index is 52.2 in February vs. initial 51.5, Duolingo started at buy with $222 price target at Seaport, Housing starts fall 14.8% in January after revised 3.3% gain in December, Building permits fall 1.5% in January, The stock market’s previous breakneck pace is slowing down. What's next?, Stocks feel pressure after Walmart's guidance renews worries about U.S. consumer, Electric-truck maker Rivian hits a milestone, and its stock jumps, Dow ends down 450 points as Walmart’s tepid outlook weighs on U.S. stocks, Dow losing over 500 points in final hour of trade as Walmart drags market down, Walmart is the Dow’s worst performer today. Analysts aren’t nervous., The Chips Act may be dead. That’s another big hurdle for semiconductor stocks., Wall Street wants to know if DOGE-led job cuts will tip U.S. into recession, There are growing signs that the labor market is slowing, Fed’s Bostic says, Satya Nadella says he’s not an economist — and proved it with this misconception, Meta approves plan for bigger executive bonuses following 5% layoffs, Amazon surpasses Walmart in revenue for the first time, Rivian beats Wall Street's fourth-quarter expectations, but expects lower deliveries in 2025, Walmart, Palantir and inflation concerns: What investors think was behind Thursday's sell-off, Alibaba shares soar 11% in Hong Kong after stellar earnings as China's e-commerce sector recovers, China backs Trump's Ukraine peace bid at G20 as U.S. allies rally behind Zelenskyy, Block shares fall on profit, revenue miss, Japan's inflation rate climbs to a 2-year high of 4% in January, supporting rate hike calls from BOJ members, Hong Kong shares hit three-year high as investors weigh Japan inflation data, Trump tariff threats, DOGE cuts nearly half of unit overseeing autonomous vehicles safety, report says, How Walmart won over wealthy shoppers, Trump says his administration will check Fort Knox 'to make sure the gold is there', Kontoor Brands CEO describes growth plans for new acquisition , MLB, ESPN opt out of TV deal for 2026-28 seasons, JPMorgan's top biopharma picks for 2025, Josh Brown says Palantir is now trapped in a 'no-man's land' after stock momentum breaks, Judge rules against union bid to block mass federal layoffs by Trump, Walmart shares drop as retailer says profit growth will slow, Texas Roadhouse gets off to slower current quarter start. But nothing it can't handle, New York Gov. Hochul won't remove Mayor Eric Adams 'at this time', Crypto firms ask Congress to roll back IRS rules for DeFi: CNBC Crypto World, How do I pay my taxes with a credit card?, Moscow loathed the U.S. for years as its economy paid a high price for war — now, it’s doing a U-turn, GameStop CEO Ryan Cohen hikes his personal stake in Alibaba to $1 billion, WSJ says, U.S. says it will drop immigration case against SpaceX, Senate confirms Kash Patel as FBI director, Friday’s big stock stories: What’s likely to move the market in the next trading session, Sen. Elizabeth Warren: DOGE's FDIC firings put banking system at risk, Palantir drops for a second day as cult stock loses momentum, Amazon to gain creative control of James Bond franchise from Broccoli family",
  @image_url=nil,
  @role="tool",
  @tool_call_id="call_3OM2XkSi1HWrJeVU7C0pXmqN",
  @tool_calls=[]>,
 #<Langchain::Assistant::Messages::OpenAIMessage:0x00007ff3a98528f8
  @content=
   "Based on the recent news and developments, here are three stocks to consider purchasing today:\n" +
   "\n" +
   "1. **Rivian (RIVN)**: Rivian has recently hit a milestone, leading to a jump in its stock. Additionally, Rivian beat Wall Street's fourth-quarter expectations, which could indicate strong underlying performance.\n" +
   "\n" +
   "2. **Alibaba (BABA)**: Alibaba shares soared 11% in Hong Kong after stellar earnings, suggesting a recovery in China's e-commerce sector. Additionally, GameStop CEO Ryan Cohen increased his personal stake in Alibaba to $1 billion, which may reflect confidence in Alibaba's growth prospects.\n" +
   "\n" +
   "3. **Duolingo (DUOL)**: Duolingo was recently started at a \"buy\" with a $222 price target at Seaport. This indicates positive analyst sentiment and potential for growth.\n" +
   "\n" +
   "These stocks reflect a mix of positive earnings news, strategic investments, and analyst upgrades, making them attractive options to consider.",
  @image_url=nil,
  @role="assistant",
  @tool_call_id=nil,
  @tool_calls=[]>]
```
</details>



## Day 2 [The Meal DB](https://www.themealdb.com/api.php)

The Meal DB is a pretty inflexible API allowing you to search the title of a recipe, category, or single ingredient.

The assistant works pretty well even when it initially doesn't find results. After giving it a hint, if no results are found, try searching one word at a time.

From the initial search, we return only the ID and meal name separated by a pipe and then a comma between meals, keeping the token count low.

The assistant can then pull the rest of the recipe once it finds a good match. Allowing it to specify a category did have it try and make multiple searches but ultimately confused it more.

* Chicken Fried Steak or cornbread didn't return anything from the database.
* Generic queries like "I need to do something with this shrimp" or "my kids want pancakes."

Lastly, I updated its prompt instructing it to improvise a recipe if none was found.

```
Agent Instructinos: You're a helpful AI assistant that can search for meal recipies
User: Find a Thai Curry Recipe 
Agent:
 **Ingredients:**
 - Potatoes
 - Green beans
 - Oil
 - Garlic
 - Green curry paste
 - Coconut milk
 - Fish sauce
 - Sugar
 - Chicken pieces
 - Lime leaves (or lime zest)
 - Basil leaves
 - Lime for garnish
 **Instructions:**
 1. **Cook the Vegetables:**
    - Put the potatoes in a pan of boiling water and cook for 5 minutes.
    - Add the beans and cook for a further 3 minutes until both are just tender. Drain and set aside.
 
 2. **Prepare the Curry:**
    - In a wok or large frying pan, heat the oil until very hot.
    - Add the garlic and cook until golden, being careful not to let it go too dark.
    - Add the curry paste and stir for a few seconds to release the flavors.
 
 3. **Simmer the Curry:**
    - Pour in the coconut milk and let it come to a bubble.
    - Stir in the fish sauce and sugar, then add the chicken pieces.
    - Turn the heat down to a simmer and cook, covered, for about 8 minutes until the chicken is cooked.
 
 4. **Add Vegetables and Flavorings:**
    - Add the potatoes and beans, warming them through in the hot coconut milk.
    - Stir in the shredded lime leaves (or lime zest) for a citrussy flavor.
    - Add the basil leaves briefly to maintain their brightness.
 
 5. **Serve:**
    - Garnish with lime and serve immediately with boiled rice.
 
 Enjoy your delicious Thai Green Curry!
```

<details>
<summary>Full Messages including tool calls</summary>

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

</details>

Asking for a recipe that isn't found in the database.

```markdown
User: I need a cornbread recipe
Agent:
It seems like there isn't a specific cornbread recipe available in the database I have access to. However, I can help you create a simple and delicious cornbread recipe right here:

### Simple Cornbread Recipe

#### Ingredients:
- 1 cup cornmeal
- 1 cup all-purpose flour
- 1/4 cup granulated sugar
- 1 tablespoon baking powder
- 1/2 teaspoon salt
- 1 cup milk
- 1/3 cup vegetable oil or melted butter
- 2 large eggs

#### Instructions:
1. **Preheat the Oven**: Preheat your oven to 400°F (200°C). Grease an 8-inch square baking dish or a cast-iron skillet.

2. **Mix Dry Ingredients**: In a large bowl, combine the cornmeal, flour, sugar, baking powder, and salt. Stir until well mixed.

3. **Combine Wet Ingredients**: In another bowl, whisk together the milk, vegetable oil (or melted butter), and eggs until well combined.

4. **Combine Wet and Dry Ingredients**: Pour the wet ingredients into the dry ingredients. Stir until just combined. Be careful not to overmix; it's okay if there are a few lumps.

5. **Pour and Bake**: Pour the batter into the prepared baking dish or skillet. Spread it evenly with a spatula.

6. **Bake**: Bake in the preheated oven for 20-25 minutes, or until the top is golden brown and a toothpick inserted into the center comes out clean.

7. **Cool and Serve**: Allow the cornbread to cool slightly before slicing. Serve warm, preferably with butter or honey.

Enjoy your homemade cornbread! If you have any special dietary requirements or preferences, let me know, and I can suggest some modifications.
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
