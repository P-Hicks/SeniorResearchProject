import player
import random

from enum import Enum

class TurnEnum(Enum):
  USED_DISCARD = 0
  USED_DRAW = 1
  DID_NOTHING = 2

class TurnStats:
  def __init__(self):
    self.turn_type = None

  def __str__(self):
    return str(self.turn_type)

class GameCardTrackerWrapper():
  def __init__(self, tracker):
    self.tracker = tracker
    self.turn_stats = TurnStats()
    self.card = None
    # because this wraps AFTER turn starts 
    self.start_turn()

  def see_discard(self):
    return self.tracker.see_discard()
    

  def start_turn(self):
    self.turn_stats = TurnStats()
    self.turn_stats.turn_type = TurnEnum.USED_DISCARD
    return self.tracker.start_turn()

  def discard(self, card):
    return self.tracker.discard(card)

  def draw_card(self):
    self.turn_stats.turn_type = TurnEnum.USED_DRAW
    result =  self.tracker.draw_card()
    self.card = result
    return result 
  
  def deal(self, players):
    return self.tracker.deal(players)
  
  def get_turn_stats(self):
    return self.turn_stats


class GameData:

  def __init__(self, turns):
    self.num_turns = len(turns)
    self.num_unused_turns = 0
    self.num_discards_used = 0
    self.num_draws_used = 0
    for turn in turns:
      if (turn.turn_type == TurnEnum.DID_NOTHING):
        self.num_unused_turns += 1
      if (turn.turn_type == TurnEnum.USED_DISCARD):
        self.num_discards_used += 1
      if (turn.turn_type == TurnEnum.USED_DRAW):
        self.num_draws_used += 1


        



class PlayerStatsTracker(player.Player):
  '''
  Should track stats of player.
  '''

  def __init__(self, player, name):
    self.player = player
    self.name = name

    self._has_racko = False
    self.turns = [ ]

  def has_racko(self):
    result = self.player.has_racko()
    if (result is True):
      self._has_racko = True
    return result
    
  def take_turn(self, game_card_tracker):
    if (self._has_racko):
      raise Exception("I have racko, i wont take a turn.")
    wrapped_tracker = GameCardTrackerWrapper(game_card_tracker)
    result = self.player.take_turn(wrapped_tracker)
    stats = wrapped_tracker.get_turn_stats()
    if (result == wrapped_tracker.card):
      stats.turn_type = TurnEnum.DID_NOTHING
    self.turns.append(stats)
    return result

  def get_turns(self):
    return GameData(self.turns)
  
  def reset_turns(self):
    self.turns = [ ]
                  

  def start_with_hand(self, hand):
    self._has_racko = False
    return self.player.start_with_hand(hand)
