from random import choice


class Choice:

    def __init__(self, *args):
        self.sequence = args

    def __get__(self, instance, owner):
        return choice(self.sequence)


class Deck:

    suits = Choice("Spades", "Hearts", "Diamonds", "Clubs")
    card = Choice(*tuple("23456789AKJQ"), "10")

    def __init__(self, deck_name):
        self.deck_name = deck_name

    def get_card(self):
        return f"{self.card:2} of {self.suits}"


my_deck = Deck("My English Deck")
for _ in range(10):
    print(my_deck.get_card())
