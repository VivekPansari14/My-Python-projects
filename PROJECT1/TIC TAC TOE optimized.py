import os
import random

def display_board(board):
    print("----------")
    for row in board:
        print(" | ".join(row))
        print("----------")

def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Please enter your mark, Player 1 (X/O): ').upper()
        if marker != 'X' and marker != 'O':
            print('Invalid choice. Please enter either X or O.')
    return marker, 'O' if marker == 'X' else 'X'

def place_marker(board, marker, position):
    mapping = {8: (2, 1), 5: (1, 1), 2: (0, 1), 7: (2, 0), 4: (1, 0), 1: (0, 0), 9: (2, 2), 6: (1, 2), 3: (0, 2)}
    row, col = mapping[position]
    if board[row][col] == ' ':
        board[row][col] = marker
        return True
    else:
        print("Position already occupied. Choose a different position.")
        return False

def win_check(board, mark):
    # Check rows
    for row in board:
        if all(cell == mark for cell in row):
            return True

    # Check columns
    for col in range(len(board[0])):
        if all(board[row][col] == mark for row in range(len(board))):
            return True

    # Check diagonals
    if all(board[i][i] == mark for i in range(len(board))):
        return True
    if all(board[i][len(board) - i - 1] == mark for i in range(len(board))):
        return True

    return False

def choose_first():
    return 'Player 1' if random.randint(0, 1) == 0 else 'Player 2'

def full_board_check(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def player_choice(board):
    while True:
        position = int(input("Enter your next position (1-9): "))
        if position in range(1, 10):
            return position

def replay():
    while True:
        play_again = input("Do you want to play again? (YES/NO): ")
        if play_again.upper() == 'YES':
            return True
        elif play_again.upper() == 'NO':
            return False
        else:
            print("Invalid input. Please enter either YES or NO.")

# Actual game setup
print('Welcome to Tic Tac Toe!')

while True:
    main_board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    player_1_marker, player_2_marker = player_input()
    current_player = choose_first()
    print(current_player + " goes first")

    play_game = input('Are you ready to play? (Y/N): ')

    if play_game.upper() != 'Y':
        break

    game_on = True

    while game_on:
        display_board(main_board)
        print("Enter your position, " + current_player)
        position = player_choice(main_board)
        if place_marker(main_board, player_1_marker if current_player == 'Player 1' else player_2_marker, position):
            if win_check(main_board, player_1_marker if current_player == 'Player 1' else player_2_marker):
                display_board(main_board)
                print(current_player + ' has won!!')
                game_on = False
            else:
                if full_board_check(main_board):
                    display_board(main_board)
                    print('Tie Game!!')
                    break
                else:
                    current_player = 'Player 2' if current_player == 'Player 1' else 'Player 1'

    if not replay():
        break
    os.system("cls")
