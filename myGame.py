import os
import random
from myGams_toolbox import *


class game:
    def __init__(self):
        self.score = 0
        self._difficulty = 5
        self.screen_cleaner = False
        while True:
            if self.screen_cleaner:
                os.system('clear')
            print('choice one of this option for continue:')
            print('q        close the program\ns        go to setting mode')
            print('d        set difficulty\nother    start a new game')
            ch = input()[:1]
            if ch == 'q':
                break
            elif ch == 'd':
                self._difficulty += 1
                continue
            elif ch == 's':
                self.setting()
                continue
            else:
                pass
            if self.screen_cleaner:
                os.system('clear')
            self.new_game()
            for i in range(10):
                self.get_guess()
                score = self.check_guess()
                if score == 10:
                    print(
                        'You Win 👍 \nyou score {0} +{1}'.format(self.score, 100 - i*10))
                    self.score += (100 - i*10)
                    break

    def new_game(self):
        self.code = list()
        for i in range(5):
            self.code.append(random.randint(1, self._difficulty))
        # self.code = [1, 1, 1, 2, 2]
        self.code_np = list(map(int, '0'*self._difficulty))
        for i in range(len(self.code_np)):
            self.code_np[i] = number_population(i+1, self.code)
        # print(self.code_np)

    def get_guess(self):
        print("Enter your guess")
        valid = False
        while not valid:
            try:
                self.guess = list(map(int, input()))[:5]
                valid = True
            except ValueError:
                print('Please enter your guess just in 5 digits number')

    def check_guess(self):
        code_chance = list(self.code_np)
        respons = ''
        score = 0
        for index, value in enumerate(self.guess):
            # print('chance of {0} is {1}'.format(
            #     value, code_chance[value-1]))
            if code_chance[value - 1] <= 0:
                respons += '\033[1;31mW'
            elif value == self.code[index]:
                respons += '\033[1;32mC'
                code_chance[value - 1] -= 1
                score += 2
            elif value in self.code:
                respons += '\033[1;33mP'
                code_chance[value - 1] -= 1
                score += 1
            else:
                respons += '\033[1;31mW'
        # print(self.code)
        # print(self.guess)
        print(respons, '\033[0m')
        # print(self.code_np)
        return score

    def setting(self):
        print('choice one of this option for continue:')
        print('a        activate screen cleaning after each game')
        print('d        deactivate screen cleaning after each game')
        choice = input('> ')[:1]
        if choice == 'a' or choice == 'A':
            self.screen_cleaner = True
        elif choice == 'd' or choice == 'D':
            self.screen_cleaner = False


game()
