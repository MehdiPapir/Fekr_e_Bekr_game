import numpy
import random
from myGams_toolbox import *


class game:
    def __init__(self):
        self.score = 0
        self._difficulty = 5
        self.new_game()
        for i in range(3):
            self.get_answer()

    def new_game(self):
        self.code = list()
        for i in range(5):
            self.code.append(random.randint(1, self._difficulty))
        self.code_np = list(map(int, '0'*self._difficulty))

    def get_answer(self):
        print("Enter your guess")
        self.guess = list(map(int, input()))[:5]
        respons = ''
        for i in range(len(self.code)):
            if self.guess[i] == self.code[i]:
                respons += '\033[1;32mC'
            elif self.guess[i] in self.code:
                respons += '\033[1;33mP'
            else:
                respons += '\033[1;31mW'
        print(self.code)
        print(self.guess)
        print(respons, '\033[0m')


game()
