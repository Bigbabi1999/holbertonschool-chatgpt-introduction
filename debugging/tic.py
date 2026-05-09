#!/usr/bin/python3
def print_board(board):
    for i, row in enumerate(board):
        print(' | '.join(row))
        if i < 2:
            print("---+---+---")
        # print("-" * 5)

def check_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def get_valid_input(prompt):
    while True:
        value = input(prompt)

        # Check if input is only 0,1 or 2
        if value in ["0", "1", "2"]:
            return int(value)
        
        print("Invalid input! Please enter only 0, 1, or 2")

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while not check_winner(board):
        print_board(board)
        row = get_valid_input(f"Enter row (0, 1, or 2) for plater {player}:")
        col = get_valid_input(f"Enter column (0, 1, or 2) for plater {player}:")
        if board[row][col] == " ":
            board[row][col] = player
            if player == "X":
                player = "O"
            else:
                player = "X"
        else:
            print("That spot is already taken! Try again.")

    print_board(board)
    print("Player " + player + " wins!")

tic_tac_toe()
