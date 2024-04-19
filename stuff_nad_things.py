import serial
import time
import tkinter as tk
from maestro import Controller                                                     


# data = b"$KT1,NULL,0.91,2.68,NULL,LO=[no soultion]\r\n"
# data = data.decode('utf-8').split(",")

MOTORS = 0
TURN = 1
BODY = 2
HEADTILT = 4
HEADTURN = 3

class myTest:

    def __init__(self):
        self.chip = serial.Serial() 
        self.chip.port = '/dev/ttyUSB0' 
        self.chip.baudrate = 115200 
        self.chip.bytesize = serial.EIGHTBITS 
        self.chip.parity = serial.PARITY_NONE 
        self.chip.stopbits = serial.STOPBITS_ONE 
        self.chip.timeout = self.chip.open()
        self.robot_contol = RobotControl()

    def readData(self):
        line1 = self.chip.readline()
        line2 = self.chip.readline()
        data = line2.decode('utf-8').split(",")
        print("Text 1 found: ", line1)
        print("Text 2 found: ", line2)
        return data


    def spinCycle(self):
        self.robot_contol.lookUp(1800)
        time.sleep(3)
        self.cords = self.readData()  # read initial spot while looking up
        print("Initial Up cords:", self.cords)
        self.robot_contol.turnRight(1200)
        time.sleep(4)
        self.cords = self.readData()  # read initial spot while looking up
        print("Turn 1 cords:", self.cords)
        # self.robot_contol.defualtMotors()
        # self.cords = self.readData()

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
        
            
    def moveFoward(self):
        self.motors += 200
        if(self.motors > 7900):
            self.motors = 7900
        self.tango.setTarget(MOTORS, self.motors)
        print("Foward")
    
    def moveBackwards(self):
        self.motors -= 200
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



t = myTest()
t.spinCycle()
t.robot_contol.defaultHead()
t.robot_contol.defualtMotors()