from requests import Session
import requests
session = Session()

# HEAD requests ask for *just* the headers, which is all you need to grab the
# session cookie
session.head('https://www.tradingview.com/markets/cryptocurrencies/quotes-all/')

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}

response = session.post(
    url='https://scanner.tradingview.com/crypto/scan',
    data={"filter":[{"left":"Recommend.MA","operation":"nempty"},{"left":"sector","operation":"nempty"},{"left":"market_cap_calc","operation":"nempty"},{"left":"name","operation":"match","right":"BTC$"}],"symbols":{"query":{"types":[]}},"columns":["sector","change","Perf.W","Perf.1M","Perf.3M","Perf.6M","Perf.YTD","Perf.Y","Volatility.D"],"sort":{"sortBy":"Recommend.MA","sortOrder":"asc"},"options":{"lang":"en"},"range":[0,50]}
    headers= headers
)

print(response.content)

print(response.text)