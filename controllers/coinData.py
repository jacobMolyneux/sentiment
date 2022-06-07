from flask import jsonify
import requests 
import json
alphavantagekey = 'M22S93GHXW8SM3TU'

def get_live_coin_price(coin:str):
    response = requests.get(f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={coin}&to_currency=USD&apikey={alphavantagekey}')
    data = response.json()
    return data['Realtime Currency Exchange Rate']['5. Exchange Rate']

def get_historical_data(coin:str, time_frame:int = None):
    response = requests.get(f'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol={coin}&market=USD&apikey={alphavantagekey}')
    data = response.json()
    price_data = data['Time Series (Digital Currency Daily)']
    final_data = []
    for date, price in price_data.items():
        final_data.append(
            {
                "Date": date,
                "Price": price['4a. close (USD)'],
                "Market Cap": price['6. market cap (USD)'],
                "Volume": price['5. volume']
            }
        )
    if time_frame:
        return final_data[0: time_frame]
    else:
        return final_data
            
print(get_historical_data('BTC', 7))
print(get_historical_data('BTC'))