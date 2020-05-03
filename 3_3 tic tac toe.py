def display_board(board):
    print("|"+board[7]+"|"+board[8]+"|"+board[9])
    print("------")
    print("|"+board[4]+"|"+board[5]+"|"+board[6])
    print("------")
    print("|"+board[1]+"|"+board[2]+"|"+board[3])
def player_input():
    marker=" "
    while marker!='X' and marker!='O':
        marker=input("choose betwwen x or o").upper()
    if marker=='X':
        return ('X','O')
    else:
        return ('O','X')
def place_marker(board, marker, position):
    board[position]=marker
def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal
import random

def choose_first():
    p=random.randint(0,1)
    if p==0:
        return "player1"
    else:
        return "player2"
def space_check(board, position):
    return board[position]== " "
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True
def player_choice(board):
    position=0
    while position not in range(1,10)or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position
def replay():
    choice=input("do u want to play again? choose yes or no").lower()
    return choice=='yes'
print('Welcome to Tic Tac Toe!')
while True:
    # Set the game up here(board,whos first,choosemarkers x,o)
    the_board=[" "]*10 #sets the blank board
    player1_marker,player2_marker= player_input()
    turn=choose_first()
    print(turn + "will go first")
    play_game=input("start the game with yes or no").lower()
    if play_game=='yes':
        game_on=True
    else:
        game_on=False
    while game_on:
        if turn=='player1':
            display_board(the_board) #shows the board
            
            #chose were to put their mark on the desired postion
            position=player_choice(the_board)
            place_marker(the_board,player1_marker,position)
            
            #chech if they won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print("player1 won")
                game_on=False
            
            #check if there was a tie between them
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("game was tie")
                    game_on=False
                else:
                    turn= 'player2'
        else:
            display_board(the_board) #shows the board
            #chose were to put their mark on the desired postion
            position=player_choice(the_board)
            place_marker(the_board,player2_marker,position)
            
            #chech if they won
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print("player2 won")
                game_on=False
            
            #check if there was a tie between them
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("game was tie")
                    game_on=False
                else:
                    turn= 'player1'

    if not replay():
        break