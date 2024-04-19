import serial
import tkinter as tk
from maestro import Controller 
import time
import pyttsx3
import tkinter as tk
from maestro import Controller                                                     

MOTORS = 0
TURN = 1
BODY = 2
HEADTILT = 4
HEADTURN = 3


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

        
        # self.robot_contol.lookUp('a', 800)
        # time.sleep(1)
        # self.cords = self.readData()
                
        # self.robot_contol.turnRight('a', 400)
        # time.sleep(1)
        # self.robot_contol.defualtMotors()
        # self.cords = self.readData()
        

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
        print("Type", type(data[1]))
        print("Val", data[1])
        self.cords = {'a0':float(data[0]), 'a1':float(data[1]), 'a2':float(data[2]), 'a3':float(data[3])} #messing with indexing here
        self.cords['a3'] = 1000
        closest_cord = min(self.cords, key=self.cords.get)
        print("Current cord:", closest_cord)
        print(self.cords)
        speak("I am in quadrant " + closest_cord)
        time.sleep(2)
        return closest_cord

    def exitBox(self):
        self.robot_contol.moveFoward(1000)
        time.sleep(1)
        self.robot_contol.defualtMotors()
        speak("I have exited the box")    


    def __init__(self):
        self.chip = serial.Serial() 
        self.chip.port = '/dev/ttyUSB0' 
        self.chip.baudrate = 115200 
        self.chip.bytesize = serial.EIGHTBITS 
        self.chip.parity = serial.PARITY_NONE 
        self.chip.stopbits = serial.STOPBITS_ONE 
        self.chip.timeout = self.chip.open()
        self.robot_contol = RobotControl()
        # First read line is HEX and next one is decimal

def speak(speech):
        engine = pyttsx3.init() 
        if (speech != " "):
        # while(speech != " "):    
            engine.say(speech)
            engine.runAndWait()      


class RobotControl():
    def __init__(self):
        self.tango = Controller()
        self.body = 6000
        self.headTurn = 6000
        self.headTilt = 6000
        self.motors = 6000
        self.turn = 6000

    def lookDown(self,val=200):
        self.headTilt -= val
        if(self.headTilt < 1510):
            self.headTilt = 1510
        self.tango.setTarget(HEADTILT, self.headTilt)
        print("Look down")

    def lookUp(self, amount=200):
        self.headTilt += amount
        if(self.headTilt > 7900):
            self.headTilt = 7900
        self.tango.setTarget(HEADTILT, self.headTilt)
        print("Look up")

    def lookRight(self):
        self.headTurn += 200
        if(self.headTurn > 7900):
            self.headTurn = 7900
        self.tango.setTarget(HEADTURN, self.headTurn)
        print("Look Right")

    def defaultHead(self):
        self.headTilt = 6000
        self.headTurn = 6000
        self.tango.setTarget(HEADTURN, self.headTurn)
        self.tango.setTarget(HEADTILT, self.headTilt)

    def lookLeft(self):
        self.headTurn -= 200
        if(self.headTurn < 1510):
            self.headTurn = 1510
        self.tango.setTarget(HEADTURN, self.headTurn)
        print("Look left")
        

    def waistLeft(self):
        self.body -= 200
        if(self.body < 1510):
            self.body = 1510
        self.tango.setTarget(BODY, self.body)
        print ('waist left')

    def waistRight(self):    
        self.body += 200
        if(self.body > 7900):
            self.body = 7900
        self.tango.setTarget(BODY, self.body)
        print("waist right")
        
            
    def moveFoward(self, amount=200):
        self.motors += amount
        if(self.motors > 7900):
            self.motors = 7900
        self.tango.setTarget(MOTORS, self.motors)
        print("Foward")
    
    def moveBackwards(self, amount=200):
        self.motors -= amount
        if(self.motors < 1510):
            self.motors = 1510
        self.tango.setTarget(MOTORS, self.motors)

    def turnRight(self, amount=200):
        self.turn += amount
        if(self.turn > 7400):
            self.turn = 7400
        self.tango.setTarget(TURN, self.turn)
        print("Turning Right")

    def slowTurnRight(self, amount=200):
        self.tango.setSpeed(TURN, 3)
        self.tango.setAccel(TURN, 3)
        self.turn += amount
        if(self.turn > 7400):
            self.turn = 7400
        self.tango.setTarget(TURN, self.turn)
        print("Turning Right")

    def turnLeft(self):
        self.turn -= 200
        if(self.turn <2110):
            self.turn = 2110
        self.tango.setTarget(TURN, self.turn)
        print("Turning left")

    def defualtMotors(self):
        self.motors = 6000
        self.turn = 6000
        self.tango.setTarget(MOTORS, self.motors)
        self.tango.setTarget(TURN, self.turn)
        print("Deafulting motors")


if __name__ == "__main__":
    myChip = LocationChip()
    current_cord = myChip.findQuadrant()
    
    print("Done")