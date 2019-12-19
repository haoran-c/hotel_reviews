import json
import csv

json_data = {}

with open('data/Datafiniti_Hotel_Reviews.csv', 'r', newline='', encoding='utf-8') as csvfile:
    raw_reader = csv.reader(csvfile, delimiter=',')
    count = 0
    for row in raw_reader:
        if count == 0:
            count += 1
            continue
        text = row[16]
        rating = row[14]
        label = 0
        if float(rating) >= 4:
            label = 1
        json_data[count] = (text, label)
        count += 1

with open("data/train_set.json", "w") as write_file:
    json.dump(json_data, write_file, indent=4)
