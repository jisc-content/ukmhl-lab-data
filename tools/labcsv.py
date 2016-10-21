import re
def join_field_list(fields):
	return str.join("|",fields)

def split_field_list(field):
	return field.split("|")

def split_typed_field_list(field):
	typed_fields = []
	fields = field.split("|")
	for field in fields:
		typed_fields.append(to_typed_field(field))
	return typed_fields

def from_typed_field(field):
	return "["+field['type']+"]"+field['value']

def from_typed_field(type, value):
	return "["+type+"]"+value

def to_typed_field(field):
	type =""
	value = ""
	field_match = re.match("\[(.*)\](.*)",field.strip())
	if field_match != None:
		if field_match.group(1) != None:
			type = field_match.group(1)
		if field_match.group(2) != None:
			value = field_match.group(2)
	else:
		value = field
	return {"type":type,"value":value}
