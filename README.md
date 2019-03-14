# RaspberryPi
Assortment of pi related items

## garage
Chamberlain liftmaster API to be able to open the garage door, the default API for the door does not allow opening it from ifttt so had to make calls to the API that the android / ios app uses in order to be able to issue the door open command which in turn runs as a flask service on the raspberry pi so that ifttt can make custom calls to the service which allows me to execute the command via google assistant to say "open garage door".  This is not a default capability oddly enough: https://myqcommunity.chamberlain.com/chamberlainmyq/topics/iftt-open-door-by-location

## weather
Reads the weather from openweathermap

## sensehatout
Displays weather / garage status on the pi sensehat