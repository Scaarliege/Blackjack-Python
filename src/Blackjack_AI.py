import random
from Blackjack_Lib import get_hand_value

def get_AI_move(hand, dealer_card=None, difficulty="easy", card_count=None):
    value = get_hand_value(hand)
    random_factor = random.randint(-1, 1)

    if difficulty == "easy":
        return "h" if value + random_factor < 17 else "s"
    elif difficulty == "medium":
        if value + random_factor < 17 or (value == 17 and dealer_card == "A"):
            return "h"
        return "s"
    elif difficulty == "hard":
        if value + random_factor < 17 or (value == 17 and dealer_card in ["7", "8", "9", "10", "J", "Q", "K"]) or (value == 18 and dealer_card in ["9", "10", "J", "Q", "K"]):
            return "h"
        return "s"
    elif difficulty == "ultra hard":
        if card_count is not None:
            if card_count > 0:
                return "h" if value + random_factor < 19 else "s"
            return "h" if value + random_factor < 17 else "s"
        if value + random_factor < 17 or (value == 17 and dealer_card in ["7", "8", "9", "10", "J", "Q", "K", "A"]) or (value == 18 and dealer_card in ["9", "10", "J", "Q", "K", "A"]) or (value == 19 and dealer_card in ["10", "J", "Q", "K", "A"]):
            return "h"
        return "s"

def get_AI_bet(hand, ai_money, current_bet, total_pot, difficulty="easy"):
    value = get_hand_value(hand)
    if ai_money - current_bet <= 0:
        return 0

    if current_bet > ai_money * 0.5:
        return -1

    if difficulty == "easy":
        return min(10, ai_money - current_bet)
    elif difficulty == "medium":
        return min(20 if value < 17 else 30, ai_money - current_bet)
    elif difficulty == "hard":
        return min(30 if value < 17 else 20, ai_money - current_bet)
    elif difficulty == "ultra hard":
        if value < 17:
            return min(50, ai_money - current_bet)
        elif value < 19:
            return min(40, ai_money - current_bet)
        return min(30, ai_money - current_bet)
    return 0