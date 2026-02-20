#!/usr/bin/env python
"""Rock Paper Scissors command line game."""

from __future__ import print_function
import random
import sys


CHOICES = ["rock", "paper", "scissors"]
WINNING_RULES = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock"
}


def get_computer_choice():
    """Generate a random choice for the computer."""
    return random.choice(CHOICES)


def determine_winner(player_choice, computer_choice):
    """
    Determine the winner based on game rules.
    
    Args:
        player_choice: The player's choice (rock, paper, or scissors)
        computer_choice: The computer's choice (rock, paper, or scissors)
    
    Returns:
        'player' if player wins, 'computer' if computer wins, 'tie' if tie
    """
    if player_choice == computer_choice:
        return "tie"
    elif WINNING_RULES[player_choice] == computer_choice:
        return "player"
    else:
        return "computer"


def display_result(player_choice, computer_choice, winner):
    """Display the result of the round to the user."""
    print("\nYou chose: " + player_choice)
    print("Computer chose: " + computer_choice)
    
    if winner == "tie":
        print("It's a tie!")
    elif winner == "player":
        print("You win!")
    else:
        print("Computer wins!")


def get_player_choice():
    """
    Get the player's choice via command line input.
    
    Returns:
        The player's valid choice or None if player wants to quit
    """
    while True:
        print("\nEnter your choice (rock, paper, scissors) or 'quit' to exit: ", end="")
        sys.stdout.flush()
        try:
            choice = raw_input().strip().lower()
        except NameError:
            choice = input().strip().lower()
        
        if choice == "quit" or choice == "q":
            return None
        
        if choice in CHOICES:
            return choice
        
        print("Invalid choice '" + choice + "'. Please choose rock, paper, or scissors.")


def play_game():
    """Main game loop that allows multiple rounds."""
    print("=" * 50)
    print("Welcome to Rock Paper Scissors!")
    print("=" * 50)
    print("\nRules:")
    print("  - Rock beats Scissors")
    print("  - Scissors beats Paper")
    print("  - Paper beats Rock")
    
    player_score = 0
    computer_score = 0
    ties = 0
    
    while True:
        player_choice = get_player_choice()
        
        if player_choice is None:
            print("\n" + "=" * 50)
            print("Thanks for playing!")
            print("Final Score - You: " + str(player_score) + " | Computer: " + str(computer_score) + " | Ties: " + str(ties))
            print("=" * 50)
            break
        
        computer_choice = get_computer_choice()
        winner = determine_winner(player_choice, computer_choice)
        display_result(player_choice, computer_choice, winner)
        
        if winner == "player":
            player_score += 1
        elif winner == "computer":
            computer_score += 1
        else:
            ties += 1
        
        print("\nScore - You: " + str(player_score) + " | Computer: " + str(computer_score) + " | Ties: " + str(ties))


def main():
    """Entry point for the game."""
    try:
        play_game()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Goodbye!")
        sys.exit(0)
    except EOFError:
        print("\n\nNo input provided. Goodbye!")
        sys.exit(0)


if __name__ == "__main__":
    main()
