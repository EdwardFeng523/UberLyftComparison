import time
import random
import requests
import json

MIN_LAT = 29645346

MAX_LAT = 30135064

MIN_LNG = -95809370

MAX_LNG = -95277361

RATIO = 1000000

num_count = 0

while True:
    if time.time() % 10 == 0:
        rand_lat_dep = str(float(random.randint(MIN_LAT, MAX_LAT)) / RATIO)
        rand_lng_dep = str(float(random.randint(MIN_LNG, MAX_LNG)) / RATIO)
        
        rand_lat_dest = str(float(random.randint(MIN_LAT, MAX_LAT)) / RATIO)
        rand_lng_dest = str(float(random.randint(MIN_LNG, MAX_LNG)) / RATIO)

        url = "https://lyber.co/api/estimate?depar_lat=" + rand_lat_dep + "&depar_lng=" + rand_lng_dep + "&dest_lat=" + rand_lat_dest + "&dest_lng=" + rand_lng_dest

        r = requests.get(url=url)
        num_count += 1
        print ("count=", num_count)


    


