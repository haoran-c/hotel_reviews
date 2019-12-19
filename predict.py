from joblib import dump, load
import json

clf = load('classifiers/SvmClassifier.jbl')
vec = load('classifiers/vectorizer.jbl')

with open("data/data_set.json", "r") as read_file:
    data = json.loads(read_file.read())
    num = len(data)
    for index in data:
        i = int(index)
        print("\rProcessing %d out of %d hotels, progress: %d%%" % (i, num, int(100*i/num)), end="")
        entry = data[index]
        total = len(entry['reviews'])
        positive = 0.0
        for text in entry['reviews']:
            if clf.predict(vec.transform([text])) == 1:
                positive += 1
        del entry['reviews']
        data[index]['number of reviews'] = total
        data[index]['applause rate'] = positive/total

with open("data/applause_rate.json", "w") as write_file:
    json.dump(data, write_file, indent=4)
