import random

class GameCardTracker:
  def __init__(self, seed=1):
    self.deck = list(range(0,60))
    random.seed(seed)
    random.shuffle(self.deck)
    self.discard_pile = []
    self.discard_pile.insert(0, self.deck.pop())
    self.can_take_card = False

  def see_discard(self):
    return self.discard_pile[0]

  def start_turn(self):
    self.can_take_card = True
    if (len(self.deck) == 0):
      self.deck = self.discard_pile[1:]
      self.discard_pile = [self.discard_pile[0]]
      random.shuffle(self.deck)
      

  def discard(self, card):
    self.discard_pile.insert(0, card)


  def draw_card(self):
    if (self.can_take_card):
      return self.deck.pop()
    else:
      raise Exception("Can only draw 1 card")
    
  def deal(self, players):
    for i in range(len(players)):
      players[i].start_with_hand(self.deck[0:10])
      self.deck = self.deck[11:]