import requests                     # python pip install requests
from bs4 import BeautifulSoup       # python pip install beautifulsoup4 || apt-get install python3-bs4

# need to make a loop for each game in the list !
gameList = [ "Exit the Gungeon", "ori and the blind forest", "fifa", "rocket league", "dungeon", "Dungeon Souls"] # => making a dict with game name and price, take evendly in mind to allow other game than "pc" platform
index = 5                                                              # when the loop are done, dont forget to delete this line
dlcompare = "https://www.dlcompare.fr/search?q="+gameList[index]       # and delete "+gameList[index]" from this line

#       ┌────────────────┐
#       │  page request  │
#       └────────────────┘

response = requests.get(dlcompare)
soup = BeautifulSoup(response.text, features="html.parser")
game_found = soup.find_all("li", class_="pc")

#       ┌────────────────┐
#       │  get_game_url  │
#       └────────────────┘

for element in game_found:
    name = str(element.find(class_="name").contents[0])

    if name == gameList[index]:
        url = element.find("a")['href']

#       ┌──────────────────┐
#       │  get_game_price  │
#       └──────────────────┘

try:
    url
except NameError:
    print("game not found on dlcompare, you need to verify the exact name")
else:
    game_response = requests.get(url)
    game_soup = BeautifulSoup(game_response.text, features="html.parser")
    game_price = float(game_soup.find(class_="lowPrice").contents[0][:-1])
    print(game_price) # now verify price with your minimal price => need to build better data structure