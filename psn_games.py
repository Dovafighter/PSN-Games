import requests
from bs4 import BeautifulSoup

def get_games():   
    #Function for getting a list of games in PS Plus Extra
    URL = 'https://www.playstation.com/pl-pl/ps-plus/games/'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    games_html = soup.find_all('a', attrs={'module-name': 'PS Plus Games List'})

    games_list = [game.text
                  .lower()
                  .replace('console','')
                  .replace('far cry®','far cry ')
                  .replace(' PS4™ & PS5™', '')
                  .replace(' (ps4™)', '')
                  .replace(' ps4 & ps5','')
                  .replace('playstation®5 version','')
                  .replace(' - ps5 & ps4','')
                  .replace('(ps4™ & ps5™)','')
                  .replace(' - ', '-')
                  .replace(' – ', '-')
                  .replace(' (ps4™)', '')
                  .replace(' ps4  ps5', '')
                  .replace('(cusa07377)', '')
                  .replace('-ps5  ps4', '')
                  .replace('/', '-')
                  .replace('-ps4', '')
                  .replace('-playstatin4 edition', '')
                  .replace(' for ps4', '')
                  .replace('ps4  ps5', '')
                  .replace(' ps4 ps5' ,'')
                  .replace(' (ps5)', '')
                  .replace(' playstation4 edition', '')
                  .replace('ps4','')
                  .replace(' ( ps5)', '')
                  .replace('  ', ' ')
                  .replace('【for-ps-plus】', '')
                  .replace('&', "and")
                  .replace('fishing-and-ps5', 'fishing-2022')
                  .replace('-playstation4-edition', '')
                  .replace('-definitive-edition','')
                  .replace('-edition', '')
                  .replace(' -and-ps5', '')
                  .replace('-playstation4','')
                  .replace('™ ', '-')
                  .replace('™', '-')
                  .replace(' (playstation plus)' ,'')
                  .replace('+', 'plus')
                  .replace('vs.', 'vs')
                  .replace('...', '') for game in games_html]
    games_list = sorted(set(games_list))
    return(games_list)

print(get_games())