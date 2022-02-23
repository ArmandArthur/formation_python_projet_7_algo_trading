import time
import csv

def time_it(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        function(*args, **kwargs)
        print(function.__name__+"--- %s seconds ---" % (time.time() - start)) 
    return wrapper

def load_shares(file_name: str):
    shares = []
    with open(file_name, 'r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file,delimiter = ',')
        next(reader)
        for share in reader:
            share['price'] = float(share['price'])
            share['gain'] = share['price']*float(share['profit'])/100
            shares.append(share)
    return shares