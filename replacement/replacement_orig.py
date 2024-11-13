
from biggest_first.biggest_first import BiggestFirstPlayer1
from player import Player


class ReplacementPlayer1(BiggestFirstPlayer1):
  
  title = "Replacement111"

  def take_turn(self, game_card_tracker):
    discard = game_card_tracker.see_discard()
    i = int(discard / 6)
    if discard % 6 < 3 and i != 0:
      i = i - 1
    elif abs(self.hand[i]-((i+1)*6)) < 5  and discard < self.hand[i] and i != 0:
      i = i - 1
    elif abs(self.hand[i]-((i+1)*6)) < 5  and discard > self.hand[i] and i != 9:
      i = i + 1



    if abs(self.hand[i]-((i+1)*6)) > 5:
      self.replace_slot_with(slot=i, card = discard)
    
    super().take_turn(game_card_tracker)
    self.do_nothing(discard)