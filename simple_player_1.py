from player import Player

class SimplePlayer(Player):
  
  title = "Simple Player 1"


  def take_turn(self, game_card_tracker):
    slot = int(game_card_tracker.see_discard() / 6)
    old_card = self.hand[slot]
    self.hand[slot] = game_card_tracker.see_discard()
    return old_card
  
