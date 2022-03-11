# Algo Trading
Phrase de présentation du projet/programme.

- [Algo Trading](#algo-trading)
- [Cloner le dépôt du projet:](#cloner-le-dépôt-du-projet)
- [Aller sur le bon répertoire:](#aller-sur-le-bon-répertoire)
- [Installer l'environnement virtuel:](#installer-lenvironnement-virtuel)
- [Lancer le programme bruteforce:](#lancer-le-programme-bruteforce)
- [Lancer le programme optimized:](#lancer-le-programme-optimized)
- [Lancer le programme optimized (meilleur):](#lancer-le-programme-optimized-meilleur)
- [Installer et run flake8:](#installer-et-run-flake8)

# Cloner le dépôt du projet:

`git clone git@github.com:ArmandArthur/formation_python_projet_7_algo_trading.git`
  
# Aller sur le bon répertoire:

`cd formation_python_projet_7_algo_trading`

# Installer l'environnement virtuel:

`python3 -m venv venv`<br />
`source ./venv/bin/activate` (UNIX)<br />
`./venv/scripts/activate` (windows)

Les fichiers de data ont été harmonisé.
Il suffit de lancer le programme avec le fichier en paramètre console.

# Lancer le programme bruteforce:

`py bruteforce.py data/shares.csv` (windows)<br />
`python3 bruteforce.py data/shares.csv` (UNIX)

# Lancer le programme optimized:

`py optimized.py data/shares_dataset1.csv` (windows)<br />
`python3 optimized.py data/shares_dataset1.csv` (UNIX)

# Lancer le programme optimized (meilleur):

`py optimized_correctif.py data/shares_dataset1.csv <capacite>` (windows)<br />
`python3 optimized_correctif.py data/shares_dataset1.csv <capacite>` (UNIX)

# Installer et run flake8:

`pip install flake8`<br />
`flake8 *.py > flake8_report.txt`


