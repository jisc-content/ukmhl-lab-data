import csv

class LabCSVReader(object):
	"""
		Simple wrapper class around csv, that sets up a CSV reader for the 
		lab day CSV files.
	"""
	csv_file = None
	csv_reader = None
	
	def __init__(self, csv_filename,fieldnames = None):
			self.csv_file = open(csv_filename,"rb")
			self.csv_reader = csv.DictReader(self.csv_file,fieldnames=fieldnames, delimiter=',', quotechar='"')
			self.csv_reader.next() #skip header
			
	def next(self):
		try: 
			return self.get_row(self.csv_reader.next())
		except csv.Error:
			return None
		except StopIteration:
			return None

	def get_row(self,row):
		return row

	def reader(self):
		return self.csv_reader

	def close(self):
		self.csv_file.close()

lab_csv_reader = LabCSVReader("/Users/danielneedham/projects/ukmhl/ukmhl-lab-data-compressed/tools/input.txt")
while(True):
	row = lab_csv_reader.next()
	if row == None:
		break
	print row
lab_csv_reader.close()