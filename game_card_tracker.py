import random
class ExtraCardDrawn(Exception):
  pass

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

  def use_discard(self):
    self.discard_pile.pop(0)

  def take_discard(self, card):
    assert card == self.discard_pile[0]
    self.discard_pile.remove(card)

  def start_turn(self):
    self.can_take_card = True
    if (len(self.deck) == 0):
      self.deck = self.discard_pile[1:]
      self.discard_pile = [self.discard_pile[0]]
      random.shuffle(self.deck)
      

  def discard(self, card):
    assert card not in self.discard_pile
    assert card not in self.deck
    self.discard_pile.insert(0, card)


  def draw_card(self):
    if (self.can_take_card):
      self.can_take_card = False
      return self.deck.pop()
    else:
      raise ExtraCardDrawn("Can only draw 1 card")
    
  def deal(self, players):
    for i in range(len(players)):
      players[i].start_with_hand(self.deck[0:10], i)
      self.deck = self.deck[10:]