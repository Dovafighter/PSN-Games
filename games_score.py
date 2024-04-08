from psn_games import get_games
import re

def create_names(games):
    # Function for changing the games' names to the correct format
    names = []
    for game in games:
        game = game.replace(' (ps4™)', '').replace(' ps4 & ps5','').replace('playstation®5 version','').replace(' - ps5 & ps4','').replace('(ps4™ & ps5™)','')
        game = re.sub("(:)|(®)|(')|(™ )|(’)|(™)|(!)|(,)", "" , game)
        game = game.replace(' - ', '-').replace(' – ', '-').replace(' (ps4™)', '').replace(' ps4  ps5', '').replace('(cusa07377)', '').replace('-ps5  ps4', '').replace('/', '-').replace('-ps4', '').replace('-playstatin4 edition', '').replace(' for ps4', '').replace('ps4  ps5', '').replace(' ps4 ps5' ,'').replace(' (ps5)', '').replace(' playstation4 edition', '').replace('ps4','').replace(' ( ps5)', '').replace('  ', ' ')
        game = re.sub('(---)', '', game)
        game = re.sub('(?!.{20})\.', '', game)
        game = game.replace(' ', '-').replace('【for-ps-plus】', '').replace('&', "and").replace('fishing-and-ps5', 'fishing-2022')

        # Conditionals for problematic names
        if game == 'absolver-downfall':
            names.append('absolver')
            continue
        elif game == "assassins-creed-4-black-flag":
            names.append("assassins-creed-iv-black-flag")
            continue
        elif game == "back-4-blood-standard-edition":
            names.append('back-4-blood')
        elif game == "assassins-creed-freedom-cry":
            names.append("assassins-creed-iv-black-flag-freedom-cry")
            continue
        elif game == 'blood-bowl-3':
            names.append('blood-bowl-iii')
            continue
        elif game == 'abzû':
            names.append('abzu')
            continue
        elif game == 'alternate-jake-hunter-daedalus-the-awakening-of-golden-jazz':
            names.append('alternate-jake-hunter-daedalus-the-awakening-of')
            continue

        else:
            names.append(game)
    return(sorted(names))

print(create_names(get_games()))