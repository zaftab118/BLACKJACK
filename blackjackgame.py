from Player import Player
from Dealer import Dealer

dealer = Dealer(50000)
player = Player(500)

print("Welcome to ThoTho's Blackjack!")
print("==============================")


def play_game(dealer1, player1):
    prize_pool = 0

    # player places a bet before the cards are dealt
    while player1.money > 0 and dealer1.money > 0:
        print('You currently have $' + str(round(player1.money, 2)) + ' to play with.')
        bet = 0
        while True:  # loop will run until break
            try:  # will let user input an integer, if a non-int is input a Value Error is raised
                bet = float(input('Please place your bet: $'))
            except ValueError:  # will replace the ValueError with a print statement
                print('Please enter a value between 1 and ' + str(player.money))
            if 0 < bet <= player1.money:  # ensures the bet can't be negative or above player's current money
                break
        prize_pool += player1.bet(bet) + dealer1.bet(bet)
        print('The prize pool is now $' + str(prize_pool) + '. Good luck!')
        print('You have $' + str(round(player1.money, 2)) + ' remaining.')
        print('---------------------------')
        break

    player1.hit()
    player1.hit()
    print('Your Hand')

    player1.print_hand()
    print("\n" + "Hand Value: " + str(player1.hand_value()))
    print('---------------------------')
    check_one = player1.invoke_win_check()
    if check_one[1] == 'Y':
        play_game(dealer1, player1)

    if not player1.invoke_win_check()[0]:
        dealer1.hit()
        dealer1.hit_face_down_card()
        print('Dealer Hand')
        dealer1.print_hand()

    possible_hands_less_21 = True

    for hand in player1.hand_value():
        if hand < 21:
            possible_hands_less_21 = False

    while possible_hands_less_21 < 21 and not player1.invoke_win_check()[0]:

        valid = True
        hit_or_stay = input('Hit or Stay? Type H/S: ')
        if hit_or_stay != 'H':
            if hit_or_stay != 'S':
                valid = False
        while not valid:
            print("Please enter a valid input.")
            break

        if hit_or_stay == 'H':
            player1.hit()
            print("===========================")
            print('Your Hand')
            player1.print_hand()
            print("\n" + "Hand Value: " + str(player1.hand_value()))
            print('---------------------------')
            # print('Dealer Hand')
            # dealer1.print_hand()
            state = player1.invoke_win_check()
            if state[1] == 'Y':
                dealer1.reset_game()
                play_game(dealer1, player1)
        elif hit_or_stay == 'S':
            player1.stay_hand()
            print('=================')
            print('Your Hand')
            player1.print_hand()
            print("\n" + "Hand Value: " + str(player1.hand_value()))
            print('---------------------------')
            break

    # Dealer's turn once player stays
    print("\nDealer begins to play!")
    print('---------------------------')
    dealer.flip_card(dealer.hand[1])
    print('Dealer Hand')
    dealer.print_hand()
    print("\n" + "Hand Value: " + str(dealer1.hand_value()))
    dealer1.invoke_win_check()
    print('-----------------------')

    dealer_possible_hands_less_21 = True

#Check into this later, to evaluate to give dealer more help in the game to not get rocked by forcing ace to be 11
    for hand in dealer1.hand_value():
        if hand < 17:
            dealer_possible_hands_less_21 = False

#Fix this to check while dealer possible hands are less than 21
    while dealer_possible_hands_less_21 < 17:
        dealer1.hit()
        print('Dealer Hand')
        dealer.print_hand()
        print("\n" + "Hand Value: " + str(dealer1.hand_value()))
        print('---------------------------')

    # > 21 it works
    # 20, 19 is broken
    # 21 works

    # ------------------------#
    print("The dealer\'s hand adds up to " + str(dealer1.hand_value()))
    print("The player hand adds up to " + str(player1.hand_value()))
    game_over = dealer1.invoke_win_check

    if game_over[0]:
        dealer_win = player1.hand_value() < dealer1.hand_value() <= 21
        dealer_tie = dealer1.hand_value() == player1.hand_value()

        if dealer.hand_value() != 21:
            if dealer_win and dealer1.hand_value():
                print('The dealer beat your hand value!')
                print('-----------------------')
                dealer.money += prize_pool
            elif dealer_tie:
                print('You tied the dealer.')
                print('-----------------------')
                dealer.money += prize_pool/2
                player.money += prize_pool/2
            else:
                print('The player wins!')
                print('-----------------------')
                player.money += prize_pool

    game_over = dealer1.game_controller(game_over)

    if game_over[1] == 'Y':
        player1.reset_game()
        play_game(dealer1, player1)


# CASH OUT
# if the player beats the dealer, the pool money is added to their money and gets subtracted from the dealers money
# if the player loses against the dealer, the money is subtracted from their money and added to the dealers
# if it's a tie, both dealer and player get their original bet back


play_game(dealer, player)

# REMAINING TASKS/ERRORS
# Assign Y and N for dealer invoke win check
# game returns to hit/stay while loop when dealer hits 20 no clue why v gay
# implement bets [almost done]
# fix A to include both 1 and 11

# WHEN PLAYER REACHES 21 WITH AN ACE IN HAND, GAME DOES NOT RESET PLAYER HAND WHEN YOU PRESS Y, ONLY RESETS DEALER HAND
# ---------------------------------------------------------------------------
# create pygame
