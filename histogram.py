import matplotlib.pyplot as plt
import numpy as np


# FONCTION plot_all_histograms(data):
    
#     # ÉTAPE 1 : Identifier les features numériques (les cours)
#     1.1 Créer une liste des colonnes à exclure 
#         (Index, First Name, Last Name, Birthday, Best Hand, Hogwarts House)
#     1.2 Récupérer toutes les colonnes du dataset
#     1.3 Filtrer pour garder seulement les colonnes numériques (les cours)
    
#     # ÉTAPE 2 : Créer une grille de graphiques
#     2.1 Créer une figure avec subplots (4 lignes × 4 colonnes)
#     2.2 Transformer la grille 2D en liste 1D pour faciliter l'accès
    
#     # ÉTAPE 3 : Pour chaque feature (cours)
#     POUR chaque feature dans la liste des features:
        
#         3.1 Sélectionner le subplot correspondant (axes[i])
        
#         # ÉTAPE 4 : Séparer les données par maison
#         POUR chaque maison dans [Gryffindor, Slytherin, Ravenclaw, Hufflepuff]:
            
#             4.1 Créer une liste vide pour stocker les valeurs de cette maison
            
#             4.2 POUR chaque ligne (élève) dans data:
#                 SI la maison de l'élève == maison actuelle:
#                     SI la valeur de la feature n'est pas vide:
#                         ESSAYER de convertir en float
#                         SI réussi: ajouter à la liste de valeurs
            
#             # ÉTAPE 5 : Afficher l'histogramme pour cette maison
#             5.1 Tracer l'histogramme (hist) avec:
#                 - values = les notes de cette maison
#                 - bins = 20 (nombre de barres)
#                 - alpha = 0.5 (transparence)
#                 - label = nom de la maison
#                 - color = couleur de la maison
        
#         # ÉTAPE 6 : Configurer le subplot
#         6.1 Définir le titre (nom du cours)
#         6.2 Afficher la légende (noms des maisons)
    
#     # ÉTAPE 7 : Masquer les subplots vides (s'il y en a)
#     POUR chaque subplot non utilisé:
#         Désactiver l'affichage
    
#     # ÉTAPE 8 : Afficher tous les graphiques
#     8.1 Ajuster l'espacement (tight_layout)
#     8.2 Afficher la fenêtre (show)

# FIN FONCTION


def plot_all_histograms(data):
	"""
	Affiche les histogrammes de toutes les features numériques
	en grille pour comparer les distributions entre les 4 maisons
	"""
