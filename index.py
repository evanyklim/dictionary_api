from base import Base
from output import Output
	
dictionary = Base('words.txt')
dictionary.get_all()

display = Output(dictionary)
display.show_all()