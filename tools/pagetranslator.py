import os
import os.path
import pagetranslator_config
from labcsvhandler import LabCSVHandler
from translator import Translator

class PageTranslator(object):
	"""
		Provides methods for translating the text of each page belonging to a publicaiton, into English.
	"""

	translator = None

	def __init__(self, api_key):
		self.translator = Translator(api_key)

	def translate_page(self, input_filepath, output_file_path, output_file_name):
		"""
			Reads in text from the input file, and then uses the Translator to determine
			whether the language is english or not. If not then it uses the Translator
			to acquire an english language version and save it to the output file.

			Args:
        	input_filepath (str): The input page text file
        	output_file_path (str): The output directory path
        	output_file_name (str): The name of the file to save the translated text to
		"""
		if os.path.exists(output_file_path+output_file_name):
			return
		with open(input_filepath, 'r') as input_file:
			page_text = input_file.read()
			is_english = self.translator.is_english(page_text)
	    	if is_english != True:
	    		print "["+is_english+"]"+input_filepath + " ---> " + output_file_path + output_file_name
	    		translation = self.translator.translate(page_text)
	    		if not os.path.exists(output_file_path):
	    			os.makedirs(output_file_path)
	    		with open(output_file_path + output_file_name, 'w') as output_file:
	    			output_file.write(str(translation['text']))

	def translate_publications(self, working_directory, translation_directory, input_file):	
		"""
			Iterates through in input csv containing ukmhl identifiers and then 
			iterates through the page text files for each publication, using translate_page
			to attempt to translate the page text if required.

			Args:
        	input_file (str): The input csv file containing a list of ukmhl identifiers to process
		"""
		lab_csv_handler = LabCSVHandler(input_file)
		for row in lab_csv_handler.reader():
			publication_directory = working_directory + row['id'] + "/pages/"
			for page_file in os.listdir(publication_directory ):
				translation_path = translation_directory + row['id'] + "/translations/"
				self.translate_page(publication_directory + page_file, translation_path, page_file)
		lab_csv_handler.close()

page_translator = PageTranslator(pagetranslator_config.translator_api['key'])
page_translator.translate_publications(pagetranslator_config.paths['working_directory'],
	pagetranslator_config.paths['translation_directory'],
	pagetranslator_config.paths['input_file'])

