import unittest
from Hand import Hand

class HandEvaluationTest(unittest.TestCase):
    def test_high_card(self):
        myHand = Hand("Vu")
        myCards = ["7C","8D","3C","KS","TC","JC","4D"]
        expected = ['7C', '8D', 'TC', 'JC', 'KS']
        myHand.setCards(myCards)
        myHand.evaluateHand()

        self.assertEqual(myHand._category, 1)
        self.assertEqual(myHand._five_cards, expected)
        myHand.show_player_cards()
        myHand.show_player_evaluated_hand_name()
        myHand.show_player_evaluated_five_cards()

    def test_one_pair(self):
        myHand = Hand("Vu")
        myCards = ["7C","TD","5D","AS","TC","3H","JD"]
        expected = ['7C', 'JD', 'AS', 'TC', 'TD']
        myHand.setCards(myCards)
        myHand.evaluateHand()

        self.assertEqual(myHand._category, 2)
        self.assertEqual(myHand._five_cards, expected)
        myHand.show_player_cards()
        myHand.show_player_evaluated_hand_name()
        myHand.show_player_evaluated_five_cards()

    def test_two_pairs(self):
        myHand = Hand("Vu")
        myCards = ["7C","8D","AD","7S","TC","KH","TD"]
        expected = ['AD', '7S', '7C', 'TD', 'TC']
        myHand.setCards(myCards)
        myHand.evaluateHand()

        self.assertEqual(myHand._category, 3)
        self.assertEqual(myHand._five_cards, expected)
        myHand.show_player_cards()
        myHand.show_player_evaluated_hand_name()
        myHand.show_player_evaluated_five_cards()

    def test_three_of_a_kind(self):
        myHand = Hand("Vu")
        myCards = ["7C","8D","7D","AS","TC","7H","JD"]
        expected = ['JD', 'AS', '7H', '7D', '7C']
        myHand.setCards(myCards)
        myHand.evaluateHand()

        self.assertEqual(myHand._category, 4)
        self.assertEqual(myHand._five_cards, expected)
        myHand.show_player_cards()
        myHand.show_player_evaluated_hand_name()
        myHand.show_player_evaluated_five_cards()

    def test_straight(self):
        myHand = Hand("Vu")
        myCards = ["7C","8D","3C","9S","TC","JC","TD"]
        expected = ["7C","8D","9S","TC","JC"]
        myHand.setCards(myCards)
        myHand.evaluateHand()

        self.assertEqual(myHand._category, 5)
        self.assertEqual(myHand._five_cards, expected)
        myHand.show_player_cards()
        myHand.show_player_evaluated_hand_name()
        myHand.show_player_evaluated_five_cards()

    def test_flush(self):
        myHand = Hand("Vu")
        myCards = ["2C","4S","5C","3C","TC","AC","8C"]
        expected = ['3C', '5C', '8C', 'TC', 'AC']
        myHand.setCards(myCards)
        myHand.evaluateHand()

        self.assertEqual(myHand._category, 6)
        self.assertEqual(myHand._five_cards, expected)
        myHand.show_player_cards()
        myHand.show_player_evaluated_hand_name()
        myHand.show_player_evaluated_five_cards()

    def test_full_house_1(self):
        myHand = Hand("Vu")
        myCards = ["AC","8D","7D","7S","TC","7H","TD"]
        expected = ['TC', 'TD', '7D', '7S', '7H']
        myHand.setCards(myCards)
        myHand.evaluateHand()

        self.assertEqual(myHand._category, 7)
        self.assertEqual(myHand._five_cards, expected)
        myHand.show_player_cards()
        myHand.show_player_evaluated_hand_name()
        myHand.show_player_evaluated_five_cards()

    def test_full_house_2(self):
        myHand = Hand("Vu")
        myCards = ["7C","8D","7D","TS","TC","7H","TD"]
        expected = ['7C', '7D', 'TS', 'TC', 'TD']
        myHand.setCards(myCards)
        myHand.evaluateHand()

        self.assertEqual(myHand._category, 7)
        self.assertEqual(myHand._five_cards, expected)
        myHand.show_player_cards()
        myHand.show_player_evaluated_hand_name()
        myHand.show_player_evaluated_five_cards()

    def test_four_of_a_kind(self):
        myHand = Hand("Vu")
        myCards = ["7C","8D","7D","7S","TC","7H","TD"]
        expected = ['TC', '7C', '7D', '7S', '7H']
        myHand.setCards(myCards)
        myHand.evaluateHand()

        self.assertEqual(myHand._category, 8)
        self.assertEqual(myHand._five_cards, expected)
        myHand.show_player_cards()
        myHand.show_player_evaluated_hand_name()
        myHand.show_player_evaluated_five_cards()

    def test_straight_flush(self):
        myHand = Hand("Vu")
        myCards = ["2C","4C","5C","3C","TC","AC","8C"]
        expected = ['AC', '2C', '3C', '4C', '5C']
        myHand.setCards(myCards)
        myHand.evaluateHand()

        self.assertEqual(myHand._category, 9)
        self.assertEqual(myHand._five_cards, expected)
        myHand.show_player_cards()
        myHand.show_player_evaluated_hand_name()
        myHand.show_player_evaluated_five_cards()


if __name__ == '__main__':
    unittest.main()
