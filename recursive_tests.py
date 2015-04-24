import poker_functions as p

cards = [None]*52

for s in range(1,5,1):
	for r in range(1,14,1):
		#print(show_card(r, s) + " : " + str((s-1)*13 + r))
		cards[(s-1)*13 + r-1] = p.show_card(r, s)
		#print(cards[(s-1)*13 + r-1] + " : " + str((s-1)*13 + r-1))

#counter = 0

def choose_n(number_to_choose):
	choose_n.counter  = 0
	def cn(arr, n):
		#global counter
		
		if n == 0:
			choose_n.counter += 1
			#if counter % 100000 == 0: print(counter)
			#if counter % 100000 == 0:
			print(str(choose_n.counter) + ": ", end="")
			for card in arr:
				print(cards[card] + " ", end="")
			print("")
			return
		
		for i in range(0,52,1):
			if i not in arr:
				#print(i)
				arr.append(i)
				cn(arr, n - 1)
				arr.pop()
		return
	cn([], number_to_choose)

def choose_n_vis(number_to_choose):

	choose_n_vis.counter = 0
	def cnv(arr, n):
		if n == 0:
			choose_n_vis.counter += 1
			if choose_n_vis.counter % 1 == 0:
				#os.system('cls')
				print(str(choose_n_vis.counter) + ":")
				for s in range(1,5,1):
					for r in range(1,14,1):
						if ( (s-1)*13 + r-1 ) in arr: print(cards[(s-1)*13 + r-1] + " ", end="")
						else: print("   ",end="")
					print("")
				print("")
			return
		
		for i in range(0,52,1):
			if i not in arr:
				#print(i)
				arr.append(i)
				cnv(arr, n - 1)
				arr.pop()
		return
	cnv([], number_to_choose)