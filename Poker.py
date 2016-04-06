from Hand import Hand

def main():
    
    myHand = Hand("Vu")
    # myCards = ["7C","8C","3C","9C","TC","JC","TD"]
    
    # Straight Check
    #myCards = ["7C","8D","3C","9S","TC","JC","TD"]
    
    # Straight Flush Check
    #myCards = ["2C","4C","5C","3C","TC","AC","8C"]

    # Quad 
    #myCards = ["7C","8D","7D","7S","TC","7H","TD"]

    # Fullhouse
    #myCards = ["AC","8D","7D","7S","TC","7H","TD"]
    #myCards = ["7C","8D","7D","TS","TC","7H","TD"]

    # TwoPairs 
    #myCards = ["7C","8D","AD","7S","TC","KH","TD"]

    # Trips
    #myCards = ["7C","8D","7D","AS","TC","7H","JD"]

    # One Pair
    myCards = ["7C","TD","5D","AS","TC","3H","JD"]


    myHand.setCards(myCards)

    myHand.showPlayerCards()
    myHand.evaluateHand()

    
if __name__ == "__main__": main()