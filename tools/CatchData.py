import urllib
import os
import os.path

TEST_NAME = "AAPL"
HISTORY_DATA_URL = "https://ca.finance.yahoo.com/q/hp?s="
ROOT_DIRECTORY = "./../"
DATA_DIRECTORY = ROOT_DIRECTORY + "./datas/"
TMP_DIRECTORY = ROOT_DIRECTORY + "./tmp/"
CACHE_FILE = TMP_DIRECTORY + "cache"
TD_CLASS = "yfnc_tabledata1"

class CatchData:
	def init(self):
		return

	def getKeywords(self, keyWord, fileName):
		returnList = []
		with open(fileName, 'r') as inF:
			for line in inF:
				if keyWord in line:
					returnList.append(line)
		return returnList

	def processHtmlTable(self, inputString):
		returnList = []
		while True:
			pos = inputString.find(">")
			if pos is -1:
				break
			inputString = inputString[pos + 1:]
			if inputString[0:1] is "<":
				continue
			else:
				start = inputString.find("<")
				print(inputString[0:start])
				returnList.append(inputString[0:start])
				inputString = inputString[start:]
		return returnList

	def catchByName(self, stock_name):
		fileName = CACHE_FILE
		urlOfPage = HISTORY_DATA_URL + stock_name
		if not os.path.exists(DATA_DIRECTORY):
			os.makedirs(DATA_DIRECTORY)
		try:
			os.remove(fileName)
		except:
			None
		with open(fileName, 'a+') as targetFile:
			targetFile.write("")
			targetFile.close()
		try:
			urllib.urlretrieve(urlOfPage, fileName)
		except:
			None
		htmlTable = self.getKeywords(TD_CLASS, fileName)[0]
		dataList = self.processHtmlTable(htmlTable)
		

if __name__ == "__main__":
	CatchData().catchByName(TEST_NAME)
	None
