from utils import count, mean, std, min_val, max_val, percentile
import sys

# dataset_train.csv 
def main():
	if len(sys.argv) != 2:
		print("Usage: python describe.py dataset.csv")
		return
	
	filename = sys.argv[1] # Récupére le nom du fichier CSV
	with open(filename, "r") as f:
		reader = csv.DictReader(f)
		data = list(reader)
	# 2. Calculer les statistiques pour chaque colonne numérique (count, Mean etc...)  
	# 3. Affichier les résultats.

if __name__ == "__main__":
	main()