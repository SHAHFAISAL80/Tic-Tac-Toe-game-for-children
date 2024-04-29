import tkinter as tk
from tkinter import messagebox
import random

# Define your global variables
board = [' ' for i in range(10)]
root = tk.Tk()
root.title("Tic Tac Toe")

# Function to insert a letter into the board
def insertLetter(letter, pos):
    board[pos] = letter

# Function to check if a space is free on the board
def spaceIsfree(pos):
    return board[pos] == ' '

# Function to print the board (not required for GUI)
def printBoard(board):
    print("   |   |   ")
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print("   |   |   ")

# Function to check if the board is full
def isBoardFull(board):
    if board.count(" ") > 1:
        return False
    else:
        return True

# Function to check if someone has won
def isWinner(b, l):
    # check all possibilities
    return ((b[1] == l and b[2] == l and b[3] == l) or
            (b[4] == l and b[5] == l and b[6] == l) or
            (b[7] == l and b[8] == l and b[9] == l) or
            (b[1] == l and b[4] == l and b[7] == l) or
            (b[2] == l and b[5] == l and b[8] == l) or
            (b[3] == l and b[6] == l and b[9] == l) or
            (b[1] == l and b[5] == l and b[9] == l) or
            (b[3] == l and b[5] == l and b[7] == l))

# Function to handle user's move
def userMove(button):
    pos = int(button["text"])
    if spaceIsfree(pos):
        insertLetter("X", pos)
        button.config(text="X", state=tk.DISABLED)
        if isWinner(board, "X"):
            messagebox.showinfo("Tic Tac Toe", "Congratulations! You Win!")
            resetGame()
        elif isBoardFull(board):
            messagebox.showinfo("Tic Tac Toe", "It's a Tie!")
            resetGame()
        else:
            compMove()

# Function to handle computer's move
def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == " " and x != 0]

    move = 0
    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                break

    if move == 0:
        move = random.choice(possibleMoves)

    insertLetter("O", move)
    buttons[move].config(text="O", state=tk.DISABLED)
    if isWinner(board, "O"):
        messagebox.showinfo("Tic Tac Toe", "Computer Wins!")
        resetGame()
    elif isBoardFull(board):
        messagebox.showinfo("Tic Tac Toe", "It's a Tie!")
        resetGame()

# Function to reset the game
def resetGame():
    global board
    board = [' ' for i in range(10)]
    for button in buttons.values():
        button.config(text=" ", state=tk.NORMAL)

# Create buttons for the Tic Tac Toe grid
buttons = {}
for i in range(1, 10):
    row = (i - 1) // 3
    col = (i - 1) % 3
    button = tk.Button(root, text=str(i), font=('Helvetica', '20'), width=4, height=2, command=lambda i=i: userMove(buttons[i]))
    button.grid(row=row, column=col, padx=5, pady=5)
    buttons[i] = button

# Run the GUI application
root.mainloop()
