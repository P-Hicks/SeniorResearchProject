from ..biggest_first import BiggestFirstPlayer

class MockGameCardTracker:

    def __init__(self, top_discard=None, top_pile=None):
        self._top_discard = top_discard
        self._top_pile = top_pile
        self._num_times_drawn_discard = 0
        self._num_times_drawn_pile = 0
    
    def see_discard(self):
        if self._num_times_drawn_discard > 0 or self._num_times_drawn_pile > 0:
            raise Exception("Doing funky draws... likely fudging turn")
        if self._top_discard is None:
            raise Exception("No discard set")
        return self._top_discard
    
    def draw_card(self):
        if self._num_times_drawn_pile > 0:
            raise Exception("Doing funky draws... likely fudging turn")
        if self._top_pile is None:
            raise Exception("No pile card set")
        return self._top_pile


def test_1():
    hand = [10, 30, 20, 40, 60, 50, 25, 32, 11, 55]
    player = BiggestFirstPlayer()
    player.start_with_hand(hand)
    potential_cards = MockGameCardTracker(top_discard=4)
    discarded_card = player.take_turn(potential_cards)
    assert player.hand[0] == 4
    assert discarded_card == 10

def test_2():
    hand = [5, 30, 20, 40, 60, 50, 25, 32, 11, 55]
    player = BiggestFirstPlayer()
    player.start_with_hand(hand)
    potential_cards = MockGameCardTracker(top_discard=4, top_pile=14)
    discarded_card = player.take_turn(potential_cards)
    assert player.hand[0] == 5
    assert player.hand[1] == 30
    assert player.hand[2] == 14
    assert discarded_card == 20