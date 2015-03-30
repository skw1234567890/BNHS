#
# DataType class
#	methods:
#		getTypeID
#

class DataType:
	@staticmethod
	def getTypeID(dataType):
		return {
		"Date" : 0,
		"Open" : 1,
		"High" : 2,
		"Low" : 3,
		"Close" : 4,
		"Volume" : 5,
		"Adj Close" : 6,
 		}.get(dataType, -1)

#
#
#
#if __name__ == "__main__":
#	print(DataType.getTypeID("Close"))
#	print(DataType.getTypeID("None"))