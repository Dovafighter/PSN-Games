from games_score import create_names
from psn_games import get_games

import requests
import re

def get_info(names):
    # Function for getting a game's info
    for name in names:
        print(name)
        url = f'https://internal-prod.apigee.fandom.net/v1/xapi/composer/metacritic/pages/games-critic-reviews/{name}/platform/pc/web?filter=all&sort=score&apiKey=1MOZgmNFxvmljaQR1X9KAij9Mo4xAY3u'
        info = requests.get(url)

        # Looking for the game's score using Regex
        score = re.search('((?<=score".)..)', info.text)
        game_score = score.group(1)

        # Looking for the game's name using Regex
        name = re.search('"title":"(.*?)",', info.text)
        game_name = name.group(1)

        # Looking for the game's release date using Regex
        release_date = re.search('"releaseDate":"(.*?)",', info.text)
        game_release = release_date.group(1)
        
        # Looking for the game's developer using Regex
        developer = re.search('"typeName":"Developer","name":"(.*?)",', info.text)
        game_developer = developer.group(1)

        # Looking for the game's publisher using Regex
        publisher = re.search('"typeName":"Publisher","name":"(.*?)",', info.text)
        game_publisher = publisher.group(1)

        print(game_name, game_score, game_release, game_developer, game_publisher, '\n')

information = get_info(create_names(get_games()))