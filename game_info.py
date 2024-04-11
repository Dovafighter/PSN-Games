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
        try:
            info = requests.get(url)
        except:
            for i in (list_of_games, list_of_scores, list_of_reviews, list_of_dates, list_of_developers, list_of_publishers):
                i.append('-')
            continue


        print(info)

        # Looking for the game's name using Regex
        game_name = re.search('"title":"(.*?)",', info.text)
        print(name)
        try:
            game_name = game_name.group(1)
            list_of_games.append(game_name)
        except:
            list_of_games.append('-')
        
        if game_name == 'undefined':
            list_of_games.append(name)
            for i in (list_of_scores, list_of_reviews, list_of_dates, list_of_developers, list_of_publishers):
                i.append('-')
            continue


        # Looking for the game's score using Regex
        score = re.search('((?<=score".)..)', info.text)
        try:
            game_score = score.group(1)
            list_of_scores.append(game_score)
        except:
            list_of_scores.append('-')

        # Looking for the game's review count
        reviews = re.search('(?<="reviewCount":)(.*?),', info.text)
        try:
            game_reviews = reviews.group(1)
            list_of_reviews.append(game_reviews)
        except:
            list_of_reviews.append('-')

        if game_name == "Assetto Corsa Competizione":
            list_of_developers.append('Kunos Simulazioni')
            list_of_publishers.append('Kunos Simulazioni')
            list_of_dates.append('2019-06-02')
            print(game_name, game_score, game_reviews, game_release, game_developer, game_publisher, '\n')
            continue

        # Looking for the game's release date using Regex
        release_date = re.search('"releaseDate":"(.*?)",', info.text)
        try:
            game_release = release_date.group(1)
            list_of_dates.append(game_release)
        except:
            list_of_dates.append('-')
            
        # Looking for the game's developer using Regex
        developer = re.search('"typeName":"Developer","name":"(.*?)",', info.text)
        try:
            game_developer = developer.group(1)
            list_of_developers.append(game_developer)
        except:
            list_of_developers.append('-')
        # Looking for the game's publisher using Regex
        publisher = re.search('"typeName":"Publisher","name":"(.*?)",', info.text)
        try:
            game_publisher = publisher.group(1)
            list_of_publishers.append(game_publisher)
        except:
            list_of_publishers.append('-')

        print(game_name, game_score, game_reviews, game_release, game_developer, game_publisher, '\n')

    print(list_of_games, list_of_scores, list_of_dates, list_of_developers, list_of_publishers)

information = get_info(create_names(get_games()))