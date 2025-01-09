from datetime import datetime
import re

class PressEntryStringParser:
    
    def __init__(self, content_string):
        self.links = []
        self.description = []
        self.date = datetime.min
        self.date_string = ""
        self.content_string = ""
        self.lines = []
        self.date_regex = "\((\d{4})\/(\d{2})\/(\d{2})\)"
        self.regex = re.compile(self.date_regex)
        self.content_string = content_string
        self.lines = content_string.splitlines()
        self.processed_lines = 0


    def parse(self):
        self.extract_and_parse_date()
        self.extract_description()
        self.extract_urls()

    def extract_and_parse_date(self):
        match = self.regex.match(self.lines[0])
        self.date_string = match.group()

        print("Year: " + match.group(1))
        print("Month: " + match.group(2))
        print("Day: " +  match.group(3))

        year = self.parse_to_int(match.group(1))
        month = self.parse_to_int(match.group(2))
        day = self.parse_to_int(match.group(3))

        self.date = datetime(year, month, day)
        
    def parse_to_int(self, string):
        return int(string)

    def extract_description(self):
        description_start_index = self.content_string.index(self.date_string) + len(self.date_string) + 1
        if len(self.lines) > 1:
            while self.is_not_last_description_text(description_start_index):
                print(self.lines[self.processed_lines][description_start_index:])
                self.description.append(self.lines[self.processed_lines][description_start_index:])
                description_start_index = 0
                self.processed_lines += 1
        else:
            description_end_index = self.content_string.index("http")
            self.description.append(self.lines[self.processed_lines][description_start_index:description_end_index])
            delimiter = "http"
            urls = [delimiter + x for x in self.lines[0].split(delimiter)[1:] if x]
            self.lines[len(self.lines):] = urls
            self.processed_lines += 1

    def is_not_last_description_text(self, description_start_index):
        return not self.lines[self.processed_lines][description_start_index:].startswith("http")

    def extract_urls(self):
        number_of_urls = len(self.lines)
        for i in range(self.processed_lines, number_of_urls):
            self.links.append(self.lines[i])
