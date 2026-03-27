#!/usr/bin/env python3
"""
Tic-Tac-Toe Game
A command-line game for two players.
"""

from typing import List, Optional, Tuple


class TicTacToe:
    def __init__(self):
        """Initialize a new game with an empty board."""
        self.board: List[List[str]] = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player: str = "X"
    
    def display_board(self) -> None:
        """Display the current state of the board."""
        print("\n  1   2   3")
        for i, row in enumerate(self.board, 1):
            print(f"{i} {row[0]} | {row[1]} | {row[2]} ")
            if i < 3:
                print("  -----------")
        print()
    
    def display_instructions(self) -> None:
        """Display game instructions to the players."""
        print("\n=== Tic-Tac-Toe Game ===")
        print("Players take turns placing their marks (X and O) on the board.")
        print("Enter your move as 'row column' (e.g., '1 2' for row 1, column 2).")
        print("The first player to get three in a row wins!\n")
    
    def is_valid_move(self, row: int, col: int) -> bool:
        """
        Check if a move is valid.
        
        Args:
            row: Row index (0-2)
            col: Column index (0-2)
            
        Returns:
            True if the move is valid, False otherwise
        """
        if row < 0 or row > 2 or col < 0 or col > 2:
            return False
        return self.board[row][col] == " "
    
    def make_move(self, row: int, col: int) -> bool:
        """
        Make a move on the board.
        
        Args:
            row: Row index (0-2)
            col: Column index (0-2)
            
        Returns:
            True if the move was successful, False otherwise
        """
        if self.is_valid_move(row, col):
            self.board[row][col] = self.current_player
            return True
        return False
    
    def check_winner(self) -> Optional[str]:
        """
        Check if there's a winner.
        
        Returns:
            The winning player's symbol ('X' or 'O'), or None if no winner yet
        """
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != " ":
                return row[0]
        
        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != " ":
                return self.board[0][col]
        
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return self.board[0][2]
        
        return None
    
    def is_board_full(self) -> bool:
        """
        Check if the board is full.
        
        Returns:
            True if the board is full, False otherwise
        """
        for row in self.board:
            if " " in row:
                return False
        return True
    
    def switch_player(self) -> None:
        """Switch to the other player."""
        self.current_player = "O" if self.current_player == "X" else "X"
    
    def get_move_input(self) -> Tuple[int, int]:
        """
        Get and validate move input from the current player.
        
        Returns:
            A tuple of (row, col) indices (0-2)
        """
        while True:
            try:
                move_input = input(f"Player {self.current_player}, enter your move (row column): ").strip()
                
                parts = move_input.split()
                if len(parts) != 2:
                    print("Invalid input. Please enter row and column separated by space (e.g., '1 2').")
                    continue
                
                row = int(parts[0]) - 1
                col = int(parts[1]) - 1
                
                if row < 0 or row > 2 or col < 0 or col > 2:
                    print("Invalid position. Row and column must be between 1 and 3.")
                    continue
                
                if not self.is_valid_move(row, col):
                    print("That position is already taken. Please choose an empty position.")
                    continue
                
                return row, col
                
            except ValueError:
                print("Invalid input. Please enter numbers only (e.g., '1 2').")
            except KeyboardInterrupt:
                print("\n\nGame interrupted by user.")
                exit(0)
    
    def play(self) -> None:
        """Main game loop."""
        self.display_instructions()
        self.display_board()
        
        while True:
            # Get player's move
            row, col = self.get_move_input()
            self.make_move(row, col)
            
            # Display updated board
            self.display_board()
            
            # Check for winner
            winner = self.check_winner()
            if winner:
                print(f"🎉 Player {winner} wins! Congratulations! 🎉")
                break
            
            # Check for draw
            if self.is_board_full():
                print("It's a draw! The board is full with no winner.")
                break
            
            # Switch to the other player
            self.switch_player()


def main():
    """Entry point for the game."""
    game = TicTacToe()
    game.play()
    
    # Ask if players want to play again
    while True:
        try:
            play_again = input("\nWould you like to play again? (yes/no): ").strip().lower()
            if play_again in ['yes', 'y']:
                game = TicTacToe()
                game.play()
            elif play_again in ['no', 'n']:
                print("Thanks for playing! Goodbye!")
                break
            else:
                print("Please enter 'yes' or 'no'.")
        except KeyboardInterrupt:
            print("\n\nThanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    main()
