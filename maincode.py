#board display
def Display_Board(board):
    print('\n'*100)
    print( '     |     |     ')
    print(f' {board[1]}   | {board[2]}   | {board[3]} ')
    print( '     |     |     ')
    print( '-----------------')
    print( '     |     |     ')
    print(f' {board[4]}   | {board[5]}   | {board[6]} ')
    print( '     |     |     ')
    print( '-----------------')
    print( '     |     |     ')
    print(f' {board[7]}   | {board[8]}   | {board[9]} ')
    print( '     |     |     ')
testboard = [' ']*10
Display_Board(testboard)

def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player ONE: Select either X or O? :').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board,mark):

    return ((board[7] == mark and board[8] == mark and board[9] == mark) or 
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal


import random
def First_Choice():
    if random.randint(0,1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def Check_Space(board, position):

    return board[position] == ' '
#fullboard check
def Check_Board(board):
    for i in range(1,10):
        if Check_Space(board, i):
            return False
    return True

def Player_Choice(board):
    pos = 0

    while pos not in range(1,10) or not Check_Space(board, pos):
        pos = int(input('Next position: (1-9):'))

    return pos

def Play_Again():

    return input('Play again? YES(y) or NO(n):').lower().startswith('y')

print('TIC TAC TOE')

while True:
    #board reset
    game_board = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = First_Choice()
    print(turn + 'You go first!')

    play_game = input('Ready to play? YES(y) or NO(n) :')

    if play_game.lower()[0] == 'y':
        wannaplay = True
    else:
        wannaplay = False

    while wannaplay:
        if turn == 'Player 1':
            #Player 1's turn

            Display_Board(game_board)
            pos = Player_Choice(game_board)
            place_marker(game_board,player1_marker,pos)

            if win_check(game_board,player1_marker):
                Display_Board(game_board)
                print('Congrats! You won the game')
                wannaplay = False
            else:
                if Check_Board(game_board):
                    Display_Board(game_board)
                    print('Game ends in a Draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            #Player 2's turn

            Display_Board(game_board)
            pos = Player_Choice(game_board)
            place_marker(game_board,player2_marker, pos)

            if win_check(game_board, player2_marker):
                Display_Board(game_board)
                print('Player 2 has won!')
                wannaplay = False
            else:
                if Check_Board(game_board):
                    Display_Board(game_board)
                    print('Game ends in a Draw!')
                    break
                else:
                    turn = 'Player 1'

    if not Play_Again():
        break
