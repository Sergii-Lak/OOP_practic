
import random

class Prop:

    def __init__(self):
        self.__pass = '123'
        self.__numb = random.random()

    def get_pass(self):
        return str(self.__pass)

    def get_numb(self):
        return self.__numb


class Check:

    p = Prop()

    def __init__(self):
        self.passw = None
        self.__c = True

    def check_pass(self):
        while self.__c:
            self.passw = input("PASSWORD: ")
            if self.passw == self.p.get_pass():
                print("Connecting...")
                print(f"Number is: {self.p.get_numb()}")
                self.__c = False
            else:
                print("Your password not corrected!")

test = Check()
test.check_pass()

