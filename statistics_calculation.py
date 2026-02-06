def count(arr):
def mean(arr):
def std(arr):
def min_val(arr):
def max_val(arr):
def percentile(arr, p):


# utiliser sorted
# Créer clean_list (déjà fait).
# Créer une nouvelle variable sorted_list en appliquant sorted() sur clean_list.
# Remplacer clean_list par sorted_list dans tous les appels de ton dictionnaire stats_function.



def get_stats(data_list):
	"""
	Calcule toutes les statistiques nécessaires pour une colonne de données
	et les retourne sous forme de dictionnaire.
	"""
	clean_list = []
	for x in data_list:
		if x == x:
			clean_list.append(x)

	
	stats_function = {
		"count": count(clean_list),
		"mean": mean(clean_list),
		"std": std(clean_list),
		"min_val": min_val(clean_list),
		"max_val": max_val(clean_list),
		"25%": percentile(clean_list, 25),
		"50%": percentile(clean_list, 50),
		"75%": percentile(clean_list, 75)
		}