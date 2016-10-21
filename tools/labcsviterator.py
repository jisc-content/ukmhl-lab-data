import csv

class LabCSVIterator(object):
	"""
		Simple wrapper class around csv, that sets up a CSV reader for the 
		lab day CSV files.
	"""
	csv_file = None
	csv_reader = None
	
	def __init__(self, csv_filename):
			self.csv_file = open(csv_filename,"rb")
			self.csv_reader = csv.DictReader(self.csv_file, delimiter=',', quotechar='"')

	def next(self):
		return self.csv_reader.next()

	def reader(self):
		return self.csv_reader

	def close(self):
		self.csv_file.close()
