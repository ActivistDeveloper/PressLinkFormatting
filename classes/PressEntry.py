from datetime import datetime
from classes.PressEntryStringParser import PressEntryStringParser
from json import JSONEncoder

class PressEntry:

    def __init__(self, content_string):
        self.date = datetime.min
        self.links = []
        self.description = ""
        self.content_string = ""
        self.content_string = content_string
        self.parser = PressEntryStringParser(content_string)

        self.initialize_from_content_string()
        
    def initialize_from_content_string(self):
        self.parser.parse()
        self.date = self.parser.date
        self.description = self.parser.description
        
        self.links = self.parser.links