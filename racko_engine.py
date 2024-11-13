import cmd_args
from config import check_should_print, get_should_print, set_should_print, set_db_name

args, kwargs = cmd_args.get_args()

if kwargs.get('db') is not None:
  set_db_name(kwargs.get('db'))

from main import setup1, setup2

setup1()
setup2()


import random
from player import Player
random.seed(12345)

import game_card_tracker
from orm.db.models import *
import player_stats_tracker

from statistics import stdev, mean

import time

def run_game(players, seed):
  num_players_playing = len(players)
  
  game_cards = game_card_tracker.GameCardTracker(seed=seed)
  game_cards.deal(players)
  turn_count = 0
  while (num_players_playing > 0):
    turn_count = turn_count = 1 + turn_count
    num_players_playing = 0
    for player in players:
      if get_should_print():
        print(f'{player.title} {player.player.hand}')
      if (not player.has_racko()):
        num_players_playing = num_players_playing + 1
        game_cards.start_turn()
        top_discard = game_cards.see_discard()
        discard = player.take_turn(game_cards)

    # num_players_playing = len([player for player in players if not player.has_racko()])
    # num_players_playing = len(players_playing)
    if get_should_print():
      print("Turn: ", turn_count, " : ", num_players_playing)
    if num_players_playing == 1:
      game_cards.start_turn()
      game_cards.discard(game_cards.draw_card())
      if get_should_print():
        print('cycle')
    assert len(game_cards.deck) == 60 - (len(players) * 10) - (len(game_cards.discard_pile)) 





def main():
  args, kwargs = cmd_args.get_args()
  players = []

  for module in args[1:]:
    # print(module)
    module_name, class_name = module.split(":")
    code = __import__(module_name, level=0, globals=globals())

    players.append(player_stats_tracker.PlayerStatsTracker(getattr(code, class_name)(), name = getattr(code, class_name).title))
  
  
  # player_stats = { player : list() for player in players}
  print(kwargs)
  if kwargs.get('db') is not None:
    set_db_name(kwargs.get('db'))
  seed = int(kwargs.get('seed', '12345'))
  n = int(kwargs.get('n', '1000'))
  should_print = kwargs.get('d', 'False') == 'True'
  
  should_save = kwargs.get('s', 'True') == 'True'
  debug_game_num = int(kwargs.get('dx', '-1'))
  if debug_game_num != -1:
    should_print = False
  set_should_print(should_print)
  check_should_print()
  random.seed(seed)
  seeds = [random.randint(-(2**32),(2**32)) for i in range(n) ]
  start_time = time.time()
  i = 0
  for game_seed in seeds:
    i = i + 1
    if debug_game_num != -1 and debug_game_num == i:
      set_should_print(True)
    else:
      set_should_print(False)
    game = Game.objects.create(
      seed = game_seed
    )
    run_game(players, game_seed)
    for player in players:
      # TODO
      if should_save:
        wrapped_data_holder = player.get_turns()
        
        # player_stats[player].append(game_stats)
        wrapped_data_holder.player.save()
        # print(wrapped_data_holder.player)
        wrapped_data_holder.starting_hand.game = game
        wrapped_data_holder.starting_hand.save()
        for turn in wrapped_data_holder.turns:
          # turn.player = wrapped_data_holder.player
          turn.game = game
        Turn.objects.bulk_create(wrapped_data_holder.turns)
        
      player.reset_turns()
    game_time = time.time() - start_time
    print(f'Game {i} : Seed {game_seed} : {game_time} seconds elapsed')

  print("--- %s seconds ---" % (time.time() - start_time))


main()



