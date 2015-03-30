#
# StockList Class:
#	Used to manage my stocks
#	Methods:
#		@static fetchALL
#		@static addStock
#		@static addStockList
#		@static removeAll
#		@static doAll
#

ROOT_DIRECTORY = "./"
DATA_DIRECTORY = ROOT_DIRECTORY + "./datas/"
CONFIG_FILE_NAME = DATA_DIRECTORY + "list.config"

class StockList:
#
# Fetch all stocks
#
	@staticmethod
	def getAll():
		result = []
		try:
			targetFile = open(CONFIG_FILE_NAME, 'r')
			for line in targetFile:
				result.append(line[:-1])
			targetFile.close()
			return result
		except:
			return result

#
# Adding one stock to my list
#
	@staticmethod
	def addStock(stockName):
		with open(CONFIG_FILE_NAME, 'a+') as targetFile:
			targetFile.write(stockName + "\n")
			targetFile.close()

#
# Adding a list of stocks to my list
#
	@staticmethod
	def addStockList(stockNameList):
		with open(CONFIG_FILE_NAME, 'a+') as targetFile:
			for e in stockNameList:
				targetFile.write(e + "\n")
			targetFile.close()

#
# Removing all stocks from my list
#
	@staticmethod
	def removeAll():
		with open(CONFIG_FILE_NAME, 'w') as targetFile:
			targetFile.close()

#
# Do the same action to all the stocks in the list
#
	@staticmethod
	def doAll(action, args):
		result = []
		try:
			targetFile = open(CONFIG_FILE_NAME, 'r')
			for line in targetFile:
				if args is None:
					result.append({line[:-1] : action(line[:-1])})
				else:
					result.append({line[:-1] : action(line[:-1], *args)})
			targetFile.close()
			return result
		except:
			return result

#
#
#
#if __name__ == "__main__":
#	StockList.removeAll()
#	print(StockList.getAll())
#	StockList.addStock("AAPL")
#	StockList.addStock("YHOO")
#	print(StockList.getAll())
#	StockList.addStockList(['GOOG', 'MSFT', 'FB', 'ORCL'])
#	print(StockList.getAll())
#	print(StockList.getAll())
#	StockList.doAll(CatchData.catchByName)
#	None