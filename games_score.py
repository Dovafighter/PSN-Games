from psn_games import get_games
import re

def create_names(games):
    # Function for changing the games' names to the correct format
    names = []
    for game in games:
        # game = game.replace(' (ps4™)', '').replace(' ps4 & ps5','').replace('playstation®5 version','').replace(' - ps5 & ps4','').replace('(ps4™ & ps5™)','')
        game = game.replace('-™™','').replace('™-', '')
        game = re.sub("(:)|(®)|(')|(™ )|(’)|(™)|(!)|(,)", "" , game)
        # game = game.replace(' - ', '-').replace(' – ', '-').replace(' (ps4™)', '').replace(' ps4  ps5', '').replace('(cusa07377)', '').replace('-ps5  ps4', '').replace('/', '-').replace('-ps4', '').replace('-playstatin4 edition', '').replace(' for ps4', '').replace('ps4  ps5', '').replace(' ps4 ps5' ,'').replace(' (ps5)', '').replace(' playstation4 edition', '').replace('ps4','').replace(' ( ps5)', '').replace('  ', ' ')
        game = re.sub('(---)', '', game)
        game = re.sub('(?!.{20})\.', '', game)
        game = game.replace(' ', '-').replace('【for-ps-plus】', '').replace('&', "and").replace('fishing', 'fishing-2022').replace('-playstation4-edition', '').replace('-definitive-edition','').replace('-and-ps5', '')
        game = game.replace(' ', '-').replace('-classic', '').replace('-standard', '').replace('0-hd', '0').replace('-(standard-version)', '').replace('-digital-edition','').replace('ö','o').replace('-edition-edition','').replace('-complete-season', '')
        game = re.sub('(-\Z)', '', game)


        # Conditionals for problematic names
        if game == 'absolver-downfall':
            names.append('absolver')
        elif game == 'dandara-trials-of-fear-edition':
            names.append('dandara')
        elif 'kingdom-hearts' in game:
            game = game.replace('.', '').replace('1', 'i').replace('plus-25', 'plus-ii5')
            names.append(game)
        elif game == 'journey-to-the-savage-planet-employee-of-the-month':
            names.append('journey-to-the-savage-planet')
        elif game == 'frostpunk-edition':
            names.append('frostpunk')
        elif 'doom-eternal' in game:
            names.append('doom-eternal')
        elif 'builders-2' in game:
            names.append('dragon-quest-builders-2')
        elif 'far-cry' in game:
            game = game.replace('-edition','')
            names.append(game)
        elif 'nba-2' in game:
            correct = re.search('(nba-2k..)', game)
            names.append(correct.group(1))
        elif game == 'back-4-blood-edition':
            names.append('back-4-blood')
        elif game == 'tennis-world-tour-2-complete-edition':
            continue
        elif 'nier' in game:
            names.append('nier-replicant-ver122474487139')
        elif game == 'get-even':
            names.append('get-even-2015')
        elif game == 'i-am-bread':
            names.append('i-am-bread-tv')
        elif 'sundered' in game:
            names.append('sundered')
        elif 'jotun' in game:
            names.append('jotun')
        elif 'mudrunner' in game:
            names.append('spintires-mudrunner')
        elif 'spiritfarer' in game:
            names.append('spiritfarer')
        elif 'space-hulk' in game:
            names.append('space-hulk-deathwing')
        elif game == 'tiny-tinas-wonderlands-next-level-edition':
            continue
        elif game == 'story-of-seasons-pioneers-of-olive-town-+-expansion-pass-set':
            continue
        elif game == 'concrete-genie-digital-deluxe':
            continue
        elif game == 'destroy-all-humans-2-reprobed-single-player':
            continue
        elif game == 'dragon-quest-heroes-ii-digital-explorers-edition':
            continue
        elif game == 'spongebob-squarepants-battle-for-bikini-bottom-rehydrated':
            names.append('spongebob-squarepants-battle-for-bikini-bottom-2')
        elif game == 'star-ocean-iaf':
            names.append('star-ocean-integrity-and-faithlessness')
        elif game == 'zombi':
            names.append('zombiu')
        elif game == "assassins-creed-4-black-flag":
            names.append("assassins-creed-iv-black-flag")
        elif game == "back-4-blood-standard":
            names.append('back-4-blood')
        elif game == "assassins-creed-freedom-cry":
            names.append("assassins-creed-iv-black-flag-freedom-cry")
        elif game == 'blood-bowl-3':
            names.append('blood-bowl-iii')
        elif game == 'abzû':
            names.append('abzu')
        elif game == 'alternate-jake-hunter-daedalus-the-awakening-of-golden-jazz':
            names.append('alternate-jake-hunter-daedalus-the-awakening-of')
        elif game == 'bound':
            names.append('bound-2016')
        elif game == 'concrete-genie-digital-deluxe-edition':
            names.append('concrete-genie')
        elif game == 'call-of-cthulhu':
            names.append('call-of-cthulhu-the-official-video-game')
        elif game == 'payday-2-crimewave-edition':
            names.append('payday-2')

        else:
            names.append(game)
        
    return(sorted(set(names)))

list = create_names(get_games())
for game in list:
    print(game)