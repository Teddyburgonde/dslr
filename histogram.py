import matplotlib.pyplot as plt
import numpy as np



# Pseudo code for plot_all_histograms

# 1. Définir la liste des maisons et une palette de couleurs associée
# (ex: Gryffindor: red, Hufflepuff: yellow, Ravenclaw: blue, Slytherin: green)

# 2. Créer une figure avec plt.subplots (ex: 4 lignes, 4 colonnes)
# Récupérer l'objet 'fig' et le tableau d'axes 'axs'

# 3. Aplatir le tableau d'axes avec .flatten() pour itérer facilement dessus

# 4. POUR chaque index et chaque nom_matiere dans la liste 'features' :
	
	# A. Sélectionner l'axe (le sous-graphique) correspondant à l'index actuel

	# B. POUR chaque maison dans la liste des maisons :

		# i. Filtrer les données : extraire les notes de 'nom_matiere' 
		# uniquement pour les élèves appartenant à cette 'maison'

		# ii. Nettoyage : Créer une liste 'notes_propres' en ignorant les 
		# valeurs vides ("") et en convertissant le reste en float

		# iii. Tracer l'histogramme sur l'axe sélectionné :
		# Passer 'notes_propres', définir le nombre de bins (ex: 20),
		# l'opacité (alpha=0.5) et le label du nom de la maison

	# C. Configurer l'axe actuel :
	# Ajouter le titre (nom_matiere) et afficher la légende

# 5. POUR les axes restants dans la grille (ceux qui n'ont pas de matière) :
	# Désactiver l'affichage de l'axe (axis off) pour ne pas avoir de carrés vides

# 6. Ajuster l'espacement entre les graphiques avec plt.tight_layout()

# 7. Afficher la fenêtre finale avec plt.show()


def plot_all_histograms(data, features):
	"""
	Affiche une grille d'histogrammes pour comparer les distributions 
	des notes entre les 4 maisons de Poudlard.

	Args:
		data (list): Liste de dictionnaires (chaque dict est une ligne du CSV).
		features (list): Liste des noms des colonnes numériques (les cours).
	"""
