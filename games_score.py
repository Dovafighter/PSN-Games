from psn_games import get_games
import re

def create_links(games):
    links = []
    for game in games:
        game = game.replace(' (ps4™)', '')
        game = re.sub("(:)|(®)|(')|(™ )|(’)|(™)|(!)", "" , game)
        game = game.replace(' - ', '-').replace(' – ', '-').replace(' (ps4™)', '').replace(' ps4  ps5', '').replace('(cusa07377)', '').replace('-ps5  ps4', '').replace('/', '-').replace('-ps4', '').replace('-playstatin4 edition', '').replace(' for ps4', '').replace('ps4  ps5', '').replace(' ps4 ps5' ,'').replace(' (ps5)', '').replace(' playstation4 edition', '').replace('ps4','').replace(' ( ps5)', '').replace('  ', ' ')
       # game = game.replace('–', '-').replace(' - ', '-').replace(' ', '-').replace('PS4', '').replace('PS5','').replace("&","").replace(':','')
        game = re.sub('(---)', '', game)
        game = re.sub('(?!.{20})\.', '', game)
        game = game.replace(' ', '-').replace('【for-ps-plus】', '').replace('&', "and")
        link = f"https://www.metacritic.com/game/{game}/"
        links.append(link)

    return(sorted(links))

links = create_links(get_games())
for link in links:
    print(link)