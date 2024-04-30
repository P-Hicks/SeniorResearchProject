from player import Player

class SimplePlayer(Player):
  
  def take_turn(self, game_card_tracker):

    print("taking turn")
    slot = int(game_card_tracker.see_discard() / 6)
    old_card = self.hand[slot]
    if (int(old_card / 6) == slot): 
      
      card = game_card_tracker.draw_card()
      slot = int(card / 6)
      old_card = self.hand[slot]
      self.hand[slot] = card
    else:
      self.hand[slot] = game_card_tracker.see_discard()

    

    print(self.hand)

    return old_card