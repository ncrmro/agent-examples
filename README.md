# Agent Examples
For the next seven days, my goal is to build an Assistant that utilizes an interesting tool.

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
