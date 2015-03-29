#
# FetchData class
#

ROOT_DIRECTORY = "./../"
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

if __name__ == "__main__":
	print(FetchData.fetchByName("AAPL"))