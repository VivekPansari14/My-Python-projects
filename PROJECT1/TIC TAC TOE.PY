import os
def display_board(board):
    #clear_output()
    print("----------")
    for row in board:
        print(" | ".join(row))
        print("----------")

def player_input():
    marker= True
    player_mark= ' '
    
    while marker:
        player_mark= input('PLs Enter Your Mark Player1; (X , O): ').upper()
        if player_mark=='X' or player_mark=='O':
            marker=False
        else:
            print('Invalid choice')
    if player_mark== 'X':
        return('X', 'O')
    else:
        return('O','X')
    

'''def place_marker(board, marker, position):
    if position==8 or position==5 or position==2:
        row=int(position/3)
        col=1
    elif position==7 or position==4 or position==1:
        row=int(position/3)
        col=0
    elif position==9 or position==6 or position==3:
        row=int((position/3)-1)
        col=2
    board[row][col]= marker'''
    
    
 #Or a more optimised code using mapping
def place_marker(board, marker, position):
    mapping = {8: (2, 1), 5: (1, 1), 2: (0, 1), 7: (2, 0), 4: (1, 0), 1: (0, 0), 9: (2, 2), 6: (1, 2), 3: (0, 2)}
    row, col = mapping[position]
    if board[row][col] == ' ':
        board[row][col] = marker
    else:
        print("Position already occupied. Choose a different position.")



def win_check(board, mark):  #mark is X
    # Check rows
    for row in board: #selcting a whole row in a board
        if all(cell == mark for cell in row): #cell and mark are being checked okay, here all checks the statemnts for all iterations
            return True

    # Check columns
    for col in range(len(board[0])): #here len is 3 for the elments in a list
        if all(board[row][col] == mark for row in range(len(board))):
            return True

    # Check diagonals
    if all(board[i][i] == mark for i in range(len(board))):
        return True
    if all(board[i][len(board)-i-1] == mark for i in range(len(board))):
        return True

    return False

import random

def choose_first():
    choice= random.randint(1,2)
    if choice==1:
        return 'player 1'
    else:
        return 'player 2'
    

'''#def space_check(board, position): #board 3*3, position no. suppose3
    mapping = {8: (2, 1), 5: (1, 1), 2: (0, 1), 7: (2, 0), 4: (1, 0), 1: (0, 0), 9: (2, 2), 6: (1, 2), 3: (0, 2)}
    row, col = mapping[position]
    return board[row][col]== " "  
'''

            
    
def full_board_check(board):
    
    for row in board:
        for cell in row:
            if cell==" ":
                return False
    return True
    
def player_choice(board):
    check = True 
    while check:
       position= int(input("Enter your next position as(1-9): "))
       if position in range(1,10):
          return position 
    #free_pos= space_check(board, position)
    #if free_pos== True:
        #return position

def replay():
    check=False
    while not check:
        play_again= input ("Do you wanna play again, type (YES or NO):")
        if play_again=='YES'or play_again=='NO':
            check=True

    return play_again.upper()=='YES'


#actual game setup
print('Welcome to Tic Tac Toe!')

while True:
    
    main_board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    
    player_1marker, player_2marker= player_input()

    turn= choose_first()
    print(turn+ " goes first")
    
    play_game= input('ready to play? Y or N?')
    
    if play_game.upper() != 'Y':
        break

    game_on = True

    while game_on:
        if turn== 'player 1':
             #show te board
             display_board(main_board)
             #choose a position
             print("Enter your position Player 1")
             position= player_choice(main_board)
             #place the marker on the position of board
             place_marker(main_board, player_1marker, position )

            #check if won
             if win_check(main_board, player_1marker):
                display_board(main_board)
                print('player 1 has won!!')  
                game_on=False
             else:
                if full_board_check(main_board):
                     display_board(main_board)
                     print('Tie Game!!')
                     break
                else:
                     turn='player 2'


        else:
            #show te board
             display_board(main_board)
             #choose a position
             print("Enter your position Player 2")
             position= player_choice(main_board)
             #place the marker on the position of board
             place_marker(main_board, player_2marker, position )

            #check if won
             if win_check(main_board, player_2marker):
                display_board(main_board)
                print('player 2 has won!!')  
                game_on=False
             else:
                if full_board_check(main_board):
                     display_board(main_board)
                     print('Tie Game!!')
                     break
                else:
                     turn='player 1'
    reply= replay()
    
    if reply== True:
        os.system("cls")
    else:
        break