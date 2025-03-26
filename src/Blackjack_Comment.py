import random
from colorama import Fore
import time

def get_dealer_comments(difficulty, dealer_money):
    """Return dealer comments based on difficulty and remaining money."""
    money_status = "rich" if dealer_money > 500 else "low" if dealer_money < 200 else "moderate"

    comments = {
        "easy": {
            "hit": {
                "rich": ["I'll take another card. Feeling lucky!", "Hit me! I've got plenty to spare."],
                "moderate": ["I'll take another card.", "Hmm, let's see what I get!"],
                "low": ["I'll take another card... running out of luck here.", "Hit me! I need this."]
            },
            "stand": {
                "rich": ["I'll stay here. No need to risk it.", "Standing with confidence!"],
                "moderate": ["I'll stay here.", "I think I'll stop now."],
                "low": ["I'll stand... can't afford to lose more.", "Stopping here. Let's see what happens."]
            },
            "win": ["Oh, I won!", "Yay, I got lucky!", "Looks like I win this time!"],
            "lose": ["Oh no, you got me!", "Well played, you win!", "I guess luck wasn't on my side."],
            "tie": ["It's a tie!", "We both did well!", "Looks like it's even."],
            "player_bust": ["Oh no, you went over 21!", "Better luck next time!", "You busted!"],
            "dealer_bust": ["Oops, I went over 21!", "Looks like I busted!", "You win this one!"]
        },
        "medium": {
            "hit": {
                "rich": ["I'll take another card. Let's keep this streak going!", "Hit me! I'm feeling good."],
                "moderate": ["I'll take another card.", "Let's see if this works."],
                "low": ["I'll take another card... need to turn this around.", "Hit me! I need a miracle."]
            },
            "stand": {
                "rich": ["I'll stand with this. Feeling confident!", "Stopping here. This should be enough."],
                "moderate": ["I'll stand with this.", "Stopping here."],
                "low": ["I'll stand... can't risk losing more.", "Stopping here. Let's hope for the best."]
            },
            "win": ["I win this round.", "Good game, but I win!", "Looks like I came out on top."],
            "lose": ["You win this time.", "Well played, you got me.", "I couldn't beat you this round."],
            "tie": ["It's a tie.", "We both played well.", "Looks like it's even."],
            "player_bust": ["You went over 21! That's unfortunate.", "Busted! Better luck next time.", "You lost this one."],
            "dealer_bust": ["I busted! Well played.", "Looks like I went over 21.", "You win this round."]
        },
        "hard": {
            "hit": {
                "rich": ["I'll take another card. Let's dominate this game!", "Hit me! I'm in control."],
                "moderate": ["I'll take another card.", "Let's see if I can improve."],
                "low": ["I'll take another card... this is risky.", "Hit me! I need to recover."]
            },
            "stand": {
                "rich": ["I'll stand with this. Victory is near!", "Stopping here. This should be enough."],
                "moderate": ["I'll stand with this.", "Stopping here."],
                "low": ["I'll stand... can't afford to lose more.", "Stopping here. Let's see how it goes."]
            },
            "win": ["Another win for me.", "I outplayed you this time.", "Looks like I win again."],
            "lose": ["You got lucky this time.", "Well played, but I'll get you next time.", "You win this round."],
            "tie": ["It's a tie.", "We both played well.", "Looks like it's even."],
            "player_bust": ["You busted! That's a shame.", "Over 21? Better luck next time.", "You lost this one."],
            "dealer_bust": ["I busted! You win this time.", "Looks like I went over 21.", "Well played, you win."]
        },
        "ultra hard": {
            "hit": {
                "rich": ["I'll take another card. Victory is inevitable!", "Hit me! I'm unstoppable."],
                "moderate": ["I'll take another card.", "Let's see if I can perfect this hand."],
                "low": ["I'll take another card... desperate times.", "Hit me! I need to turn this around."]
            },
            "stand": {
                "rich": ["I'll stand with this. Another win in the bag!", "Stopping here. This should crush you."],
                "moderate": ["I'll stand with this.", "This should be enough to win."],
                "low": ["I'll stand... can't risk losing everything.", "Stopping here. Let's see what happens."]
            },
            "win": ["Another one in the bag.", "You can't beat me.", "Victory is mine again."],
            "lose": ["You got lucky, but it won't happen again.", "Well played, but don't get used to it.", "You win this round, but I'll dominate next time."],
            "tie": ["It's a tie, but I'll win next time.", "We both played well, but I'll outplay you soon.", "Looks like it's even, for now."],
            "player_bust": ["You busted! Too bad.", "Over 21? Amateur mistake.", "You lost this one."],
            "dealer_bust": ["I busted? Impossible!", "You win this time, but don't get cocky.", "Well played, but I'll be back."]
        }
    }

    return comments[difficulty]

def dealer_commentary(event, difficulty, dealer_money):
    comments = get_dealer_comments(difficulty, dealer_money)
    if event in comments:
        if isinstance(comments[event], dict):
            money_status = "rich" if dealer_money > 500 else "low" if dealer_money < 200 else "moderate"
            print(Fore.RED + f"Dealer: {random.choice(comments[event][money_status])}")
        else:
            print(Fore.RED + f"Dealer: {random.choice(comments[event])}")
    time.sleep(1.5)