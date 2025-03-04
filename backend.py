from flask import Flask, request, jsonify

app = Flask(__name__)

# Initialize the board
board = [" " for _ in range(9)]

def check_winner(board):
    # Winning combinations
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
            return board[combo[0]]
    return None

def is_board_full(board):
    return " " not in board

@app.route('/move', methods=['POST'])
def make_move():
    global board
    data = request.json
    position = data['position']
    player = data['player']

    if board[position] != " ":
        return jsonify({"status": "error", "message": "Invalid move"})

    board[position] = player

    winner = check_winner(board)
    if winner:
        return jsonify({"status": "win", "winner": winner, "board": board})
    elif is_board_full(board):
        return jsonify({"status": "draw", "board": board})
    else:
        return jsonify({"status": "success", "board": board})

@app.route('/reset', methods=['POST'])
def reset_game():
    global board
    board = [" " for _ in range(9)]
    return jsonify({"status": "success", "board": board})

if __name__ == '__main__':
    app.run(debug=True)