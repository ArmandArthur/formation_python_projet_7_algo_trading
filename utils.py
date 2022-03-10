import time
import csv
from typing import Any, Dict, List, Tuple


def time_it(function):
    """
        Encapsule la fonction et affiche le temps d'exécutation (decorateur)
    """
    def wrapper(*args, **kwargs):
        start = time.time()
        res = function(*args, **kwargs)
        elapsed = time.time() - start
        print(f"{function.__name__} --- {elapsed:.5f} seconds ---")
        return res
    return wrapper


def load_shares(file_name: str) -> List[Dict]:
    """
        Lit un csv à l'aide du dict reader et retourne une liste d'actions
    """
    shares = []
    with open(file_name, 'r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file, delimiter=',')
        next(reader)
        for share in reader:
            share['price'] = float(share['price'])
            share['gain'] = share['price']*float(share['profit'])/100
            shares.append(share)
    return shares


def convert_shares(shares: List[Dict[str, Any]]) -> List[Tuple[str, int, int]]:
    """
        Return une liste de tuple
    """
    shares_opti = []
    for share in shares:
        if share['price'] > 0:
            tuple = (share['name'], int(share['price']*100), int(share['gain']*100))
            shares_opti.append(tuple)
    return shares_opti
