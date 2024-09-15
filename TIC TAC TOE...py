import random

def print_board(board):
  for row in board:
    print(" | ".join(row))
    print("-" * 9)

def check_win(board, player):
  for row in board:
    if all(cell == player for cell in row):
      return True
  for col in range(3):
    if all(board[row][col] == player for row in range(3)):
      return True
  if board[0][0] == board[1][1] == board[2][2] == player:
    return True
  if board[0][2] == board[1][1] == board[2][0] == player:
    return True
  return False

def play_game():
  """Plays a tic-tac-toe game."""
  board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
  current_player = "X"

  while True:
    print_board(board)

    if current_player == "X":
      row = int(input("Enter row (0-2): "))
      col = int(input("Enter column (0-2): "))
      if board[row][col] != " ":
        print("Invalid move. Cell already occupied.")
        continue
    else:
      # Computer's random move
      while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == " ":
          break

    board[row][col] = current_player

    if check_win(board, current_player):
      print_board(board)
      print(f"{current_player} wins!")
      break

    if all(all(cell != " " for cell in row) for row in board):
      print_board(board)
      print("It's a tie!")
      break

    current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
  play_game()
