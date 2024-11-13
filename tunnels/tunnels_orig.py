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


class TunnelsPlayer1(BiggestFirstPlayer):
  title = "Tunnels111"

  boolean = False
  
  def take_turn(self, game_card_tracker):
      discard = game_card_tracker.see_discard()

      displacement = 0
      ii = 0
      first_number = 0
      second_number = 0
      for i in range(10):
        ii = i
        if (abs(self.hand[i]-((i+1)*6))< 5):
          if not self.boolean:
            first_number = i
            break
        
        else:
          self.boolean = True
       
      
      if ii == 10:
        super().take_turn(game_card_tracker)
      
      for i in range(10):
        ii = i
        if (abs(self.hand[i]-((i+1)*6))< 5 and i != first_number and i != first_number - 1 and i != first_number + 1): # i is not 1st num
          second_number = i
        
      


      
      if ii == 10:
        super().take_turn(game_card_tracker)
        

      if first_number > second_number:
        ii = second_number
        second_number = first_number
        first_number = ii
      
      
      for i in range(first_number+1, second_number):
        ii = i
        if self.hand[i] < self.hand[i-1] or self.hand[i]+(second_number-i) > second_number:
          if discard > self.hand[i] and discard+(second_number-i) < second_number:

            self.replace_slot_with(slot=i, card=discard)
          else:
            card = game_card_tracker.draw_card()
            self.replace_slot_with(slot=i, card=card)
          
          break
        
      
      if ii == second_number:
        self.boolean = True
      self.do_nothing(discard)

  
    