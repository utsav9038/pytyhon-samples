import itertools

def win(current_game):
    def all_same(l):
        if l.count(l[0])==len(l) and l[0]!=0:
            return True
        else:
            return False
        
    #horizontal winer
    for row in game:
        print(row)
        if all_same(row):
            print("player won in horizontal {}".format(row[0]))
            return True
    
    #vertical winner
    for columns in range(len(game)):
        bl=[]
        for row in game:
            bl.append(row[columns])
        if all_same(bl):
            print("player won in vertical {}".format(bl[0]))
            return True
    
    #DIAGONAL IN ONE increasing order
    for row in game:
        diag=[]
        for ix in range(len(game)):
            diag.append(game[ix][ix])
        if all_same(diag):
            print('u won in DIAGONAL {diag[0]}')  
            return True
    
    #DIAGONALin decreasing order
    diags=[]
    for row,col in enumerate(reversed(range(len(game)))):
        diags.append(game[col][row])
    if all_same(diags):
        print("player won in DIAGONAL {}".format(diags[0]))
        return True
    return False

def game_board(game_map,player=0,row=0,column=0,just_display=False):
    try:
        if game_map[row][column]!=0:
            print('place is occupied')
            return game_map,False
        print('   '+'  '.join([str(i) for i in range(len(game_map))]))
        if not just_display:
            game_map[row][column]=player
        for count,row in enumerate(game_map):
            print(count,row)
        return game_map,True
        
    except IndexError as e:
        print('choose only between 0-2' ,e)
        return game_map,False
    
    except Exception as e:
        print('function is called within a function ',e)
        return game_map,False
play=True
player=[1,2]
while play:
    game_size=int(input('what size of tic tac u want'))
    game=[[0 for i in range(game_size)] for i in range(game_size)]
    print(game)
    game_won= False
    game,_=game_board(game,just_display=True)
    player_choice=itertools.cycle([1,2])
    while not game_won:
        player=next(player_choice)
        print(f'current player= {player}')
        played=False
        while not played:
            column_choice=int(input('which column u want to play 0,1,2 : '))
            row_choice=int(input('which row u want to play 0,1,2 : '))
            game,played=game_board(game,player,row_choice,column_choice)
        if win(game):
            game_won=True
            again=input('do u wanna play again y/n =')
            if again.lower()=='y':
                print('restart')
            else:
                print('byee')
                play=False
        
        
          