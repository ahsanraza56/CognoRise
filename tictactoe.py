import tkinter as tk
from tkinter import messagebox

class TicTacToeGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")

        # Customize the background color
        self.master.configure(background="#FFFFFF")

        # Create a frame to hold the game board
        self.board_frame = tk.Frame(master, bg="#FFFFFF")
        self.board_frame.pack()

        # Initialize game variables
        self.board = [[" "]*3 for _ in range(3)]
        self.current_player = 'X'

        # Create buttons for the game board
        self.buttons = [[None]*3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.board_frame, text=" ", font=("Arial", 20), width=5, height=2,
                                               command=lambda row=i, col=j: self.make_move(row, col))
                self.buttons[i][j].grid(row=i, column=j, padx=5, pady=5)

    def make_move(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player, state='disabled', disabledforeground="#000000")
            if self.check_winner():
                messagebox.showinfo("Winner", f"Player {self.current_player} wins!")
                self.reset_board()
            elif self.is_board_full():
                messagebox.showinfo("Draw", "It's a draw!")
                self.reset_board()
            else:
                self.switch_player()
                if self.current_player == 'O':
                    self.make_ai_move()

    def make_ai_move(self):
        best_move = self.get_best_move()
        self.make_move(best_move[0], best_move[1])

    def switch_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'

    def check_winner(self):
        for row in self.board:
            if all(cell == self.current_player for cell in row):
                return True
        for col in range(3):
            if all(self.board[row][col] == self.current_player for row in range(3)):
                return True
        if all(self.board[i][i] == self.current_player for i in range(3)) or all(self.board[i][2-i] == self.current_player for i in range(3)):
            return True
        return False

    def is_board_full(self):
        for row in self.board:
            if " " in row:
                return False
        return True

    def get_empty_cells(self):
        empty_cells = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    empty_cells.append((i, j))
        return empty_cells

    def get_best_move(self):
        best_move = None
        best_eval = float('-inf')
        for move in self.get_empty_cells():
            self.board[move[0]][move[1]] = 'O'
            eval = self.minimax(0, False)
            self.board[move[0]][move[1]] = ' '
            if eval > best_eval:
                best_eval = eval
                best_move = move
        return best_move

    def minimax(self, depth, maximizing_player):
        if self.check_winner():
            return 10 - depth if self.current_player == 'O' else -10 + depth
        elif self.is_board_full():
            return 0

        if maximizing_player:
            max_eval = float('-inf')
            for move in self.get_empty_cells():
                self.board[move[0]][move[1]] = 'O'
                eval = self.minimax(depth + 1, False)
                self.board[move[0]][move[1]] = ' '
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for move in self.get_empty_cells():
                self.board[move[0]][move[1]] = 'X'
                eval = self.minimax(depth + 1, True)
                self.board[move[0]][move[1]] = ' '
                min_eval = min(min_eval, eval)
            return min_eval

    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = " "
                self.buttons[i][j].config(text=" ", state='normal')


def main():
    root = tk.Tk()
    game = TicTacToeGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
