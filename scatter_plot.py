import matplotlib.pyplot as plt

def plot_scatter_comparison(data, feature_x, feature_y):
	"""
	Affiche un nuage de points comparant deux matières.
	Chaque point est coloré selon la maison de l'élève.

	Args:
		data (list): Liste de dictionnaires (les élèves).
		feature_x (str): Nom de la première matière (ex: 'Astronomy').
		feature_y (str): Nom de la deuxième matière (ex: 'Defense Against the Dark Arts').
	"""
	houses = {
		"Gryffindor": "red",
		"Hufflepuff": "yellow",
		"Ravenclaw": "blue",
		"Slytherin": "green"
	}
	plt.figure(figsize=(10, 8))

	for house_name, color in houses.items():
		note_x = []
		note_y = []
		for student in data:
			if student['Hogwarts House'] == house_name:
				value_x = student[feature_x]
				value_y = student[feature_y]
				if value_x != "" and value_y != "":
					note_x.append(float(value_x))
					note_y.append(float(value_y))
		plt.scatter(note_x, note_y, c=color, label=house_name, alpha=0.5)
	plt.xlabel(feature_x)
	plt.ylabel(feature_y)
	plt.legend()
	plt.show()
