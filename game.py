#-- My imports
import word_logic
from board import Board
from letterError import LetterError 

#-- Python imports
import os
#-- https://docs.python.org/3/library/os.html

#-- Creating the Game class
class Game:
    def __init__(self):
        self.word = word_logic.rand_word
        self.blink = word_logic.blink_word(self.word)
        self.chances = 6
        self.still = True
        self.win_lose = ''
        self.game_board = Board()
        self.tried = []

    def validate_end(self):
        """Function that validates if the game has reached the end"""
        #-- Verify if the player still has attempts
        if self.chances <= 0:
            self.still  = False

        #-- Verify if the player found the word 
        if self.blink == self.word:
            self.still = False

    def validate_win(self):
        """Function that validates if the player won or lost"""
        #-- Checks if the game is over
        if self.still == False:

            #-- Declares that the player has lost if there are no more attempts left
            if self.chances <= 0:
                self.win_lose = 'Lose'

            #-- In case there still attempts left, declares that the player won
            else:
                self.win_lose = 'Win'

    def validate_hit(self):
        """Function that validate if the player got a letter right"""
        #-- Receive a letter from the user
        letter_ = input('Enter a letter: ')

        #-- Dfensive Programming: Checking possible inconsistencies
        #-- Checking if there is more than one character
        if len(letter_) > 1:
            raise LetterError('ERROR: Enter only one letter. Press enter to continue.')
        
        #-- Checking if the player sent a number
        if letter_.isdigit():
            raise LetterError('ERROR: Enter only letters. Press enter to continue.')

        #-- Checking if the sent letter has already been tried
        if letter_ in self.tried:
            raise LetterError('ERROR: Letter already tried. Press enter to continue.')

        #-- Calls the 'validate_letter' to te letter sent by the player
        validate = word_logic.validate_letter(letter_, self.word, self.blink)

        #-- Checks if the player didin't hit 
        if validate == self.blink:
            self.chances -= 1
            self.tried.append(letter_)
        
        #-- If the player got it right, assign the new String to the 'blink' variable
        else:
            self.blink = validate

    def board(self):
        """Function that calls the 'print_board' method of the 'Board' class"""
        os.system('cls')
        self.game_board.print_board(self.chances)

    def print_end(self):
        """Function that print the result of the game"""
        if self.win_lose == 'Win':
            print('Congratulations! you win.')
        else:
            print('You lose.')

    def __call__(self):
        """Function that sews all the material created and runs the game"""
        #-- Creates a repeating loop that will run until the game is over  
        while self.still == True:
            try:
                self.board()
                print()
                print(self.blink)
                print(f'You still have: {self.chances} attempts')
                print(f'Letters already tried: {self.tried}')
                self.validate_hit()
                self.validate_end()
                self.validate_win()

            except LetterError as error:
                print(f'{error.__class__.__name__} : {error}')
                input()

        self.board()
        self.print_end()
        

    def __str__(self):
        """Function that print the game informations"""
        return f'{self.word} | {self.blink} | attempts = {self.chances}'        