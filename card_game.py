import random


class Card:
    """ A class to describe cards in a pack """
    def __init__(self, number):
        self._card_number = number

    def get_suit(self):
        suit_num = self._card_number // 13
        suit_list = ['C', 'S', 'D', 'H']
        return suit_list[suit_num]

    def get_value(self):
        number = self._card_number % 13
        value_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
        return value_list[number]

    def get_short_name(self):
        value = str(self.get_value())
        suit = self.get_suit()
        return value + suit

    def get_long_name(self):
        value_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
        suit_list = ['Clubs', 'Spades', 'Diamonds', 'Hearts']
        value = value_list[self._card_number % 13]
        suit = suit_list[self._card_number // 13]
        long_name = f"{value} of {suit}"
        return long_name


class Deck:
    """ A class to contain a pack of cards with methods for shuffling, adding or removing cards etc. """
    def __init__(self):
        self._card_list = []
        for i in range(52):
            self._card_list.append(Card(i))

    def length(self):
        length = len(deck._card_list)
        return length

    def shuffle_deck(self):
        """ shuffles the cards """
        random.shuffle(self._card_list)

    def take_top_card(self):
        top_card = deck._card_list.pop()
        return top_card


deck = Deck()
deck.shuffle_deck()

for j in range(deck.length()):
    card = deck.take_top_card()
    print(card.get_long_name())


