import sys

def main():
	if len(sys.argv) != 2:
		print("Usage: python describe.py dataset.csv")
		return
	
	filename = sys.argv[1] # Récupére le nom du fichier CSV

	# 1.Lire le CSV.
	# 2. Calculer les statistiques pour chaque colonne numérique (count, Mean etc...)  
	# 3. Affichier les résultats.

if __name__ == "__main__":
	main()