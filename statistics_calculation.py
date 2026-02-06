from math_utils import count, mean, std, min_val, max_val, percentile

def get_stats(data_list):
	"""
	Calcule toutes les statistiques nécessaires pour une colonne de données
	et les retourne sous forme de dictionnaire.
	"""
	clean_list = []
	for x in data_list:
		if x == x:
			clean_list.append(x)
	sorted_list = sorted(clean_list)
	
	stats_function = {
		"count": count(sorted_list),
		"mean": mean(sorted_list),
		"std": std(sorted_list),
		"min_val": min_val(sorted_list),
		"max_val": max_val(sorted_list),
		"25%": percentile(sorted_list, 25),
		"50%": percentile(sorted_list, 50),
		"75%": percentile(sorted_list, 75)
		}
	result = stats_function
	return result