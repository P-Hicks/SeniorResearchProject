from player import Player

def abs(x):
  if (x >= 0):
    return x
  else:
    return - x

class SimplePlayer(Player):
  
  title = "BiggestFirst"

  def take_turn(self, game_card_tracker):
    discard = game_card_tracker.see_discard()
    slot = int(discard / 6)
    old_card = self.hand[slot]
    difference = abs(old_card - (6*slot))
    if (difference > 6):
      self.hand[slot] = discard
      return old_card

    card = game_card_tracker.draw_card()
    slot = int(card / 6)
    old_card = self.hand[slot]
    self.hand[slot] = card

    return old_card