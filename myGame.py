import numpy
import random
from myGams_toolbox import *


class game:
    def __init__(self):
        self.score = 0
        self._difficulty = 5
        self.new_game()
        for i in range(3):
            self.get_guess()
            self.check_guess()

    def new_game(self):
        self.code = list()
        # for i in range(5):
        #     self.code.append(random.randint(1, self._difficulty))
        self.code = [1, 1, 1, 2, 2]
        self.code_np = list(map(int, '0'*self._difficulty))
        for i in range(len(self.code_np)):
            self.code_np[i] = number_population(i+1, self.code)
        print(self.code_np)

    def get_guess(self):
        print("Enter your guess")
        self.guess = list(map(int, input()))[:5]

    def check_guess(self):
        code_chance = list(self.code_np)
        respons = ''
        for index, value in enumerate(self.guess):
            print('chance of {0} is {1}'.format(
                value, code_chance[value-1]))
            if code_chance[value - 1] <= 0:
                respons += '\033[1;31mW'
            elif value == self.code[index]:
                respons += '\033[1;32mC'
                code_chance[value - 1] -= 1
            elif value in self.code:
                respons += '\033[1;33mP'
                code_chance[value - 1] -= 1
            else:
                respons += '\033[1;31mW'
        print(self.code)
        print(self.guess)
        print(respons, '\033[0m')
        print(self.code_np)


game()
