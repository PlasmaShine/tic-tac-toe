class BoardObject:

    def __init__(self, rows, columns):
        self.rows = int(rows)
        self.columns = int(columns)

    def generate_board(self):
        board = list()
        for row in range(self.rows):
            board.append(list())
            for column in range(self.columns):
                board[row].append('')
        return board

class Board(BoardObject):

    def __init__(self):
        super().__init__(3, 3)

    def print_board(self):
        board = self.generate_board()
        for row in board:
            print(' '.join(row))

player = 1
def turn(board, player):
    while True:
        try:
            tile = input('{0} Turn: '.format(player))
            row = int(tile[0])
            column = int(tile[-1])
            if all(iterable in range(3) for iterable in (row, column,)):
                if board[row][column] == '':
                    board[row][column] = player
                    break
                else:
                    print('Invalid turn')
            else:
                print('Invalid input')
        except ValueError:
            print('Invalid input')
    return board
