import requests 
import json

f = open('dataTest.json')
transactions = json.load(f)
f.close()

#address = input("inserisci l'indirizzo: ")
address = 'http://localhost:3000/add_transaction'

for t in transactions:
    r = requests.post(address,json = t)
    print(f"sent: {t['title']}, status: {r}")
