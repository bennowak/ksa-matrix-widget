import sys
import os

from skillset_generator import generator as jgen

csv_file = os.path.join('Resources', 'skillset.csv')
json_output = os.path.join('Output', 'skillset.json')
print((jgen.parse_csv_file(csv_file)))
# jgen.write_to_json(jgen.parse_csv_file(csv_file), json_output)
