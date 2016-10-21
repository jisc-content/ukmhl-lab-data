import labcsv

class PageRow(object):
	page_fields = ["id","record","sequence","page number","group","thumb","zoom","illustrations"]
	entries = {field:"" for field in page_fields}

	def __init__(self,fields=None):
		if fields != None:
			self.entries['id'] = fields['id']
			self.entries['record'] = fields['record']
			self.entries['page number'] = fields['page number']
			self.entries['group'] = fields['group']
			self.entries['thumb'] = fields['thumb']
			self.entries['zoom'] = fields['zoom']
			self.entries['illustrations'] = labcsv.split_field_list(fields['illustrations']