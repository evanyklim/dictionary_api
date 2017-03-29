import xml.etree.ElementTree as ET

# output class for displaying words

class Output():

	def __init__(self, base):
		self.definitions = self.organize_xml(base.responses) #dictionary of responses

	def write_to_file(self, filename):
		"""output words to a text file"""
		with open(filename, 'r') as f:
			f.write()

	def show_all(self):
		"""display all words"""
		for word, definitions in self.definitions.items():
			self.show(word, definitions)

	def show(self, word, definitions):
		"""display word definitions on screen"""
		print('{}:\n'.format(word.strip().upper()))
		for i, d in enumerate(definitions, 1):
			print('{}. {}'.format(i, d))
		print('\n')

	def organize_xml(self, responses):
		"""organize xml and parse word definitions"""
		return {w: self.extract_definitions(d) for w, d in responses.items()}

	def extract_definitions(self, response):
		"""extract definitions from xml and return them in a list"""
		root = ET.fromstring(response.content)
		return [tag.text.strip(':') for tag in root.iter('dt') if len(tag.text) > 1]
