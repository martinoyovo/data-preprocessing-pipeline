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



