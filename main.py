from Game import *
from HangMan import *
import sys

if __name__ == "__main__":
    new_game = True
    while new_game:
        h = HangMan()
        g = Game(h)
        new_game = g.run()
        if new_game == False:
            sys.exit()

