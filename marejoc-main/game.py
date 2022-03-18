
import math
import time
from player import HumanPlayer,RandomComputerPlayer, SmartComputerPlayer


class TicTacToe():
    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None

    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]

    def print_board(self):
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # check the row
        row_ind = math.floor(square / 3)
        row = self.board[row_ind*3:(row_ind+1)*3]
        # print('row', row)
        if all([s == letter for s in row]):
            return True
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        # print('col', column)
        if all([s == letter for s in column]):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            # print('diag1', diagonal1)
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            # print('diag2', diagonal2)
            if all([s == letter for s in diagonal2]):
                return True
        return False

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]


def play(dif, game, x_player, o_player, print_game=True):

    if print_game:
        game.print_board_nums()

    letter = 'X'
    if dif == '3':
      while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.make_move(square, letter):

            if print_game:
                print(letter + ' makes a move to square {}'.format(square))
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter  # ends the loop and exits the game
            letter = 'O' if letter == 'X' else 'X'  # switches player

        time.sleep(.8)

      if print_game:
        print('It\'s a tie!')
    elif dif == '1':
        while game.empty_squares():
            if letter == 'O':
                square = o_player.get_move1(game)
            else:
                square = x_player.get_move1(game)
            if game.make_move(square, letter):

                if print_game:
                    print(letter + ' makes a move to square {}'.format(square))
                    game.print_board()
                    print('')

                if game.current_winner:
                    if print_game:
                        print(letter + ' wins!')
                    return letter  # ends the loop and exits the game
                letter = 'O' if letter == 'X' else 'X'  # switches player

            time.sleep(.8)

        if print_game:
            print('It\'s a tie!')
    if dif == '2':
        contor = 0
        while game.empty_squares():
            contor = contor + 1
            if letter == 'O':
                if contor % 2 == 0:
                 square = o_player.get_move1(game)
                else :
                 square = o_player.get_move(game)
            else:
                if contor % 2 == 0:
                 square = x_player.get_move1(game)
                else :
                 square = x_player.get_move(game)
            if game.make_move(square, letter):

                if print_game:
                    print(letter + ' makes a move to square {}'.format(square))
                    game.print_board()
                    print('')

                if game.current_winner:
                    if print_game:
                        print(letter + ' wins!')
                    return letter  # ends the loop and exits the game
                letter = 'O' if letter == 'X' else 'X'  # switches player

            time.sleep(.8)

        if print_game:
            print('It\'s a tie!')


if __name__ == '__main__':
    gata = False
    contorx = 0
    contory = 0
    while gata != True:
        dificultate = input('Ce dificultate vrei? [1/2/3]  ')
        dif=dificultate
        x_player = HumanPlayer('X')
        o_player = SmartComputerPlayer('O')
        t = TicTacToe()
        final = play(dif,t, x_player, o_player, print_game=True)
        if final == 'X':
            contorx = contorx + 1
        else:
            contory = contory + 1
        raspuns = input('Mai joci inca o data? [y/n]  ')
        if raspuns.lower() == 'y':
            gata = False
        else:
            print("Papa")
            gata = True
    s = 'Ai castigat de '
    s1 = ' ori, iar el de '
    s2 = ' ori!'
    print(s + str(contorx) + s1 + str(contory) + s2)

