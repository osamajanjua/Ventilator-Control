import struct
import time
import sys
import random
import serial

arduino_data=serial.Serial('COM5',baudrate=9600)
time.sleep(2)
while True:
    input=arduino_data.readline()
    print(input)
        #returningback=input.decode("ascii")
        #print(returningback)
