
import random

class Cards:
    #__suits = ["Spades", "Hearts", "Clubs", "Diamonds"] # Масти - пики, червы, трефы и бубны
    #__name_cards = ["Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
    __suits = ["Пика", "Черв", "Треф", "Бубна"]  # Масти - пики, червы, трефы и бубны
    __name_cards = ["Шесть", "Семь", "Восемь", "Девять", "Десять", "Валет", "Дама", "Король", "Туз"]
    __final_deck = {}
    __trump = random.choice(__suits)
    __trump_list = []

    @classmethod
    def __deck_cards_creator(cls):
        """Эта функция создает колоду карт. Это словарь ключами которого есть название карт.
        Значения в словаре - это цифровая величина карты"""
        for value, name in enumerate(cls.__name_cards, 6):
            for j in cls.__suits:
                if j == cls.__trump:
                    print(f"@@@ {j} is = {cls.__trump}")
                    cls.__trump_list.append(name + "_" + j)
                cls.__final_deck[(name + "_" + j)] = [name, value, j]
        return cls.__final_deck

    @classmethod
    def shufle_deck(cls):
        """ Эта функция возвращает уже перемешанную колоду карт.
        Случайно выбирается ключ и его значение и они удаляются из словаря,
        потом они снова добавляется в конец словаря"""
        diction = cls.__deck_cards_creator()
        for el in random.sample(diction.keys(), 36):
            val = diction[el]
            del diction[el]
            diction[el] = val
        return diction

    @classmethod
    def trump_cards(cls):
        return cls.__trump_list

class User:
    deck = Cards.shufle_deck()
    trump_cards = Cards.trump_cards()

    def __init__(self):
        self.cards_user = {}

    def afish_quant_cards_deck(self):
        print(id(self.deck))
        print(f"V kolode: {self.deck} cards")
        return len(self.deck)

    def get_cards_user(self):
        return self.cards_user

    def set_cards(self, x, y):
        self.cards_user[x] = y

    def __take_card_general(self,  max_card=6):
        for card in random.sample(self.deck.keys(), (max_card - len(self.cards_user))):
            val = self.deck[card]
            del self.deck[card]
            self.set_cards(card, val)
            print(f"Вы взяли {card}")
        return self.cards_user

    def start_game_card_taken(self):
        """ Начало игры. Раздача шести карт. Возвращает словарь """
        cards_user = self.__take_card_general()
        return cards_user

    def hod(self):
        """ Ход одной картой на выбор игрока. Возвращает значение карты - список.
                      В клссе Round ее подхватывает метод turn  """
        cards_in_nand = self.cards_user.keys()
        print("Ваш ход. Карты в руке: ")
        for i in cards_in_nand:
            print(i)
        print("Какой картой будете ходить? Напишите название карты: ")
        card = input()
        while card not in cards_in_nand:
            print("У вас нет такой карты. Напишите правильное название карты: ")
            card = input()
        val = self.cards_user[card]
        del self.cards_user[card]
        return val

    def card_for_beat(self, card_oponent):
        """ Бьем карту игрока. Возвращает значение  карты  """
        print("Ваши карты: ")
        print(self.cards_user.keys())
        card = input("Какой картой будете бить? ")
        print(self.cards_user.keys())
        if card in self.cards_user:
            val = self.cards_user[card]
            if (card in self.trump_cards) and((card_oponent[0] + "_" + card_oponent[2]) in self.trump_cards):
                res = int((card_oponent[1])-(int(val[1])))
                if res < 0:
                    del self.cards_user[card]
                    return val
            elif (card in self.trump_cards):
                del self.cards_user[card]
                return val
            elif ((int(card_oponent[1]) - int(val[1])) < 0) and ((card_oponent[2]) == val[2]):
                del self.cards_user[card]
                return val
            else:
                print("Вы бьете не правильной картой. Выберите карту снова: ")
                return self.card_for_beat(card_oponent)
        else:
            print("У вас нет такой карты! Выберите карту снова: ")
            return self.card_for_beat(card_oponent)

    def turn(self):
        """ Ход одной картой на выбор игрока. Возвращает значение карты - список.
                      В клссе User ее родитель метод hod  """
        x = self.hod()
        return x

    def take_cards(self):
        """ Подбор недостающих карт, если требуется"""
        if len(self.cards_user) < 6:
            print(f"Вы берете {6 - len(self.cards_user)} карты")
            self.__take_card_general()
        elif len(self.cards_user) == 6:
            print("У вас 6 карт. Вы НЕ берете карты.")
        else:
            print("У Вас больше 6 карт. Вы НЕ берете карты")



class AI:
    pass

class Round:

    def __init__(self):
        self.user1 = User()
        self.user2 = User()

    def game(self):
        print(d.user1.trump_cards)
        print(d.user2.trump_cards)
        print(d.user1.start_game_card_taken())
        print(d.user2.start_game_card_taken())
        print("--------------------------------")
        print(d.user1.afish_quant_cards_deck())
        print(d.user2.afish_quant_cards_deck())
        print("--------------------------------")
        d.user2.card_for_beat(d.user1.hod())
        d.user1.take_cards()
        d.user2.take_cards()
        print("--------------------------------")
        d.user1.afish_quant_cards_deck()
        d.user2.afish_quant_cards_deck()
        print("--------------------------------")
        d.user1.card_for_beat(d.user2.hod())
        d.user2.take_cards()
        d.user1.take_cards()
        print(d.user1.get_cards_user())
        print(d.user2.get_cards_user())
        print("--------------------------------")
        print(d.user1.afish_quant_cards_deck())
        print(d.user2.afish_quant_cards_deck())


#TEST

d = Round()
d.game()