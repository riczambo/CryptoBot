import config
import requests
from datetime import datetime
import json
class Bot:
    def __init__(self):
        self.url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        self.params = {
            'start': '1',
            'limit': '100',
            'convert': 'USD'
        }
        self.headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': config.api_key
        }
        self.orders = []

    def fetchCurrenciesData(self):
        r = requests.get(url=self.url, headers=self.headers, params=self.params).json()
        return r['data']

impactBot = Bot()

now = datetime.now()
currencies = impactBot.fetchCurrenciesData()
sorted_currencies = sorted(currencies, key=lambda x: x['quote']['USD']['percent_change_24h'], reverse=True)

results_1 = {}
results_2 = {}
results_3 = {}
maxFlowCurrency = [None, 0]
totPrice = 0
h24volume = 76000000
totPrice24 = 0
totGain = 0

# logic1
for currency in currencies:
    if currency['quote']['USD']['volume_24h'] > maxFlowCurrency[1]:
        maxFlowCurrency[0] = currency['name']
        maxFlowCurrency[1] = currency['quote']['USD']['volume_24h']
results_1.update({maxFlowCurrency[0]: maxFlowCurrency[1]})

# logic2
for currency in sorted_currencies[:10]:
    percent_change = currency['quote']['USD']['percent_change_24h']
    results_2.update({currency['name']: f'{percent_change}%'})

# logic3
for currency in sorted_currencies[-10:]:
    percent_change = currency['quote']['USD']['percent_change_24h']
    results_3.update({currency['name']: f'{percent_change}%'})

# logic4
for currency in currencies[:20]:
    totPrice += currency['quote']['USD']['price']

# logic5
for currency in currencies:
    if currency['quote']['USD']['volume_24h'] > h24volume:
        totPrice24 += currency['quote']['USD']['price']

# logic6
for currency in currencies[:20]:
    Gain = currency['quote']['USD']['price']-(currency['quote']['USD']['price']/(1+currency['quote']['USD']['percent_change_24h']/100))
    totGain += Gain
totPerc = totGain * 100 / totPrice

# JSON format
x = {
    "La criptovaluta con il volume maggiore (in $) delle ultime 24 ore": results_1,
    "Le migliori 10 criptovalute in termini di incremento percentuale nelle ultime 24 ore": results_2,
    "Le peggiori 10 criptovalute in termini di incremento percentuale nelle ultime 24 ore": results_3,
    "Denaro necessario per acquistare una unita di ciascuna delle prime 20 criptovalute": totPrice,
    "Denaro necessario per acquistare una unita delle criptovalute con volume last24h > 76.000.000$": totPrice24,
    "% realizzata se avessi comprato una unita di ciascuna delle prime 20 criptovalute il giorno prima": f'{totPerc}%'
}

# JSON export
file_time = datetime.now().strftime("%d%m%Y_%I%M%S%p")
with open("Results_JSON_" + file_time, "w") as outfile:
    json.dump(x, outfile, indent=4)
