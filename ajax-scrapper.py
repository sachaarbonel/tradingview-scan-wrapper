from requests import Session
import requests
session = Session()

# HEAD requests ask for *just* the headers, which is all you need to grab the
# session cookie
session.head('https://www.tradingview.com/markets/cryptocurrencies/quotes-all/')

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}

response = session.post(
    url='https://scanner.tradingview.com/crypto/scan',
    data="{\"filter\":[{\"left\":\"change\",\"operation\":\"nempty\"}],\"symbols\":{\"query\":{\"types\":[]}},\"columns\":[\"name\",\"Recommend.Other\",\"ADX\",\"AO\",\"ATR\",\"CCI20\",\"MACD.macd\",\"MACD.signal\",\"Mom\",\"RSI\",\"Stoch.K\",\"Stoch.D\",\"description\",\"name\",\"subtype\",\"ADX\",\"ADX+DI\",\"ADX-DI\",\"ADX+DI[1]\",\"ADX-DI[1]\",\"AO\",\"AO[1]\",\"CCI20\",\"CCI20[1]\",\"MACD.macd\",\"MACD.signal\",\"Mom\",\"Mom[1]\",\"RSI\",\"RSI[1]\",\"Stoch.K\",\"Stoch.D\",\"Stoch.K[1]\",\"Stoch.D[1]\"],\"sort\":{\"sortBy\":\"change\",\"sortOrder\":\"desc\"},\"options\":{\"lang\":\"en\"},\"range\":[0,150]}",
    headers= headers
)

print(response.content)

print(response.text)