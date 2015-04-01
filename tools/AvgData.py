#
# AvgData class
#

#TODO: ROOT_DIRECTORY
ROOT_DIRECTORY = "./"
DATA_DIRECTORY = ROOT_DIRECTORY + "./datas/"

class AvgData:
	@staticmethod
	def avgDataAll(stockname, period):
		readFileName = DATA_DIRECTORY + stockname + ".csv"
		writeFileName = DATA_DIRECTORY + stockname + "_AVG_" + str(period) + ".csv"
		try:
			readTargetFile = open(readFileName, 'r')
		except:
			readTargetFile.close()
			with open(writeFileName, 'a+') as writeTargetFile:
				writeTargetFile.write("")
			return
		readList = list(readTargetFile)
		with open(writeFileName, 'w') as writeTargetFile:
			writeTargetFile.write("")
			startPos = 1
			sum = [0, 0, 0, 0, 0, 0, 0]
			endPos = 1
			end = len(readList)
			while endPos < period:
				tmpList = readList[endPos].split(",")
				sum[1] += float(tmpList[1])
				sum[2] += float(tmpList[2])
				sum[3] += float(tmpList[3])
				sum[4] += float(tmpList[4])
				sum[5] += float(tmpList[5])
				sum[6] += float(tmpList[6][:-1])
				endPos += 1
			while endPos < end:
				tmpList = readList[endPos].split(",")
				sum[1] += float(tmpList[1])
				sum[2] += float(tmpList[2])
				sum[3] += float(tmpList[3])
				sum[4] += float(tmpList[4])
				sum[5] += float(tmpList[5])
				sum[6] += float(tmpList[6][:-1])
				startTmpList = readList[startPos].split(",")
				writeTargetFile.write(startTmpList[0] + "," + str(float(float(sum[1])/float(period))) + "," + str(float(float(sum[2])/float(period))) + "," + str(float(float(sum[3])/float(period))) + "," + str(float(float(sum[4])/float(period))) + "," + str(float(float(sum[5])/float(period))) + "," + str(float(float(sum[6])/float(period))) + "\n")
				sum[1] -= float(startTmpList[1])
				sum[2] -= float(startTmpList[2])
				sum[3] -= float(startTmpList[3])
				sum[4] -= float(startTmpList[4])
				sum[5] -= float(startTmpList[5])
				sum[6] -= float(startTmpList[6][:-1])
				endPos += 1
				startPos += 1
			writeTargetFile.close()
#
#
#
#if __name__ == "__main__":
#	AvgData.avgDataAll("AAPL", 50)
#	AvgData.avgDataAll("AAPL", 200)
#	None
