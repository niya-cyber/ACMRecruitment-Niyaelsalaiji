import random
moves=[]
compcanselect=[]
board = [' ' for _ in range(9)]

def showboard():
    row1 = '| {} | {} | {} |'.format(board[0], board[1], board[2])
    row2 = '| {} | {} | {} |'.format(board[3], board[4], board[5])
    row3 = '| {} | {} | {} |'.format(board[6], board[7], board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()

def player(icon):
    if icon == 'X':
        text="Your"
    elif icon == 'O':
        text="Computers"

    print("{} turn".format(text))

    if icon=="X":
        choice = int(input("Enter your move (1-9): ").strip())
        if choice>=10 or choice<=0:
            print("Out of index please select valid position")
            choice = int(input("Enter your move (1-9): ").strip())
        moves.append(choice)
        if board[choice - 1] == ' ':
            board[choice - 1] = icon
        else:
            print("Sorry already occupied please choose another move")
    else:
        for i in range(1, 10):
           if i not in moves:
             compcanselect.append(i)
        choice=random.choice(compcanselect)
        if board[choice - 1] == ' ':
            board[choice - 1] = icon   

def wins(icon):
    if (board[0] == icon and board[1] == icon and board[2] == icon) or (board[3] == icon and board[4] == icon and board[5] == icon) or (board[6] == icon and board[7] == icon and board[8] == icon) or  (board[0] == icon and board[3] == icon and board[6] == icon) or (board[1] == icon and board[4] == icon and board[7] == icon) or (board[2] == icon and board[5] == icon and board[8] == icon) or (board[0] == icon and board[4] == icon and board[8] == icon) or (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False

while True:
    showboard()
    player('X')
    showboard()
    if wins('X'):
        print("You wins! Congratulations!")
        break
    elif ' ' not in board:
        print("It's a tie")
        break
    player('O')
    if wins('O'):
        print()
        print("Computer wins.Better luck next time!")
        break
