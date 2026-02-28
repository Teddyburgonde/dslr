# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    math_utils.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tebandam <tebandam@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/28 12:33:37 by tebandam          #+#    #+#              #
#    Updated: 2026/02/28 17:49:37 by tebandam         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


def	count(value: list):
	"""
	Returns the number of elements in a list as a float.
	"""
	result = float(len(value))
	return result

def	mean(value: list):
	"""
	Returns the mean of a list.
	"""
	sum = 0
	size = count(value)
	for x in value:
		sum = sum + x
	mean = sum / size
	return mean

def	std(value: list):
	"""
	Computes the population standard deviation.
	std = square root of the mean of squared deviations.
	"""
	size = count(value)
	mean_value = mean(value)
	sum_of_squares = 0
	for x in value:
		sum_of_squares += (x - mean_value) ** 2
	result = (sum_of_squares / size) ** 0.5
	return result


def min_val(values: list):
	"""Returns the minimum value of a list."""
	values.sort()
	result = values[0]
	return result


def max_val(values: list):
	"""Returns the maximum value of a list."""
	values.sort()
	result = values[-1]
	return result


def percentile(values: list, percent: int):
	"""
	Returns the p percentile (p between 0 and 100).
	A percentile tells you: 'X% of values are below this value.'
	The weight variable measures the distance between two indexes.
	Linear interpolation: estimates a value between two points proportionally.
	"""
	values.sort()
	index = (percent / 100) * (len(values) -1)
	floor_index = int(index)
	if (index == floor_index):
		result = values[floor_index]
	else:
		weight = index - floor_index
		result = values[floor_index] + weight * (values[floor_index + 1] - values[floor_index])
	return result

