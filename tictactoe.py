from random import randint


board_size = 3
players = 'XO'


class Board:

    def __init__(self, board_size):
        self.board_size = board_size
        self.board = [[' ' for column in range(self.board_size)]for row in range(self.board_size)]

    def print_board(self):
        for (index, rows) in enumerate(self.board):
            if index == 0:
                columns = [str(column) for column in range(self.board_size)]
                print('   ', '   '.join(columns), sep='  ')
                print('   ', '+{0}'.format('---+' * self.board_size), sep='')
                print('{0: =2d} '.format(index), ' | '.join(rows), sep='| ', end=' |\n')
                print('   ', '+{0}'.format('---+' * self.board_size), sep='')
            else:
                print(' {0} '.format(index), ' | '.join(rows), sep='| ', end=' |\n')
                print('   ', '+{0}'.format('---+' * self.board_size), sep='')

class Player:

    def __init__(self, players):
        self.players = players
        self.player = ''
        self.player_config = {player: None for player in self.players}
        self.player_cycle = self.__cycle_players()

    def select_player(self):
        while True:
            player_input = input('Select player (X or O): ').upper()
            if self._validate_player_input(player_input):
                self.player = player_input
                break
        self._set_player_configuration()

    def _validate_player_input(self, player_input):
        if player_input in self.players:
            return True
        else:
            print('Invalid input!')
            return False

    def _set_player_configuration(self):
        for (key, value) in self.player_config.items():
            if key == self.player:
                self.player_config[key] = False
            else:
                self.player_config[key] = True

    def cycle_players(self):
        while self.players:
            for player in self.players:
                yield player

    __cycle_players = cycle_players

class Game(Board, Player):

    def __init__(self, board_size, players):
        Board.__init__(self, board_size)
        Player.__init__(self, players)
        self.row = None
        self.column = None

    def cycle_players(self):
        self.player = next(self.player_cycle)

    def select_board_square(self):
        while True:
            if not self.player_config[self.player]:
                board_square_input = input('{0} Turn (row, column): '.format(self.player)).split(',')
            else:
                board_square_input = [randint(0, self.board_size - 1), randint(0, self.board_size - 1)]
            if self._validate_board_square_input(board_square_input):
                self.row, self.column = self._parse_board_square_input(board_square_input)
                break
        self._mark_board_square()

    def _validate_board_square_input(self, board_square_input):
        if type(board_square_input) is list:
            try:
                row, column = self._parse_board_square_input(board_square_input)
                if not self.board[row][column] in self.players:
                    return True
                else:
                    if not self.player_config[self.player]:
                        print('Invalid input')
                    return False
            except IndexError:
                print('Invalid input')
                return False
            except ValueError:
                print('Invalid input')
                return False
        else:
            print('Invalid input')
            return False

    def _parse_board_square_input(self, board_square_input):
        return (int(axis_point) for axis_point in board_square_input)

    def _mark_board_square(self):
        self.board[self.row][self.column] = self.player

    def is_winner(self):
        if self.board[self.row].count(self.player) == self.board_size:
            return True
        elif [self.board[row][self.column] for row in range(self.board_size)].count(self.player) == self.board_size:
            return True
        elif [self.board[index][index] for index in range(self.board_size)].count(self.player) == self.board_size:
            return True
        elif [self.board[(self.board_size - 1) - index][index] for index in range(self.board_size)].count(self.player) == self.board_size:
            return True
        else:
            return False

    def select_restart_option(self):
        while True:
            restart_option_input = input('Restart game (Y or N)? ').upper()
            if self._validate_restart_option_input(restart_option_input):
                break
        if restart_option_input == 'N':
            print('End game')
            return False
        else:
            return True

    def _validate_restart_option_input(self, restart_option_input):
        if restart_option_input in 'YN':
            return True
        else:
            print('Invalid input')
            return False


while True:
    game = Game(board_size, players)
    game.select_player()
    game.print_board()
    number_of_turns = 0
    while number_of_turns < (board_size * board_size):
        game.cycle_players()
        game.select_board_square()
        if game.player_config[game.player]:
            print('{0} Turn (row, column): {1},{2}'.format(game.player, game.row, game.column))
        game.print_board()
        if game.is_winner():
            print('{0} Winner!'.format(game.player))
            break
        number_of_turns += 1
    if number_of_turns == 9:
        print('XO Draw!')
    if not game.select_restart_option():
        break
