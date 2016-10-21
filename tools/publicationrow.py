import labcsv
class PublicationRow(object):
	publication_fields = ["id","url","record","summary title","identifiers","collection","authors","publication dates", "publication places","publisher","volume","series dates","topics","notes","dimensions","extents", "page count","image count", "page numbers", "illustrated", "toc","thumb","pdf","epub","text","illustrations"]
	entries = {field:"" for field in publication_fields}

	def __init__(self,fields=None):
		if fields != None:
			self.entries['id'] = fields['id']
			self.entries['url'] = fields['url']
			self.entries['record'] = fields['record']
			self.entries['summary title'] = fields['summary title']
			self.entries['identifiers'] = labcsv.split_typed_field_list(fields['identifiers'])
			self.entries['collection'] = labcsv.split_field_list(fields['collection'])
			self.entries['authors'] = labcsv.split_field_list(fields['authors'])
			self.entries['publication dates'] = labcsv.split_field_list(fields['publication dates'])
			self.entries['publication places'] = labcsv.split_field_list(fields['publication places'])
			self.entries['publisher'] = labcsv.split_field_list(fields['publisher'])
			self.entries['volume'] = labcsv.split_field_list(fields['volume'])
			self.entries['series dates'] = labcsv.split_typed_field_list(fields['series dates'])
			self.entries['topics'] = labcsv.split_field_list(fields['topics'])
			self.entries['notes'] = labcsv.split_typed_field_list(fields['notes'])
			self.entries['dimensions'] = labcsv.split_field_list(fields['dimensions'])
			self.entries['extents'] = labcsv.split_field_list(fields['extents'])
			self.entries['page count'] = fields['page count']
			self.entries['image count'] = fields['image count']
			self.entries['page numbers'] = fields['page numbers']
			self.entries['illustrated'] = fields['illustrated']
			self.entries['toc'] = fields['toc']
			self.entries['thumb'] = fields['thumb']
			self.entries['pdf'] = fields['pdf']
			self.entries['epub'] = fields['epub']
			self.entries['text'] = fields['text']
			self.entries['illustrations'] = labcsv.split_field_list(fields['illustrations'])
