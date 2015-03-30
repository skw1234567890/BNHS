#
# SampleModel class:
#	method:
#		avgOfHistoryPrice
#		avgOfHistoryPriceRatio
#		avgOfHistoryPriceRatioPrinter
#

import sys
sys.path.append("./tools")

from FetchData import *

ROOT_DIRECTORY = "./"
DATA_DIRECTORY = ROOT_DIRECTORY + "./datas/"

class SampleModel:
	@staticmethod 
	def avgOfHistoryPrice(stockname, days, dataType):
		result = FetchData.fetchByNameAndPeriodUpToNowByType(stockname, days, dataType)
		total = 0
		for e in result:
			total += float(e)
		return total/len(result)

	@staticmethod
	def avgOfHistoryPriceRatio(stockname, longDays, shortDays, dataType):
		longAvg = SampleModel.avgOfHistoryPrice(stockname, longDays, dataType)
		shortAvg = SampleModel.avgOfHistoryPrice(stockname, shortDays, dataType)
		ratio = float(float(shortAvg) - float(longAvg))/float(longAvg)
		return longAvg, shortAvg, ratio

	@staticmethod
	def avgOfHistoryPriceRatioPrinter(stockname, longDays, shortDays, dataType):
		longAvg, shortAvg, ratio = SampleModel.avgOfHistoryPriceRatio(stockname, longDays, shortDays, dataType)
		return dataType + "::" + str(longDays) + "days Avg: " + str(longAvg) + "    " + str(shortDays) + "days Avg: " + str(shortAvg) + "    ratio: " + str(ratio)