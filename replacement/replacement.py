'''
the Replacement algorithm looks at the top of the discard deck, and figures out its ideal slot (rounding its value divided by 6). Then, it either replaces the card there, or one of its neighbors, depending on whether or not it or its neighbors are within 6 of their ideal numbers (or the ideal number of the ideal slot of the top discard card).
'''

from player import Player


class ReplacementPlayer(Player):
  
  title = "Replacement"

  def take_turn(self, game_card_tracker):
    discard = game_card_tracker.see_discard()
    slot = int(discard / 6)
    old_card = self.hand[slot]
    real_difference = old_card - (6*slot)
    abs_difference = abs(real_difference)
    if (abs_difference > 6):
      self.replace_slot_with(slot=slot, card=discard)
      return
    if (old_card > discard):
      while slot > 0 and self.hand[slot] > discard:
        slot = slot - 1
      if slot < 0:
        return self.do_nothing(discard=discard)
      self.replace_slot_with(slot=slot, card=discard)
      return
    else:
      while slot < len(self.hand) and self.hand[slot] < discard:
        slot = slot + 1
      if (slot >= len(self.hand)):
        return self.do_nothing(discard=discard)
      self.replace_slot_with(slot=slot, card=discard)
      return
    self.do_nothing(discard)