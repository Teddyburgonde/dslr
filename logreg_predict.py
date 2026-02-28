from logreg_train import sigmoid, create_zscore, fill_nan
from math_utils import count
import sys
import pandas as pd
import numpy as np


def predict(Weight: pd.DataFrame, df: pd.DataFrame) -> pd.DataFrame:
	"""
	Predicts the Hogwarts house for each student using trained weights and biases.
	Saves the predictions to houses.csv and returns them as a DataFrame.
	"""
	houses_list = ['Gryffindor', 'Ravenclaw', 'Hufflepuff', 'Slytherin']
	zscores = create_zscore(df)
	zscore_without_house = zscores.drop(columns='Hogwarts House').values
	Bias = pd.read_csv("bias.csv", index_col=0).values
	predictions = sigmoid(np.dot(zscore_without_house, Weight) + Bias.T)

	# Returns the index of the highest probability for each student (= predicted house)
	predicted_indices = np.argmax(predictions, axis=1)

	result_list = [houses_list[idx] for idx in predicted_indices]
	result = pd.DataFrame(result_list, columns=['Hogwarts House'])
	result.index.name = "Index"
	result.to_csv("houses.csv")
	return pd.DataFrame(result)

def cmp_result(prediction: pd.DataFrame, df: pd.DataFrame):
	"""
    Compares predictions to the actual houses and prints the accuracy percentage.
    """
	count_total = count(df)
	count_good = (prediction['Hogwarts House'] == df['Hogwarts House']).sum()
	percentil = (count_good * 100) / count_total
	print(f"Result: {percentil}%")


def main():
	try:
		if len(sys.argv) != 2:
			raise AssertionError("Usage: python3 logreg_predict.py dataset_train.csv")
		filename = sys.argv[1]
		if filename != "dataset_train.csv":
			raise AssertionError("Error: argv[1] should be named 'dataset_train.csv'") #! faire pareil sur tout les fichier
		buf = pd.read_csv(filename)
		exclude = ["Index", "First Name", "Last Name", "Birthday", "Best Hand"]
		df = buf.drop(columns=exclude)
		fill_nan(df)
		weight = pd.read_csv("weight.csv", index_col=0)
		prediction = predict(weight, df)
		cmp_result(prediction, buf)

	except FileNotFoundError:
		print(f"Error: The file '{filename}' cannot be found.")
		return
	except Exception as error:
		print(f"{type(error)} : {error}")

if __name__ == "__main__":
    main()