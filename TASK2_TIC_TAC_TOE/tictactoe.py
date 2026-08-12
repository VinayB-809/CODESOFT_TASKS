import math

board = [" " for _ in range(9)]
def print_board():
    print()

    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])

    print()

def show_empty_board():
    print("\nAvailable Moves\n")

    for i in range(9):

        if board[i] == " ":
            print(i + 1, end="")
        else:
            print(" ", end="")

        if i % 3 != 2:
            print(" | ", end="")
        else:
            print()
            if i != 8:
                print("--+---+--")

    print()


def print_positions():
    print("\nBoard Positions")
    print("1 | 2 | 3")
    print("--+---+--")
    print("4 | 5 | 6")
    print("--+---+--")
    print("7 | 8 | 9")
    print()


def check_winner(player):
    win_positions = [
        [0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

    for position in win_positions:
        if board[position[0]] == board[position[1]] == board[position[2]] == player:
            return True
    return False


def board_full():
    return " " not in board


def minimax(is_maximizing):

    if check_winner("O"):
        return 1

    if check_winner("X"):
        return -1

    if board_full():
        return 0

    if is_maximizing:

        best_score = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(score, best_score)

        return best_score

    else:

        best_score = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(score, best_score)

        return best_score


import random

def ai_move():
    empty = []

    for i in range(9):
        if board[i] == " ":
            empty.append(i)

    # Sometimes AI chooses a random move
    if random.random() < 0.2:
        move = random.choice(empty)
        board[move] = "O"
        return

    # Otherwise AI uses Minimax
    best_score = -math.inf
    move = random.choice(empty)

    for i in empty:
        board[i] = "O"
        score = minimax(False)
        board[i] = " "

        if score > best_score:
            best_score = score
            move = i

    board[move] = "O"

print("=================================")
print("      TIC-TAC-TOE AI GAME")
print("=================================")

print_positions()

while True:

    print_board()
    show_empty_board()

    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1

            if move < 0 or move > 8:
                print("Please enter a number between 1 and 9.")
                continue

            if board[move] != " ":
                print("That position is already taken.")
                continue

            board[move] = "X"
            break

        except:
            print("Invalid input. Enter a number.")

    if check_winner("X"):
        print_board()
        print("Congratulations! You Win!")
        break

    if board_full():
        print_board()
        print(" It's a Draw!")
        break

    print("\nAI is thinking...")
    ai_move()

    if check_winner("O"):
        print_board()
        print(" AI Wins!")
        break

    if board_full():
        print_board()
        print("It's a Draw!")
        break

print("\nThank you for playing!")
