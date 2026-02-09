import numpy as np

# Un contre tous (One-vs-All) 
# "Est-ce que cet élève va chez Gryffondor ?"

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


def predict_prob(X: np.ndarray, weights: np.ndarray) -> np.ndarray:
	"""Calcule la probabilité finale de savoir dans quel maison l'éleve va partir"""
	z = np.dot(X, weights)
	return sigmoid(z)


def loss_function(X, y, weights):
	"""
	Calcule l'erreur globale (Log Loss) du modèle.

	Args:
		X: Matrice des caractéristiques (notes des élèves).
		y: Vecteur des étiquettes réelles (0 ou 1).
		weights: Vecteur des poids actuels de l'expert.

	Returns:
		La valeur scalaire de la perte (plus elle est basse, meilleur est le modèle).
	"""
	z = np.dot(X, weights)
	prediction = sigmoid(z)
	loss = -np.mean( y * np.log(prediction) + (1 - y) * np.log(1 - prediction))
	return loss

# 1. Charger les données : Lire ton fichier CSV pour obtenir les notes des élèves (X) et leurs maisons respectives (y).

# 2. Identifier les maisons : Lister les noms uniques des 4 maisons présentes dans tes données (Gryffondor, Serpentard, etc.).

# 3. Préparer le stockage : Créer une structure (comme un dictionnaire) pour sauvegarder les poids finaux de chaque maison.

# 4. Boucler sur chaque maison : Pour chaque maison de la liste :

#     - Créer une cible binaire : Transformer le vecteur des maisons en 0 et 1 (1 si c'est la maison actuelle, 0 pour toutes les autres).
#     - Lancer l'entraînement (fit) : Utiliser tes données et cette cible binaire pour obtenir les poids spécifiques à cette maison.
#     - Sauvegarder les poids : Stocker ces poids associés au nom de la maison.

# 5. Exporter les résultats : Enregistrer tous les poids (les 4 vecteurs) dans un fichier (souvent un .csv ou un .json) pour que ton programme de prédiction puisse les réutiliser plus tard.




def main():

	if len(sys.argv) != 2:
		print("Usage: python describe.py dataset.csv")
		return
	
	filename = sys.argv[1]
	all_stats = {}

	result = []
	for y in house
		weights = fit(X, y)
