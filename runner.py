# runner.py
import cmd_args
from config import check_should_print, get_should_print, set_should_print, set_db_name

args, kwargs = cmd_args.get_args()
args = args[1:]
import subprocess

import itertools
import threading
import time
import signal 

signal.signal(signal.SIGINT, signal.SIG_DFL)
x = 1
if 'min_players' in kwargs.keys():
    x = int(kwargs.get('min_players', '1'))
    kwargs.pop('min_players')
db = None
if 'db' in kwargs.keys():
    db = 'data'

python_cmd = 'python'

is_running = True

def timer():
    i = 0
    while is_running:
        time.sleep(1.0)
        i = i + 1
        print(f'{i} seconds elapsed')


timer_thread = threading.Thread(
    target=timer,
    args=[],
    daemon=False
)

timer_thread.start()



for i in range(x, len(args)+1):
    players_combinations = list(itertools.combinations(args, i))
    for players in players_combinations:
        games = list(itertools.permutations(players))

        kwargs_list = []
        kwargs_str = ""
        for key, value in kwargs.items():
            kwargs_list = kwargs_list + [key, str(value)]
            kwargs_str = kwargs_str + f" -{key} {value}"
        

        import os
        j = 0
        for game in games:
            j = j + 1
            game_str = " ".join(game)
            command = f"{python_cmd} racko_engine.py " + game_str + kwargs_str
            if db is None:
                command = command + f' -db games-size-{i}-id'
            print(command)
            # Create a thread object
            result = subprocess.run(
              command,
             capture_output=True,
             text=True,
             check=True,
             shell=True,
            )
            
            # Print the output
            print(result.stdout)

            # thread = threading.Thread(target = lambda a : subprocess.run(a, capture_output=True, text=True, check=True, shell=True), args=[command])

            # Start the thread
            # thread.start()
    # result = subprocess.run(command, capture_output=True, text=True, check=True, shell=True)
    
    # os.spawnl(os.P_DETACH, command)
    # process = subprocess.Popen(command, 
    #                        stdout=subprocess.PIPE, 
    #                        stderr=subprocess.PIPE, 
    #                        shell=True,
    #                        start_new_session=True)

is_running = False

time.sleep(1)

print('done!')

# print(result.stdout)

# print(result.stderr)