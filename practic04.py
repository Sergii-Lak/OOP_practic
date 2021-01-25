import random

class Cards:
    #__suits = ["Spades", "Hearts", "Clubs", "Diamonds"] # Масти - пики, червы, трефы и бубны
    #__name_cards = ["Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
    __suits = ["Пика", "Черв", "Треф", "Бубна"]  # Масти - пики, червы, трефы и бубны
    __name_cards = ["Шесть", "Семь", "Восемь", "Девять", "Десять", "Валет", "Дама", "Король", "Туз"]
    __final_deck = {}

    @classmethod
    def __deck_cards_creator(cls):
        """Эта функция создает колоду карт. Это словарь ключами которого есть название карт.
        Значения в словаре - это цифровая величина карты"""
        for value, name in enumerate(cls.__name_cards, 6):
            for j in cls.__suits:
                cls.__final_deck[(name + "_" + j)] = [name, value, j]
        return cls.__final_deck

    def shufle_deck(self):
        """ Эта функция возвращает уже перемешанную колоду карт.
        Случайно выбирается ключ и его значение и они удаляются из словаря,
        потом они снова добавляется в конец словаря"""
        diction = self.__deck_cards_creator()
        for el in random.sample(diction.keys(), 36):
            val = diction[el]
            del diction[el]
            diction[el] = val
        return diction

class User:

    def __init__(self):
        self.cards_user = {}

    def get_cards_user(self):
        return self.cards_user

    def set_cards(self, x, y):
        self.cards_user[x] = y

    def hod(self, test_cards_user):
        """ Ход одной картой на выбор игрока. Возвращает значение карты - список.
                      В клссе Round ее подхватывает метод turn  """
        cards_in_nand = test_cards_user.keys()
        print("Ваш ход. Карты в руке: ")
        for i in cards_in_nand:
            print(i)
        print("Какой картой будете ходить? Напишите название карты: ")
        card = input()
        while card not in cards_in_nand:
            print("У вас нет такой карты. Напишите правильное название карты: ")
            card = input()
        val = test_cards_user[card]
        del test_cards_user[card]
        return val

    def card_for_beat(self):
        """ Бьем карту игрока. Возвращает значение  карты  """
        print("Ваши карты: ")
        print(self.cards_user.keys())
        card = input("Какой картой будете бить? ")
        print(self.cards_user.keys())
        if card in self.cards_user:
            val = self.cards_user[card]
            del self.cards_user[card]
            return val
        else:
            print("У вас нет такой карты! Выберите карту снова: ")
            return self.card_for_beat()

class AI:
    pass

class Round:
    __deck = Cards()
    __user = User()
    #TEST
    __user2 = User()

    def __init__(self):
        self.deck = self.__deck.shufle_deck()
        self.user_cards = self.__user.get_cards_user()
        #Test
        self.user2_cards = self.__user2.get_cards_user()

    def afish_quant_cards_deck(self):
        return len(self.deck)

    def get_user1(self):
        return self.__user

    def get_user2(self):
        return self.__user2

    def __take_card_general(self, user, cards_user, max_card=6):
        for card in random.sample(self.deck.keys(), (max_card - len(cards_user))):
            val = self.deck[card]
            del self.deck[card]
            user.set_cards(card, val)
            print(f"Вы взяли {card}")
        return cards_user

    def start_game_card_taken(self, user, cards_user):
        """ Начало игры. Раздача шести карт. Возвращает словарь """
        cards_user = self.__take_card_general(user, cards_user)
        return cards_user

    def take_cards(self, user, cards_user):
        """ Подбор недостающих карт, если требуется"""
        if len(cards_user) < 6:
            print(f"Вы берете {6 - len(cards_user)} карты")
            self.__take_card_general(user, cards_user)
        elif len(cards_user) == 6:
            print("У вас 6 карт. Вы НЕ берете карты.")
        else:
            print("У Вас больше 6 карт. Вы НЕ берете карты")

    def turn(self, user,  cards_user):
        """ Ход одной картой на выбор игрока. Возвращает значение карты - список.
                      В клссе User ее родитель метод hod  """
        x = user.hod(cards_user)
        return x



#TEST

d = Round()
user1 = d.get_user1()
user2 = d.get_user2()
cards1 = d.user_cards
cards2 = d.user2_cards

d.start_game_card_taken(user1, cards1)
print("----------------------")
d.start_game_card_taken(user2, cards2)
print(d.afish_quant_cards_deck())
print(d.user_cards)
print("--------------------")
print(d.user2_cards)
print(d.turn(user1, cards1))
print(d.turn(user2, cards2))
print("--------------------")
print(d.user_cards)
print(d.user2_cards)
d.take_cards(user1, cards1)
d.take_cards(user2, cards2)
print("--------------------")
print("картой бить!!!")
print(user1.card_for_beat())
print(user2.card_for_beat())
print("--------------------")
d.take_cards(user1, cards1)
d.take_cards(user2, cards2)
print(d.afish_quant_cards_deck())