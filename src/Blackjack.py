import Blackjack_ASCII as ASCII
import Blackjack_Lib as Lib
import Blackjack_AI as AI
import Blackjack_UI as UI
import Blackjack_Comment as Comment
import time
from colorama import init, Fore
import random

# Initialize colorama
init(autoreset=True)

class Game:
    def __init__(self):
        self.player_hand = []
        self.AI_hand = []
        self.deck = Lib.shuffle_deck()
        self.player_money = 1000
        self.ai_money = 1000
        self.total_pot = 0
        self.game_over = False
        self.card_count = 0
        self.difficulty = self.get_difficulty()
        self.mode = self.get_mode()
        self.player_is_big_blind = True
        self.player_bet = 0
        self.ai_bet = 0

    def get_mode(self):
        while True:
            mode = input(Fore.CYAN + "Choose mode (reshuffle, continuous) [r/c]: ").lower()
            if mode in ["reshuffle", "continuous", "r", "c"]:
                return mode
            print(Fore.RED + "Invalid input. Please enter 'reshuffle' or 'continuous'.")

    def get_difficulty(self):
        while True:
            difficulty = input(Fore.CYAN + "Choose difficulty (easy, medium, hard, ultra hard) [e/m/h/u]: ").lower()
            difficulty_map = {
                "e": "easy",
                "m": "medium",
                "h": "hard",
                "u": "ultra hard"
            }
            if difficulty in difficulty_map:
                return difficulty_map[difficulty]
            elif difficulty in ["easy", "medium", "hard", "ultra hard"]:
                return difficulty
            print(Fore.RED + "Invalid input. Please enter 'easy', 'medium', 'hard', or 'ultra hard'.")

    def game_loop(self):
        while not self.game_over:
            self.random_event()
            if self.mode == "reshuffle":
                self.deck = Lib.shuffle_deck()
            print(Fore.YELLOW + "\n" + "-" * 40)
            print(Fore.YELLOW + ASCII.drawing_art())
            print(Fore.YELLOW + "-" * 40)
            time.sleep(1)

            self.player_hand = Lib.get_hand(self.deck, 2)
            self.AI_hand = Lib.get_hand(self.deck, 2)
            print(Fore.GREEN + "\nYour hand:")
            Lib.display_hand(self.player_hand, False)
            print(Fore.RED + "\nDealer's hand:")
            Lib.display_hand(self.AI_hand, hide_first_card=True)
            print(Fore.GREEN + f"\nYour hand value: {Lib.get_hand_value(self.player_hand)}")
            time.sleep(1.5)

            player_stands = False
            ai_stands = False

            while not player_stands or not ai_stands:
                if not player_stands:
                    self.player_move = Lib.get_move()
                    if self.player_move == 'h':
                        drawn_card = self.deck.pop()
                        self.player_hand.append(drawn_card)
                        self.card_count = Lib.update_card_count(drawn_card, self.card_count)
                        print(Fore.GREEN + "\nYour hand:")
                        Lib.display_hand(self.player_hand, False)
                        print(Fore.GREEN + f"\nYour hand value: {Lib.get_hand_value(self.player_hand)}")
                        time.sleep(1)
                        if Lib.get_hand_value(self.player_hand) > 21:
                            break
                    else:
                        player_stands = True

                if not ai_stands:
                    print(Fore.RED + "\nDealer is deciding...")
                    time.sleep(random.uniform(1.5, 2.5))
                    self.ai_move = AI.get_AI_move(self.AI_hand, self.AI_hand[0].split()[0], self.difficulty, self.card_count)
                    
                    if self.ai_move == 'h':
                        Comment.dealer_commentary("hit", self.difficulty, self.ai_money)
                        drawn_card = self.deck.pop()
                        self.AI_hand.append(drawn_card)
                        self.card_count = Lib.update_card_count(drawn_card, self.card_count)
                        print(Fore.RED + "\nDealer's hand:")
                        Lib.display_hand(self.AI_hand, hide_first_card=True)
                        time.sleep(1)
                        if Lib.get_hand_value(self.AI_hand) > 21:
                            break
                    else:
                        Comment.dealer_commentary("stand", self.difficulty, self.ai_money)
                        ai_stands = True

            print(Fore.YELLOW + "\n" + "-" * 40)
            print(Fore.YELLOW + ASCII.betting_art())
            print(Fore.YELLOW + "-" * 40)
            time.sleep(1)
            print(Fore.GREEN + "Your hand:")
            Lib.display_hand(self.player_hand, False)
            print(Fore.GREEN + f"Your hand value: {Lib.get_hand_value(self.player_hand)}")
            print(Fore.RED + "Dealer's hand:")
            Lib.display_hand(self.AI_hand, hide_all_cards=True)
            time.sleep(1)

            if Lib.get_hand_value(self.player_hand) > 21:
                print(Fore.RED + "You busted! Dealer wins this round.")
                Comment.dealer_commentary("player_bust", self.difficulty, self.ai_money)
                self.player_money -= self.player_bet
                self.ai_money += self.player_bet
                time.sleep(2)
                continue
            elif Lib.get_hand_value(self.AI_hand) > 21:
                print(Fore.GREEN + "Dealer busted! You win this round!")
                Comment.dealer_commentary("dealer_bust", self.difficulty, self.ai_money)
                self.player_money += self.ai_bet
                self.ai_money -= self.ai_bet
                time.sleep(2)
                continue
            else:
                time.sleep(1)
                self.betting_round()

            print(Fore.RED + "Dealer's hand:")
            Lib.display_hand(self.AI_hand, hide_first_card=False)
            print(Fore.RED + f"Dealer's hand value: {Lib.get_hand_value(self.AI_hand)}")
            time.sleep(1)

            self.win_check()
            if self.player_money <= 0:
                print(Fore.RED + "You are out of money! Game over.")
                print(Fore.RED + ASCII.lose_art())
                time.sleep(3)
                self.prompt_restart()
            if self.ai_money <= 0:
                print(Fore.GREEN + "You have won the game!")
                print(Fore.GREEN + ASCII.win_art())
                time.sleep(3)
                self.prompt_restart()

    def handle_blinds(self):
        big_blind = 20
        little_blind = 10
        if self.player_is_big_blind:
            self.player_money -= big_blind
            self.ai_money -= little_blind
            self.player_bet = big_blind
            self.ai_bet = little_blind
            print(Fore.GREEN + f"\nPlayer posts big blind: ${big_blind}")
            print(Fore.RED + f"Dealer posts little blind: ${little_blind}")
        else:
            self.player_money -= little_blind
            self.ai_money -= big_blind
            self.player_bet = little_blind
            self.ai_bet = big_blind
            print(Fore.GREEN + f"\nPlayer posts little blind: ${little_blind}")
            print(Fore.RED + f"Dealer posts big blind: ${big_blind}")
        self.total_pot = big_blind + little_blind
        self.player_is_big_blind = not self.player_is_big_blind

    def betting_round(self):
        self.handle_blinds()
        player_folded = False
        ai_folded = False
        player_stands = False
        ai_stands = False

        while not player_folded and not ai_folded and not player_stands and not ai_stands:
            print(Fore.YELLOW + f"\nTotal Pot: ${self.total_pot}")
            print(Fore.GREEN + f"Your Money: ${self.player_money}")
            print(Fore.RED + f"Dealer's Money: ${self.ai_money}")
            time.sleep(1)

            player_bet = self.get_player_bet()
            if player_bet == -1:
                player_folded = True
                break
            elif player_bet == 0:
                player_stands = True
            else:
                self.player_bet += player_bet
                self.total_pot += player_bet
                self.player_money -= player_bet
                print(Fore.GREEN + f"You bet ${player_bet}.")
                print(Fore.GREEN + f"Your Remaining Money: ${self.player_money}")
                time.sleep(1)

            print(Fore.RED + "\nDealer is deciding...")
            time.sleep(random.uniform(1.5, 2.5))
            ai_bet = self.get_ai_bet()
            if ai_bet == -1:
                ai_folded = True
                break
            elif ai_bet == 0:
                ai_stands = True
            else:
                self.ai_bet += ai_bet
                self.total_pot += ai_bet
                self.ai_money -= ai_bet
                print(Fore.RED + f"Dealer raises by ${ai_bet}.")
                print(Fore.RED + f"Dealer's Remaining Money: ${self.ai_money}")
                time.sleep(1.5)

            print(Fore.YELLOW + f"Updated Total Pot: ${self.total_pot}")
            time.sleep(1)

            if self.player_bet == self.ai_bet and player_stands and ai_stands:
                break

        if player_folded:
            print(Fore.RED + "You folded. Dealer wins.")
            self.ai_money += self.total_pot
        elif ai_folded:
            print(Fore.GREEN + "Dealer folded. You win!")
            self.player_money += self.total_pot
        elif player_stands and ai_stands:
            print(Fore.YELLOW + "Both players stand. Proceeding to showdown.")
        time.sleep(2)
    
    def get_player_bet(self):
        max_bet = min(self.player_money, 100 + self.card_count * 10)
        while True:
            try:
                bet = int(input(f"You have ${self.player_money}. Enter your bet (max ${max_bet}, -1 to fold, 0 to stand): "))
                if bet == -1 or bet == 0:
                    return bet
                elif bet > max_bet:
                    print(f"You cannot bet more than the maximum allowed (${max_bet}).")
                elif bet <= 0:
                    print("You must bet a positive amount.")
                else:
                    return bet
            except ValueError:
                print("Invalid input. Please enter a number.")

    def get_ai_bet(self):
        ai_bet = AI.get_AI_bet(self.AI_hand, self.ai_money, self.ai_bet, self.total_pot, self.difficulty)
        return ai_bet

    def win_check(self):
        player_value = Lib.get_hand_value(self.player_hand)
        ai_value = Lib.get_hand_value(self.AI_hand)
        print(Fore.YELLOW + "\n" + "-" * 40)
        print(Fore.YELLOW + "Checking results...")
        print(Fore.YELLOW + "-" * 40)
        time.sleep(2)

        if player_value > 21:
            print(Fore.RED + "You busted! Dealer wins this round.")
            Comment.dealer_commentary("player_bust", self.difficulty, self.ai_money)
            self.ai_money += self.total_pot
        elif ai_value > 21:
            print(Fore.GREEN + "Dealer busted! You win this round!")
            Comment.dealer_commentary("dealer_bust", self.difficulty, self.ai_money)
            self.player_money += self.total_pot
        elif player_value > ai_value:
            print(Fore.GREEN + "You win this round!")
            Comment.dealer_commentary("lose", self.difficulty, self.ai_money)
            self.player_money += self.total_pot
            self.ai_money -= self.total_pot
        elif player_value < ai_value:
            print(Fore.RED + "Dealer wins this round.")
            Comment.dealer_commentary("win", self.difficulty, self.ai_money)
            self.player_money -= self.total_pot
            self.ai_money += self.total_pot
        else:
            print(Fore.YELLOW + "It's a tie!")
            Comment.dealer_commentary("tie", self.difficulty, self.ai_money)
        time.sleep(2)

    def prompt_restart(self):
        if UI.prompt_restart():
            self.__init__()
            self.game_loop()
        else:
            self.game_over = True

    def random_event(self):
        event = random.choice(["reshuffle_penalty", "forced_bet", None])
        if event == "reshuffle_penalty":
            print(Fore.YELLOW + "Random Event: Deck reshuffled! Card count reset.")
            self.deck = Lib.shuffle_deck()
            self.card_count = 0
        elif event == "forced_bet":
            penalty = min(50, self.player_money)
            print(Fore.RED + f"Random Event: Forced bet! You lose ${penalty}.")
            self.player_money -= penalty
            self.total_pot += penalty

    def dealer_commentary(self, event):
        pass

if __name__ == "__main__":
    print(Fore.MAGENTA + ASCII.title_art())
    print(Fore.MAGENTA + "\n" + "Welcome to Blackjack!")
    print(Fore.MAGENTA + "Get ready to test your luck and strategy.")
    print(Fore.MAGENTA + "-"*40 + "\n")
    time.sleep(2)   
    
    game = Game()
    game.game_loop()