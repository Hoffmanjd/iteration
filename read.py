#!/usr/bin/env python
import sys

data = open("cars.csv", 'r')
lines = data.readlines()

# animal_names = []
# animal_ratings = []
# animal_countries = []
# for i in range(1, len(lines)):
# 	info = lines[i].rstrip().split(",") # [Bird, 2, Poland]
# 	animal_names.append(info[0])
# 	animal_ratings.append(info[1])
# 	animal_countries.append(info[2])

# for i in range(0, len(animal_names)):
# 	print animal_names[i], "is rated", animal_ratings[i], "and is like in", animal_countries[i]

userid = []
make = []
model = []
year = []
color = []
for i in range(1, len(lines)):
	info = lines[i].rstrip().split(",")
	userid.append(info[0])
	make.append(info[1])
	model.append(info[2])
	year.append(info[3])
	color.append(info[4])

def cars_from_year(make, model, years, target_string):
	output = []
	for row in range(0, len(years)):
		if years[row] == target_string:
			car_data = make[row] + ' ' + model[row]
			output.append(car_data)

	return output

# print cars_from_year(make, model, year, "2006")

def make_since_year(make, years, target_make, after_year):
	count = 0
	for row in range(0, len(years)):
		if make[row] == target_make:
			if int(years[row]) > after_year:
				count += 1
	return count

# print make_since_year(make, year, "Toyota", 2000)

def most_popular_color():
	color_list = []
	color_count = []
	for row in range(0, len(year)):
		if not list_contains(color_list, color[row]):
			color_list.append(color[row])
			color_count.append(1)
		else:
			for i in range(0, len(color_list)):
				if color_list[i] == color[row]:
					color_count[i] += 1
	largest_color_count = 0
	position = 0
	for row in range(0, len(color_list)):
		current_color = color_count[row]
		if current_color > largest_color_count:
			largest_color_count = current_color
			position = row
	output = color_list[position]
	return output

def list_contains(values, target):
	for i in range(0, len(values)):
		if values[i] == target:
			return True
	return False

print most_popular_color()