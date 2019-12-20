import csv
import json
import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd


abbr = {'Alabama': 'AL',
        'Alaska': 'AK',
        'American Samoa': 'AS',
        'Arizona': 'AZ',
        'Arkansas': 'AR',
        'California': 'CA',
        'Colorado': 'CO',
        'Connecticut': 'CT',
        'Delaware': 'DE',
        'District of Columbia': 'DC',
        'Federated States Of Micronesia': 'FM',
        'Florida': 'FL',
        'Georgia': 'GA',
        'Guam': 'GU',
        'Hawaii': 'HI',
        'Idaho': 'ID',
        'Illinois': 'IL',
        'Indiana': 'IN',
        'Iowa': 'IA',
        'Kansas': 'KS',
        'Kentucky': 'KY',
        'Louisiana': 'LA',
        'Maine': 'ME',
        'Marshall Islands': 'MH',
        'Maryland': 'MD',
        'Massachusetts': 'MA',
        'Michigan': 'MI',
        'Minnesota': 'MN',
        'Mississippi': 'MS',
        'Missouri': 'MO',
        'Montana': 'MT',
        'Nebraska': 'NE',
        'Nevada': 'NV',
        'New Hampshire': 'NH',
        'New Jersey': 'NJ',
        'New Mexico': 'NM',
        'New York': 'NY',
        'North Carolina': 'NC',
        'North Dakota': 'ND',
        'Northern Mariana Islands': 'MP',
        'Ohio': 'OH',
        'Oklahoma': 'OK',
        'Oregon': 'OR',
        'Palau': 'PW',
        'Pennsylvania': 'PA',
        'Puerto Rico': 'PR',
        'Rhode Island': 'RI',
        'South Carolina': 'SC',
        'South Dakota': 'SD',
        'Tennessee': 'TN',
        'Texas': 'TX',
        'Utah': 'UT',
        'Vermont': 'VT',
        'Virgin Islands': 'VI',
        'Virginia': 'VA',
        'Washington': 'WA',
        'West Virginia': 'WV',
        'Wisconsin': 'WI',
        'Wyoming': 'WY'
        }

populations = {}
with open('data/population_estimate.csv', 'r', encoding='utf8') as csvfile:
    raw_reader = csv.reader(csvfile, delimiter=',')
    count = 0
    for row in raw_reader:
        name = abbr[row[0]]
        population = int(row[1])
        populations[name] = population
ratings = {}
with open('data/state_ratings.json', 'r', encoding='utf8') as f:
    data = json.loads(f.read())
    for state in data:
        ratings[state] = (data[state], populations[state])
train = pd.DataFrame.from_dict(ratings, orient='index')
train.reset_index(level=0, inplace=True)
x = np.array(train[0]).reshape(-1, 1)
y = np.array(train[1]).reshape(-1, 1)
regr = LinearRegression()
regr.fit(x, y)
print(regr.score(x, y))
