import random


def computer_move(board):
    valid = False
    while valid == False:
        x = random.randint(0,2)
        y = random.randint(0,2)
        if board[y][x] != " ":
            valid = False
        else:
            valid = True
    position = [x, y]
    return(position)


def player_move(board):
    valid = False
    while valid == False:
        x = int(input("Enter for column 1,2,3: "))-1
        y = int(input("Enter for row 1,2,3: "))-1
        if x not in [0,1,2] or y not in [0,1,2]:
            valid = False
        elif board[y][x] != " ":
            valid = False
        else:
            valid = True
    position = [x, y]
    return position


def displayboard(board):
    for i in range(len(board)):
        print("-------------------")
        print(f"|  {board[i][0]}  |  {board[i][1]}  |  {board[i][2]}  |")
    print("-------------------")


def updateboard(player,board):
    if player == 1:
        player_poss = player_move(board)
        board[player_poss[1]][player_poss[0]] = "X"
    else:
        comp_poss = computer_move(board)
        board[comp_poss[1]][comp_poss[0]] = "O"

def createboard():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    return board


def  checkwin(board,xo):
    for i in range(len(board)):
        if board[i][0] == xo and board[i][1] == xo and board[i][2] == xo:
            return True
        elif board[0][i] == xo and board[1][i] == xo and board[2][i] == xo:
            return True

    if (board[0][0] == xo and board[1][1] == xo and board[2][2] == xo) or (board[0][2] == xo and board[1][1] == xo and board[2][0] == xo):
        return True
    return False


def main():
    win = False
    player = 0
    board = createboard()

    while win == False:
        player = (player + 1) % 2
        displayboard(board)
        updateboard(player, board)
        win = checkwin(board, "X")
        win = checkwin(board, "O")
    print(f"Winner is player {player}")

main()
