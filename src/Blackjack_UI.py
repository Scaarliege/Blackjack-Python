import Blackjack_Lib as Lib

def display_welcome_message():
    print("\n" + "-" * 50)
    print("Welcome to Blackjack!")
    print("Get ready to test your luck and strategy.")
    print("-" * 50 + "\n")

def display_player_hand(player_hand, player_money):
    print("\n" + "-" * 50)
    print("Your Hand:")
    print("Cards: [" + ", ".join(player_hand) + "]")
    print(f"Total Value: {Lib.get_hand_value(player_hand)}")
    print(f"Your Money: ${player_money}")
    print("-" * 50)

def display_dealer_hand(dealer_hand, hide_first_card=True):
    print("\n" + "-" * 50)
    if hide_first_card:
        print("Dealer's Hand: [X, " + ", ".join(dealer_hand[1:]) + "]")
    else:
        print("Dealer's Hand: [" + ", ".join(dealer_hand) + "]")
    print(f"Dealer's Total Value: {Lib.get_hand_value(dealer_hand)}")
    print("-" * 50)

def display_betting_info(player_bet, ai_bet):
    print("\n" + "-" * 50)
    print(f"Your Bet: ${player_bet}")
    print(f"Dealer's Bet: ${ai_bet}")
    print("-" * 50)

def display_game_result(player_hand, dealer_hand):
    player_value = Lib.get_hand_value(player_hand)
    dealer_value = Lib.get_hand_value(dealer_hand)
    print("\n" + "-" * 50)
    print("Final Results:")
    print(f"Your Hand Value: {player_value}")
    print(f"Dealer's Hand Value: {dealer_value}")
    print("-" * 50)

    if player_value > 21:
        print("You busted! Dealer wins this round.")
    elif dealer_value > 21:
        print("Dealer busted! You win this round!")
    elif player_value > dealer_value:
        print("You win this round!")
    elif player_value < dealer_value:
        print("Dealer wins this round.")
    else:
        print("It's a draw!")

def prompt_restart():
    while True:
        restart = input("Do you want to play again? (y/n): ").lower()
        if restart in ['y', 'n']:
            return restart == 'y'
        print("Invalid input. Please enter 'y' or 'n'.")