PokerGame is written in Python 2.7. The game is based on Texas Holdem Poker.
Each player has 2 private cards and there are 5 common cards on the table

Features :
- The game can evaluate 7 card hand.
- Hand has 5 best cards out of 7 cards.
- The 5 best cards are sorted in ascending order to simplify the hand comparison in case 2 hands have the same category. For example : when a hand is One Pair, the last 2 cards are the Pair, the third card is the highest Kicker, the second card is the second highest Kicker, the first card is the third highest Kicker.
- There are 2 players at the moment : User and the House.


To play the game, open Terminal and go to PokerGame directory then execute this command

MacBook-Pro:PokerGame User$ python Poker.py
