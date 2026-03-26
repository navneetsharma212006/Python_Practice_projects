board = [" "] * 9

def print_board():
    print(board[0], "|", board[1], "|", board[2])
    print("---------")
    print(board[3], "|", board[4], "|", board[5])
    print("---------")
    print(board[6], "|", board[7], "|", board[8])


def check_winner(player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],   # rows
        [0,3,6], [1,4,7], [2,5,8],   # columns
        [0,4,8], [2,4,6]             # diagonals
    ]

    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False


player = "X"

for turn in range(9):

    print_board()

    position = int(input(f"Player {player}, choose position (1-9): ")) - 1

    if board[position] == " ":
        board[position] = player
    else:
        print("Position already taken!")
        continue

    if check_winner(player):
        print_board()
        print(f"Player {player} wins!")
        break

    if player == "X":
        player = "O"
    else:
        player = "X"

else:
    print_board()
    print("Match Draw!")