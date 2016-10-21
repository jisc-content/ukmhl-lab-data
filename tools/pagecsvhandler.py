from labcsvhandler import LabCSVHandler
class PageCSVHandler(LabCSVHandler):
	page_fields = ["id","record","sequence","page number","group","thumb","zoom","illustrations"]
	def __init__(self, csv_filename):
		LabCSVHandler.__init__(self, csv_filename, page_fields)