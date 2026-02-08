import numpy as np

# Un contre tous (One-vs-All)

def sigmoid(z):
	"""
	Transforme un score brut (z) en une probabilité comprise entre 0 et 1.
	Si z est élevé, le résultat sera proche de 1 (Vrai).
	Si z est bas, le résultat sera proche de 0 (Faux).
	"""
	return 1 / (1 + np.exp(-z))


# X matrice , y vecteur
def fit(X, y):
	weight


def loss_function(X, y, weights):


def predict_prob(X, weights):

def main():