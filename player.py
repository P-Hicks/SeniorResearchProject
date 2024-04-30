
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

  def start_with_hand(self, hand):
    self.hand = hand