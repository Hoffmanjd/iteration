#!/usr/bin/env python
import sys
import plotly
import plotly.graph_objs as go

data = open("jobs.csv", 'r')
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

user_id = []
income = []
age = []
department = []
college_years = []
for i in range(1, len(lines)):
	info = lines[i].rstrip().split(",")
	user_id.append(info[0])
	income.append(info[1])
	age.append(info[2])
	department.append(info[3])
	college_years.append(info[4])

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

# print most_popular_color()

def popular_color(color):
	color_dict = {}
	for current_color in color:
		color_exist = color_dict.get(current_color, None)
		if not color_exist:
			color_dict[current_color] = 1
		else:
			color_dict[current_color] += 1
	largest_color = ""
	largest_color_count = 0
	for current_color, color_count in color_dict.items():
		if color_count > largest_color_count:
			largest_color = current_color
			largest_color_count = color_count
	return largest_color

# print popular_color(color)

def colors_graph():
	color_list = []
	color_count = []
	markers = []
	for row in range(0, len(year)):
		if not list_contains(color_list, color[row]):
			color_list.append(color[row])
			color_count.append(1)
		else:
			for i in range(0, len(color_list)):
				if color_list[i] == color[row]:
					color_count[i] += 1

	data = [go.Bar(
			x = color_list,
			y = color_count,
			marker = dict(
				color = ['rgba(0,128,128,0.8)', 'rgba(255,192,203,0.8)',
				'rgba(255,0,0,0.8)', 'rgba(64,224,208,0.8)', 
				'rgba(112,32,32,0.8)', 'rgba(255,165,0,0.8)', 
				'rgba(128,0,0,0.8)', 'rgba(75,0,130,0.8)', 
				'rgba(238,130,238,0.8)', 'rgba(0,128,0,0.8)', 
				'rgba(255,105,180,0.8)', 'rgba(218,165,32,0.8)', 
				'rgba(127,255,212,0.8)', 'rgba(255,255,0,0.8)', 
				'rgba(240,230,140,0.8)', 'rgba(145,95,109,0.8)', 
				'rgba(0,0,255,0.8)', 'rgba(220,20,60,0.8)', 
				'rgba(128,0,128,0.8)']),
		)]

	plotly.offline.plot(data, filename = 'basic-bar')

#colors_graph()

def years_graph():
	year_list = []
	car_count = []
	for row in range(0, len(year)):
		if not list_contains(year_list, year[row]):
			year_list.append(year[row])
			car_count.append(1)
		else:
			for i in range(0, len(year_list)):
				if year_list[i] == year[row]:
					car_count[i] += 1
	data = [go.Bar(
			x = year_list,
			y = car_count
		)]

	plotly.offline.plot(data, filename = 'basic-bar')

# years_graph()

def position_in_list(values, target):
	for i in values:
		if values[i] == target:
			return i

def scatter_plot(xvar, year):
	data = [go.Scatter(
		x = xvar,
		y = year,
		mode = 'markers'
		)]
	plotly.offline.plot(data, filename='basic-scatter')

# scatter_plot(age, income)

def pie_chart(inputs):
	input_list = []
	values = []
	for value in inputs:
		if not list_contains(input_list, value):
			input_list.append(value)
			values.append(1)
		else:
			for i in range(0, len(input_list)):
				if input_list[i] == value:
					values[i] += 1
	data = [go.Pie(labels=input_list, values=values)]

	plotly.offline.plot(data, filename='pie-chart')

# pie_chart(department)

def line_graph(xvar, year):
	data = [go.Scatter(
		x = xvar,
		y = year
		)]
	plotly.offline.plot(data, filename='basic-line')

line_graph(user_id, income)