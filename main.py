import sys
sys.path.append("./tools")
sys.path.append("./models")

from StockList import *
from CatchData import *
from FetchData import *
from DataType import *

if __name__ == "__main__":
#	print(StockList.getAll())
#	print(FetchData.fetchByNameAndPeriodUpToNowByType("AAPL", 50, "Close"))
#	StockList.addStock("GS")
#	StockList.doAll(CatchData.catchByName, None)
#	CatchData.catchByName("V")
#	for e in StockList.doAll(FetchData.fetchByNameAndPeriodUpToNowByType, (100, "Open")):
#		print e