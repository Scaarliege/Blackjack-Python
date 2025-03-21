import Blackjack_ASCII as ASCII
import Blackjack_Lib as Lib
import Blackjack_AI as AI
import time
from colorama import init, Fore
import pyfiglet

# Initialize colorama
init(autoreset=True)

class Game:
    def __init__(self):
        self.player_hand = []
        self.AI_hand = []
        self.deck = Lib.shuffle_deck()
        self.player_money = 1000
        self.player_move = ""
        self.player_bet = 0
        self.ai_move = ""
        self.ai_bet = 0
        self.ai_money = 1000
        self.bet = 0
        self.game_over = False
        self.card_count = 0
        self.difficulty = ""
        self.mode = self.get_mode()
    
    def get_mode(self):
        while True:
            mode = input(Fore.CYAN + "Choose mode (reshuffle, continuous): ").lower()
            if mode in ["reshuffle", "continuous"]:
                return mode
            else:
                print(Fore.RED + "Invalid input. Please enter 'reshuffle' or 'continuous'.")
    
    def get_difficulty(self):
        while True:
            self.difficulty = input(Fore.CYAN + "Choose difficulty (easy, medium, hard, ultra hard): ").lower()
            if self.difficulty in ["easy", "medium", "hard", "ultra hard"]:
                break
            else:
                print(Fore.RED + "Invalid input. Please enter 'easy', 'medium', 'hard', or 'ultra hard'.")
    
    def game_loop(self):
        while not self.game_over:
            if self.mode == "reshuffle":
                self.deck = Lib.shuffle_deck()
            print(Fore.YELLOW + "\n" + "-"*40)
            print(Fore.YELLOW + "Starting a new round...")
            print(Fore.YELLOW + "-"*40)
            time.sleep(1)
            self.get_bet()
            self.player_hand = Lib.get_hand(self.deck)
            self.AI_hand = Lib.get_hand(self.deck)
            print(Fore.GREEN + "\nYour hand:")
            Lib.display_hand(self.player_hand, False)
            print(Fore.RED + "\nDealer's hand:")
            Lib.display_hand(self.AI_hand, True)
            print(Fore.GREEN + f"\nYour hand value: {Lib.get_hand_value(self.player_hand)}")
            time.sleep(1)
            
            player_stands = False
            ai_stands = False
            
            while not player_stands or not ai_stands:
                if not player_stands:
                    self.player_move = Lib.get_move()
                    if self.player_move == 'h':
                        self.player_hand.append(self.deck.pop())
                        print(Fore.GREEN + "\nYour hand:")
                        Lib.display_hand(self.player_hand, False)
                        print(Fore.GREEN + f"\nYour hand value: {Lib.get_hand_value(self.player_hand)}")
                        if Lib.get_hand_value(self.player_hand) > 21:
                            break
                    else:
                        player_stands = True
                
                if not ai_stands:
                    if self.difficulty == "easy":
                        self.ai_move = AI.get_easy_AI_move(self.AI_hand)
                    elif self.difficulty == "medium":
                        self.ai_move = AI.get_medium_AI_move(self.AI_hand, self.AI_hand[0].split()[0])
                    elif self.difficulty == "hard":
                        self.ai_move = AI.get_hard_AI_move(self.AI_hand, self.AI_hand[0].split()[0])
                    elif self.difficulty == "ultra hard":
                        if self.mode == "continuous":
                            self.ai_move = AI.get_ultra_hard_AI_move(self.AI_hand, self.AI_hand[0].split()[0], self.card_count)
                        else:
                            self.ai_move = AI.get_ultra_hard_AI_move(self.AI_hand, self.AI_hand[0].split()[0])
                    
                    if self.ai_move == 'h':
                        self.AI_hand.append(self.deck.pop())
                        print(Fore.RED + "\nDealer's hand:")
                        Lib.display_hand(self.AI_hand, True)
                        if Lib.get_hand_value(self.AI_hand) > 21:
                            break
                    else:
                        ai_stands = True
            
            print(Fore.YELLOW + "\n" + "-"*40)
            print(Fore.YELLOW + "Final hands:")
            print(Fore.YELLOW + "-"*40)
            time.sleep(1)
            print(Fore.GREEN + "Your hand:")
            Lib.display_hand(self.player_hand, False)
            print(Fore.GREEN + f"Your hand value: {Lib.get_hand_value(self.player_hand)}")
            print(Fore.RED + "Dealer's hand:")
            Lib.display_hand(self.AI_hand, False)
            print(Fore.RED + f"Dealer's hand value: {Lib.get_hand_value(self.AI_hand)}")
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
    
    def get_bet(self):
        print(Fore.YELLOW + "\n" + "-"*40)
        print(Fore.YELLOW + "Place your bet")
        print(Fore.YELLOW + "-"*40)
        time.sleep(1)
        self.player_bet = Lib.get_bet(self.player_money)
        if self.difficulty == "easy":
            self.ai_bet = AI.get_easy_AI_bet()
        elif self.difficulty == "medium":
            self.ai_bet = AI.get_medium_AI_bet(self.AI_hand)
        elif self.difficulty == "hard":
            self.ai_bet = AI.get_hard_AI_bet(self.AI_hand)
        elif self.difficulty == "ultra hard":
            self.ai_bet = AI.get_ultra_hard_AI_bet(self.AI_hand)
    
    def win_check(self):
        player_value = Lib.get_hand_value(self.player_hand)
        ai_value = Lib.get_hand_value(self.AI_hand)
        print(Fore.YELLOW + "\n" + "-"*40)
        print(Fore.YELLOW + "Checking results...")
        print(Fore.YELLOW + "-"*40)
        time.sleep(2)
        if player_value > 21:
            print(Fore.RED + "You busted! Dealer wins.")
            self.player_money -= self.player_bet
        elif ai_value > 21 or player_value > ai_value:
            print(Fore.GREEN + "You win!")
            self.player_money += self.player_bet
        elif player_value < ai_value:
            print(Fore.RED + "Dealer wins.")
            self.player_money -= self.player_bet
        elif player_value == ai_value:
            print(Fore.YELLOW + "It's a tie!")
    
    def prompt_restart(self):
        while True:
            restart = input(Fore.CYAN + "Do you want to play another game? (yes/no): ").lower()
            if restart == "yes":
                self.reset_game()
                break
            elif restart == "no":
                self.game_over = True
                break
            else:
                print(Fore.RED + "Invalid input. Please enter 'yes' or 'no'.")
    
    def play(self):
        self.get_difficulty()
        self.game_loop()
    
    def reset_game(self):
        self.player_hand = []
        self.AI_hand = []
        self.deck = Lib.shuffle_deck()
        self.player_money = 1000
        self.ai_money = 1000
        self.game_over = False
        self.game_loop()

def main():
    print(Fore.CYAN + pyfiglet.figlet_format("Blackjack"))
    time.sleep(1)
    print(Fore.CYAN + "Welcome to Blackjack!")
    print(Fore.CYAN + "Instructions: Try to get as close to 21 as possible without going over. Good luck!\n")
    time.sleep(1)
    game = Game() 
    game.play()

if __name__ == "__main__":
    main()