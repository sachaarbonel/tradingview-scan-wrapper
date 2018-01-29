import json
from collections import namedtuple

data = '{"name": "John Smith", "hometown": {"name": "New York", "id": 123}}'
data2 = "{\"filter\":[{\"left\":\"change\",\"operation\":\"nempty\"}],\"symbols\":{\"query\":{\"types\":[]}},\"columns\":[\"name\",\"Recommend.Other\",\"ADX\",\"AO\",\"ATR\",\"CCI20\",\"MACD.macd\",\"MACD.signal\",\"Mom\",\"RSI\",\"Stoch.K\",\"Stoch.D\",\"description\",\"name\",\"subtype\",\"ADX\",\"ADX+DI\",\"ADX-DI\",\"ADX+DI[1]\",\"ADX-DI[1]\",\"AO\",\"AO[1]\",\"CCI20\",\"CCI20[1]\",\"MACD.macd\",\"MACD.signal\",\"Mom\",\"Mom[1]\",\"RSI\",\"RSI[1]\",\"Stoch.K\",\"Stoch.D\",\"Stoch.K[1]\",\"Stoch.D[1]\"],\"sort\":{\"sortBy\":\"change\",\"sortOrder\":\"desc\"},\"options\":{\"lang\":\"en\"},\"range\":[0,150]}"
# Parse JSON into an object with attributes corresponding to dict keys.
x = json.loads(data2, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
#print(x.name, x.hometown.name, x.hometown.id)
print(x.filter[0].left,x.filter[0].operation,x.symbols,x.columns,x.sort,x.options,x.range)