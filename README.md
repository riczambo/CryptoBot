# CryptoBot_v2

VERSIONE ITALIANA

Il bot manda una richiesta a CoinMarketCap per ottenere una lista delle 100 criptovalute con maggior capitalizzazione.
Il bot elabora i seguenti punti e salva i risultati in un file JSON.

- La criptovaluta con il volume maggiore (in $) delle ultime 24 ore
- Le migliori e peggiori 10 criptovalute (per incremento in percentuale delle ultime 24 ore)
- La quantità di denaro necessaria per acquistare una unità di ciascuna delle prime 20 criptovalute
- La quantità di denaro necessaria per acquistare una unità di tutte le criptovalute il cui volume delle ultime 24 ore sia superiore ad una certa cifra
- La percentuale di guadagno o perdita realizzata in caso di acquisto di una unità di ciascuna delle prime 20 criptovalute il giorno prima (ipotizzando che la classifca non sia cambiata nel frattempo)

Un esempio di file è il seguente:
[Example_JSON_Results](Example_JSON_Results)

----------------------------------------------------------------------------
ENGLISH VERSION

The bot sends a request to CoinMarketCap to obtain a list of the 100 most capitalised cryptocurrencies.
The bot processes the information below and saves the results in a JSON file.

- The cryptocurrency with the highest volume (in $) in the last 24 hours
- The best and worst 10 cryptocurrencies (by percentage increase over the last 24 hours)
- The amount of money needed to buy one unit of each of the top 20 cryptocurrencies
- The amount of money required to buy one unit of all cryptocurrencies whose volume in the last 24 hours is above a certain figure
- The percentage gain or loss realised when buying one unit of each of the top 20 cryptocurrencies the day before (assuming the rankings have not changed in the meantime)

This is an example file:
[Example_JSON_Results](Example_JSON_Results)
