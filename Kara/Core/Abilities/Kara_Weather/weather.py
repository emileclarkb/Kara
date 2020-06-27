# native
import requests
import json
import os


meta = 'https://www.metaweather.com/api/'
location = meta + 'location/search/'
info = meta + 'location/{}/'



# get the weather for the next 5 days
def forcast(query, days=1, log=False):
	# get location id
	IDdata = requests.get(url=location, params={'query': query}).json()
	try:
		# return id
		id = IDdata[0]['woeid']
	except IndexError:
		return 1

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

	# get path
	path = os.path.dirname(os.path.abspath(__file__))

	# log data to file
	if log:
		# write to file
		with open(path + '/' + log, 'w') as file:
			# write json neatly
			json.dump(formatted, file,
					  sort_keys=True, indent=4, separators=(',', ': '))

	return formatted

# format sun rise or sunset to time
# "2020-06-20T06:37:35.157116+10:00" -> "06:37"
def sunFormat(time):
	# begin splitting
	time = time.split('T')[-1]
	# get first to parts of time
	time = time.split(':')[:2]

	return ':'.join(time)
