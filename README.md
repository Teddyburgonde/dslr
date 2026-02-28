# DSLR - Data Science × Logistic Regression

## Description

Ce projet consiste à recréer le **Choixpeau magique** de Poudlard à l'aide d'un modèle de régression logistique. À partir des notes des élèves dans différentes matières, le modèle prédit dans quelle maison (Gryffindor, Hufflepuff, Ravenclaw, Slytherin) chaque élève doit être placé.

---

## Structure du projet

```
.
├── describe.py          # Affiche les statistiques des données (count, mean, std, min, max, percentiles)
├── histogram.py         # Histogrammes des notes par maison
├── scatter_plot.py      # Nuage de points comparant deux matières
├── pair_plot.py         # Matrice de graphiques entre toutes les matières
├── logreg_train.py      # Entraîne le modèle et sauvegarde les poids
├── logreg_predict.py    # Prédit les maisons et génère houses.csv
├── math_utils.py        # Fonctions mathématiques (mean, std, percentile, etc.)
├── weight.csv           # Poids générés après l'entraînement
├── bias.csv             # Bias générés après l'entraînement
└── houses.csv           # Prédictions générées par logreg_predict.py
```

---

## Utilisation

### 1. Analyser les données
```bash
python3 describe.py dataset_train.csv
```

### 2. Visualiser les données
```bash
python3 histogram.py dataset_train.csv
python3 scatter_plot.py dataset_train.csv
python3 pair_plot.py dataset_train.csv
```

### 3. Entraîner le modèle
```bash
python3 logreg_train.py dataset_train.csv
```
Génère `weight.csv` et `bias.csv`.

### 4. Prédire les maisons
```bash
python3 logreg_predict.py dataset_test.csv weight.csv
```
Génère `houses.csv`.

---

## Algorithme

Le modèle utilise une **régression logistique one-vs-all** :
- Un classifieur binaire par maison
- La fonction sigmoid transforme un score en probabilité
- La descente de gradient minimise l'erreur à chaque itération
- Les notes sont normalisées en **z-score** avant l'entraînement

---

## Dépendances

```bash
pip install numpy pandas matplotlib
```
