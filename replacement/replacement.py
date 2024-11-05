'''
the Replacement algorithm looks at the top of the discard deck, and figures out its ideal slot (rounding its value divided by 6). Then, it either replaces the card there, or one of its neighbors, depending on whether or not it or its neighbors are within 6 of their ideal numbers (or the ideal number of the ideal slot of the top discard card).
'''

from player import Player


class ReplacementPlayer(Player):
  
  title = "Replacement"

  def take_turn(self, game_card_tracker):
    discard = game_card_tracker.see_discard()
    
    self.try_card(discard)
    other_card = game_card_tracker.draw_card()
    self.try_card(other_card, is_second= True)
    self.do_nothing(other_card)
    return
  
  def has_improved_condition(self, card, slot, is_second = False):
    check_1 = not (self.hand[slot - 1] < self.hand[slot] and self.hand[slot] < self.hand[slot + 1]) and (self.hand[slot - 1] < card and card < self.hand[slot + 1])
    if check_1:
      return True
    check_2 = not (self.hand[slot - 1] < self.hand[slot] or self.hand[slot] < self.hand[slot + 1]) and (self.hand[slot - 1] < card or card < self.hand[slot + 1])
    if not is_second or check_2:
      return check_2
    check_3 = (self.hand[slot - 1] < self.hand[slot]) == (self.hand[slot - 1] < card) and (self.hand[slot] < self.hand[slot + 1]) == (card < self.hand[slot + 1])
    return check_3


  def try_card(self, discard, is_second = False):
    slot = int(discard / 6)
    old_card = self.hand[slot]
    real_difference = old_card - (6*slot)
    abs_difference = abs(real_difference)
    if (abs_difference > 5):
      self.replace_slot_with(slot=slot, card=discard)
      return
    if (old_card > discard):
      while slot > 0 and self.hand[slot] > discard:
        slot = slot - 1
      if slot < 0:
        return
      if slot == 0 and not self.hand[1] > self.hand[0]:
        self.replace_slot_with(slot=slot, card=discard)
      elif not slot == 0 and self.has_improved_condition(discard, slot):
        self.replace_slot_with(slot=slot, card=discard)
      elif not slot == 0 and is_second and self.has_improved_condition(discard, slot, is_second=True):
        self.replace_slot_with(slot=slot, card = discard)
      return
    else:
      while slot < len(self.hand) and self.hand[slot] < discard:
        slot = slot + 1
      max_num = len(self.hand)
      if (slot >= max_num):
        return
      if slot == max_num - 1 and (not self.hand[slot - 1] < self.hand[slot]):
        self.replace_slot_with(slot=slot, card=discard)
      elif not slot == max_num - 1 and self.has_improved_condition(discard, slot):
        self.replace_slot_with(slot=slot, card=discard)
      elif not slot == max_num - 1 and is_second and self.has_improved_condition(discard, slot, is_second=True):
        self.replace_slot_with(slot=slot, card = discard)
      return
    