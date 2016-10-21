from labcsvreader import LabCSVReader
from pagerow import PageRow
class PageCSVReader(LabCSVReader):
    def __init__(self,csv_filename):
        super(PageCSVReader, self).__init__(csv_filename)

    def get_row(self,row):
		page_row = PageRow(row)
		return page_row

page_csv_reader = PageCSVReader("/Users/danielneedham/tmp/sample/anatomy/pages/ukmhl-b2038810x/pages.csv")
while(True):
	row = page_csv_reader.next()
	if row == None:
		break
	print row.entries["illustrations"]
page_csv_reader.close()