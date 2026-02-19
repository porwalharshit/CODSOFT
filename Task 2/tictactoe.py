import random

board = [" " for _ in range(9)]

def print_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-+-+-")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-+-+-")
    print(board[6] + "|" + board[7] + "|" + board[8])

def check_win(player):
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    for w in wins:
        if board[w[0]] == board[w[1]] == board[w[2]] == player:
            return True
    return False

print("🎮 Tic Tac Toe Game")
print("Positions are 0 to 8")

while True:
    print_board()

    move = int(input("Enter your move: "))

    if board[move] == " ":
        board[move] = "X"

        if check_win("X"):
            print_board()
            print("🎉 You win!")
            break

        if " " not in board:
            print_board()
            print("Draw!")
            break

        ai_move = random.choice([i for i in range(9) if board[i] == " "])
        board[ai_move] = "O"

        if check_win("O"):
            print_board()
            print("🤖 AI wins!")
            break
    else:
        print("Invalid move, try again.")
