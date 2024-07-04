import random
from art import logo
from replit import clear

# Initial balance
player_balance = 1000

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)

def calculate_score(cards):
  score = sum(cards)
  if score == 21 and len(cards) == 2:
      return 0
  if score > 21 and 11 in cards:
      cards.remove(11)
      cards.append(1)
  return sum(cards)

def compare(user_score, computer_score):
  if computer_score == 0:
      return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
      return "Win with a Blackjack 😎"
  elif computer_score > 21:
      return "Opponent went over. You win 😁"
  elif user_score > 21:
      return "You went over. You lose 😭"
  elif computer_score == user_score:
      return "Draw 🙃"
  elif computer_score > user_score:
      return "You lose 😤"
  elif computer_score < user_score:
      return "You win 😃"

def play_hand(hand, bet, computer_hand):
  global player_balance
  game_over = False

  while not game_over:
    score = calculate_score(hand)

    print(f"\tYour hand: {hand}, current score: {sum(hand)}")
    print(f"\tComputer's first card: {computer_hand[0]}")

    if score == 0 or score > 21:
      game_over = True
    elif score < 21:
      draw_card = input("Type 'y' to get another card, type 'n' to pass, or type 'd' to double down: ")
      if draw_card == 'y':
        hand.append(deal_card())
      elif draw_card == 'd':
        if len(hand) == 2:
          bet *= 2
          hand.append(deal_card())
          game_over = True
        else:
          print("You can only double down on your first two cards.")

    return hand, bet

def play_game():
  global player_balance
  print(logo)

  user_hand = []
  computer_hand = []

  for _ in range(2):
      user_hand.append(deal_card())
      computer_hand.append(deal_card())

  user_score = 0
  computer_score = 0

  bet = int(input(f"You have ${player_balance}. How much would you like to bet? "))

  # Offer insurance if dealer's first card is an Ace
  if computer_hand[0] == 11:
    insurance = input("Dealer has an Ace. Would you like to take insurance? Type 'y' or 'n': ")
    if insurance == 'y':
      insurance_bet = bet / 2
    else:
      insurance_bet = 0
  else:
    insurance_bet = 0

  # Dealer's turn
  while computer_score < 17:
      computer_hand.append(deal_card())
      computer_score = calculate_score(computer_hand)

  # Check for split option
  if user_hand[0] == user_hand[1]:
    split = input("You have a pair. Would you like to split? Type 'y' or 'n': ")
    if split == 'y':
        hand1 = [user_hand[0], deal_card()]
        hand2 = [user_hand[1], deal_card()]
        print("Playing first hand...")
        hand1, bet1 = play_hand(hand1, bet, computer_hand)
        print("Playing second hand...")
        hand2, bet2 = play_hand(hand2, bet, computer_hand)
        user_hands = [(hand1, bet1), (hand2, bet2)]
    else:
        user_hands = [(play_hand(user_hand, bet, computer_hand))]
  else:
    user_hands = [(play_hand(user_hand, bet, computer_hand))]

  # print(f"\tComputer's final hand: {computer_hand}, final score: {sum(computer_hand)}")

  # Resolve insurance bet
  if insurance_bet > 0 and computer_score == 0:
    player_balance += 2 * insurance_bet
    print("Insurance bet won! Dealer has Blackjack.")
  elif insurance_bet > 0:
    player_balance -= insurance_bet
    print("Insurance bet lost. Dealer does not have Blackjack.")

  for hand, bet in user_hands:
    user_score = calculate_score(hand)
    print(f"\tYour final hand: {hand}, final score {sum(hand)}")
    print(f"\tComputer's final hand: {computer_hand}, final score: {sum(computer_hand)}")
    result = compare(user_score, computer_score)
    print(result)
    if "win" in result.lower():
        player_balance += bet
    elif "lose" in result.lower():
        player_balance -= bet

  play_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
  if play_again == 'y':
      clear()
      play_game()

want_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if want_to_play == 'y':
    clear()
    play_game()