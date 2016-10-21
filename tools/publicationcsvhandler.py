from labcsvhandler import LabCSVHandler
class PublicationCSVHandler(LabCSVHandler):
	publication_fields = ["id","url","record","summary title","identifiers","collection","authors","publication dates", "publication places","publisher","volume","series dates","topics","notes","dimensions","extents", "page count","image count", "page numbers", "illustrated", "toc","thumb","pdf","epub","text","illustrations"]
	def __init__(self, csv_filename):
		LabCSVHandler.__init__(self, csv_filename, publication_fields)