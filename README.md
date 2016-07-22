PokerGame is written in Python 2.7. The game is based on Texas Holdem Poker.
Each player has 2 private cards and there are 5 common cards on the table

Features :
- The game can evaluate 7 card hand.
- Hand has 5 best cards out of 7 cards.
- The 5 best cards are sorted in ascending order to simplify the hand comparison in case 2 hands have the same category. For example : when a hand is One Pair, the last 2 cards are the Pair, the third card is the highest Kicker, the second card is the second highest Kicker, the first card is the third highest Kicker.
- There are 2 players at the moment : User and the House.


To play the game, open Terminal and go to PokerGame directory then execute this command

MacBook-Pro:PokerGame User$ python Poker.py

------------------------INSTRUCTION----------------------------------
Welcome to Texas Holdem Poker
Game Rules :
Each player has 2 cards. There are common cards on the table
The cards on the table are dealt in this order : FLOP(3 cards), TURN, RIVER
Player places the Bet before cards are dealt. Player can Check, Raise or Fold

Abbreviation :
S: Spades , C: Clubs , D: Diamonds, H: Hearts
T: 10 , J: Jack , Q: Queen , K: King , A: Ace
Examples:
4H : Four of diamonds
JC : Jack of clubs
-----------------------END OF INSTRUCTION----------------------------
Press Enter to continue ...
Enter amount of chips per player ( recommended 1000 ): 200
Enter Big blind ( recommended 20 ): 20
---------------------ROUND 1 -----------------------
Player has  200 chips
House has  200 chips
Big blind is 20
Dealer has dealt 2 cards for each player
Player has : ['9S', 'QH']
House has : [X,X]
Board has : []
Player : 180 chips. House : 180 chips.  Pot: 40 chips
(C)heck  (R)aise  (F)old or (E)xit game ?r
----------------------------------------------------
Player Raised
This is the FLOP
Player has : ['9S', 'QH']
House has : [X,X]
Board has : ['QC', '2S', '6S']
Player : 160 chips. House : 160 chips.  Pot: 80 chips
(C)heck  (R)aise  (F)old or (E)xit game ?r
----------------------------------------------------
Player Raised
This is the TURN
Player has : ['9S', 'QH']
House has : [X,X]
Board has : ['QC', '2S', '6S', 'KH']
Player : 140 chips. House : 140 chips.  Pot: 120 chips
(C)heck  (R)aise  (F)old or (E)xit game ?r
----------------------------------------------------
Player Raised
This is the RIVER
Player has : ['9S', 'QH']
House has : [X,X]
Board has : ['QC', '2S', '6S', 'KH', '5D']
Player : 120 chips. House : 120 chips.  Pot: 160 chips
(C)heck  (R)aise  (F)old or (E)xit game ?c
----------------------------------------------------
Player Checked
This is the FINAL
Player has : ['9S', 'QH']
House has : [X,X]
Board has : ['QC', '2S', '6S', 'KH', '5D']
Player : 120 chips. House : 120 chips.  Pot: 160 chips


Player WINS this round
Common cards on table: ['QC', '2S', '6S', 'KH', '5D']
House has 2 cards: ['AC', 'TD']
Player has 2 cards: ['9S', 'QH']


House has High Card ['6S', 'TD', 'QC', 'KH', 'AC']
Player has One Pair ['6S', '9S', 'KH', 'QH', 'QC']
Player : 280 chips. House : 120 chips.  Pot: 0 chips
Press Enter to continue
---------------------ROUND 2 -----------------------
Player has  280 chips
House has  120 chips
Big blind is 20
Dealer has dealt 2 cards for each player
Player has : ['8S', 'QH']
House has : [X,X]
Board has : []
Player : 260 chips. House : 100 chips.  Pot: 40 chips
(C)heck  (R)aise  (F)old or (E)xit game ?
