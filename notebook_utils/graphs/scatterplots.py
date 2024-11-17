import pandas as pd
from ..queries import run_query
import matplotlib.pyplot as plt 
import numpy as np

def scatterplot(df, name, xfield, yfield, field, show_size = True, max_turns = None):
    query = f'''
    select name,
    numturns,
    percent{field},
    count(game_id) as count
    from player_game_stats_outer
    group by name, numturns, percent{field}
    '''
    _data = run_query(query)
    data = {
        "name" : [i[0] for i in _data],
        "numturns" : [i[1] for i in _data],
        "count" : [i[3] for i in _data],
        xfield : [i[2] for i in _data]
    }
    _df1 = pd.DataFrame(data)
    if name is not None:
        _df1 = _df1[(_df1['name'] == name)]
    if max_turns is not None:
        _df1 = _df1[(_df1['numturns'] <= max_turns)]
    # _df2 = df1.groupby([xfield, yfield]).count()
    x = _df1[xfield]
    y = _df1[yfield]
    sizes = _df1['count']
    if show_size:
        plt.scatter(x, y, s= sizes)
    else:
        plt.scatter(x, y, s=2.5)
    plt.show()

'''
SELECT name, count(db_turn.id), avg(computational_time)
FROM "db_turn"
join db_player on db_turn.player_id = db_player.id
where computational_time > 0 and name = 'Replacement'
group by name

'''

def comp_time_scatterplot(name = None, show_size = True, max_turns = None):
    query = f'''
    select name,
    numturns,
    avg_computational_time,
    count(game_id) as count
    from player_game_stats_outer
    group by name, numturns, avg_computational_time
    '''
    _data = run_query(query)
    data = {
        "name" : [i[0] for i in _data],
        "numturns" : [i[1] for i in _data],
        "count" : [i[3] for i in _data],
        'avg_computational_time' : [i[2] for i in _data]
    }
    _df = pd.DataFrame(data)
    if name is not None:
        _df = _df[(_df['name'] == name)]
    if max_turns is not None:
        _df = _df[(_df['numturns'] <= max_turns)]
    # _df2 = df1.groupby([xfield, yfield]).count()
    x = _df['avg_computational_time']
    y = _df['numturns']
    sizes = _df['count']
    if show_size:
        plt.scatter(x, y, s= sizes)
    else:
        plt.scatter(x, y, s=2.5)
    plt.show()