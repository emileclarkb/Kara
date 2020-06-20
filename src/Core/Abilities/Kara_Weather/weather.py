# native
import argparse
import requests
import json


meta = 'https://www.metaweather.com/api/'
location = meta + 'location/search/'
info = meta + 'location/{}/'



# get the weather for the next 5 days
def forcast(query, days=1, log=False):
	# get location id
	IDdata = requests.get(url=location, params={'query': query}).json()
	# return id
	id = IDdata[0]['woeid']

	# get weather data
	data = requests.get(info.format(id)).json()

	# store imporant data from metaweather
	formatted = {}
	# transfer data
	formatted['location'] = data['title']
	formatted['sun_rise'] = data['sun_rise']
	formatted['sun_set'] = data['sun_set']
	formatted['weather'] = []

	# tansfer days data
	for day in data['consolidated_weather'][:days]:
		# data to remove
		rm = ['created', 'id', 'predictability', 'the_temp', 'wind_direction',
			  'weather_state_abbr', 'wind_direction_compass']

		# remove unimportant attributes
		for key in rm:
			# remove data
			del day[key]

		# rename data for easier usage
		day['date'] = day.pop('applicable_date')
		day['weather'] = day.pop('weather_state_name')

		# add to formatted data
		formatted['weather'].append(day)

	# log data to file
	if log:
		# write to file
		with open(log, 'w') as file:
			# write json neatly
			json.dump(formatted, file,
					  sort_keys=True, indent=4, separators=(',', ': '))

	return formatted

#forcast('brisbane', log='data.json')
