import sys
import json
from classes.PressEntry import PressEntry
from classes.DefaultPressEntryRenderer import DefaultPressEntryRenderer

press_articles = []
current_article_content = ""

filepath_input = sys.argv[1]
print("Start reading file:" + filepath_input)
file = open(filepath_input)
content = file.readlines()

filepath_output = sys.argv[2]

header_content = ""
if(len(sys.argv) > 3):
    filepath_header = sys.argv[3]
    header_file = open(filepath_header)
    header_content = ''.join(header_file.readlines())


def create_press_entry():
    global current_article_content
    press_articles.append(PressEntry(current_article_content))
    current_article_content = ""

for line in content:
    
    if not line.isspace():
            current_article_content += line
            
    if line.isspace():
        create_press_entry()

if len(current_article_content) > 0:
    create_press_entry()

sorted_entries = sorted(press_articles, key=lambda x: x.date, reverse= True)

renderer = DefaultPressEntryRenderer()

output = header_content
output += "\n"

for entry in sorted_entries:
    output += renderer.render(entry)
    output += "\n"

output_file = open(filepath_output, 'w')
output_file.writelines(output)

print()
print("############ Wrote to " + filepath_output + ": ##############")
print(output, '')



