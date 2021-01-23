import random

class Cards:
    #__suits = ["Spades", "Hearts", "Clubs", "Diamonds"] # Масти - пики, червы, трефы и бубны
    #__name_cards = ["Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
    __suits = ["Пика", "Черв", "Треф", "Бубна"]  # Масти - пики, червы, трефы и бубны
    __name_cards = ["Шест", "Семь", "Восемь", "Девять", "Десять", "Валет", "Дама", "Король", "Туз"]
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

    #TEST
    def hod(self, test_cards_user):
        res = random.randint(1, 6)
        print(f"Уничтожено {res} Карт")
        for card in random.sample(test_cards_user.keys(), res):
            del test_cards_user[card]


class Round():
    __deck = Cards()
    __user = User()

    def __init__(self):
        self.deck = self.__deck.shufle_deck()
        self.user_cards = self.__user.get_cards_user()

    def afish_quant_cards_deck(self):
        return len(self.deck)

    def __take_card_general(self, cards_user, max_card=6):
        for card in random.sample(self.deck.keys(), (max_card - len(cards_user))):
            val = self.deck[card]
            del self.deck[card]
            self.__user.set_cards(card, val)
        return cards_user

    def start_game_card_taken(self, cards_user):
        cards_user = self.__take_card_general(cards_user)
        return cards_user

    def take_cards(self, cards_user):
        if len(cards_user) < 6:
            print(f"Вы берете {6 - len(cards_user)} карты")
            self.__take_card_general(cards_user)
        elif len(cards_user) == 6:
            print("У вас 6 карт. Вы НЕ берете карты.")
        else:
            print("У Вас больше 6 карт. Вы НЕ берете карты")

    #Test
    def ggg(self):
        self.__user.hod(self.user_cards)

    def jjj(self):
        return  self.__user.get_cards_user()


f = Round()
print(f.start_game_card_taken(f.user_cards))
print(f"in deck {f.afish_quant_cards_deck()}")
f.ggg()
print(f"Cart user is: {f.jjj()}")
f.take_cards(f.user_cards)
print(f"in deck {f.afish_quant_cards_deck()}")
print(f"Cart user is: {f.jjj()}")