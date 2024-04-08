from games_score import create_names
from psn_games import get_games

import requests
import re

def get_info(names):
    # Function for getting a game's info

    list_of_games = []
    list_of_scores = []
    list_of_reviews = []
    list_of_dates = []
    list_of_developers = []
    list_of_publishers = []

    for name in names:
        print(name)
        url = f'https://internal-prod.apigee.fandom.net/v1/xapi/composer/metacritic/pages/games-critic-reviews/{name}/platform/pc/web?filter=all&sort=score&apiKey=1MOZgmNFxvmljaQR1X9KAij9Mo4xAY3u'
        info = requests.get(url)
        print(info)

        # Looking for the game's name using Regex
        name = re.search('"title":"(.*?)",', info.text)
        print(name)
        game_name = name.group(1)
        list_of_games.append(game_name)


        # Looking for the game's score using Regex
        score = re.search('((?<=score".)..)', info.text)
        game_score = score.group(1)
        list_of_scores.append(game_score)

        # Looking for the game's review count
        reviews = re.search('(?<="reviewCount":)(.*?),', info.text)
        game_reviews = reviews.group(1)
        list_of_reviews.append(game_reviews)

        if game_name == "Assetto Corsa Competizione":
            list_of_developers.append('Kunos Simulazioni')
            list_of_publishers.append('Kunos Simulazioni')
            list_of_dates.append('2019-06-02')
            print(game_name, game_score, game_reviews, game_release, game_developer, game_publisher, '\n')
            continue

        # Looking for the game's release date using Regex
        release_date = re.search('"releaseDate":"(.*?)",', info.text)
        game_release = release_date.group(1)
        list_of_dates.append(game_release)

            
        # Looking for the game's developer using Regex
        developer = re.search('"typeName":"Developer","name":"(.*?)",', info.text)
        game_developer = developer.group(1)
        list_of_developers.append(game_developer)

        # Looking for the game's publisher using Regex
        publisher = re.search('"typeName":"Publisher","name":"(.*?)",', info.text)
        game_publisher = publisher.group(1)
        list_of_publishers.append(game_publisher)

        print(game_name, game_score, game_reviews, game_release, game_developer, game_publisher, '\n')

    print(list_of_games, list_of_scores, list_of_dates, list_of_developers, list_of_publishers)

information = get_info(create_names(get_games()))