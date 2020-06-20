# geolocation (ip to location)
import geocoder
# Kara Weather
from Core.Abilities.Kara_Weather.weather import forcast, sunFormat


# weather at a location
def weather(Kara, command):
    # get current location from ip
    g = geocoder.ip('me')

    # pass city
    data = forcast(g.city, days=1)

    # ie. light showers
    weatherState = data['weather'][0]['weather']

    # "Today in brisbane you can expect light rain"
    line = 'Today in {} you can expect {}'.format(g.city, weatherState)
    Kara.speak(line)


# time of sunrise
def sunrise(Kara, command):
    # get current location from ip
    g = geocoder.ip('me')

    # pass city
    data = forcast(g.city, days=1)

    # format sun time data better
    time = sunFormat(data['sun_rise'])

    # period of the day (AM or PM)
    period = 'AM'

    # not morning
    if int(time[:2]) >= 12:
        # convert from 24h time
        time = str(int(time[:2]) % 12) + time[2:]
        # change period
        period = 'PM'

    # 05:55 -> 5:55
    if time[0] == '0':
        time = time[1:]


    # "Today in brisbane the sun will rise at 4:29AM"
    line = 'Today in {} the sun will rise at {}{}'.format(g.city, time, period)
    Kara.speak(line)

# time of sunrise
def sunset(Kara, command):
    # get current location from ip
    g = geocoder.ip('me')

    # pass city
    data = forcast(g.city, days=1)

    # format sun time data better
    time = sunFormat(data['sun_set'])

    # period of the day (AM or PM)
    period = 'AM'

    # not morning
    if int(time[:2]) >= 12:
        # convert from 24h time
        time = str(int(time[:2]) % 12) + time[2:]
        # change period
        period = 'PM'

    # 05:55 -> 5:55
    if time[0] == '0':
        time = time[1:]


    # "Today in brisbane the sun will set at 5:36PM"
    line = 'Today in {} the sun will set at {}{}'.format(g.city, time, period)
    Kara.speak(line)


# get air pressure (lol)
def airPressure(Kara, command):
    # get current location from ip
    g = geocoder.ip('me')

    # pass city
    data = forcast(g.city, days=1)

    # get air pressure
    pressure = data['weather'][0]['air_pressure']

    # "Today in brisbane the average air pressure will be 1023.5 millibars"
    line = 'Today in {} the average air pressure will be {} millibars'.format(
           g.city, pressure)
    Kara.speak(line)
