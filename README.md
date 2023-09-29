**Data  Preprocessing  Program**

**What is it about ?**

Ce programme permet d'effectuer les tâches classiques à effectuer avant une analyse de données, à savoir :

* Récupérer un jeu de données
* Nettoyer les données
* Réduire les données
* Faire du feature engineering
* Afficher quelques statistiques sommaires relatives aux données

**Installation**

Pour installer le programme, il suffit de cloner le dépôt Git et d'installer les dépendances :

```
git clone https://github.com/martinoyovo/data-preprocessing-pipeline.git
data-preprocessing-pipeline

# Installer les dépendances
pip install -r requirements.txt
```

**Utilisation**

Pour utiliser le programme, il suffit d'exécuter la commande suivante :

```
python -m github_actions.workflow
```

Cette commande exécutera le workflow GitHub Actions, qui effectue les tâches suivantes :

* Télécharge le fichier `dataset.csv` dans le répertoire `data/raw`

**Arborescence du projet**

Le projet est organisé de la manière suivante :

```
.
├── data
│   ├── raw
│   │   └── dataset.csv
│   └── cleaned
│       └── dataset_cleaned.csv
├── processed
│   └── dataset_processed.csv
├── reports
│   └── stats.txt
├── requirements.txt
├── src
│   ├── process.py
│   └── train.py
└── README.md
```

