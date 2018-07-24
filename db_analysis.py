import pymongo
from collections import defaultdict

client = pymongo.MongoClient("mongodb://terrence:HelloWorld!@127.0.0.1:27018/lyber-server")

db = client["lyber-server"]

estimates = db["estimates"]

print (estimates.count())

price_total = defaultdict(int)
price_count = defaultdict(int)
price_avg = {}

for estimate in estimates.find():
    estData = estimate['estData']
    for i in range(len(estData)):
        if estData[i]['max_estimate'] != None and estData[i]['min_estimate'] != None:
            price_total[estData[i]['display_name']] += (estData[i]['max_estimate'] + estData[i]['min_estimate']) / 2.0
            price_count[estData[i]['display_name']] += 1
            print ("Added " + str((estData[i]['max_estimate'] + estData[i]['min_estimate']) / 2.0) + " into total.")


print (price_total)
print (price_count)

for key, value in price_total.items():
    price_avg[key] = price_total[key] / price_count[key]

print price_avg
