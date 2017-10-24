# iteration pattern
# doing the same thing once for each member of a list

# [1, 5, 7 ,8 , 4, 3]

def iterate(list):
	# standard for loop with range
	# for i in range(0, len(list)):
	# 	print list[i]

	# for each loop
	for item in list:
		print item

def add_one(list):
	# standard for loop with range
	for i in rnage(0, len(list)):
		list[i] += 1

	return list

def print_scores(names, scores):
	for i in range(0, len(names)):
		print names[i] , " scored " , scores[i]


# filter pattern
def congratulations(names, scores):
	for i in range(0, len(names)):
		if (scores[i] == 100):
			print "Congrats", names[i], "! You got a perfect score!"
