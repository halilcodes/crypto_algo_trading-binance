from binance.client import Client
import pandas as pd
from binance import ThreadedWebsocketManager
import os
# import keys

api_key = os.getenv("binance_udemy_public_key")
secret_key = os.getenv("binance_udemy_secret_key")

client = Client(api_key=api_key, api_secret=secret_key, tld="com", testnet=True)

twm = ThreadedWebsocketManager()
twm.start()


def simple_bot(msg):
    """ define how to process incoming WebSocket messages """

    time = pd.to_datetime(msg["E"], unit="ms")
    price = float(msg["c"])

    print("Time: {} | Price: {}".format(time, price))

    if int(price) % 10 == 0:
        order = client.create_order(symbol="BTCUSDT", side="BUY", type="MARKET", quantity=0.1)
        print("\n" + 50 * "-")
        print("Buy {} BTC for {} USDT".format(order["executedQty"], order["cummulativeQuoteQty"]))
        print(50 * "-" + "\n")

        twm.stop()  # stop defined inside callback


twm.start_symbol_miniticker_socket(callback=simple_bot, symbol="BTCUSDT")
twm.join()  # required if stop is defined in callback function
