import serial
import tkinter as tk
from maestro import Controller 
import time
import pyttsx3

# try: #print("in try") 
#     ser = serial.Serial() 
#     ser.port = '/dev/ttyUSB0' 
#     ser.baudrate = 115200 
#     ser.bytesize = serial.EIGHTBITS 
#     ser.parity = serial.PARITY_NONE 
#     ser.stopbits = serial.STOPBITS_ONE 
#     ser.timeout = 1 ser.open()
#     Ser.readline()

class LocationChip:

    def __init__(self):
        ser = serial.Serial() 
        ser.port = '/dev/ttyUSB0' 
        ser.baudrate = 115200 
        ser.bytesize = serial.EIGHTBITS 
        ser.parity = serial.PARITY_NONE 
        ser.stopbits = serial.STOPBITS_ONE 
        ser.timeout = ser.open() 
        text = ser.readline()
        print("Text found: ", text)


if __name__ == "__main__":
    chip = LocationChip()
    print("Done")