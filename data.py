'''
Class: Data
Parameters: actual data
Purpose: this is what is used to handle the actual data
'''
class Data:
	def __init__(self, data):
		self.set_data(data)
	
	def set_data(self,data):
		self.__data = data

	def get_data(self):
		return self.__data

'''
Class: DataAttr
Parameters: category, list of related categories
Purpose: This is used to describe the data being kept
The only two things I can think of right now is category and related cateories
I could possibly add tags but related basically means the same
'''
class DataAttr:
	def __init__(self, category, *args): #everything after category is related
		self.set_category(category)
		self.set_related(*args)

	def set_category(self,category):
		self.__category = category
	
	def set_related(self,*args):
		for related in args
		self.__related.append(related)

	def get_category(self):
		return self.__category

	def get_related(self):
		return self.__related


'''
Class: DataContainer
Parameters: fileName, start, stop, Data object, DataAttr object
Purpose: To keep information about the data being stored
'''
class DataContainer:
	
	def __init__(self, file_name, start, stop, data_object, data_attribute):
		self.set_file_name(file_name)
		self.set_start(start)
		self.set_stop(stop)
		self.set_o_data(data_object)
		self.set_o_data_attribute(data_attribute)

	def set_file_name(self, file_name):
		self.__file_name = file_name

	def set_start(self,start):
		self.__start = start

	def set_stop(self,stop):
		self.__stop = stop

	def set_o_data(self,data):
		self.__data_object = data_object

	def set_o_data_attribute(self,data_attribute):
		self,__data_attribute = data_attribute


'''
Function: writeDate
Parameters: a file and data stream
Return: a Data object
Purpose: the function takes a file and data stream, writes the data to the file
then finds the start and end line of the data and creates a data object to
be used somewhere else
'''
def writeData(fileName,data):
	file = open(fileName, 'a')
	start = file.tell() # note starts from here
	file.write(data)
	stop = file.tell() # note ends here
	file.close()
	print start, stop
	
'''
Function: readData
Parameters: fileName and a Data object
Returns: data
Purpose: the function will take a Data object and read data stored in a file
The data is probably a string or data stream
'''
def readData(fileName, oData):
	file = open(fileName, 'r')
	file.seek(oData.start)
	data = file.read(oData.stop-oData.start)
	print data
