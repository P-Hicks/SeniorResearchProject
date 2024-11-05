from player import UnusedTurnException
from ..replacement import ReplacementPlayer

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
    hand = [25, 17, 12, 18, 27, 59, 1, 47, 48, 0]
    player = ReplacementPlayer()
    player.start_with_hand(hand)
    potential_cards = MockGameCardTracker(top_discard=49,top_pile=1)
    try:
        discarded_card = player.take_turn(potential_cards)
    except UnusedTurnException:
        assert False
    except Exception:
        pass
    assert hand == [1, 17, 12, 18, 27, 59, 1, 47, 48, 0]
    