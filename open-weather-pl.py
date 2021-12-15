#
# ---------------------------------------------
# Open Weather - PL version
# ---------------------------------------------
# Author: Adam Blaszczyk
#         http://wyciekpamieci.blogspot.com
# Date:   2021-12-15
# ---------------------------------------------
#
# Requirements:
#         - Python 3.x
#

# http://api.openweathermap.org/data/2.5/weather?q=Warsaw&units=metric&lang=pl&appid=5ef52906ea9fb13f1ab8649c9018bb09

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
url2 = url + city + "&units=metric&lang=pl&appid=" + apikey
print(url2)

city_weather = request.urlopen(url2)
data_weather = city_weather.read()
data = json.loads(data_weather.decode())

# ---ALL JSON DATA-------------------------------------------------------------
print()
print("--- JSON DATA ----------------------------------------------------")
print()
print("coord:")
print("    lon = %s   <-- dlugosc geograficzna" %data['coord']['lon'])
print("    lat = %s   <-- szerokosc geograficzna" %data['coord']['lat'])
print("weather:")
print("    0:")
print("        id          = %s   <-- id?" %data['weather'][0]['id'])
print("        main        = %s   <-- rodzaj pogody" %data['weather'][0]['main'])
print("        description = %s   <-- warunki pogodowe" %data['weather'][0]['description'])
print("        icon        = %s   <-- ikona obrazujaca pogode" %data['weather'][0]['icon'])
print("base = %s   <-- INTERNAL PARAMETER" %data['base'])
print("main:")
print("    temp       = %s   <-- temperatura [C]" %data['main']['temp'])
print("    feels_like = %s   <-- temperatura odczuwana [C]" %data['main']['feels_like'])
print("    temp_min   = %s [C]" %data['main']['temp_min'])
print("    temp_max   = %s [C]" %data['main']['temp_max'])
print("    pressure   = %s   <-- cisnienie [hPa]" %data['main']['pressure'])
print("    humidity   = %s   <-- wilgotnosc powietrza [%%]" %data['main']['humidity'])
print("visibility = %s" %data['visibility'])
print("wind:")
print("    speed = %s   <-- predkosc wiatru [m/s]" %data['wind']['speed'])
print("    deg   = %s   <-- kierunek wiatru [stopnie]" %data['wind']['deg'])
print("    gust  = %s   <-- porywy wiatru [m/s]" %data['wind']['gust'])
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
print("    all = %s   <-- zachmurzenie [%%]" %data['clouds']['all'])
print("dt = %s   <-- data i czas [unix UTC]" %data['dt'])
print("sys:")
print("    type    = %s   <-- INTERNAL PARAMETER" %data['sys']['type'])
print("    id      = %s   <-- INTERNAL PARAMETER" %data['sys']['id'])
print("    country = %s   <-- kod kraju" %data['sys']['country'])
print("    sunrise = %s   <-- wschod slonca [unix UTC]" %data['sys']['sunrise'])
print("    sunset  = %s   <-- zachod slonca [unix UTC]" %data['sys']['sunset'])
print("timezone = %s   <-- przesuniecie w sekundach wzgledem UTC (strefa czasowa)" %data['timezone'])
print("id       = %s   <-- ID miejscowosci" %data['id'])
print("name     = %s   <-- nazwa miejscowosci" %data['name'])
print("cod      = %s   <-- INTERNAL PARAMETER" %data['cod'])

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

print ("Aktualna pogoda w miejscowosci %s (%s): %s" %(city1, t, weather_description),
        "\nTemperatura          : %s C" %temp,
        "\nWilgotnosc powietrza : %s %%" %humidity,
        "\nCisnienie            : %s hPa" %pressure,
        "\nWiatr                : %s m/s" %wind,
        "\nZachmurzenie         : %s %%" %clouds,
        "\nWschod slonca        : %s" %sunrise,
        "\nZachod slonca        : %s" %sunset)

city_weather.close()

print()
