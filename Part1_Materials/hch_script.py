import os
from keys import testnet_api_public, testnet_api_secret
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager

public_key = os.getenv("binance_udemy_public_key")
secret_key = os.getenv("binance_udemy_secret_key")

print(public_key)
print(secret_key)

client = Client(api_key=public_key, api_secret=secret_key, tld="com")