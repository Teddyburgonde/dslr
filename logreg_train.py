# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    logreg_train.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tebandam <tebandam@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/28 17:41:07 by tebandam          #+#    #+#              #
#    Updated: 2026/02/28 17:53:59 by tebandam         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


from math_utils import mean, std
import numpy as np
import sys
import pandas as pd

def sigmoid(z: np.ndarray) -> np.ndarray:
	"""
	Converts a raw score (z) into a probability between 0 and 1.
	If z is high, the result will be close to 1 (True).
	If z is low, the result will be close to 0 (False).
	"""
	return 1 / (1 + np.exp(-z))


def fill_nan(df: pd.DataFrame):
	"""Replaces missing values (NaN) in each column with the column mean."""
	for col in df:
		if col == "Hogwarts House":
			continue
		mean_value = mean(df[col].dropna().to_list())
		df[col] = df[col].fillna(mean_value)


def create_zscore(df: pd.DataFrame) -> pd.DataFrame:
	"""
	Normalizes the grades of the 4 selected courses using z-score.
	Each grade becomes: (grade - mean) / std
	This allows comparison between courses with different scales.
	"""
	data = df[['Hogwarts House', 'Astronomy', 'Herbology', 'Defense Against the Dark Arts', 'Ancient Runes']].copy()
	for col in data.columns:
		if col == 'Hogwarts House':
			continue
		# Compute the z-score for each grade in the current column
		data[col] = (data[col] - mean(data[col].tolist())) / std(data[col].tolist())
	return data

def create_ytrue(zscores: pd.DataFrame) -> np.array:
	"""
	Converts the 'Hogwarts House' column into a one-hot encoding matrix.
	Each student becomes a row of 4 values: [1,0,0,0] for Gryffindor, etc.
	Returns a matrix of shape (nb_students, 4).
	"""
	houses = ['Gryffindor', 'Ravenclaw', 'Hufflepuff', 'Slytherin']
	result = np.zeros((len(zscores), 4))
	for i, house in enumerate(zscores["Hogwarts House"]):
		result[i][houses.index(house)] = 1
	return result


def train(zscores: pd.DataFrame) -> np.array:
	"""
	Trains the logistic regression model using gradient descent.
	At each epoch, computes predictions, error, and updates weights and biases.
	Returns the final weights and biases after 1000 iterations.
	"""
	nb_lessons = len(zscores.columns) - 1 # -1 to exclude 'Hogwarts House'
	nb_house = 4
	learning_rate = 0.01
	y_true = create_ytrue(zscores)
	weight = np.zeros((nb_lessons, nb_house))
	bias = np.zeros((nb_house, 1)) # Base value to improve prediction accuracy.
	zscores_without_house = zscores.drop(columns=["Hogwarts House"]).values
	for epoch in range(1000):
		# For each student, compute the probability of belonging to each house
		predictions = sigmoid(np.dot(zscores_without_house, weight) + bias.T)
		error = predictions - y_true
		# Update weights based on the error (gradient descent)
		weight -= learning_rate * np.dot(zscores_without_house.T, error)
		# Update bias by summing the errors across all students
		bias -= learning_rate * error.sum(axis=0, keepdims=True).T
	return weight, bias


def save_weights(weight: np.array, bias: np.array,  zscores: pd.DataFrame):
	"""
	Saves the weights and biases into two CSV files.
	- weight.csv: one row per course, one column per house
	- bias.csv: one base value per house
	"""
	houses = ['Gryffindor', 'Ravenclaw', 'Hufflepuff', 'Slytherin']
	df_weight = pd.DataFrame(weight)
	df_weight.index = zscores.columns.drop("Hogwarts House")
	df_weight.columns = houses
	df_weight.to_csv('weight.csv')
	df_bias = pd.DataFrame(bias)
	df_bias.to_csv("bias.csv")


def main():
	if len(sys.argv) != 2:
		print("Usage: python3 logreg_train.py dataset_train.csv")
		return
	try:
		filename = sys.argv[1]
		buf = pd.read_csv(filename)
		exclude = ["Index", "First Name", "Last Name", "Birthday", "Best Hand"]
		df = buf.drop(columns=exclude)
		fill_nan(df)
		zscores = create_zscore(df)
		Weight, Bias = train(zscores)
		save_weights(Weight, Bias, zscores)

	except FileNotFoundError:
		print(f"Error: The file '{filename}' cannot be found.")
		return
	except Exception as error:
		print(f"{type(error)} : {error}")

if __name__ == "__main__":
	main()