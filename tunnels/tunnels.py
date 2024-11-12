'''
if there are two cards that are less than 6 away from their ideal number, then it focuses on replacing any out of order cards between those two cards. It does so by taking off the discard pile or the draw pile to fill in the slots when possible. When the criteria of the two cards is not met, it defaults to the BiggestGoals algorithm.
'''

from config import get_should_print
from player import Player
from .biggest_first import BiggestFirstPlayer, BiggestFirstPlayer1

def abs(x):
  if (x >= 0):
    return x
  else:
    return - x

class CannotUseCardException(Exception):
  pass


class NewTunnelsPlayer(BiggestFirstPlayer):
  
  title = "Tunnels"

  def take_turn(self, game_card_tracker):
    # ((i+1)*6)-3
    self.differences = [self.hand[i] - i*6 for i in range(len(self.hand))]
    self.indexes_of_in_place_slots = [i for i in range(len(self.hand)) if abs(self.differences[i]) < 5]
    last_index = -1
    is_on_run = True
    if 0 in self.indexes_of_in_place_slots:
      last_index = 0
    for i in range(1,len(self.hand)):
      if not self.hand[i] > self.hand[i-1]:
        is_on_run = False
      if i in self.indexes_of_in_place_slots:
        if is_on_run:
          self.indexes_of_in_place_slots = self.indexes_of_in_place_slots + list(range(last_index + 1, i))
        last_index = i
        is_on_run = True

    self.indexes_of_in_place_slots.sort()    
    if len(self.indexes_of_in_place_slots) < 2:
      return super().take_turn(game_card_tracker)
    if self.indexes_of_in_place_slots == list(range(min(self.indexes_of_in_place_slots), max(self.indexes_of_in_place_slots)+1)):
      return super().take_turn(game_card_tracker)

    discard = game_card_tracker.see_discard()
    try:
      result = self.try_card(discard)
      return result
    except CannotUseCardException as cuce:
      pass
    card = game_card_tracker.draw_card()
    try:
      result = self.try_card(card, is_second=True)
      return result
    except CannotUseCardException as cuce:
      pass
    self.do_nothing(card)

  def try_card(self, discard, is_second=False):
    
    if get_should_print():
      print(f'card:{discard}, set indices:{self.indexes_of_in_place_slots}')
    discard_slot = round(discard / 6)
    if discard_slot == len(self.hand):
      discard_slot = discard_slot - 1
    # if discard_slot in self.indexes_of_in_place_slots:
    #   self.do_nothing(discard=discard)
    
    a = None
    b = None
    for i in self.indexes_of_in_place_slots:
      if self.hand[i] < discard:
        a = i
      elif b is None and self.hand[i] > discard:
        b = i

    if get_should_print():
      print(f'a:{a} b:{b}')
    # a and b are the two indexes in place around discard
    if not a is None and not b is None and not a == b - 1:
      m = (self.hand[b] - self.hand[a]) / (b - a)
      b = self.hand[a] - (m*a)
      # y = mx+b
      # discard = mx+b
      # (discard - b) / m = x
      potential_slot = int((discard - b) / m)
      if potential_slot == a:
        potential_slot = potential_slot + 1
      if not potential_slot in self.indexes_of_in_place_slots:
        self.replace_slot_with(slot=potential_slot, card=discard)
    if is_second:
      self.replace_slot_with(slot=discard_slot, card=discard)
    raise CannotUseCardException()
    
  
    


class TunnelsPlayer(BiggestFirstPlayer):
  
  title = "Tunnels"

  def take_turn(self, game_card_tracker):
    
    # ((i+1)*6)-3
    self.differences = [self.hand[i] - ((i+1)*6)-3 for i in range(len(self.hand))]
    self.indexes_of_in_place_slots = [i for i in range(len(self.hand)) if abs(self.differences[i]) < 5]
    last_index = -1
    is_on_run = True
    for i in range(1,len(self.hand)):
      if not self.hand[i] > self.hand[i-1]:
        is_on_run = False
      if i in self.indexes_of_in_place_slots:
        if is_on_run:
          self.indexes_of_in_place_slots = self.indexes_of_in_place_slots + list(range(last_index + 1, i))
        last_index = i
        is_on_run = True

    if len(self.indexes_of_in_place_slots) < 2:
      return super().take_turn(game_card_tracker)
    discard = game_card_tracker.see_discard()
    try:
      result = self.try_card(discard)
      return result
    except CannotUseCardException as cuce:
      pass
    card = game_card_tracker.draw_card()
    try:
      result = self.try_card(card)
      return result
    except CannotUseCardException as cuce:
      pass
    self.do_nothing(card)
  
  def try_card(self, card):
    slot = round(card / 6)
    if slot == 10:
      slot = 9

    print(f'slot:{slot}, set indices:{self.indexes_of_in_place_slots}')
    is_in_a_good_spot = (slot == 0 or (slot - 1 in self.indexes_of_in_place_slots and self.hand[slot] > self.hand[slot - 1])) and \
                        (slot == len(self.hand) - 1 or (slot + 1 in self.indexes_of_in_place_slots and self.hand[slot] < self.hand[slot + 1]))
    #here is wasted turns... check run                     
    if not slot in self.indexes_of_in_place_slots and not is_in_a_good_spot:
      self.replace_slot_with(slot=slot, card=card)
    # MAYBE 
    if slot != 0 and slot != len(self.hand) - 1 and self.hand[slot - 1] < card and self.hand[slot + 1] > card and not (self.hand[slot - 1] < self.hand[slot] and self.hand[slot + 1] > self.hand[slot]): #and self.differences[slot - 1] < 12  and self.differences[slot + 1] < 12:
      self.replace_slot_with(slot=slot, card=card)
    

    
    
    old_card = self.hand[slot]
    if old_card > card:
      while old_card > card and slot >= 0 and slot not in self.indexes_of_in_place_slots:
        slot = slot - 1
        old_card = self.hand[slot]
      if slot == -1:
        print(1)
        raise CannotUseCardException()
      if slot in self.indexes_of_in_place_slots:
        print(f"2 {slot} {card}")
        raise CannotUseCardException()
      self.replace_slot_with(slot=slot, card=card)
      return
    else:
      while old_card < card and slot < len(self.hand) - 1 and slot not in self.indexes_of_in_place_slots:
        slot = slot + 1
        old_card = self.hand[slot]
      if slot == len(self.hand):
        print(3)
        raise CannotUseCardException()
      if slot in self.indexes_of_in_place_slots:
        print(f"4 {slot} {card}")
        raise CannotUseCardException()
      self.replace_slot_with(slot=slot, card=card)
      return 

