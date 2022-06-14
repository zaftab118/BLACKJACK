import sys

from Deck import Deck
import random


class Player:

    cash_out = False

    def __init__(self, money):
        self.deck = Deck()
        self.money = money
        self.hand = []
        self.stay = False
        self.aces = 0

    def bet(self, amount):
        if (self.money > 0) and (0 < amount <= self.money):
            self.money -= amount
            return amount
        return False

    def stay_hand(self):
        if not self.stay:
            self.stay = True

    def hit(self):
        card_position = random.randint(0, len(self.deck.cards) - 1)
        self.hand.append(self.deck.cards.pop(card_position))

    # def hand_value(self):
    #     hand_sum = 0
    #     for card in self.hand:
    #         card_holder = card.value
    #         if (card.value == 'J') or (card.value == 'Q') or (card.value == 'K'):
    #             card_holder = 10
    #         if card.value == 'A':
    #             card_holder = 11
    #         hand_sum += card_holder
    #     return hand_sum
    #
    # def check_ace(self):
    #     while self.hand_value() > 21 and self.aces:
    #         self.hand_value -= 10
    #         self.aces -= 1

    def reset_game(self):
        self.hand = []
        self.deck = Deck()

    def invoke_win_check(self):
        game_end = [False, '']
        possible_hands = self.hand_value()

        for hand in possible_hands:
            if hand == 21:
                print("\nYour cards add up to 21! You win!")
                self.reset_game()
                game_end[0] = True
            if hand > 21:
                print("You bust.")
                self.reset_game()
                game_end[0] = True

            if game_end[0]:
                keep_playing = input('Play again? Y/N? ')
                if keep_playing == 'Y':
                    game_end[0] = False
                    game_end[1] = 'Y'
                    self.reset_game()
                    print("===========================")
                if keep_playing == 'N':
                    self.cash_out = True
                    game_end[0] = True
                    game_end[1] = 'N'
                    print('Your total cash is: $' + str(self.money))
                    print("===========================")
                    sys.exit(1)
                # if keep_playing != 'Y' or keep_playing != 'N':
                #     print('That is not a valid option.')
        return game_end

    def print_hand(self):
        for card in self.hand:
            if card.show:
                print(card.value, end="\t")
            elif not card.show:
                print("X")

    def hand_value(self):
        hand_sum = 0
        is_ace = False
        possible_hand_values = []
        for card in self.hand:
            card_holder = card.value
            if (card.value == 'J') or (card.value == 'Q') or (card.value == 'K'):
                card_holder = 10
            if card.value == 'A':
                is_ace = True
                card_holder = 1
            hand_sum += card_holder
        if is_ace:
            possible_hand_values.append(hand_sum)
            if hand_sum + 10 <= 21:
                possible_hand_values.append(hand_sum + 10)
        if not is_ace:
            possible_hand_values.append(hand_sum)
        if is_ace:
            is_ace = not is_ace
        return possible_hand_values

