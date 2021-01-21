import random

class Person:
    __person_humor = ["good", "bad", "neitral"]
    __move_list = ["walking", "run", "march"]

    def __init__(self, move=None):
        self.name = input("Your name: ")
        self.move = move
        self.humor = random.choice(self.__person_humor)

    def __set_move(self, x):
        self.move = x

    def get_move(self):
        return self.move

    def get_humor(self):
        return self.humor

    def info_p(self):
        print(f"Hes name is {self.name} and he have {self.humor} humor")

    def set_change_H(self):
        x = random.randint(1, 100)
        if x <= 20:
            self.humor = random.choice(self.__person_humor)

    def set_move_change(self, meteo_Eta, humor):
        if meteo_Eta == "rain" and humor == "good":
            self.__set_move(self.__move_list[2])
            return self.move
        elif (meteo_Eta == "sun" or meteo_Eta == "cloud cover") and humor == "good":
            self.move = self.__move_list[0]
            return self.move
        elif (meteo_Eta == "rain" or meteo_Eta == "cloud cover") and humor == "bad":
            self.move = self.__move_list[1]
            return self.move
        elif meteo_Eta == "rain" and humor == "sun":
            self.move = self.__move_list[2]
            return self.move
        elif (meteo_Eta == "sun" or meteo_Eta == "cloud cover") and humor == "neitral":
            self.move = self.__move_list[2]
            return self.move
        elif meteo_Eta == "rain" and humor == "neitral":
            self.move = self.__move_list[1]
            return self.move


class Meteo:
    __meteo = ["rain", "sun", "cloud cover"]

    def __init__(self):
        self.meteo = random.choice(self.__meteo)

    def get_meteo_Eta(self):
        return self.meteo

    def set_change_Meteo(self):
        self.meteo = random.choice(self.__meteo)

#-----------------------------------------------------



def run():
    z = True
    p = Person()
    m = Meteo()
    while z:
        p.set_move_change(m.get_meteo_Eta(), p.get_humor())
        p.info_p()
        print(f"He {p.get_move()}, bechaus meteo is {m.get_meteo_Eta()} ")
        print("If humor change? Or Meteo?")
        m.set_change_Meteo()
        p.set_move_change(m.get_meteo_Eta(), p.get_humor())
        p.set_change_H()
        print("-" * 20)
        p.set_move_change(m.get_meteo_Eta(), p.get_humor())
        p.info_p()
        print(f"He {p.get_move()}, bechaus meteo is {m.get_meteo_Eta()} ")
        r = input("you wont exit? Entrez X: ")
        print("IIIIIIIIIIIIIIIIIIIIIII")
        if r == "X":
            z = False
            print("By-by!")


run()
