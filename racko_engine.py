import random
from player import Player
random.seed(12345)

import game_card_tracker
  

  
num_turns = []

def run_game(players):
  num_players_playing = len(players)
  game_cards = game_card_tracker.GameCardTracker(seed=12345)
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
  print(turn_count)
  num_turns.append(turn_count)


import cmd_args

def main():
  args, kwargs = cmd_args.get_args()
  players = []
  for module in args[1:]:
    code = __import__(module)
    players.append(code.SimplePlayer())

  for i in range(1000):
    run_game(players)

main()
print(sum(num_turns) / len(num_turns))

