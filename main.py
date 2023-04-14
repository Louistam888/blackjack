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

def calculate_score(cardsInput):
  if 11 in cardsInput and 10 in cardsInput and len(cardsInput) == 2:
    if sum(cardsInput) == 21 and len(cardsInput) == 2:
      return 0
    if 11 in cardsInput and sum(cardsInput) > 21:
      cardsInput.remove(11)
      cardsInput.append(1)
  return sum(cardsInput)