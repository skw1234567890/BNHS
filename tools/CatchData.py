#
# CatchData Class:
#	Used for catching history price of a specific stock and save the data in .csv file
#	Methods:
#		CatchByNameAndDate
#		CatchByNameAndDateToSpecificFile
#		CatchByName
#		CatchByNameToSpecificFile		
#

import urllib
import os
import os.path
import datetime

ROOT_DIRECTORY = "./"
DATA_DIRECTORY = ROOT_DIRECTORY + "./datas/"
HISTORY_DATA_CSV_URL_DOMAIN = "http://real-chart.finance.yahoo.com/table.csv?s="

class CatchData:
#
# Catch history price of a given stock with given period
#
	@staticmethod
	def catchByNameAndDate(stock_name, fromYear, fromMonth, fromDay, toYear, toMonth, toDay):
		fileName = DATA_DIRECTORY + stock_name + ".csv"
		CatchData.catchByNameToSpecificFile(stock_name, fromYear, fromMonth, fromDay, toYear, toMonth, toDay, fileName)

#
# Catch history price of a given stock with given period and store the data to a file with given file name
#
	@staticmethod
	def catchByNameAndDateToSpecificFile(stock_name, fromYear, fromMonth, fromDay, toYear, toMonth, toDay, fileName):
		urlOfPage = HISTORY_DATA_CSV_URL_DOMAIN + stock_name + "&d=" + str(toMonth - 1) + "&e=" + str(toDay) + "&f=" + str(toYear) + "&g=d&a=" + str(fromMonth - 1) + "&b=" + str(fromDay) + "&c=" + str(fromYear) + "&ignore=.csv"
		CatchData.catchByURL(urlOfPage, fileName)

#
# Catch history price of a given stock up to now
#
	@staticmethod
	def catchByName(stock_name):
		fileName = DATA_DIRECTORY + stock_name + ".csv"
		CatchData.catchByNameToSpecificFile(stock_name, fileName)

#
# Catch history price of a given stock up to now and store the data to a file with given file name
#
	@staticmethod
	def catchByNameToSpecificFile(stock_name, fileName):
		now = datetime.datetime.now()
		CatchData.catchByNameAndDateToSpecificFile(stock_name, 1980, 12, 12, now.year, now.month, now.day, fileName)

#
# Store the content with given url to a file with given file name
#
	@staticmethod
	def catchByURL(urlOfPage, fileName):
		print("update " + fileName[10:-3])
		if not os.path.exists(DATA_DIRECTORY):
			os.makedirs(DATA_DIRECTORY)
		try:
			os.remove(fileName)
		except:
			None
		with open(fileName, 'w') as targetFile:
			targetFile.close()
		try:
			urllib.urlretrieve(urlOfPage, fileName)
		except:
			None

#
# Not used
# Find the string by keywords
#
	def getKeywords(self, keyWord, fileName):
		returnList = []
		with open(fileName, 'r') as inF:
			for line in inF:
				if keyWord in line:
					returnList.append(line)
		return returnList

#
# Not used
# processing HTML tag, get the data in the table
#
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


#
#
#
#if __name__ == "__main__":
#	CatchData.catchByName("AAPL")
#	CatchData.catchByName("YHOO")
#	None