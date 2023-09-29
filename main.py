#YOVO, KOSSI MARTINO, MASTER 2 DIT
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def load_data(data_path):
    """Charge les données brutes à partir d'un chemin donné."""
    data = pd.read_csv(data_path)
    return data



