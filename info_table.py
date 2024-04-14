
from game_info import get_info
from games_score import create_names
from psn_games import get_games
import pandas as pd

def create_table(lists):

    data = {
        'Game': lists[0],
        'Score': lists[1],
        'Number of reviews': lists[2],
        'Release date': lists[3],
        'Developer': lists[4],
        'Publisher': lists[5]
    }

    return data

info = create_table(get_info(create_names(get_games())))
df = pd.DataFrame(info)
df.drop_duplicates()
df.to_csv('all_info.csv', index=False, sep='|')
