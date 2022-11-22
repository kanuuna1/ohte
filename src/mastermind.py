import os
import random


class Mastermind:
    

    def __init__(self, size):
        self.size = size

    def moikkaa(self):
        print("Hello")

    def create_code(self):
        code =[]
        for i in range(self.size):
            code.append(random.randint(1,6))
        return code

    def create_code_without_duplicates(self):
        code = random.sample(range(1,6), self.size)
        return code

    def check(self, guess, code):
        if (guess == code):
            print("You won!")
        else:
            print("Wrong")

if __name__ == "__main__":
    m = Mastermind(4)
    code = m.create_code_without_duplicates()
    print(f"Code: {code}")
    guess = [1,4,2,3]
    m.check(guess, code)