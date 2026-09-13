import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__ (self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("400x400")
        self.root.resizable(False, False)
        self.root.configure(bg="white")

        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=0)
        root.grid_columnconfigure(2, weight=0)
        root.grid_columnconfigure(3, weight=0)
        root.grid_columnconfigure(4, weight=1)

        self.current_player = "X"
        self.board = [""] * 9 # list of 9 empty strings to represent the board
        self.buttons = []

        self.gameTitle = tk.Label(
            root, text="Tic Tac Toe", font=("Georgia", 18, "bold"), pady=8, bg="white"
        )
        self.gameTitle.grid(row=0, column=1, columnspan=3)
        self.status = tk.Label(
            root, text="Player X's turn", font=("Helvetica", 10), pady=10, bg="white"
        )
        self.status.grid(row=1, column=1, columnspan=3)

        for i in range(9):
            btn = tk.Button(
                root,
                text="",
                font=("Helvetica", 32),
                width=3,
                height=1,
                command=lambda i=i: self.onClick(i),
            )
            btn.grid(row=(i // 3) + 2, column=(i % 3) + 1)
            self.buttons.append(btn)

        play_again = tk.Button(root, text="Play again", font=("Helvetica", 12), bg="light blue", activebackground="#003159", command=self.reset)
        play_again.grid(row=5, column=2, pady=10)

        self.winning_combos = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6),
        ]

    def onClick (self, index):
        self.board[index] = self.current_player
        self.buttons[index].config(text=self.current_player, state="disabled")

        winner = self.checkWinner()
        if winner:
            self.status.config(text=f"Player {winner} wins!")
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            return

        if "" not in self.board:
            self.status.config(text="It's a draw!")
            messagebox.showinfo("Game Over", "It's a draw!")
            return

        if self.current_player == "X":
            self.current_player = "O"
        else :
            self.current_player = "X"

        self.status.config(text=f"Player {self.current_player}'s turn")

    def checkWinner (self):
        for combo in self.winning_combos:
            if (
                self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ""
            ):
                return self.board[combo[0]]
        return None

    def reset (self):
        self.board = [""] * 9
        self.current_player = "X"
        self.status.config(text="Player X's turn")
        for btn in self.buttons:
            btn.config(text="", state="normal")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
