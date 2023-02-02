import word_logic
from game import Game

import os
#-- https://docs.python.org/3/library/os.html
os.system('cls')

if __name__ == '__main__':
    game = Game()
    print(game)    
    print()
    print(game.validate_end())
