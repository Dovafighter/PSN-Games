import requests
from bs4 import BeautifulSoup

def get_games():   
    #Function for getting a list of games in PS Plus Extra
    URL = 'https://www.playstation.com/pl-pl/ps-plus/games/'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    games_html = soup.find_all('a', attrs={'module-name': 'PS Plus Games List'})

    games_list = [game.text for game in games_html]
    return(games_list)