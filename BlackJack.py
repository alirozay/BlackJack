import random
from typing import List

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
computer_cards = []


def deal(card: List[int]) -> None:
    """Deals cards to the respective player"""
    card.append(random.choice(cards))


def initial_deal(cards1: List[int], cards2: List[int]) -> None:
    """Dealer sends out two cards to each player"""
    for i in range(2):
        deal(cards1)
        deal(cards2)


def score(card: List[int]) -> int:
    """Returns the score of the current hand"""
    return sum(card)


def player_score_printer() -> str:
    """Returns the score and hand of the player"""
    player_score = score(player_cards)
    string = f"You have the following cards {player_cards}. " \
             f"Current score is {player_score}"
    return string


def total_score_printer() -> str:
    """Returns the total score of the players and their respective hands"""
    player_score = score(player_cards)
    computer_score = score(computer_cards)
    string = f"Your score is {player_score} and your hand is {player_cards}, " \
             f"computer score is {computer_score} and computer's hand " \
             f"is {computer_cards}. "
    return string


def reset(cards1: List[int], cards2: List[int]) -> None:
    """Resets the cards players hold"""
    cards1.clear()
    cards2.clear()


def score_checker(cards1: List[int], cards2: List[int]) -> None:
    """Checks scores and prints out the winner"""
    if score(cards1) > score(cards2):
        print(total_score_printer())
        print("You win!")
    elif score(cards2) > score(cards1):
        print(total_score_printer())
        print("You lose.")
    else:
        print(total_score_printer())
        print("You drew.")


def get_card():
    """Asks user whether they want another card"""
    string = input("Type 'y' to get another card, type 'n' to pass: ")
    return string.lower()


print("Welcome to BlackJack!")
play = True
end_game = False
while play:
    initial_deal(player_cards, computer_cards)
    print(player_score_printer())
    print(f"Computer has the following card {computer_cards[0]}")
    while score(computer_cards) < 17:
        deal(computer_cards)
    ask = get_card()
    while ask == 'y':
        deal(player_cards)
        print(player_score_printer())
        if score(player_cards) > 21:
            print("You have busted. You lose :(")
            print(total_score_printer())
            end_game = True
            break
        ask = get_card()
    if score(computer_cards) > 21:
        print("Computer has busted. You win!")
        print(total_score_printer())
        end_game = True
    if not end_game:
        score_checker(player_cards, computer_cards)
    ask2 = input("Do you want to play another round? Type 'y' for yes or 'n'"
                 "for no: ")
    if ask2.lower() == 'n':
        play = False
    else:
        reset(player_cards, computer_cards)
        end_game = False
