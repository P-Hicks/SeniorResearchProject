import player
import random 

class TurnStats:
  def __init__(self):
    self.used_discard = False
    self.used_draw_pile = False

class GameCardTrackerWrapper():
  def __init__(self, tracker):
    self.tracker = tracker

  def see_discard(self):
    return self.tracker.see_discard()

  def start_turn(self):
    self.turn_stats = TurnStats()
    return self.tracker.start_turn()

  def discard(self, card):
    return self.tracker.discard(card)

  def draw_card(self):
    return self.tracker.draw_card()
    
  def deal(self, players):
    return self.tracker.deal(players)
  
  def get_turn_stats(self):
    pass


class PlayerStatsTracker(player.Player):
  '''
  Should track stats of player.
  '''

  def __init__(self, player, name):
    self.player = player
    self.name = name

    self._has_racko = False

  def has_racko(self):
    result = self.player.has_racko()
    if (result is True):
      self._has_racko = True
    return result
    
  def take_turn(self, game_card_tracker):
    if (self._has_racko):
      raise Exception("I have racko, i wont take a turn.")
    wrapped_tracker = 
    result = self.player.take_turn(wrapped_tracker)

  def start_with_hand(self, hand):
    self._has_racko = False

