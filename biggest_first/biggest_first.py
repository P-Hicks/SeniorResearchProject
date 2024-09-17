from player import Player

def abs(x):
  if (x >= 0):
    return x
  else:
    return - x

class BiggestFirstPlayer(Player):
  '''
  BiggestGoals essentially categorizes cards/slots into 3 categories by the difference of the card value from their ideal number. If the difference is greater than 6, they will use discards to replace it, otherwise, they will only replace that card by drawn cards. 
  '''
  title = f"BiggestFirst"
  
  def take_turn(self, game_card_tracker):
    discard = game_card_tracker.see_discard()
    slot = int(discard / 6)
    old_card = self.hand[slot]
    difference = abs(old_card - (6*slot))
    if (difference > 6):
      self.replace_slot_with(slot=slot, card=discard)
      return
    card = game_card_tracker.draw_card()
    slot = int(card / 6)
    self.replace_slot_with(slot=slot, card=card)