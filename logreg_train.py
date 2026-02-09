import numpy as np

# Un contre tous (One-vs-All)

def sigmoid(z: np.ndarray) -> np.ndarray:
	"""
	Transforme un score brut (z) en une probabilité comprise entre 0 et 1.
	Si z est élevé, le résultat sera proche de 1 (Vrai).
	Si z est bas, le résultat sera proche de 0 (Faux).
	"""
	return 1 / (1 + np.exp(-z))


def fit(X: np.ndarray, y: np.ndarray) -> np.ndarray:
	"""
	Apprend à reconnaître une maison en ajustant les coefficients.
	X : Les notes des élèves
	y : La bonne réponse (la maison)
	weights : L'importance accordée à chaque matière pour une maison.
	"""
	n_students, n_features = X.shape
	weights = np.zeros(n_features)

	# Entrainement 1000 fois sur la mêmes données
	epochs = 1000
	for i in range(epochs):
		z = np.dot(X, weights)
		# Transformation en probalité (0 à 1)
		prediction = sigmoid(z)
		# Error est la difference entre pédiction et le résultat réel y
		error = prediction - y

		# Le gradient indique la direction dans laquelle l'erreur augmente le plus vite. 
		# Comme nous, on veut que l'erreur diminue, on va dans le sens opposé
		gradient = np.dot(X.T, error) / n_students
		# On descend la pente de l'erreur, cela permet de donner un coefficient à chaque matière
		weights -= 0.1 * gradient
	return weights


def loss_function(X, y, weights):
	...

def predict_prob(X, weights):
	...

def main():
	...