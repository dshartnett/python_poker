# David H
# 2015-04-22
# Toy project to help me learn python
# Various csv and poker test shit

import csv
import os

import poker_functions as p
import recursive_tests as r
#import numpy as np

#class Card

# def recurse_test(n):
	# if n == 1: return 1
	# else: return n*recurse_test(n-1)
	
counter = 0

training_hands = []
test_hands = []

counter = 0
with open('.\\..\\data\\train.csv') as train_csvfile:
	test_reader = csv.reader(train_csvfile, delimiter=',')
	for row in test_reader:
		if row[0].isnumeric():# and int(row[10]) == 9:
		
			counter += 1
			hand = []
			for i in range(0,10,2): hand.append({'rank':int(row[i+1]), 'suit':int(row[i])})
			
			to_append = {'hand':hand, 'rank':row[10]}
			training_hands.append(to_append)
			
			if int(row[10]) != p.calc_value(hand): print(str(counter) + ": " + row[10] + " " + p.show_hand(hand))
		else:
			print(row)

counter = 0
with open('.\\..\\data\\test.csv') as test_csvfile:
	test_reader = csv.reader(test_csvfile, delimiter=',')
	for row in test_reader:
		if row[0].isnumeric():# and int(row[10]) == 9:
		
			counter += 1
			hand = []
			for i in range(1,11,2): hand.append({'rank':int(row[i+1]), 'suit':int(row[i])})
			
			to_append = {'hand':hand, 'rank':p.calc_value(hand)}
			test_hands.append(to_append)
		else:
			print(row)

			
#for row in training_hands: print(p.show_hand(row['hand']) + "-> " + row['rank'])

for row in test_hands:
	if row['rank'] == 7:
		print(p.show_hand(row['hand']) + "-> " + str(row['rank']))

#print(show_hand([{'rank':3, 'suit':2},{'rank':4, 'suit':1}]))


# for s in range(1,5,1):
	# for r in range(1,14,1): print(cards[(s-1)*13 + r-1] + " ", end="")
	# print("")

#print(len(cards))
#print(__name__)
