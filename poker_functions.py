# David H
# Poker based functions

ranks = {1:'A',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'T',11:'J', 12:'Q', 13:'K'}
suits = {1:'\u0003',2:'\u0006',3:'\u0004',4:'\u0005'}
#suits = {1:'H',2:'S',3:'D',4:'C'}
#suits = {1:'♥',2:'♠',3:'♦',4:'♣'}

def show_card(rank, suit):
	return ranks[rank] + suits[suit]

def show_hand(hand):
	hand_string = ""
	for card in hand:
		hand_string += show_card(card['rank'], card['suit']) + " "
	return hand_string
	
# can a machine learn to write code as bad as this?
#def calc_value(hand):
def calc_value(hand_to_eval):
	value = 0
	one_pair = False
	two_pairs = False
	three_of_a_kind = False
	straight = False
	flush = False
	full_house = False
	four_of_a_kind = False
	
	hand = sorted(hand_to_eval, key = lambda item: item['rank'])
	#hand.sort(key = lambda item: item['rank'])
	
	ranks = []
	for card in hand: ranks.append(card['rank'])
	
	rank_counter = 0
	for r in ranks: rank_counter += ranks.count(r)
	
	if rank_counter == 7: one_pair = True
	if rank_counter == 9: two_pairs = True
	if rank_counter == 11: three_of_a_kind = True
	if rank_counter == 13: full_house = True
	if rank_counter == 17: four_of_a_kind = True
	
	if hand[1]['rank']-1 == hand[2]['rank']-2 == hand[3]['rank']-3 == hand[4]['rank']-4:
		if hand[4]['rank'] - 4 == hand[0]['rank']: straight = True
		if hand[0]['rank'] == 1 and hand[1]['rank'] == 10: straight = True
	if hand[0]['suit'] == hand[1]['suit'] == hand[2]['suit'] == hand[3]['suit'] == hand[4]['suit']: flush = True
	
	if one_pair: value = 1
	if two_pairs: value = 2
	if three_of_a_kind: value = 3
	if straight: value = 4
	if flush: value = 5
	if full_house: value = 6
	if four_of_a_kind: value = 7
	if flush and straight: value = 8
	if flush and straight and hand[0]['rank'] == 1 and hand[4]['rank'] == 13: value = 9
	return value
