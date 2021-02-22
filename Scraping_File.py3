#installing beautifulsoup
import sys
import subprocess
#implement pip as a subprocess
subprocess.check_call([sys.executable, '-m', 'pip','install','beautifulsoup4'])
subprocess.check_call([sys.executable, '-m', 'pip','install','pandas'])
subprocess.check_call([sys.executable, '-m', 'pip','install','pymongo'])

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


#importing everything we need
from bs4 import BeautifulSoup
import pandas as pd
import time as t
#Include the site
from requests import get
url = "https://www.blockchain.com/btc/unconfirmed-transactions"
response = get(url)
isCalled = False

def Scraping(url,isCalled):
    #re-read the site
    response = get(url)
    html_Soup = BeautifulSoup(response.text,'html.parser')
    bitcoin_containers = html_Soup.find_all(class_ = 'sc-1g6z4xm-0 hXyplo')
    #scarping
    hashes = []
    times = []
    amount_BTC = []
    amount_USD = []
    for container in bitcoin_containers:
        #the hash
        hash = container.find('div', class_='sc-1au2w4e-0 bTgHwk')
        hashes.append(hash.a.text)
        #print(hash.a.text)
        #time
        time = container.find_all('span', class_ = 'sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC')[0].text
        times.append(time)
        #print(time)
        #BTC
        btc = container.find_all('span', class_ = 'sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC')[1].text
        btc = btc.replace(' BTC' , '')
        amount_BTC.append(btc)
        #print(btc)
        #USD
        usd = container.find_all('span', class_ = 'sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC')[2].text
        amount_USD.append(usd)
        #print(usd)

    bitcoin_df = pd.DataFrame({
        'Hash': hashes,
        'time': times,
        'BTC': amount_BTC,
        'USD': amount_USD
    })
    #export to file
    file = open("BitCoinTransactions.txt",'a')
    if isCalled:
        BTC_string = bitcoin_df[bitcoin_df.BTC == bitcoin_df.BTC.max()].to_string(index=False,header=False)
    else:
        BTC_string = bitcoin_df[bitcoin_df.BTC == bitcoin_df.BTC.max()].to_string(index=False)

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
    #}

    #print(BTC_string)
    file.write('\n'+BTC_string)
    file.close()
    #print(bitcoin_df.info)
    #bitcoin_df





   

#functions call
while True:
    print("Scrapping begins")
    url = "https://www.blockchain.com/btc/unconfirmed-transactions"
    Scraping(url,isCalled)
    isCalled = True
    print("Scrapping done waiting 1 min for next scrape. Press ctrl + c to exit")
    t.sleep(60) #1min







