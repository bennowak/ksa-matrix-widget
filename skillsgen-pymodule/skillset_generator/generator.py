# skillset_generator.generator.py

import csv
import json



def parse_csv_file(csvpath):
    entries = []
    candidate = {"skills": []}
    with open(csvpath, 'r') as csvfile:

        csvreader = csv.reader(csvfile, skipinitialspace=True, delimiter=',')

        csvheader = next(csvreader)

        for row in csvreader:
            entries.append(row)

    temp_list = []
    for entry in entries:
        temp_list.append(entry[0])
    s = set(temp_list)

    for domain in s:
        temp_dict = {domain: []}
        candidate["skills"].append(temp_dict)

    for entry in entries:
        for domain in candidate["skills"]:
            # ToDo: Figure how to get keys and compare against entry
            if entry[1] == domain.items():
                domain[entry[1]].append(
                    {entry[2]: {"certifiable": entry[3], "agency": entry[4], "agency_url": entry[5]}}
                )
    return candidate


def write_to_json(json_objet, output_path):
    with open(output_path, 'w', newline='') as jsonfile:

        jsonfile.write(json.dumps(json_objet, indent=2))


# WORKING IMPLEMENTATION
# def parse_csv_file(csvpath):
#     entries = []
#     domains = {}
#     with open(csvpath, 'r') as csvfile:
#
#         csvreader = csv.reader(csvfile, skipinitialspace=True, delimiter=',')
#
#         csvheader = next(csvreader)
#
#         for row in csvreader:
#             entries.append(row)
#     for entry in entries:
#
#         # if domain is not in the list
#         if not entry[0] in domains:
#
#             # add domain to the list
#             domains[entry[0]] = {}
#
#         # iterate through the domains and seed the categories
#         if not entry[1] in domains[entry[0]]:
#             # domains[entry[0]][entry[1]] = []
#             domains[entry[0]][entry[1]] = []
#         # add entry to the dictionary
#         domains[entry[0]][entry[1]].append(
#             {entry[2]: {"certifiable": entry[3], "agency": entry[4], "agency_url": entry[5]}})
#     return domains
