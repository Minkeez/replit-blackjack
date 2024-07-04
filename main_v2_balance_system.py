import random
from art import logo
from replit import clear

# Initial balance
player_balance = 1000

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)

def calculate_score(card):
  score = sum(card)
  if score == 21 and len(card) == 2:
    return 0
  if score > 21 and 11 in card:
    card.remove(11)
    card.append(1)
  return sum(card)

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

  game_over = False

  bet = int(input(f"You have ${player_balance}. How much would you like to bet? "))

  while not game_over:
    user_score = calculate_score(user_hand)
    computer_score = calculate_score(computer_hand)

    print(f"\tYour cards: {user_hand}, current score: {sum(user_hand)}")
    print(f"\tComputer's first card: {computer_hand[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      game_over = True
    elif user_score < 21:
      draw_card = input("Type 'y' to get another card, type 'n' to pass: ")
      if draw_card == 'y':
          user_hand.append(deal_card())
      else:
          game_over = True

  while computer_score < 17:
    computer_hand.append(deal_card())
    computer_score = calculate_score(computer_hand)

  print(f"\tYour final hand: {user_hand}, final score {sum(user_hand)}")
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