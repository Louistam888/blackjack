import random 

def dealCard():
  # returns a random card from the deck
  cards = [11, 2, 3, 4, 5, 6, 7, 8,9 , 19, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

userCards = []
computerCards = []

for _ in range(2):
  userCards.append(dealCard())
  computerCards.append(dealCard())