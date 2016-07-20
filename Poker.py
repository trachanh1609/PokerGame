from Hand import Hand
from Deck import PokerGame

def main():
    player_name = "Player"
    amount = 0
    big_blind = 20

    print_instruction()
    amount = ask_amount_of_chips_per_player()
    big_blind = ask_for_blind()
    Game = PokerGame(player_name, amount, big_blind)
    Game.start()


def print_instruction():
    print "------------------------INSTRUCTION----------------------------------"
    print "Welcome to Texas Holdem Poker"
    print "Game Rules :"
    print "Each player has 2 cards. There are common cards on the table"
    print "The cards on the table are dealt in this order : FLOP(3 cards), TURN, RIVER"
    print "Player places the Bet before cards are dealt. Player can Check, Raise or Fold"
    print "\n"
    print "Abbreviation :"
    print "S: Spades , C: Clubs , D: Diamonds, H: Hearts"
    print "T: 10 , J: Jack , Q: Queen , K: King , A: Ace"
    print "Examples:"
    print "4H : Four of diamonds"
    print "JC : Jack of clubs"
    print "-----------------------END OF INSTRUCTION----------------------------"
    raw_input("Press Enter to continue ...")

def ask_amount_of_chips_per_player():
    amount = 0
    while True:
        try:
            amount = int(raw_input("Enter amount of chips per player ( recommended 1000 ): "))
        except ValueError:
            print "Oops!  That was no valid number.  Try again..."
        else:
            if amount in range(1,1000000):
                break
            else:
                print "Oops! Out of range, should be from 1-1000000 chips. Try again..."
    return amount

def ask_for_blind():
    blind = 0
    blind_list = [1,2,5,10,15,20,25,30,40,50,60,70,80,90,100,150,200,300,400,500]
    while True:
        try:
            blind = int(raw_input("Enter Big blind ( recommended 20 ): "))
        except ValueError:
            print "Oops!  That was no valid number.  Try again..."
        else:
            if blind in blind_list:
                break
            else:
                print "Oops! Out of range"
                print "Available blind is [1,2,5,10,15,20,25,30,40,50,60,70,80,90,100,150,200,300,400,500].Try again..."
    return blind



if __name__ == "__main__":
    main()
