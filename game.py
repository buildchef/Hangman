import word_logic
from board import Board

import os

class Game:
    def __init__(self):
        self.word = word_logic.rand_word
        self.blink = word_logic.blink_word(self.word)
        self.chances = 6
        self.still = True
        self.win_lose = ''
        self.game_board = Board()

    def validate_end(self):
        if self.chances <= 0:
            self.still  = False

        if self.blink == self.word:
            self.still = False

    def validate_win(self):
        if self.still == False:
            if self.chances <= 0:
                self.win_lose = 'Lose'
            else:
                self.win_lose = 'Win'

    def validate_hit(self):
            letter_ = input('Enter a letter: ')
            validate = word_logic.validate_letter(letter_, self.word, self.blink)
            if validate == self.blink:
                self.chances -= 1
            else:
                self.blink = validate

    def board(self):
        os.system('cls')
        self.game_board.print_board(self.chances)

    def print_end(self):
        if self.win_lose == 'Win':
            print('Congratulations! you win.')
        else:
            print('You lose.')

    def __call__(self):
        while self.still == True:
            self.board()
            print()
            print(self.blink)
            print(self.word)
            print(f'You still have: {self.chances} attempts')
            self.validate_hit()
            self.validate_end()
            self.validate_win()

        self.board()
        self.print_end()
        

    def __str__(self):
        return f'{self.word} | {self.blink}'        