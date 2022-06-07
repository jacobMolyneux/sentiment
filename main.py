from flask import Flask
import controllers.coinData as coinController

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/livePrices')
def livePriceRoute():
    return coinController.get_live_coin_price('BTC')
@app.route('/historicalPrices')
def historicalPrice():
    return coinController.get_historical_data('BTC')
