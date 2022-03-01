import sys
from utils import time_it, load_shares


@time_it
def optimized(file_name: str):
    shares = load_shares(file_name)

    # Trie par du plus haut profil_net au plus bas
    shares = sorted(shares, key=lambda d: -d['gain'])

    best_combination_price = 0
    best_combination = []

    for share in shares:
        if best_combination_price+share['price'] <= 500:
            best_combination_price += share['price']
            best_combination.append(share)

    print([share['name'] for share in best_combination])
    print(sum([share['price'] for share in best_combination]))
    print(sum([share['gain'] for share in best_combination]))


if __name__ == '__main__':
    optimized(sys.argv[1])
