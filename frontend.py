import tkinter as tk
from tkinter import messagebox
import requests

# Backend URL
BACKEND_URL = "http://127.0.0.1:5000"

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.current_player = "X"  # Start with Player X
        self.buttons = []

        # Create buttons for the board
        for i in range(9):
            button = tk.Button(root, text="", font=("Arial", 20), width=5, height=2,
                               command=lambda i=i: self.make_move(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

        # Reset button
        reset_button = tk.Button(root, text="Reset", font=("Arial", 12), command=self.reset_game)
        reset_button.grid(row=3, column=1)

    def make_move(self, position):
        # Send move to the backend
        data = {"position": position, "player": self.current_player}
        response = requests.post(f"{BACKEND_URL}/move", json=data)

        if response.status_code == 200:
            result = response.json()
            if result["status"] == "success":
                self.update_board(result["board"])
                self.switch_player()  # Switch to the other player
            elif result["status"] == "win":
                self.update_board(result["board"])
                messagebox.showinfo("Game Over", f"Player {result['winner']} wins!")
                self.reset_game()
            elif result["status"] == "draw":
                self.update_board(result["board"])
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
        else:
            messagebox.showerror("Error", "Invalid move or server error")

    def update_board(self, board):
        # Update the buttons with the current board state
        for i in range(9):
            self.buttons[i].config(text=board[i])

    def switch_player(self):
        # Switch between Player X and Player O
        self.current_player = "O" if self.current_player == "X" else "X"

    def reset_game(self):
        # Reset the game by sending a request to the backend
        response = requests.post(f"{BACKEND_URL}/reset")
        if response.status_code == 200:
            result = response.json()
            self.update_board(result["board"])
            self.current_player = "X"  # Reset to Player X
        else:
            messagebox.showerror("Error", "Failed to reset the game")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()