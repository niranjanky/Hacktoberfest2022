#Get the price for single currency
# Import libraries
import json
import requests
  
# defining key/request url
key = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
  
# requesting data from url
data = requests.get(key)  
data = data.json()
print(f"{data['symbol']} price is {data['price']}")

#Get the price for multiple currency
# Import libraries
import json
import requests
  
# Defining Binance API URL
key = "https://api.binance.com/api/v3/ticker/price?symbol="
  
# Making list for multiple crypto's
currencies = ["BTCUSDT", "DOGEUSDT", "LTCUSDT"]
j = 0
  
# running loop to print all crypto prices
for i in currencies:
    
    # completing API for request
    url = key+currencies[j]  
    data = requests.get(url)
    data = data.json()
    j = j+1
    print(f"{data['symbol']} price is {data['price']}")
