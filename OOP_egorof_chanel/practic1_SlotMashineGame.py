import random

class Slot_General:
    def __init__(self, slots_quantyty=3, combinations=None, score_money=0, roll_price = 10):
        self.__slots_quantyty = slots_quantyty
        self.__combinations = combinations
        self.__score_money = score_money
        self.__roll_price = roll_price

    def get_score(self):
        return self.__score_money

    def set_score_loss(self, loss):
        self.__score_money -= loss
        return self.__score_money

    def win_money(self, winning, mult):
        self.__score_money += (int(winning) * int(mult))

    def deposit(self, summe):
        self.__score_money += summe
        print(f'Your score now: {self.get_score()}')
        return self.__score_money


    def get_multipl(self):
        return self.__roll_price

    def get_slot_quantyty(self):
        return self.__slots_quantyty

    def __print_loss(self):
        print("you loss")
        print(f"You score: {self.get_score()}")
        print("-------------------")

    def choises_roll_result(self, mult, list_roll):
        self.set_score_loss(int((self.get_multipl())) * int(mult))
        list_choises = []
        for i in range(0, self.get_slot_quantyty()):
            chois = random.choice(list_roll)
            list_choises.append(chois)
        return list_choises

    def check_combination(self, strfinal, combination, mult):
        if strfinal in combination:
            amount = combination[strfinal]
            if amount > 0:
                print(f"Yes you win!!! {strfinal} = {amount} * {mult}")
                self.win_money(amount, mult)
                print(f"You score: {self.get_score()}")
                print("-----------")
            else:
                self.__print_loss()
        else:
            self.__print_loss()



class Slot_Mashine01(Slot_General):
    def __init__(self):
        self.list_roll = ["K", "P", "Q", "7", "A", "Z"]
        self.combination = {
            "KK": 5,
            "KKK": 10,
            "777": 500,
            "77": 100,
            "AAA": 100,
            "AA": 50,
            "PP": 5,
            "PPP": 10,
            "QQQ": 5,
            "ZZZ": 5,
            "-": 0
        }
        super().__init__()

    def roll(self, mult):

        list_choises =self.choises_roll_result(mult, self.list_roll)
        strfinal = "-"
        print("-------------------")
        print("|                 |")
        print(f"|    {list_choises[0]} - {list_choises[1]} - {list_choises[2]}    |")
        print("|                 |")
        print("-------------------")
        if list_choises[0] == list_choises[1] and list_choises[0] == list_choises[2]:
            strfinal = str(list_choises[0] + list_choises[1] + list_choises[2])
        elif list_choises[0] == list_choises[1]:
            strfinal = list_choises[0] + list_choises[1]
        elif list_choises[1] == list_choises[2]:
            strfinal = list_choises[1] + list_choises[2]


        self.check_combination(strfinal, self.combination, mult)



class Game_Slot:

    def __init__(self):
        self.__t = Slot_Mashine01()

    def run_game(self):
        stop = True
        while stop:
            x = input("Enter for run roll or EXIT for finish game: ")
            if x == "EXIT":
                stop = False
            y = input("Enter your multiple: ")
            self.__t.roll(y)

    def deposit(self, x:int):
        self.__t.deposit(x)

game1 = Game_Slot()
game1.deposit(100)
game1.run_game()
