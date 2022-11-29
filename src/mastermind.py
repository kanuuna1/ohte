import random

class Mastermind:

    def __init__(self):
        self.size = 4

    #def create_code_with_duplicates(self):
    #    code = []
    #    for i in range(self.size):
    #        code.append(random.randint(1, 6))
    #    return code

    def create_code(self):
        code = random.sample(range(1, 6), self.size)
        return code

    def play(self):
        code = self.create_code()
        print(code)

        turn = 1
        while True:
            if turn >= 8:
                print("Game over")
                break
            guess = self.get_guess()
            if guess == code:
                print("You won!")
                break
            feedback_list = self.compare(code, guess)
            print(f"Feedback: {feedback_list}")
            turn+=1

    def compare(self, list1, list2):
        feedback = []
        list_1 = list1[:]
        list_2 = list2[:]
        #mustat; poista tarkastellut listalta
        for count1, value1 in enumerate(list1):
            for count2, value2 in enumerate(list2):
                if count1 == count2 and value1 == value2:
                    feedback.append("black")
                    list_1[count1] = None
                    list_2[count2] = None
        for count1, value1 in enumerate(list1):
            for count2, value2 in enumerate(list2):
                if count1 != count2 and value1 == value2 and value1 is not None:
                    feedback.append("white")
                    list_1[count1] = None
                    list_2[count2] = None
        return feedback

    def get_guess(self):
        guess = []
        print("Anna nelinumeroinen arvauksesi: ")
        while True:
            if len(guess) == 4:
                break
            try:
                num = int(input("Anna luku: "))
            except ValueError:
                num = -1
            if num < 1 or num > 6:
                print("luvun tulee olla välillä 1-6")
                continue
            guess.append(num)
        return guess


if __name__ == "__main__":
    m = Mastermind()
    m.play()
    