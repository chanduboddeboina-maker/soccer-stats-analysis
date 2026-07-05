
from statsbombpy import sb
import pandas as pd



def get_competition():
    return sb.competitions()


def get_matches(c_id,s_id):
    return sb.matches(c_id,s_id)

def get_clean_events(mat_id):

    events=sb.events(match_id=mat_id)
    events[['x','y']]=events['location'].apply(pd.Series)

    shots=events[events['type']=='Shot'].copy()

    shots=shots[[
        'player','team','minute',
        'x','y','shot_outcome',
        'shot_statsbomb_xg',
        'shot_body_part'
    ]].dropna(subset=['x','y'])
    

    events[['end_x','end_y']]=events["pass_end_location"].apply(pd.Series)
    passes=events[events['type']=='Pass'].copy()

    passes=passes[['player','team','minute',
        'x','y','end_x','end_y',
        'pass_outcome','pass_recipient'
    ]].dropna(subset=['x','y','end_x','end_y'])



    touch=events.dropna(subset=['location']).copy()
    touch=touch[['player','team','type','x','y','minute']]


    return shots,passes,touch
