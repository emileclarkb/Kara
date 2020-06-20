# geolocation (ip to location)
import geocoder
# Kara Weather
from Core.Abilities.Kara_Weather.weather import forcast


def weather(Kara, command):
    # get current location from ip
    g = geocoder.ip('me')

    # pass city
    data = forcast(g.city, days=1)

    line = 'Today in ' + g.city + 'you can expect ' + data['weather'][0]['weather']
    # in brisbane you can expect light rain
    Kara.speak(line)
