# -*- coding: utf-8 -*-
"""
Author: Aaron Flores
Description: Reads data from sensors connected to the Arduino.
"""
import serial
import datetime
import json
import os
port = serial.Serial("COM5") #Port may vary.
todays_date = datetime.datetime.today().strftime("%m-%d-%y");
while(True): 
    if os.path.isfile(todays_date + ".txt"):
        data_file = open(todays_date + ".txt",'a')
    else:
        data_file = open(todays_date + ".txt",'w')
    sensors_data = port.readline().decode("utf-8")
    sensors_data.replace('\r\n','')
    data = json.loads(sensors_data)
    data["Date"] = datetime.datetime.now().isoformat(' ', timespec='minutes')
    data_file.write(json.dumps(data) + "\n")
    data_file.flush()
