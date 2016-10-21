from labcsvreader import LabCSVReader
from publicationrow import PublicationRow
class PublicationCSVReader(LabCSVReader):
    def __init__(self,csv_filename):
        super(PublicationCSVReader, self).__init__(csv_filename,PublicationRow.publication_fields)

    def get_row(self,row):
		publication_row = PublicationRow(row)
		return publication_row

publication_csv_reader = PublicationCSVReader("/Users/danielneedham/tmp/sample/anatomy/publications.csv")
while(True):
	row = publication_csv_reader.next()
	if row == None:
		break
	print row.entries["identifiers"]
publication_csv_reader.close()