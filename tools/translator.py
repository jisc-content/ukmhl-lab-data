from yandex_translate import YandexTranslate

class Translator(object):

	"""
		Wrapper around the Yandex translate API package.

		Provides methods for determining whether a text is english, and translating it english if not.

	"""

	translator = None

	def __init__ (self, api_key):
		self.translator = YandexTranslate(api_key)


	def translator(self):
		"""
			Returns:
				YandexTranslate: the initialised YandexTranslate instance
		"""
		return self.translator
	
	def is_english(self, input_text):
		"""
			Use the translator to determine whether the input text is English.
			If it is then returns True, otherwise it returns the detected language 
			type.

			Returns:
				True if english, otherwise language string if not english.
		"""
		language = self.translator.detect(input_text)
		if language == "en":
			return True
		return language

	def translate(self, input_text):
		"""
			Translates the input text into English.

			Returns:
				str: The translated text
		"""
		return self.translator.translate(input_text, "en")
		

