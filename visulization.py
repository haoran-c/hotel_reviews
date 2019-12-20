import folium
import json
import requests
import pandas as pd
import webbrowser

data = {}
with open('data/applause_rate.json', newline='', encoding='utf8') as f:
    data = json.loads(f.read())
states = {}
for index in data:
    state = data[index]['state']
    if len(state) == 2:
        total = data[index]['number of reviews']
        applauds = data[index]['number of reviews'] * data[index]['applause rate']
        if state not in states:
            states[state] = {'number of reviews': total, 'number of applauds': applauds}
        else:
            states[state]['number of reviews'] += total
            states[state]['number of applauds'] += applauds
rating = {}
for state in states:
    percentage = 100 *states[state]['number of applauds'] / states[state]['number of reviews']
    if percentage == 0:
        continue
    rating[state] = percentage

# initialize a us map
us_map = folium.Map(location=[35, -95], zoom_start=4)
# fetch geo json file of the states in the us
url = 'https://raw.githubusercontent.com/python-visualization/folium/master/examples/data'
us_states = f'{url}/us-states.json'
us_geo = json.loads(requests.get(us_states).text)
train = pd.DataFrame.from_dict(rating, orient='index')
train.reset_index(level=0, inplace=True)
bins = list(train[0].quantile([0, 0.2, 0.4, 0.6, 0.75, 0.86, 0.92, 1]))
# render a map of each state's average applause rate
folium.Choropleth(
    geo_data=us_geo,
    data=rating,
    columns=['State', 'Rating'],
    key_on='feature.id',
    fill_color='YlOrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    bins=bins,
    legend_name='Avg. Hotel Applause Rate(%)'
).add_to(us_map)

# save the world map to an html file
us_map.save('map.html')
webbrowser.open('map.html')
