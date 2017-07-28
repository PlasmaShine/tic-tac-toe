class GenerateBoard():

    def __init__(self, rows, columns):
        self.board = list()
        self.rows = int(rows)
        self.columns = int(columns)

    def generate_board(self):
        for row in range(self.rows):
            self.board.append(list())
            for column in range(self.columns):
                self.board[row].append('')
        return self.board
