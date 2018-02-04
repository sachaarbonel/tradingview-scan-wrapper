from requests import Session
import requests
import jsonpickle
import json
session = Session()

# HEAD requests ask for *just* the headers, which is all you need to grab the
# session cookie
session.head('https://www.tradingview.com/markets/cryptocurrencies/quotes-all/')

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}

params = ["name","Recommend.Other","ADX","AO", "ATR","CCI20","MACD.macd","MACD.signal", "Mom","RSI","Stoch.K","Stoch.D","description","name","subtype","ADX", "ADX+DI","ADX-DI", "ADX+DI[1]","ADX-DI[1]","AO","AO[1]","CCI20","CCI20[1]", "MACD.macd", "MACD.signal", "Mom", "Mom[1]", "RSI", "RSI[1]", "Stoch.K", "Stoch.D", "Stoch.K[1]", "Stoch.D[1]"]
volatility = ['Volatility.D','change']
operations = ['nempty','in_range']
orders = ['desc','asc']
ranges = [1,1e+100]
paramsD = {'order':orders[0],'left_first':volatility[1],'operation_first':operations[0],'left_second':volatility,'operation_second':operations[1],"right":ranges}
# filters = [{'left':paramsD['left_first'],'operation':paramsD['operation_first']},
# {'left':paramsD['operation_second'],'operation':paramsD['operation_second'],
# 'right':paramsD['right']}]
filters = [{'left':paramsD['left_first'],'operation':paramsD['operation_first']}]
symbols = {'query':{'types':[]}}
languages = ['en']
columns = params
sort =  {'sortBy':volatility[1],'sortOrder':paramsD['order']}
options = {'lang':languages[0]}
ranges = [0,150]

data = {"filter":filters,"symbols":symbols,"columns":columns,"sort":sort,"options":options,'range':ranges}

data2 = "{\"filter\":[{\"left\":\"change\",\"operation\":\"nempty\"}],\"symbols\":{\"query\":{\"types\":[]}},\"columns\":[\"name\",\"Recommend.Other\",\"ADX\",\"AO\",\"ATR\",\"CCI20\",\"MACD.macd\",\"MACD.signal\",\"Mom\",\"RSI\",\"Stoch.K\",\"Stoch.D\",\"description\",\"name\",\"subtype\",\"ADX\",\"ADX+DI\",\"ADX-DI\",\"ADX+DI[1]\",\"ADX-DI[1]\",\"AO\",\"AO[1]\",\"CCI20\",\"CCI20[1]\",\"MACD.macd\",\"MACD.signal\",\"Mom\",\"Mom[1]\",\"RSI\",\"RSI[1]\",\"Stoch.K\",\"Stoch.D\",\"Stoch.K[1]\",\"Stoch.D[1]\"],\"sort\":{\"sortBy\":\"change\",\"sortOrder\":\"desc\"},\"options\":{\"lang\":\"en\"},\"range\":[0,150]}"
response = session.post(
    url='https://scanner.tradingview.com/crypto/scan',
    data=json.dumps(data),
    headers= headers
)

#print(response.content)

res = jsonpickle.decode(response.text)
print(len(res['data'][0]['d']))
# print(len(params))