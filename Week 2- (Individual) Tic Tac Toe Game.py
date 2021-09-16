from IPython.display import clear_output
def display_board(board):
    clear_output()  
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def player_input():
   marker = ''
   while not (marker == 'X' or marker == 'O'):
      marker = input('Player 1: Do you want to be X or O? ').upper()
   if marker == 'X':
      return ('X', 'O')
   else:
      return ('O', 'X')

def place_marker(board, marker, position):
   board[position] = marker

def win_check(board, mark):
   return ((board[1] == mark and board[2] == mark and board[3] == mark) or  # across the top
           (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
           (board[7] == mark and board[8] == mark and board[9] == mark) or  # across the bottom
           (board[1] == mark and board[4] == mark and board[7] == mark) or  # down the left side
           (board[2] == mark and board[5] == mark and board[8] == mark) or  # down the middle
           (board[3] == mark and board[6] == mark and board[9] == mark) or  # down the right side
           (board[1] == mark and board[5] == mark and board[9] == mark) or  # diagonal
           (board[3] == mark and board[5] == mark and board[7] == mark))  # diagonal

import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Computer'
    else:
        return 'Player 1'

def space_check(board, position):
   return board[position] == ' '

def full_board_check(board):
   for i in range(1, 10):
      if space_check(board, i):
         return False
   return True

def player_choice(board):
   position = 0
   while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
      position = int(input('Choose your next position: (1-9) '))
   return position

def computer_choice(board,p):
   
   b=[0,1, 2, 3, 4, 5, 6, 7, 8, 9]
   b.remove(p)
   position=0
   while position not in b or not  space_check(board, position):
      position = random.choices(b,k=1)
   return position

def replay():
   return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

p=0
print('Welcome to Tic Tac Toe!')
while True:
   # Reset the board
   theBoard = [' '] * 10
   player1_marker, player2_marker = player_input()
   turn = choose_first()
   print(turn + ' will go first.')
   play_game = input('Are you ready to play? Enter Yes or No.')
   if play_game.lower()[0] == 'y':
      game_on = True
   else:
      game_on = False
   while game_on:
      if turn == 'Player 1':
         # Player1's turn.
         display_board(theBoard)
         p = player_choice(theBoard)
         place_marker(theBoard, player1_marker, p)
         if win_check(theBoard, player1_marker):
            display_board(theBoard)
            print('Congratulations! You have won the game!')
            game_on = False
         elif full_board_check(theBoard):
               display_board(theBoard)
               print('The game is a draw!')
               break
         else:
            turn = 'Player 2'
      else:
         # Player2's turn.
         display_board(theBoard)
         position = computer_choice(theBoard,p)
         place_marker(theBoard, player2_marker, position)
         if win_check(theBoard, player2_marker):
            display_board(theBoard)
            print('Player 2 has won!')
            game_on = False
         else:
            if full_board_check(theBoard):
               display_board(theBoard)
               print('The game is a draw!')
               break
            else:
               turn = 'Player 1'
   if not replay():
      break
