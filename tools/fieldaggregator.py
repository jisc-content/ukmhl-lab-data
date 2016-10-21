from publicationcsvreader import PublicationCSVReader
import operator

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
				field_value = self.normalise_value(field_value)
				if field_value in field_map:
					field_map[field_value] +=1
				else:
					field_map[field_value] = 1
		publication_csv_reader.close()
		return field_map

	def normalise_value(self, value):
		return value

	def sort_aggregated_fields(self,aggregated_fields):
		return sorted(aggregated_fields.items(), key=operator.itemgetter(1), reverse=True)


