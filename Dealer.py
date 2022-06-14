import sys

from Deck import Deck
from Card import Card
import random
from Player import Player


class Dealer(Player):

    def __init__(self, money):
        self.money = money
        super().__init__(money)

    def hit_face_down_card(self):
        card_position = random.randint(0, len(self.deck.cards) - 1)
        face_down_card = self.deck.cards.pop(card_position)
        self.hand.append(face_down_card)
        face_down_card.show = False

    def flip_card(self, card):
        if not card.show:
            card.show = True

    def invoke_win_check(self):
        game_end = [False, '']
        possible_hands = self.hand_value()
        for hand in possible_hands:
            if hand == 21:
                print('The dealer\'s hand adds up to 21! You lose.')
                game_end[0] = True
            if hand > 21:
                print("The dealer\'s bust!")
                game_end[0] = True
            if 16 < hand < 21:
                game_end[0] = True
        return game_end

    def game_controller(self, game_end):
        if game_end[0]:
            offer_to_play_again = input('Would you like to play again? Y/N? ')
            if offer_to_play_again == 'Y':
                game_end[0] = False
                game_end[1] = 'Y'
                self.reset_game()
                print("===========================")
            if offer_to_play_again == 'N':
                self.cash_out = True
                game_end[0] = True
                game_end[1] = 'N'
                print('Your total cash is: $' + str(self.money))
                print("===========================")
                sys.exit(1)

            return game_end






# for i in range(len(zozo.deck.cards)):
#     print("Before: ", len(zozo.deck.cards))
#     random_card = zozo.deal_face_up_card()
#     print(str(random_card.value) + " of " + random_card.suit)
#     print("After: ", len(zozo.deck.cards))
#     print("----------------")

# card1 = zozo.deal_face_up_card()
# card2 = zozo.deal_face_down_card()
#
#
# list_cards = [card1, card2]
#
# for card in list_cards:
#     if card.show == False:
#         print('Card is Facedown!')
#     else:
#         print(card.suit, card.value)

# create flip card face up



