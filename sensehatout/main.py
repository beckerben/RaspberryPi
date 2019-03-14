#!/usr/bin/env python
import sys
sys.path.append('/home/pi/proj')

from sense_hat import SenseHat
import time
import paramiko


s = SenseHat()
s.low_light = True

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)

s.rotation = 180

def trinket_logo():
    G = green
    Y = yellow
    B = blue
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O,
    O, Y, Y, Y, B, G, O, O,
    Y, Y, Y, Y, Y, B, G, O,
    Y, Y, Y, Y, Y, B, G, O,
    Y, Y, Y, Y, Y, B, G, O,
    Y, Y, Y, Y, Y, B, G, O,
    O, Y, Y, Y, B, G, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def raspi_logo():
    G = green
    R = red
    O = nothing
    logo = [
    O, G, G, O, O, G, G, O, 
    O, O, G, G, G, G, O, O,
    O, O, R, R, R, R, O, O, 
    O, R, R, R, R, R, R, O,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    O, R, R, R, R, R, R, O,
    O, O, R, R, R, R, O, O,
    ]
    return logo

def plus():
    W = white
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O, 
    O, O, O, W, W, O, O, O,
    O, O, O, W, W, O, O, O, 
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, O, O, W, W, O, O, O,
    O, O, O, W, W, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def equals():
    W = white
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O, 
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def heart():
    P = pink
    W = white
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O,
    O, W, W, O, W, W, O, O,
    W, P, P, W, P, P, W, O,
    W, P, P, P, P, P, W, O,
    O, W, P, P, P, W, O, O,
    O, O, W, P, W, O, O, O,
    O, O, O, W, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo
    
def ben():
    P = pink
    B = blue
    Y = yellow
    G = green
    O = nothing
    logo = [
    P, P, O, B, B, B, O, O,
    P, O, P, B, O, O, O, O,
    P, P, O, B, B, O, O, O,
    P, O, P, B, O, O, O, O,
    P, P, O, B, B, B, O, O,
    O, O, O, O, O, G, O, G,
    O, O, O, O, O, G, G, G,
    O, O, O, O, O, G, O, G,
    ]
    return logo    

images = [trinket_logo, trinket_logo, plus, raspi_logo, raspi_logo, equals, heart, heart]
count = 0

#while True: 
#    s.set_pixels(images[count % len(images)]())
#    time.sleep(.75)
#    count += 1

while True:
    try:
        try: 
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect('pi01', username='xxx', password='xxx')  #todo: replace
            stdin, stdout, stderr = client.exec_command('gpio read 0')
            door_state_code = ' '.join(stdout).strip()
            client.close()
            if door_state_code == '0': 
                door_state_desc = "Open"
            else:
                door_state_desc = "Closed"
        except: 
            door_state_desc = "Error"
            pass
        f = open("/home/pi/proj/weather.txt","r")
        weather=eval(f.read())
        #from the sensehat    
        #temp = round(s.get_temperature()*1.8 +32,1)
        humidityhome = int(s.get_humidity())
        #pressure = round(s.get_pressure(),1)
        temp = round(weather['temperature'],1)
        humidity = weather['humidity']
        windspeed = round(weather['windspeed'],1)
        winddirection = weather['winddirection']
        maxtemp = int(weather['maxtemperature'])
        mintemp = int(weather['mintemperature'])
        message= 'temp out {0}F hum out {1}% / hum in {2}% low {3}F high {4}F wind {5} @ {6} {7}'.format(temp,humidity,humidityhome,mintemp,maxtemp,windspeed,winddirection,door_state_desc)
        s.show_message(message, scroll_speed=(0.05),text_colour=[0,102,255], back_colour= [0,0,0])
        s.set_pixels(heart())
        time.sleep(1.0)
        s.set_pixels(ben())
        time.sleep(2.0)
        s.clear()
    except: 
        s.clear()
        pass
    
