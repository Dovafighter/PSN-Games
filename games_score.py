from psn_games import get_games

def create_links(games):
    links = []
    for game in games:
        game = game.lower().replace(' ', '-').replace("'", "")
        link = f"https://www.metacritic.com/game/{game}/"
        links.append(link)

    return(links)

links = create_links(get_games())
print(links)