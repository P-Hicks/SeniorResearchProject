
class Player:
  def has_racko(self):
    i = -1
    for next in self.hand:
      if (next < i):
        return False
      i = next
    return True
  
  def take_turn(self, game_card_tracker):
    pass

  def start_with_hand(self, hand):
    self.hand = hand

  def replace_slot_with(slot, card):
    old_card = self.hand[slot]
    slef.hand[slot] = card
    return old_card

  # def replace_when(slot, card, condition, step):
  #   '''
  #   condition = condition(card_in_slot, card)
  #   step = step(i)
  #   '''
  #   while not condition(self.hand[slot], card):
  #     slot = step(slot)
  #   if slot < 0 or slot > len(self.hand):
  #     raise Exception("")
  #   return replace_slot_with(slot, card)
  
  # def place_near_when(slot, card, condition):
  #   if (self.hand[slot] > card):
  #     return self.replace_when(slot, card, lamda i : condition, lambda i : i - 1)
  #   else:
  #     return self.replace_when(slot, card, lambda i : condition, lambda i : i + 1)
