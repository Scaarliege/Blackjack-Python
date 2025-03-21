def get_easy_AI_move(hand):
    from Blackjack_Lib import get_hand_value
    value = get_hand_value(hand)
    if value < 17:
        return "h"
    else:
        return "s"

def get_easy_AI_bet():
    return 10

def get_medium_AI_move(hand, dealer_card):
    from Blackjack_Lib import get_hand_value
    value = get_hand_value(hand)
    if value < 17:
        return "h"
    elif value == 17 and dealer_card == "A":
        return "h"
    else:
        return "s"

def get_medium_AI_bet(hand):
    from Blackjack_Lib import get_hand_value
    if get_hand_value(hand) < 17:
        return 20
    else:
        return 30

def get_hard_AI_move(hand, dealer_card):
    from Blackjack_Lib import get_hand_value
    value = get_hand_value(hand)
    if value < 17:
        return "h"
    elif value == 17 and dealer_card in ["7", "8", "9", "10", "J", "Q", "K"]:
        return "h"
    elif value == 18 and dealer_card in ["9", "10", "J", "Q", "K"]:
        return "h"
    else:
        return "s"

def get_hard_AI_bet(hand):
    from Blackjack_Lib import get_hand_value
    if get_hand_value(hand) < 17:
        return 30
    else:
        return 20

def get_ultra_hard_AI_move(hand, dealer_card, card_count=None):
    from Blackjack_Lib import get_hand_value
    value = get_hand_value(hand)
    if card_count is not None:
        if card_count > 0:
            if value < 19:
                return "h"
            else:
                return "s"
        else:
            if value < 17:
                return "h"
            else:
                return "s"
    else:
        if value < 17:
            return "h"
        elif value == 17 and dealer_card in ["7", "8", "9", "10", "J", "Q", "K", "A"]:
            return "h"
        elif value == 18 and dealer_card in ["9", "10", "J", "Q", "K", "A"]:
            return "h"
        elif value == 19 and dealer_card in ["10", "J", "Q", "K", "A"]:
            return "h"
        else:
            return "s"

def get_ultra_hard_AI_bet(hand):
    from Blackjack_Lib import get_hand_value
    if get_hand_value(hand) < 17:
        return 50
    elif get_hand_value(hand) < 19:
        return 40
    else:
        return 30