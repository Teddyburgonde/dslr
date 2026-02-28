# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    scatter_plot.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tebandam <tebandam@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/28 17:49:52 by tebandam          #+#    #+#              #
#    Updated: 2026/02/28 17:49:55 by tebandam         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import matplotlib.pyplot as plt
import pandas as pd

def scatter_plot(df: pd.DataFrame, feature_x: str, feature_y: str):
	"""
	Displays a scatter plot comparing two courses.
	Each point is colored according to the student's house.
	Args:
		df (pd.DataFrame): DataFrame containing the students data.
		feature_x (str): Name of the first course (e.g. 'Astronomy').
		feature_y (str): Name of the second course (e.g. 'Defense Against the Dark Arts').
	"""
	houses_list = {
		"Gryffindor": "red",
		"Hufflepuff": "yellow",
		"Ravenclaw": "blue",
		"Slytherin": "green"
	}
	plt.figure(figsize=(10, 8))

	for house_name, color in houses_list.items():
		house_note = df[df['Hogwarts House'] == house_name][[feature_x, feature_y]].dropna()
		plt.scatter(house_note[feature_x], house_note[feature_y], c =color, label=house_name, alpha=0.5)
	plt.xlabel(feature_x)
	plt.ylabel(feature_y)
	plt.title(f"Correlation between {feature_x} and {feature_y}")
	plt.legend()
	plt.show()
