class move:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.start_index = translate_to_index(self.start)
        self.end_index = translate_to_index(self.end)

    def __str__(self):
        return "{}-{}".format(self.start, self.end)


class player:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.pieces = []

    def make_move(self, board):
        print("Make a move, {}!".format(self.name))
        move_str = input("Move: ")
        m = move(move_str.split(" ")[0], move_str.split(" ")[1])
        return m


def translate_to_index(position):
    positions = [*position.translate(
        str.maketrans("abcdefgh", "01234567"))]

    return [int(positions[1])-1, int(positions[0])]


class piece:
    def __init__(self, name, color, position, player):
        self.name = name
        self.color = color
        self.position = position
        self.position_index = translate_to_index(self.position)
        self.player = player
        self.player.pieces.append(piece)


class rook(piece):
    def __init__(self, color, position, player):
        super().__init__("rook", color, position, player)


class knight(piece):
    def __init__(self, color, position, player):
        super().__init__("knight", color, position, player)


class bishop(piece):
    def __init__(self, color, position, player):
        super().__init__("bishop", color, position, player)


class queen(piece):
    def __init__(self, color, position, player):
        super().__init__("queen", color, position, player)


class king(piece):
    def __init__(self, color, position, player):
        super().__init__("king", color, position, player)


class pawn(piece):
    def __init__(self, color, position, player):
        super().__init__("pawn", color, position, player)


class board:
    def __init__(self) -> None:
        self.board = [[None for i in range(8)] for j in range(8)]

    def add_piece(self, piece):
        self.board[piece.position_index[0]
                   ][piece.position_index[1]] = piece

    def move_piece(self, start_index, end_index):
        piece = self.board[start_index[0]][start_index[1]]
        self.board[end_index[0]][end_index[1]] = piece
        self.board[start_index[0]][start_index[1]] = None

    def get_figure(self, position):
        return self.board[position[0]][position[1]]

    def print_board(self):
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == None:
                    print(" ", end=" ")
                else:
                    print(self.board[i][j].name[0], end=" ")
            print()


class game:
    def __init__(self) -> None:
        self.player1 = player("player1", "white")
        self.player2 = player("player2", "black")
        self.board = board()
        self.whos_turn = self.player1
        self.init_board()
        self.play()

    def init_board(self):
        # init white side
        self.board.add_piece(rook("white", "a1", self.player1))
        self.board.add_piece(knight("white", "b1", self.player1))
        self.board.add_piece(bishop("white", "c1", self.player1))
        self.board.add_piece(queen("white", "d1", self.player1))
        self.board.add_piece(king("white", "e1", self.player1))
        self.board.add_piece(bishop("white", "f1", self.player1))
        self.board.add_piece(knight("white", "g1", self.player1))
        self.board.add_piece(rook("white", "h1", self.player1))
        for i in range(8):
            self.board.add_piece(pawn("white", chr(i+97)+"2", self.player1))

        # init black side
        self.board.add_piece(rook("black", "a8", self.player2))
        self.board.add_piece(knight("black", "b8", self.player2))
        self.board.add_piece(bishop("black", "c8", self.player2))
        self.board.add_piece(queen("black", "d8", self.player2))
        self.board.add_piece(king("black", "e8", self.player2))
        self.board.add_piece(bishop("black", "f8", self.player2))
        self.board.add_piece(knight("black", "g8", self.player2))
        self.board.add_piece(rook("black", "h8", self.player2))
        for i in range(8):
            self.board.add_piece(pawn("black", chr(i+97)+"7", self.player2))

    def play(self):
        self.board.print_board()
        while True:
            self.turn()
            self.board.print_board()

    def check_win(self):
        pass

    def check_move(self, move):
        if move.start_index[0] < 0 or \
                move.start_index[0] > 7 or \
                move.start_index[1] < 0 or \
                move.start_index[1] > 7 or \
                move.end_index[0] < 0 or \
                move.end_index[0] > 7 or \
                move.end_index[1] < 0 or \
                move.end_index[1] > 7:
            print("Invalid move")
            return False

        if self.board.get_figure(move.start_index) == None:
            print("Invalid move")
            return False

        if self.board.get_figure(move.start_index).color != self.whos_turn.color:
            print("Invalid move")
            return False

        return True

    def get_legal_moves():
        pass

    def execute_move(self, move):
        self.board.move_piece(move.start_index, move.end_index)

    def turn(self):
        player_move = self.whos_turn.make_move(self.board)
        if self.check_move(player_move):
            self.execute_move(player_move)
        else:
            return
        self.check_win()
        self.whos_turn = self.player2 if self.whos_turn == self.player1 else self.player1


if __name__ == "__main__":
    game = game()
