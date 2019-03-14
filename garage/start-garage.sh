#!/bin/bash
cd /home/pi/proj/garage
runuser -l pi -c 'cd /home/pi/proj/garage; source /home/pi/.profile; ./garage.py &' 
cd ..
./main.py &
