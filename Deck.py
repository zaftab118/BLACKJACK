from Card import Card


class Deck:

    def __init__(self):
        self.cards = []
        self.create_deck()

    def create_deck(self):
        suits = ['Spades', 'Hearts', 'Diamond', 'Clover']
        values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
        for suit in suits:
            for value in values:
                new_card = Card(suit=suit, value=value)
                self.cards.append(new_card)


# my_deck = Deck()
# for card in my_deck.cards:
#     print(card.suit + " " + str(card.value))
