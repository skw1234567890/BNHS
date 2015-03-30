#
# FetchData class
#

from DataType import *

ROOT_DIRECTORY = "./"
DATA_DIRECTORY = ROOT_DIRECTORY + "./datas/"

class FetchData:
	@staticmethod
	def fetchByName(stockname):
		result = []
		fileName = DATA_DIRECTORY + stockname + ".csv"
		try:
			targetFile = open(fileName, 'r')
			for line in targetFile:
				tmpList = line.split(",")
				tmpList[6] = tmpList[6][:-1]
				result.append(tmpList)
			targetFile.close()
			return result
		except:
			return result

	@staticmethod
	def fetchByNameAndPeriodUpToNowByType(stockname, period, dataType):
		typeId = DataType.getTypeID(dataType)
 		if typeId is -1:
 			return []
 		result = []
 		fileName = DATA_DIRECTORY + stockname + ".csv"
 		targetFile = open(fileName, 'r')
 		try:
 			targetFile = open(fileName, 'r')
 			count = period
 			for line in targetFile:
 				if typeId is not 6:
 					result.append(line.split(",")[typeId])
 				else:
 					result.append(line.split(",")[typeId][:-1])
 				count -= 1
 				if count < 0:
 					break
 			targetFile.close()
 			return result[1:]
 		except:
 			return []

#
#
#
#if __name__ == "__main__":
#	print(FetchData.fetchByName("AAPL"))
#	print(FetchData.fetchByNameAndPeriodUpToNowByType("C", 100, "Open"))