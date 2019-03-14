#!/usr/bin/env python
import sys
sys.path.append('/home/pi/proj/garage')
import myq as q
from flask import Flask, json, request
app = Flask(__name__)

@app.route('/echo', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_echo():
    if request.method == 'GET':
        return "ECHO: GET\n"

    elif request.method == 'POST':
        return "ECHO: POST\n"

    elif request.method == 'PATCH':
        return "ECHO: PACTH\n"

    elif request.method == 'PUT':
        return "ECHO: PUT\n"

    elif request.method == 'DELETE':
        return "ECHO: DELETE"

@app.route('/garage', methods = ['POST'])
def garage():
    state_request = q.myq_main2('status')
    state = state_request.split(' ')[4].lower().replace('.','')
    #print (command + ' ' + state)

    if request.headers['Content-Type'] == 'application/json':
        content = request.get_json()
        code = content['code']
        command = content['command']
        if code == "4785":
            if command == 'status':
                return "The garage door is currently " + state
            elif (command == 'close' and state == 'open') or (command == 'toggle' and state == 'open'):
                q.myq_main2('close','Garage Door Opener')
                return "The garage is open but I will close it at once for you!"
            elif (command == 'open' and state == 'closed') or (command == 'toggle' and state == 'open'):
                q.myq_main2('open','Garage Door Opener')
                return "The garage is closed but I will open it for you now!"
            elif command == 'open' and state == 'open':
                return "The garage is already opened for you!"
        else: 
            return "Unauthorized"
        
    else:
        return "415 Unsupported Media Type ;)"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090)
