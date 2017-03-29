import xml.etree.ElementTree as ET

# output class for displaying words

class Output():

	def __init__(self, base):
		self.responses = base.responses #dictionary of responses

	def write_to_file(self, filename):
		"""output words to a text file"""
		with open(filename, 'r') as f:
			f.write()

	def show_all(self):
		"""display all words"""
		for word, response in self.responses.items():
			self.show(word, response)

	def show(self, word, response):
		"""display word meaning on screen"""
		root = ET.fromstring(response.content)
		print('{}: {}\n'.format(word.strip().upper(), root[0].find('def').find('dt').text[1:]))
