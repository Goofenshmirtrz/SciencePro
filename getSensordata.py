# -*- coding: utf-8 -*-
"""
Author: Aaron Flores
Description: Reads data from sensors connected to the Arduino.
"""
import serial
import datetime
import json
port = serial.Serial("COM4") #Port may vary.
todays_date = datetime.datetime.today().strftime("%m-%d-%y");
data_file = open(todays_date + ".txt",'a')
while(True): 
    sensors_data = port.readline().decode("utf-8")
    sensors_data.replace('\r\n','')
    data = json.loads(sensors_data)
    data["Date"] = datetime.datetime.now().isoformat(' ', timespec='minutes')
    data_file.write(json.dumps(data))
    data_file.flush()
