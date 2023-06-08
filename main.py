import random
from replit import clear
from art import logo
import pyfiglet


win_ascii = pyfiglet.figlet_format("You Win")
Draw_ascii = pyfiglet.figlet_format("Draw")
loss_ascii = pyfiglet.figlet_format("You Loss")



# Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.
def deal_card():
    """return a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
# print(deal_card())
def calculate_score(cards):
    """return Sum of the card."""

    #Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
    if sum(cards) == 21 and len(cards) == 2:
        return 0

        #Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
    return sum(cards)
# Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, 
# then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. 
# If the user_score is over 21, then the user loses.
# If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.  
def compare(user_score, computer_score):
    """ return show massage what happened."""
    if user_score == computer_score:
        return f"{Draw_ascii}"
    elif computer_score == 0:
        return "loss, opponent has blackjack"
    elif user_score == 0:
        return "Win with a black jack"
    elif user_score > 21:
        return f"you want over. \n {loss_ascii}"
    elif computer_score > 21:
        return f"Opponent went over.\n {win_ascii}. "
    elif user_score > computer_score:
        return f"{win_ascii}"
    else:
        return f"{loss_ascii}" 

def play_game():
# show the logo from art.py.
    print(logo)
    user_cards = []
    computer_cards = []

    is_game_over = False

# Deal the user and computer 2 cards each using deal_card() and append().

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

# Create a function called calculate_score() that takes a List of cards as input
#and returns the score.
#Look up the sum() function to help you do this.

    while not is_game_over:

# Call calculate_score().
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        
        
        print(f"your card: {user_cards},your score: {user_score}")
        print(f"Computer card: {computer_cards}, computer score: {computer_score} ")

# If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True

# If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
        else:
            user_should_deal = input("type 'y' to get another card.and type 'n' to escape: ")

# The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

# Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
        
    print(f"Your final card {user_cards} \ncomputer final card {computer_cards}")
    
    print(compare(user_score,computer_score))
    
#  Ask the user if they want to restart the game. 
# If they answer yes, clear the console and start a new game of blackjack.
while input("Do you want to play game.? 'y' ot 'n': ") == 'y':
    clear()
    play_game()
    
    
    
    
    
    
    