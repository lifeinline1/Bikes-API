import requests
import json
from plotly.graph_objs import bar
from plotly import offline

url = 'http://api.citybik.es/v2/networks'

r = requests.get(url)
data = r.json()

bikes = len(data['networks'])
names = dict()

for bike in range(bikes):
    name = data['networks'][bike]['name']
    if name in names.keys():
        names[name] += 1
    else:
        names[name] = 1



sorted = (sorted( ((v,k) for k,v in names.items()), reverse=True))

company, locs = [], []

# Top 20 brands
for i in range(20):
    locs.append(sorted[i][0])
    company.append(sorted[i][1])


# Make visualization

data = [{
    'type': 'bar',
    'x': company,
    'y': locs,
    'marker': {
    'color': 'rgb(60, 100, 150)',
    'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,

}]

layout = {
    'title': 'Top 20 bikesharing brands using citybik.es API',
    'xaxis': {'title': 'Brands'},
    'yaxis': {'title': 'Number of locations'},
}

fig = {'data': data, 'layout': layout}
offline.plot(fig, filename='bikestations.html')
        
        



