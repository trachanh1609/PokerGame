import unittest
import Deck

class DeckObjectsTest(unittest.TestCase):
    def setUp(self):
        self._deck = Deck.Deck()
        self._player1 = Deck.Player("Jack")
        self._player2 = Deck.Player("John")
        self._board = Deck.Player("Board")

        self._deck.reset_deck()
        print "SetUp. Deck has" , self._deck._cards

    def test_Deck_class_reset_cards_function(self):
        self.assertEqual(len(self._deck._cards),52)
        self.assertNotEqual(self._deck._cards, list(Deck.DECK))
        print "\nInitiate deck, should have 52 random cards. Deck has", \
            len(self._deck._cards) , "cards"
        print "They are" , self._deck._cards

        self.assertListEqual(self._deck._random_card, [])

    def test_Deck_class_deal_to_function(self):
        self._deck.deal_to(self._player1)
        self.assertEqual(len(self._deck._cards),51)
        self.assertEqual(len(self._player1._cards),1)
        print "\nDeal 1st card, self._player1 has", self._player1._cards
        print "Deck has", len(self._deck._cards) , "cards"

        self._deck.deal_to(self._player1)
        self.assertEqual(len(self._deck._cards),50)
        self.assertEqual(len(self._player1._cards),2)
        print "Deal 2nd card, self._player1 has", self._player1._cards
        print "Deck has", len(self._deck._cards) , "cards"

    def test_Player_class_reset_cards_function(self):
        self._player1.reset_player_cards()
        self.assertEqual(len(self._player1._cards),0)
        print "\nReset player's card, self._player1 has", self._player1._cards


if __name__ == '__main__':
    unittest.main()
