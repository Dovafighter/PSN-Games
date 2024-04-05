from psn_games import get_games
import re

def create_links(games):
    links = []
    for game in games:
        game = game.replace('PS4', '').replace('PS5','').replace("&","").lower()
        game = re.sub('(   )|(®)|', '', game)
        game = re.sub('(®: )|(: )|( )','-',game)
        link = f"https://www.metacritic.com/game/{game}/"
        links.append(link)

    return(links)

links = create_links(get_games())
print(links)