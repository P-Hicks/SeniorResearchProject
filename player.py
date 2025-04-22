
from config import get_should_print


class CardUsedException(Exception):
  def __init__(self, card_inserted, card_discarded, slot):
    self.card_inserted = card_inserted
    self.card_discarded = card_discarded
    self.slot = slot

class UnusedTurnException(Exception):
  def __init__(self, discard):
    self.discard = discard

class Player:
  def has_racko(self):
    i = -1
    for next in self.hand:
      if (next < i):
        return False
      i = next
    return True
  
  def take_turn(self, game_card_tracker):
    pass

  def start_with_hand(self, hand, turn_number):
    self.hand = hand

  def replace_slot_with(self, slot, card):
    old_card = self.hand[slot]
    self.hand[slot] = card
    if get_should_print():
      print(f'{self.title}:Replaced {old_card} at {slot} with {card} for {self.hand}')
    raise CardUsedException(
      card_inserted=card,
      slot=slot,
      card_discarded=old_card
    )
    # return old_card
  
  def do_nothing(self, discard):
    if get_should_print():
      print(f'{self.title}:Did nothing with {discard} for {self.hand}')
    raise UnusedTurnException(discard=discard)

