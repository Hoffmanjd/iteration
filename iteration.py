import math

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

def alternating_sum(numbers):
	total = numbers[0]
	for n in range(1, len(numbers)):
		if n % 2 == 0:
			total -= numbers[n]
		else:
			total += numbers[n]
	return total

def sum_outside(numbers, minimum, maximum):
	total = 0
	for n in range(0, len(numbers)):
		if n < minimum - 1:
			total += numbers[n]
		elif n >= maximum - 1:
			total += numbers[n]
	return total

def count_close_remainders(numbers, divisor):
	count = 0
	for n in range(0, len(numbers)):
		if numbers[n] % divisor == 1:
			count += 1
		elif numbers[n] % divisor == divisor - 1:
			count += 1
		elif numbers[n] % divisor == 0:
			count += 1
	return count

def average(scores):
	total = float(sum(scores))
	amount = float(len(scores))
	av = total / amount
	return av

def double_down(numbers, target):
	doubled_version = []
	previous_number = numbers[0]
	for n in range(0, len(numbers)):
		diff = numbers[n] - target
		if diff > -4 and diff < 4:
			doubled_version.append(numbers[n] * 2)
		elif numbers[n] < previous_number:
			doubled_version.append(numbers[n] * 2)
		else:
			doubled_version.append(numbers[n])
		previous_number = numbers[n]
	return doubled_version

def standard_deviation(numbers):
	av = average(numbers)
	total_diff = float(0)
	for n in range(0, len(numbers)):
		diff = float(numbers[n]) - av
		squared_diff = diff * diff
		total_diff += squared_diff
	variance = total_diff / len(numbers)
	deviation = math.sqrt(variance)
	return deviation

def mountain_count(numbers):
	count = 0
	for n in range(1, len(numbers) - 1):
		prev_num = numbers[n - 1]
		next_num = numbers[n + 1]
		if prev_num < numbers[n] and next_num < numbers[n]:
			count += 1
	return count