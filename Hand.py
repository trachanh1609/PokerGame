RANK_TO_STRING = {2: "2", 3: "3", 4: "4", 5: "5", 6: "6",7: "7",8: "8",9: "9",10: "T",11: "J",12: "Q",13: "K",14: "A"}
RANK_LOOKUP = "0023456789TJQKA2345"
SUIT_LOOKUP = "SCDH"

class Hand:
	def __init__(self, name):
		self._all_cards = []
		self.name = name            #   Player1_hand , Player2_hand
		self._category = 0			#	0:"Not_Yet_Evaluated" 1: "High_Card" , 9:"Straight_Flush"
		self._five_cards = []        #  ['4D','5D','9S','AS', 'AD']
		# self._fiveCardValue = []    # [9,8,7,6,5]  , [A,A,4,4,9]
		self._hand_name = ""        # High_Card , One_Pair , Flush etc
		self._rank_list = []	# rank_list =  ['2', '3', '4', '5', '8', 'T', 'A']
		self._suit_list = []	# suit_list =  ['C', 'D', 'H', 'C', 'C', 'H', 'S']
		self._flush_cards = []	# self._flush_cards = ['4D','5D','6D','7D','8D','AD']
		self._arranged_card = [] #arranged_card =  [[0], [1, '3C'], [1, '7C'], [1, '8D'], [1, '9S'], [2, 'TC', 'TD'], [1, 'JC']]
	
	def setCards(self,seven_cards = []):
		self._all_cards = seven_cards
		self._all_cards = sorted(self._all_cards ,key=lambda card: RANK_LOOKUP.index(card[0]))
		print "self._all_cards = " , self._all_cards

		for card in self._all_cards :
			self._rank_list.append(card[0])
			self._suit_list.append(card[1])

		print "self._rank_list = " , self._rank_list
		print "self._suit_list = " , self._suit_list

	def evaluateHand(self):
		"""
		Do Evaluation . After hand Evaluation, self.handCategory and sefl.handBestCards will not be None

		"""
		if len(self._all_cards) != 7 :
			raise Exception("There are not enough 7 cards in this hand, quit evaluation now ! ")
			

		print "Evaluating the hand"

		# sorting 7 cards based on their Rank
		# Both works exactly the same self._all_cards.sort(key=lambda card: RANK_LOOKUP.index(card[0]))
		

		# self._rank_list = # [ RANK_LOOKUP.index(card[0]) for card in self._all_cards]
		# print "self._rank_list = " , self._rank_list

		#self._arranged_card = self._get_rank_category(self._all_cards)
		#print "self._arranged_card = " , self._arranged_card
		self._sort_cards_by_rank(self._all_cards)
		

		# if self._has_straight_flush() :
		# 	self._category = 9
		# 	self._hand_name = "Straight Flush"
		# elif self._has_four() :
		# 	self._category = 8
		# 	self._hand_name = "Four of a Kind"
		# elif self._has_fullhouse() :
		# 	self._category = 7
		# 	self._hand_name = "Full house"
		# elif self._has_flush() :
		# 	self._category = 6
		# 	self._hand_name = "Flush"
		#	i = len(self._flush_cards)
		#	self._five_cards = [card for card in self._flush_cards[i-5:i]]
		# elif self._has_straight(self._all_cards) :
		# 	self._category = 5
		# 	self._hand_name = "Straight"
		# elif self._has_three() :
		# 	self._category = 4
		# 	self._hand_name = "Three of a Kind"
		# elif self._has_two_pairs() :
		# 	self._category = 3
		# 	self._hand_name = "Two Pairs"
		# elif self._has_pair() :
		# 	self._category = 2
		# 	self._hand_name = "One Pair"
		# elif self._has_high_card() :
		# 	self._category = 1
		# 	self._hand_name = "High Card"

		
	def showPlayerCards(self):
		print "Player %s has these cards %s" %(self.name, self._all_cards)

	def _has_straight_flush(self):
		if self._has_flush():
			if self._check_straight_flush(self._flush_cards):

				return True
	def _check_straight_flush(self, flush_cards):
		self._five_cards = self._get_straight_cards(flush_cards)
		if len(self._five_cards) != 0 :
			return True
		else:
			return False

	def _has_four(self, all_Cards):
		set_of_cards = list(set(self._rank_list))
		if len(set_of_cards) > 4 :
			return False
		else:
			for rank in set_of_cards:
				rank_count = self._rank_list.count(rank)
				if rank_count == 4:
					self._five_cards = [card for card in all_Cards if card[0] == rank]
					set_of_cards.remove(rank)
					kicker_rank = max(set_of_cards)
					kicker_index = self._rank_list(kicker_rank)
					kicker_suit = self._suit_list[kicker_index]
					kicker_card = kicker_rank + kicker_suit

					self._five_cards.insert(0, kicker_card)
					return True
		return False
	
	def _has_fullhouse(self) :
		return True
	
	def _has_flush(self) :
		for suit in SUIT_LOOKUP:
			suit_count = self._suit_list.count(suit)
			if suit_count >= 5 :
				self._flush_cards = [card for card in self._all_cards if card[1]== suit]
				print "self._flush_cards = " , self._flush_cards
				return True
		return False
	

	def _has_straight(self, all_cards) :
		diff_rank_cards = self._get_different_rank_list(all_cards)
		self._five_cards = self._get_straight_cards(diff_rank_cards)
		if len(self._five_cards) != 0 :
			return True
		else:
			return False

	def _get_different_rank_list(self, all_cards):
		different_rank_list = []
		different_rank_list.append(all_cards[0])
		for card in all_cards:
		    if(card[0] != different_rank_list[-1][0]):
        	     different_rank_list.append(card)

		return different_rank_list

	def _get_straight_cards(self, Cards):
		highest_card = Cards[-1]
		if highest_card[0] == 'A':
			Cards.insert(0,highest_card)

		i = len(Cards)
		while ( i - 5 >= 0):
			hand_to_check = ''.join(card[0] for card in Cards[i-5:i])
			is_straight = RANK_LOOKUP.find(hand_to_check)
			if is_straight > 0 :
				five_cards = [card for card in Cards[i-5:i]]
				return five_cards
			i -= 1
		return []
	
	def _get_rank_category(self, all_cards):
		"""  This will check if hand has Four, Three, Two cards with same rank  """
		card_group = []
		card_group_element = []
		current_rank = 0
		count = 0
		
		for card in all_cards :
			rank = RANK_LOOKUP.index(card[0])

			if rank == current_rank:
				count += 1
				card_group_element.append(card)
			elif rank != current_rank:
				card_group_element.insert(0,count)
				card_group.append(card_group_element)

				# reset counting
				count = 1
				card_group_element = []
				card_group_element.append(card)
				current_rank = rank
		card_group_element.insert(0,count)
		card_group.append(card_group_element)
		return card_group

	def _sort_cards_by_rank(self, all_cards):

		card_group = []
		card_group_element = []
		product = 1
		prime_lookup = {0:1, 1:1, 2:2, 3:3, 4:5}
		count = 0
		current_rank = 0
		product_lookup = {	1 : 'High_Card',
           					2 : 'One_Pair',
           					3 : 'Three_of_a_Kind',
           					4 : 'Two_Pairs',
           					5 : 'Four_of_a_Kind',
           					6 : 'Fullhouse',
           					8 : 'Two_Pairs',
           					9 : 'Fullhouse',
           					10: 'Four_of_a_Kind',
           					12: 'Fullhouse',
           					15: 'Four_of_a_Kind',
							}

		for card in all_cards:
			rank = RANK_LOOKUP.index(card[0])
			if rank == current_rank :
				count += 1
				card_group_element.append(card)
			elif rank != current_rank:
				product *= prime_lookup[count]
				# Explanation :
				# if count == 2, then product *= 2
				# if count == 3, then product *= 3
				# if count == 4, then product *= 5
				# if there is a Quad, then product = 5 ( 4, 1, 1, 1) or product = 10 ( 4, 2, 1) or product= 15 (4,3)
				# if there is a Fullhouse, then product = 12 ( 3, 2, 2) or product = 9 (3, 3, 1) or product = 6 ( 3, 2, 1, 1)
				# if there is a Trip, then product = 3 ( 3, 1, 1, 1, 1)
				# if there is TwoPair, then product = 4 ( 2, 1, 2, 1, 1) or product = 8 ( 2, 2, 2, 1)
				# if there is a Pair, then product = 2 (2, 1, 1, 1, 1, 1)
				# if there is HighCard, then product = 1 (1, 1, 1, 1, 1, 1, 1)
				card_group_element.insert(0,count)
				card_group.append(card_group_element)
				# reset counting
				count = 1
				card_group_element = []
				card_group_element.append(card)
				current_rank = rank
		card_group_element.insert(0,count)
		card_group.append(card_group_element)
		print "card_group = " , card_group


		self._hand_name = product_lookup[product]
		print "hand_name = " , self._hand_name




	def _has_three(self) :
		return True
	

	def _has_two_pairs(self) :
		return True
	

	def _has_pair(self) :
		return True
	

	def _has_high_card(self) :
		return True
    


