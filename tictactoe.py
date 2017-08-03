import itertools
import random
import sys


def select_player(player_list):
    while True:
        player = input('Select player (X or O): ').upper()
        if player in player_list:
            break
        else:
            print('Invalid input')
    return player

def start_game():
    print('Start game')

def generate_board():
    board = list()
    for row in range(3):
        board.append(list())
        for column in range(3):
            board[row].append(' ')
    return board

def print_board(board):
    for (index, row) in enumerate(board):
        if index == 0:
            print('    0   1   2 ')
            print('  +---+---+---+')
            print('{0} |'.format(index), ' | '.join(row), '|')
            print('  +---+---+---+')
        else:
            print('{0} |'.format(index), ' | '.join(row), '|')
            print('  +---+---+---+')

def user_turn(board, player):
    while True:
        try:
            tile = input('{0} Turn: '.format(player))
            row = int(tile[0])
            column = int(tile[-1])
            if all(i in range(3) for i in (row, column,)):
                if board[row][column] == ' ':
                    board[row][column] = player
                    break
                else:
                    print('Invalid turn')
            else:
                print('Invalid input')
        except ValueError:
            print('Invalid input')
    return row, column, board

def computer_turn(board, player):
    while True:
        row = random.randint(0, 2)
        column = random.randint(0, 2)
        if board[row][column] == ' ':
            board[row][column] = player
            break
    print('{0} Turn: {1}{2}'.format(player, row, column))
    return row, column, board

def evaluate_turn(board, row, column, player):
    if board[row].count(player) == 3:
        return True
    elif list(board[i][column] for i in range(3)).count(player) == 3:
        return True
    elif list(board[i][i] for i in range(3)).count(player) == 3:
        return True
    elif list(board[i][2 - i] for i in range(3)).count(player) == 3:
        return True
    else:
        return False

def board_status(result, player):
    if result is True:
        print('{0} Winner'.format(player))
        return False
    else:
        return True

def end_game():
    while True:
        selection = input('Restart game (Y or N)? ').upper()
        if selection in ['Y', 'N']:
            break 
        else:
            print('Invalid input')
    if selection == 'N':
        print('End game')
        return False
    else:
        return True


while True:
    player_list = ['X', 'O']
    player_config = {'X': None, 'O': None}

    user = select_player(player_list)
    computer = player_list[player_list.index(user) - 1]

    player_config[user] = user_turn
    player_config[computer] = computer_turn

    board = generate_board()
    next_player = itertools.cycle(player_list)

    start_game()
    print_board(board)

    turn_tally = 0
    while True:
        if turn_tally == 9:
            print('XO Draw')
            break
        if turn_tally < 9:
            player = next(next_player)
            turn = player_config[player]
            row, column, board = turn(board, player)
            print_board(board)
            turn_result = evaluate_turn(board, row, column, player)
            if not board_status(turn_result, player):
                break
        turn_tally += 1
    if not end_game():
        break

sys.exit()
