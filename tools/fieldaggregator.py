from publicationcsvreader import PublicationCSVReader

class FieldAggregator(object):

	def aggregate_field(self, file, field):
		field_map = {}
		publication_csv_reader = PublicationCSVReader(file)
		while(True):
			row = publication_csv_reader.next()
		
			if row == None:
				break
			field_values = row.entries[field]
			for field_value in field_values:
				if field_value in field_map:
					field_map[field_value] +=1
				else:
					field_map[field_value] = 1
		publication_csv_reader.close()
		return field_map

field_aggregator = FieldAggregator()
print field_aggregator.aggregate_field("/Users/danielneedham/tmp/sample/anatomy/publications.csv","dimensions")

		

