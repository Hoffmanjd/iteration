# iteration pattern
# doing the same thing once for each member of a list

# [1, 5, 7 ,8 , 4, 3]

def print_list(list):
	# standard for loop with range
	# for i in range(0, len(list)):
	# 	print list[i]

	# for each loop
	for item in list:
		print item

def add_one(list):
	# standard for loop with range
	for i in range(0, len(list)):
		list[i] += 1

	return list

def print_scores(names, scores):
	for i in range(0, len(names)):
		print names[i] , " scored " , scores[i]


# filter pattern
# exclude a calculation from list memberes

def congratulations(names, scores):
	for i in range(0, len(names)):
		if (scores[i] == 100):
			print "Congrats", names[i], "! You got a perfect score!"


# accumulation pattern - a type of iteration
# keep track of other data as we go

def sum(numbers):
	total = 0
	for n in numbers:
		total += n

	return total

def max(numbers):
	current_max = numbers[0]
	for n in numbers:
		if n > current_max:
			current_max = n

	return current_max

# homework ->
	# a) write a function that finds the average of the scores
	# b) write a second function that also finds the average,
	#	 but drops the lowest 2 scores