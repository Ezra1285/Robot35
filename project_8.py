import serial
import tkinter as tk
from maestro import Controller 
import time
import pyttsx3
from new_keyboard_control import KeyControl

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

    def findExit(self, current_cord):

        if current_cord == 'a0':
            pass
        elif current_cord == 'a1':
            pass
        elif current_cord == 'a2':
            pass
        elif current_cord == 'a3':
            pass

        
        self.robot_contol.lookUp('a', 800)
        time.sleep(1)
        self.cords = self.readData()
                
        self.robot_contol.turnRight('a', 400)
        time.sleep(1)
        self.robot_contol.defualtMotors()
        self.cords = self.readData()
        

        # Move Robot foward a tiny amount
        # Compare the new and prev coordinates
        # Determine which way we just moved
        # NOTE If robot exits we assume it was out of the correct exit
        #      and stop the robot/speak
        # while True:
        #     self.robot_contol.moveFoward()
        #     self.robot_contol.moveFoward()
        #     time.sleep(2)
        #     self.robot_contol.defualtMotors()
        #     prev_cords = self.cords
        #     self.cords = self.readData()

        



    # Returns data as list, i.e) [a0, a1, a2, a3]
    def readData(self):
        line1 = self.chip.readline()
        line2 = self.chip.readline()
        data = line2.decode('utf-8').split(",")
        print("Text 1 found: ", line1)
        print("Text 2 found: ", line2)
        return data

    def startReading(self):
        count = 0
        while count <= 10:
            self.readData()
            time.sleep(2)
            count += 1

    def findQuadrant(self):
        data = self.readData()
        self.cords = {'a0':data[0], 'a1':data[1], 'a2':data[2], 'a3':data[3]} #messing with indexing here
        self.cords['a3'] = 1000
        closest_cord = min(self.cords, key=self.cords.get)
        print("Current cord:", closest_cord)
        print(self.cords)
        speak("I am in quadrant " + closest_cord)
        time.sleep(2)
        return closest_cord
        


    def __init__(self):
        self.chip = serial.Serial() 
        self.chip.port = '/dev/ttyUSB0' 
        self.chip.baudrate = 115200 
        self.chip.bytesize = serial.EIGHTBITS 
        self.chip.parity = serial.PARITY_NONE 
        self.chip.stopbits = serial.STOPBITS_ONE 
        self.chip.timeout = self.chip.open()
        self.robot_contol = KeyControl() 
        # First read line is HEX and next one is decimal

def speak(speech):
        engine = pyttsx3.init() 
        if (speech != " "):
        # while(speech != " "):    
            engine.say(speech)
            engine.runAndWait()      

if __name__ == "__main__":
    myChip = LocationChip()
    current_cord = myChip.findQuadrant()
    print("Done")