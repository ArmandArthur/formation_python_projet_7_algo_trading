import sys
from utils import time_it, load_shares, convert_shares


@time_it
def optimized(file_name: str, capacite: str):
    """
        Obliger de multipler les données par un cofficient car la matrice n'accepte pas les floats
    """
    coefficient = 100
    capacite = int(capacite)*coefficient
    shares = load_shares(file_name)
    elements = convert_shares(shares)
    matrice = [[0 for x in range(capacite + 1)] for x in range(len(elements) + 1)]

    # Création de la matrice
    for i in range(1, len(elements) + 1):
        for w in range(1, capacite + 1):
            if elements[i-1][1] <= w:
                matrice[i][w] = max(elements[i-1][2] + matrice[i-1][w-elements[i-1][1]], matrice[i-1][w])
            else:
                matrice[i][w] = matrice[i-1][w]

    # Retrouve les éléments en fonction de la somme
    w = capacite
    n = len(elements)
    elements_selection = []

    while w >= 0 and n >= 0:
        e = elements[n-1]
        if matrice[n][w] == matrice[n-1][w-e[1]] + e[2]:
            elements_selection.append(e)
            w -= e[1]
        n -= 1

    # Rendement
    print(matrice[-1][-1]/coefficient)
    # Prix dépensé
    print(sum([share[1]/coefficient for share in elements_selection]))
    # Actions choisies
    print([share[0] for share in elements_selection])


if __name__ == '__main__':
    optimized(sys.argv[1], sys.argv[2])
