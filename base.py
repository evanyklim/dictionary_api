import requests

# base class to connect to api
class Base():

	def __init__(self, input_path):
		self.path = 'http://www.dictionaryapi.com/api/v1/references/collegiate/xml/'
		self.input_path = input_path
		self.words = []
		self.responses = {}
		self.payload = None
		self.get_inputs()
		self.get_keys()
		print('\nAPI is initiated')

	def get_keys(self):
		"""get auth keys from file"""
		with open('keys.txt', 'r') as f:
			for line in f:
				self.payload = {'key': line}

	def get_inputs(self):
		"""get the list of words from file"""
		with open('words.txt', 'r') as f:
			for line in f:
				self.words.append(line.strip())

	def get_all(self):
		"""search the dictionary api for all words obtained by get_inputs"""
		for word in self.words:
			self.get(word)

	def get(self, word):
		"""search the dictionary api"""
		url = self.path + word
		r = requests.get(url, params=self.payload)
		if r.status_code == requests.codes.ok:
			self.store(word, r)

	def store(self, word, response):
		"""store the word and response"""
		if word not in self.responses:
			self.responses[word] = response
