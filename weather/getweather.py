#!/usr/bin/env python
import pyowm
import json 

owm = pyowm.OWM('xxx')  #todo: You MUST provide a valid API key
observation = owm.weather_at_place('Fishers,US')
w = observation.get_weather()
forecast = owm.daily_forecast('Fishers,US',limit=1).get_forecast()
j = json.loads(forecast.to_JSON())

output = dict()
output['windspeed'] = w.get_wind('miles_hour')['speed']
output['winddirection'] = int(w.get_wind('miles_hour')['deg'])
output['humidity'] = w.get_humidity()
output['temperature'] = round(w.get_temperature('fahrenheit')['temp'],1)
output['maxtemperature'] = round(((j['weathers'][0]['temperature']['max']*9/5)-459.67),1)
output['mintemperature'] = round(((j['weathers'][0]['temperature']['min']*9/5)-459.67),1)

f = open("/home/pi/proj/weather.txt","w")
f.write(str(output))

#print(w)           
#print(w.get_wind('miles_hour')) # {'speed': 4.6, 'deg': 330}
#print(w.get_humidity()) # 87
#print(w.get_temperature('fahrenheit'))  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
#print(w.get_heat_index()) #{u'speed': 9.171454, u'deg': 230}


