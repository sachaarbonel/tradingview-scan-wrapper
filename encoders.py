# from collections import namedtuple
from json import JSONEncoder,dumps

# class TupleEncoder(JSONEncoder):

#     def _iterencode(self, obj, markers=None):
#         if isinstance(obj, tuple) and hasattr(obj, '_asdict'):
#             gen = self._iterencode_dict(obj._asdict(), markers)
#         else:
#             gen = JSONEncoder._iterencode(self, obj, markers)
#         for chunk in gen:
#             yield chunk

# ## TODO change to default argument for handling 1 argument (simple json key value)
# class tupler(namedtuple('f', 'foo, bar')):
#     pass

params = ["name","Recommend.Other","ADX","AO", "ATR","CCI20","MACD.macd","MACD.signal", "Mom","RSI","Stoch.K","Stoch.D","description","name","subtype","ADX", "ADX+DI","ADX-DI", "ADX+DI[1]","ADX-DI[1]","AO","AO[1]","CCI20","CCI20[1]", "MACD.macd", "MACD.signal", "Mom", "Mom[1]", "RSI", "RSI[1]", "Stoch.K", "Stoch.D", "Stoch.K[1]", "Stoch.D[1]"]
volatility = 'Volatility.D'
operations = ['nempty','in_range']
orders = ['desc','asc']
ranges = [1,1e+100]
paramsD = {'order':orders[0],'left_first':volatility,'operation_first':operations[0],'left_second':volatility,'operation_second':operations[1],"right":ranges}
filters = [{'left':paramsD['left_first'],'operation':paramsD['operation_first']},{'left':paramsD['operation_second'],'operation':paramsD['operation_second'],'right':paramsD['right']}]
symbols = {'query':{'types':[]}}
languages = ['en']
columns = params
sort =  {'sortBy':volatility,'sortOrder':paramsD['order']}
options = {'lang':languages[0]}
ranges = [0,150]

data = {"filter":filters,"symbols":symbols,"columns":columns,"sort":sort,"options":options,'range':ranges}

print(dumps(data))

		
	# filter		[]
		
	# symbols		{}
		
	# columns		[]
		
	# sort		{}
		
	# options		{}
		
	# range		[]
