import matplotlib.pyplot as plt
import pandas as pd
from math_utils import std, mean

def histogram(df: pd.DataFrame):

	houses_list = {
		"Gryffindor": "red",
		"Hufflepuff": "yellow",
		"Ravenclaw": "blue",
		"Slytherin": "green"
	}
	exclude = ["Index", "First Name", "Last Name", "Birthday", "Best Hand", "Hogwarts House"]
	fig, axs = plt.subplots(4, 4, figsize=(14, 10))
	axs_flat = axs.flatten()

	lessons = [c for c in df.columns if c not in exclude] # on cree une list contenant tout les nom de cours

	for i, course in enumerate(lessons):
		house_means = []
		for house_name, color in houses_list.items():
			scores = df[df['Hogwarts House'] == house_name][course].dropna()
			axs_flat[i].hist(scores, color = color, alpha=0.5, label=house_name)
			if not scores.empty:
				house_means.append(mean(scores))
		std_result = std(house_means)
		if i == 0:
			axs_flat[i].legend()
		axs_flat[i].set_title(f"{course}\n(std: {std_result:.4f})")

	for j in range(len(lessons), len(axs_flat)):
		axs_flat[j].axis('off')
	plt.tight_layout()
	plt.show()