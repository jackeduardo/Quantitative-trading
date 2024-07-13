from binance.client import Client
client = Client(api_key, api_secret)
print(client.get_account())

print(client.get_asset_balance(asset='BTC'))