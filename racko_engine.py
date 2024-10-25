from main import setup1, setup2
setup1()
setup2()

import random
from player import Player
random.seed(12345)

import game_card_tracker
from orm.db.models import *
import player_stats_tracker
import cmd_args

from statistics import stdev, mean

import time

def run_game(players, seed):
  num_players_playing = len(players)
  
  game_cards = game_card_tracker.GameCardTracker(seed=seed)
  game_cards.deal(players)
  turn_count = 0
  while (num_players_playing > 0):
    turn_count = turn_count = 1 + turn_count
    for player in players:
      if (not player.has_racko()):
        game_cards.start_turn()
        top_discard = game_cards.see_discard()
        discard = player.take_turn(game_cards)
        # game_cards.discard(discard)
      players_playing = []
      for player in players:
        if player.has_racko():
          print(player.title + " has racko")
        else:
          players_playing.append(player)
      # num_players_playing = len([player for player in players if not player.has_racko()])
      num_players_playing = len(players_playing)
      print(num_players_playing)
      if num_players_playing == 1:
        game_cards.start_turn()
        game_cards.discard(game_cards.draw_card())




def main():
  args, kwargs = cmd_args.get_args()
  players = []

  for module in args[1:]:
    print(module)
    module_name, class_name = module.split(":")
    code = __import__(module_name, level=0, globals=globals())

    players.append(player_stats_tracker.PlayerStatsTracker(getattr(code, class_name)(), name = getattr(code, class_name).title))
  
  
  # player_stats = { player : list() for player in players}
  
  seed = int(kwargs.get('seed', '12345'))
  n = int(kwargs.get('n', '1000'))
  random.seed(seed)
  seeds = [random.randint(-(2**32),(2**32)) for i in range(n) ]
  start_time = time.time()
  i = 0
  for game_seed in seeds:
    i = i + 1
    game = Game.objects.create(
      seed = game_seed
    )
    run_game(players, game_seed)
    for player in players:
      # TODO
      wrapped_data_holder = player.get_turns()
      
      # player_stats[player].append(game_stats)
      wrapped_data_holder.player.save()
      wrapped_data_holder.starting_hand.game = game
      wrapped_data_holder.starting_hand.save()
      for turn in wrapped_data_holder.turns:
        turn.game = game
      Turn.objects.bulk_create(wrapped_data_holder.turns)
      
      player.reset_turns()
    game_time = time.time() - start_time
    print(f'Game {i} : Seed {seed} : {game_time} seconds elapsed')

  print("--- %s seconds ---" % (time.time() - start_time))


main()

