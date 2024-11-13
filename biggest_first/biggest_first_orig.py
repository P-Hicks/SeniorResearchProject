from player import Player



class BiggestFirstPlayer1(Player):
  
  title = f"BiggestFirst111"
  howManyTimes=0
  previosNumber = 0

  def take_turn(self, game_card_tracker):
    discard = game_card_tracker.see_discard()
    i = 0
    displacement = 0

    for  n in range(9):
      if (abs(self.hand[n]-((n+1)*6))>displacement and ((abs(self.hand[n+1]-((n+2)*6))>5 or self.hand[n] > self.hand[n+1]) or (abs(self.hand[n-1]-((n)*6))>5 or self.hand[n-1] > self.hand[n]))):
        if (self.howManyTimes < 10 or n != self.previosNumber or n == 0):
          displacement = abs(self.hand[n]-((n+1)*6))
          i = n
        else:
          displacement = abs(self.hand[n-1]-((n)*6))
          i = n-1
          self.howManyTimes = 0
        
        
    if (i == self.previosNumber):
      self.howManyTimes = self.howManyTimes + 1
        
    self.previosNumber = i;
    if ((abs(discard-((i+1)*6)) <5) and (discard < self.hand[i+1] or  (abs(self.hand[i+1]-((i+2)*6)) <5))):
      
      self.replace_slot_with(slot=i, card=discard)
    else:
      card = game_card_tracker.draw_card()
      self.replace_slot_with(slot=i, card=card)
    self.do_nothing(game_card_tracker.draw_card())

    