# data from com port
#!/usr/bin/python
import os, sys
import serial
from serial import Serial
import time
import serial.tools.list_ports as port_list
from pprint import pprint
import inquirer

ports = list(port_list.comports())

questions = [
    inquirer.List(
        'port',
        message="select port:",
        choices=ports,
    ),
]
answer = inquirer.prompt(questions).get('port')
port = answer.name
manufacturer = answer.manufacturer
description = answer.description

print("port: " + port)
print("manufacturer: " + manufacturer)
print("description: " + description)

ser = serial.Serial()
ser.baudrate = 19200
ser.port = port
ser.timeout = 5
ser.open()
print(port + ' is now open')
print("loading...")
res = ser.readline()
#print(res.decode('Ascii'))
print(res)
print("Closing connection...")
ser.close()
ser.is_open
print(port + ' offline')
