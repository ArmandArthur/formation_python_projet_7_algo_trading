# Algo Trading

- [Algo Trading](#algo-trading)
- [Set up répertoire:](#set-up-répertoire)
- [Installer l'environnement virtuel:](#installer-lenvironnement-virtuel)
- [Lancer le programme forcebrute:](#lancer-le-programme-forcebrute)
- [Lancer le programme optimized:](#lancer-le-programme-optimized)
- [Installer et run flake8:](#installer-et-run-flake8)
  
# Set up répertoire:

`cd formation_python_projet_7_algo_trading`

# Installer l'environnement virtuel:

`sudo apt-get install python3.10-dev python3.10-venv`<br />
`python -m venv .venv`<br />
`source .venv/bin/activate` (linux)

Les fichiers de data ont été harmonisé.
Il suffit de lancer le programme avec le fichier en paramètre console.

# Lancer le programme forcebrute:

`py bruteforce.py data/shares.csv` (windows)<br />
`python bruteforce.py data/shares.csv` (linux)

# Lancer le programme optimized:

`py optimized.py data/shares_dataset1.csv` (windows)<br />
`python optimized.py data/shares_dataset1.csv` (linux)

# Installer et run flake8:

`pip install flake8`<br />
`flake8 > flake8_repport.txt`


