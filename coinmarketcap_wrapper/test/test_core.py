from coinmarketcap_wrapper import Market
market = Market()
market.coin('bitcoin', limit=1)
market.stats()
