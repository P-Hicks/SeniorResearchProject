from config import get_should_print
import player
import random
from orm.db.models import Turn, StartingHand, Player as PlayerRecord
from enum import Enum
import time

class WrappedDataHolder:
  def __init__(self, player, starting_hand, turns):
    self.player = player
    self.starting_hand = starting_hand
    self.turns = turns

class GameCardTrackerWrapper():

  def __init__(self, tracker):
    self._discard_card = None
    self._draw_card = None
    self.tracker = tracker
    # because this wraps AFTER turn starts 
    self.start_turn()

  def see_discard(self):
    result = self.tracker.see_discard()
    self._discard_card = result
    return result 
  
  
  def use_discard(self):
    return self.tracker.use_discard()
  
  def take_discard(self, card):
    self.tracker.take_discard(card)

  def start_turn(self):
    return self.tracker.start_turn()

  def discard(self, card):
    return self.tracker.discard(card)

  def draw_card(self):
    result =  self.tracker.draw_card()
    self._draw_card = result
    return result 
  
  def deal(self, players):
    return self.tracker.deal(players)
  

        
def print_deck_state(game_card_tracker):
  if get_should_print():
    print(f"Deck: {game_card_tracker.deck}")
    print(f"Discard Pile: {game_card_tracker.discard_pile}")
      


class PlayerStatsTracker(player.Player):
  '''
  Should track stats of player.
  '''
  @property
  def title(self):
    return self.player.title

  def __init__(self, player, name):
    self.player = player
    self.name = name
    self.player_record = PlayerRecord(name=name)
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
    self._turn_number = self._turn_number + 1
    try:
      start = time.perf_counter_ns()
      result = self.player.take_turn(wrapped_tracker)
    except player.CardUsedException as cue:
      elapsed = (time.perf_counter_ns()  - start)
      turn = Turn(
        draw_choice = wrapped_tracker._draw_card,
        discard_choice = wrapped_tracker._discard_card,
        card_used = cue.card_inserted,
        card_discarded = cue.card_discarded,
        player = self.player_record,
        turn_number = self._turn_number,
        slot = cue.slot,
        computational_time = elapsed,
      )
      turn.set_type()
      self.turns.append(turn)
      if (cue.card_discarded == game_card_tracker.see_discard()):
        wrapped_tracker.take_discard(cue.card_discarded)
      elif cue.card_inserted == game_card_tracker.see_discard():
        wrapped_tracker.use_discard()
      wrapped_tracker.discard(cue.card_discarded)
      print_deck_state(game_card_tracker)
      return
    except player.UnusedTurnException as ute:
      elapsed = (time.perf_counter_ns() - start)
      turn = Turn(
        turn_type = Turn.Types.NONE,
        draw_choice = wrapped_tracker._draw_card,
        discard_choice = wrapped_tracker._discard_card,
        card_used = None,
        card_discarded = ute.discard,
        player = self.player_record,
        turn_number = self._turn_number,
        slot = None,
        computational_time = elapsed,
      )
      self.turns.append(turn)
      if (ute.discard == game_card_tracker.see_discard()):
        wrapped_tracker.take_discard(ute.discard)
    
      wrapped_tracker.discard(ute.discard)
      print_deck_state(game_card_tracker)
      return
    
  def get_turns(self):
    return WrappedDataHolder(
      player=self.player_record,
      starting_hand=self.starting_hand,
      turns=self.turns
    )
  
  def reset_turns(self):
    self.turns = [ ]
                  

  def start_with_hand(self, hand, turn_number):
    self._has_racko = False
    self._turn_number = 0
    self.starting_hand = StartingHand(
      cards = str(hand),
      player = self.player_record,
      turn_order = turn_number
    )
    return self.player.start_with_hand(hand, turn_number)
