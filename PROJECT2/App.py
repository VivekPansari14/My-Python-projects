from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
current_player = 'X'
game_over = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    global board, current_player, game_over

    if game_over:
        return jsonify({'validMove': False})

    position = int(request.json['position'])
    row, col = position // 3, position % 3

    if board[row][col] == ' ':
        board[row][col] = current_player
        game_over, winner = check_game_over()
        if game_over:
            return jsonify({'validMove': True, 'winner': winner, 'tie': False})
        elif not any(' ' in row for row in board):
            return jsonify({'validMove': True, 'winner': None, 'tie': True})
        else:
            current_player = 'O' if current_player == 'X' else 'X'
            return jsonify({'validMove': True, 'winner': None, 'tie': False})
    else:
        return jsonify({'validMove': False})

def check_game_over():
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return True, row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return True, board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True, board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return True, board[0][2]

    return False, None

if __name__ == '__main__':
    app.run()


