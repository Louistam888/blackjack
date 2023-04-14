import random 

def dealCard():
  # returns a random card from the deck
  cards = [11, 2, 3, 4, 5, 6, 7, 8,9 , 19, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculateScore(cardsInput):
  # takes a list of cards and returns the score calculated from the cards
  if sum(cardsInput) == 21 and len(cardsInput) == 2:
    return 0
  if 11 in cardsInput and sum(cardsInput) > 21:
    cardsInput.remove(11)
    cardsInput.append(1)
  return sum(cardsInput)

def compare(userScore, computerScore):
  if userScore == computerScore: 
    return "Draw"
  elif computerScore == 0: 
    return "Lose. Computer has blackjack."
  elif userScore == 0: 
    return "You win. Blackjack!"
  elif userScore > 21:
    return "You went over 21. You lose"
  elif computerScore > 21:
    return "You win. Computer went over 21"
  elif userScore > computerScore: 
    return "You win!"
  else: 
    return "You lose!"


userCards = []
computerCards = []
isGameOver = False

for _ in range(2):
  userCards.append(dealCard())
  computerCards.append(dealCard())

while not isGameOver:

  userScore = calculateScore(userCards)
  computerScore = calculateScore(computerCards)
  print(f"Your cards {userCards}. Current score: {userScore}")
  print(f"Computer's first card: {computerCards[0]}")

  if userScore == 0 or computerScore == 0 or userScore > 21: 
    isGameOver = True
  else: 
    userShouldDeal = input("Type 'y' to get another card. Type 'n' to pass.")
    if userShouldDeal == "y":
      userCards.append(dealCard())
    else: 
      isGameOver == True

while computerScore != 0 and computerScore < 17:
  computerCards.append(dealCard())
  computerScore = calculateScore(computerCards)

print(f"Your final hand: {userCards}. Your final score: {userScore}")
print(f"Computer's final hand: {computerCards}. Computer's final score: {computerScore}")
print(compare(userScore, computerScore)) 

