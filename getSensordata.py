# -*- coding: utf-8 -*-
"""
Author: Aaron Flores
Description: Reads data from sensors connected to the Arduino.
"""
import serial
port = serial.Serial("/dev/ttyUSB0") #Port may vary.
while(True): 
    print port.readline()
    
    
