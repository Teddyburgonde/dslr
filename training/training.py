import sys

"""
- nan -> C'est une valeur vide dans le tableau.
- La fonction count est important car elle permet de calculer toutes les autres statistiques.
"""
def count(arr):
	"""Compte le nombre de valeurs non-NaN"""
	counter = 0
	for x in arr:
		# NaN est la seule valeur qui n'est pas égale à elle-même
		if x == x:
			counter+=1
	return counter

"""
μ = Σx / n
moyenne = Somme des valeurs / nombre total
"""
def mean(arr):
	"""Calcule la moyenne en ignorant les NaN"""
	somme = 0
	counter = count(arr)

	for x in arr:
		if x == x:
			somme += x
	if counter == 0: # Evite les divisions par 0
		return float('nan')
	
	moyenne = somme / counter
	return moyenne

# def std(arr):
# 	"""Calcule l'écart-type (population)"""





def main():
    print(count([1, 2, 'nan' ,4]))

if __name__=="__main__":
    main()