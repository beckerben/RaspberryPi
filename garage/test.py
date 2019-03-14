#!/usr/bin/env python
import myq as q

command = 'close'
state_request = q.myq_main2('status')
state = state_request.split(' ')[4].lower().replace('.','')
print (command + ' ' + state)
if command == 'close' and state == 'open':
    print(q.myq_main2('close','Garage Door Opener'))

if command == 'open' and state == 'closed':
    print(q.myq_main2('open','Garage Door Opener'))
