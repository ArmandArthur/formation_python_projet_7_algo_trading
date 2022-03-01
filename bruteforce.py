from itertools import combinations
import sys
from utils import time_it, load_shares


@time_it
def bruteforce(file_name: str):
    shares = load_shares(file_name)

    best_combination = None
    gain_best_combination = 0
    price_best_combination = 0

    for rep in range(1, len(shares)+1):
        for combination in combinations(shares, rep):
            price_combination = sum(share['price'] for share in combination)
            if price_combination <= 500:
                gain_combination = sum(share['gain'] for share in combination)
                if gain_combination > gain_best_combination:
                    best_combination = combination
                    gain_best_combination = gain_combination
                    price_best_combination = price_combination

    print([share['name'] for share in best_combination])
    print(gain_best_combination)
    print(price_best_combination)


if __name__ == '__main__':
    bruteforce(sys.argv[1])
