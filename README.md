### Description
PokerGame is a Poker Game based on Texas Hold'em rules. The Player plays against the House. Player choose the total amount of chips and a fixed Ante, for example 1000 chips per player and 20 chips Ante. Game is over when one player has no more chips.

### Installation
Game is written in Python 2.7, no dependencies so it will be working as long as Python 2.7 is installed. Follow the steps below:

 1. Install [Python 2.7](https://www.python.org/downloads/)
 2. Download or clone the project
 3. Open Terminal
 4. Navigate to the folder
 5. Run the Poker.py file PokerGame$python Poker.py

### Features :

- Hand.py evaluates 7 card and picks 5 best cards out of 7 cards.
- The 5 best cards are sorted in ascending order to simplify the hand comparison in case 2 hands have the same category.

( Note : S stands for Spades, C for Clubs, D for Diamonds, H for Hearts)
Ex1:
Input 7 cards ['KC', '2S', '6S', 'KH', '5D', '3D', '4S']
Hand.py will evaluates and picks out 5 cards ['2S', 3D', '4S', '5D', '6S'] - Straight , not One Pair

Ex2:
Input 7 cards ['KC', 'KS', '6S', 'KH', '6D', '6H', '4S']
Hand.py will evaluates and picks out 5 cards ['6S', 6D', 'KH', 'KD', 'KS']  - Full house '66KKK' not 'KK666'

### Test
hand_test.py is the test file for Hand.py and
deck_test.py is the test file for Deck.py

Hand.py contains the 7 card Evaluation
Deck.py contains the Game-Flow and all other Objects

### User Interface
Below is an example of the game



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
    4D : Four of diamonds  
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
