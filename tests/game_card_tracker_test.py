import random

from game_card_tracker import ExtraCardDrawn, GameCardTracker
from player import Player
# from player_stats_tracker import PlayerStatsTracker

def test_does_initialize_deck_properly():
  gct = GameCardTracker()
  checks = [0 for i in range(60)]
  for i in gct.deck:
    checks[i] = 1
  assert checks.count(1) == 59
  assert checks.count(0) == 1




def test_drawing_cards_1():
  gct = GameCardTracker()
  gct.deck = [5, 4, 3, 2, 1]
  gct.discard_pile = [6, 7, 8, 9, ]
  gct.start_turn()
  assert gct.see_discard() == 6
  assert gct.draw_card() == 1


def test_drawing_cards_2():
  gct = GameCardTracker()
  gct.deck = [5, 4, 3, 2, 1]
  gct.discard_pile = [6, 7, 8, 9, ]
  gct.start_turn()
  assert gct.draw_card() == 1
  try:
    gct.draw_card()
    assert False
  except ExtraCardDrawn:
    pass


def test_drawing_cards_3():
  gct = GameCardTracker()
  gct.deck = [5, 4, 3, 2, 1]
  gct.discard_pile = [6, 7, 8, 9, ]
  gct.start_turn()
  assert gct.draw_card() == 1
  gct.discard(1)
  gct.start_turn()
  assert gct.see_discard() == 1

class MockPlayer(Player):

  def __init__(self):
    pass

  def setup_turn_to_discard(self, slot):
    self.slot = slot

  def take_turn(self, game_card_tracker):
    self.replace_slot_with(slot=self.slot, card = game_card_tracker.see_discard())

# def test_drawing_cards_4():
#   '''
#   IMPORTANT: TESTS IF DISCARD CARDS ARE ACTUALLY USED
#   '''
#   gct = GameCardTracker()
#   gct.deck = [10, 11, 12]
#   gct.discard_pile = [5, 4, 3, 2, 1]
#   player = MockPlayer()
#   player.hand = list(range(101, 111))
#   gameplayer = PlayerStatsTracker(player)
#   player.setup_turn_to_discard(0)
#   gameplayer.take_turn(gct)
#   assert gct.see_discard() == 101
#   assert not 5 in gct.discard_pile
#   player.setup_turn_to_discard(1)
#   gameplayer.take_turn(gct)
#   assert gct.see_discard() == 102
#   assert not 4 in gct.discard_pile
  
def test_reshuffle_1():
  gct = GameCardTracker()
  gct.deck = list(range(5))
  gct.deck.reverse()
  gct.discard_pile = [11]
  for i in range(5):
    gct.start_turn()
    assert gct.draw_card() == i
    gct.discard(i+6)
  new_draws = []  
  for i in range(5):
    gct.start_turn()
    card =  gct.draw_card() 
    assert card > 5
    new_draws.append(card)

  new_draws.sort()
  missing = [i for i in list(range(6,12)) if i not in new_draws]
  assert len(missing) == 1
  assert missing[0] in list(range(6,12))
  
  

def test_dealing_cards_1():
  gct = GameCardTracker()
  gct.deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
  gct.discard_pile = [12]
  gct.start_turn()
  player = Player()
  gct.deal([player])
  assert player.hand == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  assert gct.deck == [11]



def test_dealing_cards_2():
  gct = GameCardTracker()
  gct.deck = list(range(1,31))
  gct.discard_pile = [12]
  gct.start_turn()
  p1 = Player()
  p2 = Player()
  gct.deal([p1, p2])
  assert p1.hand == list(range(1, 11))
  assert p2.hand == list(range(11, 21))
  assert gct.deck == list(range(21, 31))




# class GameCardTracker:
#   def __init__(self, seed=1):
#     self.deck = list(range(0,60))
#     random.seed(seed)
#     random.shuffle(self.deck)
#     self.discard_pile = []
#     self.discard_pile.insert(0, self.deck.pop())
#     self.can_take_card = False

#   def see_discard(self):
#     return self.discard_pile[0]

#   def start_turn(self):
#     self.can_take_card = True
#     if (len(self.deck) == 0):
#       self.deck = self.discard_pile[1:]
#       self.discard_pile = [self.discard_pile[0]]
#       random.shuffle(self.deck)
      

#   def discard(self, card):
#     self.discard_pile.insert(0, card)


#   def draw_card(self):
#     if (self.can_take_card):
#       return self.deck.pop()
#     else:
#       raise Exception("Can only draw 1 card")
    
#   def deal(self, players):
#     for i in range(len(players)):
#       players[i].start_with_hand(self.deck[0:10], i)
#       self.deck = self.deck[11:]