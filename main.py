#YOVO, KOSSI MARTINO, MASTER 2 DIT
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def load_data(data_path):
    """Charge les données brutes à partir d'un chemin donné."""
    data = pd.read_csv(data_path)
    return data


def clean_data(data):
    """Nettoie les données."""
    # Supprime les valeurs manquantes
    data.dropna(inplace=True)

    # Convertit les données catégorielles en variables numériques
    data = pd.get_dummies(data)

    return data


def reduce_data(data):
    """Réduit les données."""
    # Sélectionne les variables les plus importantes
    data = data[data.corr()["target"] > 0.2]

    # Sélectionne les données les plus représentatives
    data = data.sample(frac=0.1)

    return data


def feature_engineering(data):
    """Effectue du feature engineering."""
    # calculer le ratio valence-energy,
    data["valence_energy_ratio"] = data["valence"] / data["energy"]
    # calculer le ratio durée-dancabilité,
    data["duration_danceability_ratio"] = data["duration"] / data["danceability"]

    return data


def display_statistics(data):
    """Affiche quelques statistiques sommaires relatives aux données."""
    # Affiche la description des données
    print(data.describe())

    # Affiche la distribution des variables
    data.hist()
    plt.show()


def main():
    """Exécute le programme."""
    # Charge les données brutes
    data = load_data("data/raw/data.csv")

    # Nettoie les données
    data = clean_data(data)

    # Réduit les données
    data = reduce_data(data)

    # Effectue du feature engineering
    data = feature_engineering(data)

    # Affiche quelques statistiques sommaires
    display_statistics(data)


if __name__ == "__main__":
    main()
