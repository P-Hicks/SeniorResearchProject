import pandas as pd
from .queries import run_query, run_query_file

def get_df():
    query_1 = '''
        SELECT
            number_of_turns, name, numplayers
        FROM
            player_with_numturns
        '''
    data= run_query(
        query_1
    )
    
    data = {
        'numturns':[i[0] for i in data],
        'name':[i[1] for i in data],
        'numplayers':[i[2] for i in data]
    }

    df = pd.DataFrame(data)
    return df

'''
name,
player_id, 
game_id, 
numturns,
numdiscards,
numdraws,
numnones,
(numdiscards::float) / (numturns::float) as percentdiscards,
(numdraws::float) / (numturns::float) as percentdraws,
(numnones::float) / (numturns::float) as percentnones
'''

def get_stats_df():
    
    data_stats = run_query_file('sql_queries/player_game_stats.sql')
    fields = {
        'name':0,
        'numturns':3,
        'numdiscards':4,
        'numdraws':5,
        'numnones':6,
        'percentdiscards':7,
        'percentdraws':8,
        'percentnones':9,
        'avgcomputationaltime':10,
    }
    data = {

    }
    for key, value in fields.items():
        data[key] = [i[value] for i in data_stats]

    df = pd.DataFrame(data)
    return df