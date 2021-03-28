#Reddis
import redis
import pickle
import zlib
expiration_Seconds = 60
r = redis.Redis(
    host = 'localhost',
    port = 6379,
    password = 'myP@ass'
)

 #mongoDB
from pymongo import MongoClient
import urllib.parse
username = urllib.parse.quote_plus('superuser')
password = urllib.parse.quote_plus('testp@ss')
try: 
    client = MongoClient("mongodb://%s:%s@127.0.0.1:27017" % (username,password))
    db = client["Bitcoin_db"]
    print("Connected successfully!!!") 
except:   
    print("Could not connect to MongoDB") 

    
print("ReddisToMono.py3 is running")

hashes = []
times = []
amount_BTC = []
amount_USD = []
string_BTC = []


keys = r.keys('*')

max = 47 #when scraping there will always be 49
print("length in redisToMongo: ", max)
for key in range(max):
    val = r.get(key)
    val = val.decode("utf-8") 
    print(key)
    hashes.append(val.split(": '")[0].split('\n')[0].strip())
    print(val.split(": '")[0].split('\n')[0].strip())
    times.append(val.split(": '")[0].split('\n')[1].strip())
    amount_BTC.append(val.split(": '")[0].split('\n')[2].strip())
    amount_USD.append(val.split(": '")[0].split('\n')[3].strip())
    

bitcoin_df = pd.DataFrame({
    'Hash': hashes,
    'time': times,
    'BTC': amount_BTC,
    'USD': amount_USD
})

#insert in mongoDB
dataMongo = bitcoin_df[bitcoin_df.BTC == bitcoin_df.BTC.max()].to_string(index=False,header=False)
collections = db.Bitcoin_Highest_Value
stringDataMongo = dataMongo.split(" ")
bigHash = stringDataMongo[0]
bigTime = stringDataMongo[1]
bigBTC = stringDataMongo[2]
bigDollar = stringDataMongo[3]
btc_rec = {
    "Hash": bigHash,
    "Time":bigTime,
    "BTC":bigBTC,
    "USD":bigDollar
}

    #insert data
rec_id = collections.insert_one(btc_rec)
print("Data inserted with record ids",btc_rec)

cursor = collections.find()
for record in cursor:
    print(record)



print("ReddisToMono.py3 is closing")

#loop over all strings and put them in arrays
    

