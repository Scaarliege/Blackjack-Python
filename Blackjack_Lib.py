def shuffle_deck():
    import random
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    deck = [f"{rank} of {suit}" for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck

def get_hand(deck):
    hand = [deck.pop() for _ in range(2)]
    return hand

def get_hand_value(hand):
    card_value = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 10,
        "Q": 10,
        "K": 10,
        "A": [1, 11]
    }
    value = 0
    aces = 0
    for card in hand:
        rank = card.split()[0]
        if rank == "A":
            value += card_value[rank][1]
            aces += 1
        else:
            value += card_value[rank]
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

def display_hand(hand, hide_first_card):
    if hide_first_card:
        print("Dealer's hand: [X, " + ", ".join(hand[1:]) + "]")
    else:
        print("Hand: [" + ", ".join(hand) + "]")

def get_bet(player_money):
    while True:
        try:
            bet = int(input(f"You have ${player_money}. How much would you like to bet? "))
            if bet > player_money:
                print("You cannot bet more than you have.")
            elif bet <= 0:
                print("You must bet a positive amount.")
            else:
                return bet
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_move():
    while True:
        move = input("Enter 'h' to hit or 's' to stand: ").lower()
        if move in ['h', 's']:
            return move
        else:
            print("Invalid input. Please enter 'h' or 's'.")