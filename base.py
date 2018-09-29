import requests
# config parser for obtaining dictionary api key
import configparser
config = configparser.ConfigParser()
config.read('config.ini')

API_KEY = config['dictionary-api']['key']

# base class to connect to api
class Base():

	def __init__(self, input_path):
		self.path = 'http://www.dictionaryapi.com/api/v1/references/collegiate/xml/'
		self._input_path = input_path
		self.words = []
		self.responses = {}
		self.get_inputs()
		print('\nAPI is initiated...')

	def get_inputs(self):
		"""get the list of words from file"""
		with open(self._input_path, 'r') as f:
			for line in f:
				self.words.append(line.strip())

	def get_all(self):
		"""search the dictionary api for all words obtained by get_inputs"""
		for word in self.words:
			self.get(word)

	def get(self, word):
		"""search the dictionary api for the word"""
		url = self.path + word
		r = requests.get(url, params={'key': API_KEY})
		if r.status_code == requests.codes.ok:
			self.store(word, r)

	def store(self, word, response):
		"""store the word and response"""
		if word not in self.responses:
			self.responses[word] = response
