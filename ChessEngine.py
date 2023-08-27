class ChessGame:

    def __init__(self):
        self.board = [
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
        ]
        self.current_player = 'white'

    def print_board(self):
        for row in self.board:
            print(' '.join(row))

    def get_moves(self, row, col):
        piece = self.board[row][col]
        moves = []

        if piece.lower() == 'p':
            pawn_moves = []
            if self.current_player == 'white':
                if row > 0 and self.board[row - 1][col] == '.':
                    pawn_moves.append((row, col, row - 1, col))
                    if row == 6 and self.board[row - 2][col] == '.':
                        pawn_moves.append((row, col, row - 2, col))
                if row > 0 and col > 0 and self.board[row - 1][col -
                                                               1].islower():
                    pawn_moves.append((row, col, row - 1, col - 1))
                if row > 0 and col < 7 and self.board[row - 1][col +
                                                               1].islower():
                    pawn_moves.append((row, col, row - 1, col + 1))
            elif self.current_player == 'black':
                if row < 7 and self.board[row + 1][col] == '.':
                    pawn_moves.append((row, col, row + 1, col))
                    if row == 1 and self.board[row + 2][col] == '.':
                        pawn_moves.append((row, col, row + 2, col))
                if row < 7 and col > 0 and self.board[row + 1][col -
                                                               1].isupper():
                    pawn_moves.append((row, col, row + 1, col - 1))
                if row < 7 and col < 7 and self.board[row + 1][col +
                                                               1].isupper():
                    pawn_moves.append((row, col, row + 1, col + 1))
            moves.extend(pawn_moves)

        elif piece.lower() == 'r':
            rook_moves = []
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for direction in directions:
                dx, dy = direction
                new_row, new_col = row + dx, col + dy
                while 0 <= new_row < 8 and 0 <= new_col < 8:
                    if self.board[new_row][new_col] == '.':
                        rook_moves.append((row, col, new_row, new_col))
                    elif self.board[new_row][new_col].islower(
                    ) and self.current_player == 'white':
                        rook_moves.append((row, col, new_row, new_col))
                        break
                    elif self.board[new_row][new_col].isupper(
                    ) and self.current_player == 'black':
                        rook_moves.append((row, col, new_row, new_col))
                        break
                    else:
                        break
                    new_row += dx
                    new_col += dy
            moves.extend(rook_moves)

        elif piece.lower() == 'n':
            knight_moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2),
                            (1, 2), (2, -1), (2, 1)]
            for move in knight_moves:
                dx, dy = move
                new_row, new_col = row + dx, col + dy
                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    if self.board[new_row][new_col] == '.' or (
                            self.board[new_row][new_col].islower()
                            and self.current_player == 'white') or (
                                self.board[new_row][new_col].isupper()
                                and self.current_player == 'black'):
                        moves.append((row, col, new_row, new_col))
            moves.extend(knight_moves)

        return moves

    def make_move(self, start_row, start_col, end_row, end_col):
        piece = self.board[start_row][start_col]
        moves = self.get_moves(start_row, start_col)

        if (start_row, start_col, end_row, end_col) in moves:
            self.board[end_row][end_col] = piece
            self.board[start_row][start_col] = '.'
            self.current_player = 'black' if self.current_player == 'white' else 'white'
            return True
        else:
            return False

    def play(self):
        while True:
            self.print_board()
            if self.current_player == 'white':
                print("White player's turn")
            else:
                print("Black player's turn")

            move = input("Enter your move (e.g., 'a2 a4'): ")
            start_col, start_row, end_col, end_row = self.parse_input(move)

            if self.make_move(start_row, start_col, end_row, end_col):
                print("Move successful!")
            else:
                print("Invalid move. Please try again.")

    def parse_input(self, move):
        start_col, start_row, end_col, end_row = move.split()
        if len(start_col) != 1 or len(start_row) != 1 or len(
                end_col) != 1 or len(end_row) != 1:
            raise ValueError(
                "Invalid move format. Please use the format 'a2 a4'.")

        start_col = ord(start_col) - ord('a')
        start_row = int(start_row) - 1
        end_col = ord(end_col) - ord('a')
        end_row = int(end_row) - 1
        return start_col, start_row, end_col, end_row
