#
# ---------------------------------------------
# Open Weather
# ---------------------------------------------
# Author: Adam Blaszczyk
#         http://wyciekpamieci.blogspot.com
# Date:   2021-12-15
# ---------------------------------------------
#
# Requirements:
#         - Python 3.x
#

# http://api.openweathermap.org/data/2.5/weather?q=Warsaw&units=metric&appid=5ef52906ea9fb13f1ab8649c9018bb09

from urllib import request
import json
import time
 
def unix_to_local_time(t):
    return time.strftime("%Y-%m-%d %H:%M", time.localtime(int(t)))

url = "http://api.openweathermap.org/data/2.5/weather?q="

#city = input("Please enter a city: ")
city = 'Warsaw'

apikey = "5ef52906ea9fb13f1ab8649c9018bb09"

print()
url2 = url + city + "&units=metric&appid=" + apikey
print(url2)

city_weather = request.urlopen(url2)
data_weather = city_weather.read()
data = json.loads(data_weather.decode())

# ---ALL JSON DATA-------------------------------------------------------------
print()
print("--- JSON DATA ----------------------------------------------------")
print()
print("coord:")
print("    lon = %s" %data['coord']['lon'])
print("    lat = %s" %data['coord']['lat'])
print("weather:")
print("    0:")
print("        id          = %s" %data['weather'][0]['id'])
print("        main        = %s" %data['weather'][0]['main'])
print("        description = %s" %data['weather'][0]['description'])
print("        icon        = %s" %data['weather'][0]['icon'])
print("base = %s" %data['base'])
print("main:")
print("    temp       = %s [C]" %data['main']['temp'])
print("    feels_like = %s [C]" %data['main']['feels_like'])
print("    temp_min   = %s [C]" %data['main']['temp_min'])
print("    temp_max   = %s [C]" %data['main']['temp_max'])
print("    pressure   = %s [hPa]" %data['main']['pressure'])
print("    humidity   = %s  [%%]" %data['main']['humidity'])
print("visibility = %s" %data['visibility'])
print("wind:")
print("    speed = %s [m/s]" %data['wind']['speed'])
print("    deg   = %s [degrees]" %data['wind']['deg'])
print("    gust  = %s [m/s]" %data['wind']['gust'])
print("rain:")
try:
    print("    1h = %s" %data['rain']['1h'])
except:
    pass
try:
    print("    3h = %s" %data['rain']['3h'])
except:
    pass
print("snow:")
try:
    print("    1h = %s" %data['snow']['1h'])
except:
    pass
try:
    print("    3h = %s" %data['snow']['3h'])
except:
    pass
print("clouds:")
print("    all = %s [%%]" %data['clouds']['all'])
print("dt = %s [unix UTC]" %data['dt'])
print("sys:")
print("    type    = %s" %data['sys']['type'])
print("    id      = %s" %data['sys']['id'])
print("    country = %s" %data['sys']['country'])
print("    sunrise = %s [unix UTC]" %data['sys']['sunrise'])
print("    sunset  = %s [unix UTC]" %data['sys']['sunset'])
print("timezone = %s [s]" %data['timezone'])
print("id       = %s" %data['id'])
print("name     = %s" %data['name'])
print("cod      = %s" %data['cod'])

print()
print("------------------------------------------------------------")
print()

# ----------------------------------------------------------------------------

city1 = data['name']
t = unix_to_local_time(data['dt'])
weather_description = data['weather'][0]['description']

temp = data['main']['temp']
humidity = data['main']['humidity']
pressure = data['main']['pressure']
wind = data['wind']['speed']
clouds = data['clouds']['all']
sunrise = unix_to_local_time(data['sys']['sunrise'])
sunset = unix_to_local_time(data['sys']['sunset'])

print ("Current weather in %s (%s): %s" %(city1, t, weather_description),
        "\nTemperature : %s C" %temp,
        "\nHumidity    : %s %%" %humidity,
        "\nPressure    : %s hPa" %pressure,
        "\nWind        : %s m/s" %wind,
        "\nClouds      : %s %%" %clouds,
        "\nSunrise     : %s" %sunrise,
        "\nSunset      : %s" %sunset)

city_weather.close()

print()
