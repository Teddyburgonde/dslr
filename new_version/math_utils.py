# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    math_utils.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tebandam <tebandam@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/28 12:33:37 by tebandam          #+#    #+#              #
#    Updated: 2026/02/28 13:18:00 by tebandam         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	count(value: list):
	"""
	Retourne le nombre d'éléments d'une liste sous forme de float.
	"""
	result = float(len(value))
	return result

def	mean(value: list):
	"""
	Retourne la moyenne d'une liste.
	"""
	sum = 0
	size = count(value)
	for x in value:
		sum = sum + x
	mean = sum / size
	return mean

def	std(value: list):
	"""Calcule l'écart-type (population).
	écart-type = racine carrée de la moyenne des carrés des écarts"""
	mean_value = mean(value)
	sum_of_squares = 0
	for x in value:
		sum_of_squares += (x - mean_value) ** 2
	result = (sum_of_squares / mean_value) ** 0.5
	return result


def min_val(values: list):
	"""Retourne la valeur minimum d'une list"""
	values.sort()
	result = values[0]
	return result


def max_val(values: list):
	"""Retourne la valeur maximum d'une list"""
	values.sort()
	result = values[-1]
	return result


def percentile(values: list, percent: int):
	"""Retourne le percentile p (p entre 0 et 100)
	Un percentile te dit : "X% des valeurs sont en dessous de cette valeur
	La variable weight sert à savoir à quelle distance tu te trouves entre les deux cases.
	Interpolation linéaire : estime une valeur entre deux points 
	en suivant une ligne droite proportionnelle."""
	values.sort()
	index = (percent / 100) * (len(values) -1)
	floor_index = int(index)
	if (index == floor_index):
		result = values[floor_index]
	else:
		weight = index - floor_index
		result = values[floor_index] + weight * (values[floor_index + 1] - values[floor_index])
	return result

