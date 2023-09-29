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


