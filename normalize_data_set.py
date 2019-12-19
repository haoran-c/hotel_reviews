import json
import csv
import zipcodes

json_data = {}

total = 0
with open('data/raw_data.csv', 'r', encoding='utf-8') as f:
    total = sum(1 for line in f)

with open('data/raw_data.csv', 'r', newline='', encoding='utf-8') as csvfile:
    raw_reader = csv.reader(csvfile, delimiter=',')
    line = 0
    id = 0
    for row in raw_reader:
        line += 1
        print("\rProcessing %d out of %d reviews, progress: %d%%" % (line, total, int(100*line/total)), end="")
        if id == 0:
            id += 1
            continue
        addr = row[0]
        city = row[2]
        name = row[6]
        postcode = row[7]
        state = row[8]
        if len(state) != 2:
            lookup = zipcodes.matching(postcode)
            if len(lookup) != 0:
                state = lookup[0]['state']
        text = row[14]
        visited = False
        for key in json_data.keys():
            if name == json_data[key]['name']:
                if postcode == json_data[key]['postcode']:
                    json_data[key]['reviews'].append(text)
                    visited = True
                    break
        if not visited:
            review = {'name': name, 'address': addr, 'city': city, 'state': state, 'postcode': postcode, 'reviews': [text]}
            json_data[id] = review
            id += 1

with open("data/data_set.json", "w") as write_file:
    json.dump(json_data, write_file, indent=4)

