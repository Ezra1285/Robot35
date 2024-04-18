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

    def readData(self):
        line1 = self.chip.readline()
        line2 = self.chip.readline()
        print("Text 1 found: ", line1)
        print("Text 2 found: ", line2)

    def startReading(self):
        count = 0
        while count <= 10:
            self.readData()
            time.sleep(2)
            count += 1


    def __init__(self):
        self.chip = serial.Serial() 
        self.chip.port = '/dev/ttyUSB0' 
        self.chip.baudrate = 115200 
        self.chip.bytesize = serial.EIGHTBITS 
        self.chip.parity = serial.PARITY_NONE 
        self.chip.stopbits = serial.STOPBITS_ONE 
        self.chip.timeout = self.chip.open() 
        # First read line is HEX and next one is decimal
        

if __name__ == "__main__":
    myChip = LocationChip()
    myChip.startReading()
    print("Done")