'''
if there are two cards that are less than 6 away from their ideal number, then it focuses on replacing any out of order cards between those two cards. It does so by taking off the discard pile or the draw pile to fill in the slots when possible. When the criteria of the two cards is not met, it defaults to the BiggestGoals algorithm.
'''

from player import Player
from .biggest_first import BiggestFirstPlayer

def abs(x):
  if (x >= 0):
    return x
  else:
    return - x

class TunnelsPlayer(BiggestFirstPlayer):
  
  title = "Tunnels"

  def take_turn(self, game_card_tracker):
    self.differences = [self.hand[i] - (i*6) for i in range(len(self.hand))]
    self.indexes_of_in_place_slots = [i for i in range(len(self.hand)) if abs(self.differences[i]) <= 6]
    if len(self.indexes_of_in_place_slots) < 2 or True:
      return super().take_turn(game_card_tracker)
    discard = game_card_tracker.see_discard()
    try:
      result = self.try_card(discard)
      return result
    except:
      pass
    card = game_card_tracker.draw_card()
    try:
      result = self.try_card(card)
      return result
    except:
      pass
    return card
  
  def try_card(self, card):
    slot = int(card / 6)
    if not slot in self.indexes_of_in_place_slots:
      old_card = self.hand[slot]
      self.hand[slot] = card
      return old_card
    raise Exception()
    old_card = self.hand[slot]
    if old_card > card:
      while old_card > card and slot >= 0 and slot not in self.indexes_of_in_place_slots:
        slot = slot - 1
        old_card = self.hand[slot]
      if slot == 0:
        raise Exception()
      self.hand[slot] = card
      return old_card
    else:
      while old_card < card and slot < len(self.hand) and slot not in self.indexes_of_in_place_slots:
        slot = slot + 1
        old_card = self.hand[slot]
      if slot >= len(self.hand):
        raise Exception()
      self.hand[slot] = card
      return old_card