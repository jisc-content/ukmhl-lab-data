import csv

class LabCSVWriter(object):
	"""
		Simple wrapper class around csv, that sets up a CSV writer for the 
		lab day CSV files.
	"""
	csv_file = None
	csv_writer = None
	
	def __init__(self, csv_filename,fieldnames = None):
			self.csv_file = open(csv_filename,"rb")
			self.csv_writer = csv.DictWriter(self.csv_file,fieldnames=fieldnames, delimiter=',', quotechar='"')
			self.csv_writer.writeheader()

	def writer(self):
		return self.csv_writer

	def close(self):
		self.csv_file.close()

	def writerow(self,row):
		self.csv_writer.writerow(row)
	
