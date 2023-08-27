from flask import Flask, jsonify, request
from ChessEngine import ChessGame

app = Flask(__name__)
game = ChessGame()


@app.route('/')
def routeRoot():
    response = "Moreweb's Chess API\n200: OK  |  Running ..."
    return response


@app.route('/api/make-move', methods=['POST'])
def make_move():
    data = request.get_json()
    start_row = data['start_row']
    start_col = data['start_col']
    end_row = data['end_row']
    end_col = data['end_col']

    success = game.make_move(start_row, start_col, end_row, end_col)

    if success:
        message = 'Move successful!'
    else:
        message = 'Invalid move. Please try again.'

    response = {'success': success, 'message': message}
    return jsonify(response)


@app.route('/api/get-board', methods=['GET'])
def get_board():
    board = game.board
    current_player = game.current_player

    response = {'board': board, 'current_player': current_player}
    return jsonify(response)


@app.route('/api/reset-game', methods=['POST'])
def reset_game():
    game.reset()
    response = {'message': 'Game reset successfully!'}
    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
