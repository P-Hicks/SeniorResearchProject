import random
from player import Player
random.seed(12345)

import game_card_tracker
  
import player_stats_tracker
import cmd_args

from statistics import stdev, mean

class Stats:

  def __init__(self, lst, f):
    f_lst = [f(i) for i in lst]
    self.mean = float(mean(f_lst))
    self.std_dev = float(stdev(f_lst, self.mean))

def avg(lst, f):
    sum_of_list = 0
    for i in range(len(lst)):
        sum_of_list += f(lst[i])
    average = sum_of_list/len(lst)
    return average

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
        game_cards.discard(discard)

      num_players_playing = len([player for player in players if not player.has_racko()])
      if num_players_playing == 1:
        game_cards.start_turn()
        game_cards.discard(game_cards.draw_card())




def main():
  args, kwargs = cmd_args.get_args()
  players = []

  for module in args[1:]:
    code = __import__(module, level=0, globals=globals())
    players.append(player_stats_tracker.PlayerStatsTracker(code.SimplePlayer(), name = code.SimplePlayer.title))
  
  player_stats = { player : list() for player in players}
  
  seed = int(kwargs.get('seed', '12345'))
  n = int(kwargs.get('n', '1000'))
  random.seed(seed)
  seeds = [random.randint(-(2**32),(2**32)) for i in range(n) ]
  for game_seed in seeds:
    run_game(players, game_seed)
    for player in players:
      game_stats = player.get_turns()
      player_stats[player].append(game_stats)
      player.reset_turns()
  for player in players:
    game_stats_list = player_stats[player]
    punused_stats = Stats(game_stats_list, lambda s : (s.num_unused_turns / s.num_turns))
    pdraw_stats = Stats(game_stats_list, lambda s : (s.num_draws_used / s.num_turns))
    pdiscard_stats = Stats(game_stats_list, lambda s : (s.num_discards_used / s.num_turns))
    unused_stats = Stats(game_stats_list, lambda s : (s.num_unused_turns))
    draw_stats = Stats(game_stats_list, lambda s : (s.num_draws_used))
    discard_stats = Stats(game_stats_list, lambda s : (s.num_discards_used))
    
    turns_stats = Stats(game_stats_list, lambda s : s.num_turns)
    print(player.player.title)
    # for game in game_stats_list:
    #   print(f"t:{game.num_turns} dr:{game.num_draws_used} di:{game.num_discards_used} un:{game.num_unused_turns} ")
    print("\tTurns: {:.2f}(+-{:.2f})".format(turns_stats.mean, turns_stats.std_dev))
    print("\t% Draws: {:.5f}(+-{:.5f})".format(100* pdraw_stats.mean, 100*pdraw_stats.std_dev))
    print("\t% Discards: {:.5f}(+-{:.5f})".format(100* pdiscard_stats.mean, 100*pdiscard_stats.std_dev))
    print("\t% Unused: {:.5f}(+-{:.5f})".format(100* punused_stats.mean, 100*punused_stats.std_dev))
    print("\tDraws: {:.2f}(+-{:.2f})".format(draw_stats.mean, draw_stats.std_dev))
    print("\tDiscards: {:.2f}(+-{:.2f})".format(discard_stats.mean, discard_stats.std_dev))
    print("\tUnused: {:.2f}(+-{:.2f})".format(unused_stats.mean, unused_stats.std_dev))


    

main()

