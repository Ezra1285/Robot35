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
    # TODO: 
    #  1) Drive forward
    #  2) If the dist. from prev cord to new cord is rapidly approaching desired target then its probaly going the right way
    #  3) If its not getting way closer then we need to turn and try again
    def findExit(self, current_cord):
        if current_cord == 'a0':
            while True:
                prev_cord = self.cords
                self.robot_contol.moveBackwards(1200)
                time.sleep(1.8)
                self.robot_contol.defualtMotors()
                time.sleep(2)
                self.cords = self.readData()
                if float(prev_cord[0]) - float(self.cords[0]) > .25:
                    # self.leaveBox(self.cords[0])
                    break
                print("Prev cord,", prev_cord, " - type:", type(prev_cord))
                print("Prev:", prev_cord[0], "- New:", self.cords[0])
                self.robot_contol.turnLeft(800)
                time.sleep(3)
                self.robot_contol.defualtMotors()
                time.sleep(2)
        elif current_cord == 'a1':
            while True:
                prev_cord = self.cords
                self.robot_contol.moveBackwards(800)
                time.sleep(1.8)
                self.robot_contol.defualtMotors()
                time.sleep(2)
                self.cords = self.readData()
                if float(prev_cord[1]) - float(self.cords[1]) > .25:
                    # self.leaveBox(self.cords[1])
                    break
                print("Prev:", prev_cord[1], "- New:", self.cords[1])
                self.robot_contol.turnLeft(800)
                time.sleep(3)
                self.robot_contol.defualtMotors()
                time.sleep(2)
        elif current_cord == 'a2':
            while True:
                prev_cord = self.cords
                self.robot_contol.moveBackwards(800)
                time.sleep(1.8)
                self.robot_contol.defualtMotors()
                time.sleep(2)
                self.cords = self.readData()
                if float(prev_cord[2]) - float(self.cords[2]) > .25:
                    # self.leaveBox(self.cords[2])
                    break
                print("Prev:", prev_cord[2], "- New:", self.cords[2])
                self.robot_contol.turnLeft(800)
                time.sleep(3)
                self.robot_contol.defualtMotors()
                time.sleep(2)
        elif current_cord == 'a3':
            while True:
                prev_cord = self.cords
                self.robot_contol.moveBackwards(800)
                time.sleep(1.8)
                self.robot_contol.defualtMotors()
                time.sleep(2)
                self.cords = self.readData()
                if float(prev_cord[3]) - float(self.cords[3]) > .25:
                    # self.leaveBox(self.cords[3])
                    break
                print("Prev:", prev_cord[3], "- New:", self.cords[3])
                self.robot_contol.turnLeft(800)
                time.sleep(3)
                self.robot_contol.defualtMotors()
                time.sleep(2)


    # Returns data as list, i.e) [a0, a1, a2, a3]
    def readData(self):
        while True:      
            self.chip.reset_input_buffer()  
            time.sleep(2)
            line1 = self.chip.readline()
            line2 = self.chip.readline()
            data = line2.decode('utf-8').split(",")
            print("Text 2 found: ", line2)
            print("Data:", data)
            if len(data) == 0 or len(data) == 1:
                continue
            elif data[0] == '$RANGE_ERROR':
                continue
            elif data[0] == 'NULL' or data[0] == 'null': 
                continue
            elif data[1] == 'NULL' or data[1] == 'null': 
                continue
            elif data[2] == 'NULL' or data[2] == 'null': 
                continue
            elif data[3] == 'NULL' or data[3] == 'null': 
                continue
            elif data[4] == 'NULL' or data[4] == 'null': 
                continue
            return data[1:]

    #  Returns true is we have exited
    def isInBox(self):
        # for x in range(2):      
        self.chip.reset_input_buffer()  
        line1 = self.chip.readline()
        line2 = self.chip.readline()
        data = line2.decode('utf-8').split(",")
        # for lo in data[5]:
        lo1, lo2, lo3 = float(data[5][4:]), float(data[6]), float(data[7][:-3])
        # print("Data 5 is:", float(data[5][4:]))
        # print("Data 6 is:", float(data[6]))
        # print("Data 7 is:", float(data[7][:-3]))
        # for lo in 
        if lo1 < 0 or lo1 < 0 or lo2 < 0:
            return False
        print("isExited Data:", data)
            # if data[0] != '$RANGE_ERROR':
            #     return True
        return True
            

    def fowardMove(self, amount):
        self.robot_contol.setMotorsTo(amount) 
        
    def defaultMove(self):
        print("Trying to default")
        self.robot_contol.defualtMotors() 
        
    def leaveBox(self, current_anchor_dist):
        #  Values will most likely need tweaking
        if float(current_anchor_dist) > 2:
            self.robot_contol.moveBackwards(1200)
            time.sleep(4)
        else:
            self.robot_contol.moveBackwards(1000)
            time.sleep(3)
        self.robot_contol.defualtMotors()
        speak("I have exited")


    def findQuadrant(self):
        data = self.readData()
        if len(data) == 0:
            return False
        if data[0] == 'NULL' or data[0] == 'null': 
            data[0] = 1000
        if data[1] == 'NULL' or data[1] == 'null': 
            data[1] = 1000
        if data[2] == 'NULL' or data[2] == 'null': 
            data[2] = 1000
        if data[3] == 'NULL' or data[3] == 'null': 
            data[3] = 1000
        self.cords = data
        cords_dict = {'a0':float(data[0]), 'a1':float(data[1]), 'a2':float(data[2]), 'a3':float(data[3])} #messing with indexing here
        # self.cords['a2'] = 1000
        closest_cord = min(cords_dict, key=cords_dict.get)
        print("Current cord:", closest_cord)
        print(cords_dict)
        speak("I am in quadrant " + closest_cord)
        time.sleep(2)
        return closest_cord
    

    def exitBox(self):
        self.robot_contol.tango.setAccel(TURN, 3)
        self.robot_contol.tango.setSpeed(TURN, 3)
        self.robot_contol.turnLeft(1200)
        time.sleep(3)
        self.robot_contol.defualtMotors()
        time.sleep(2)
        self.robot_contol.moveBackwards(900)
        time.sleep(2.5)
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

    def setMotorsTo(self, amount=200):
        if self.motors == amount:
            return False
        self.motors = amount
        if(self.motors < 1510):
            self.motors = 1510
        if(self.motors > 7900):
            self.motors = 7900
        self.tango.setSpeed(MOTORS, 2)
        self.tango.setAccel(MOTORS, 245)
        self.tango.setTarget(MOTORS, self.motors)
        return True

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

    def turnLeft(self, amount=200):
        self.turn -= amount
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
    # if current_cord == False:
    #     speak("Range error")
    # else: 
    #     myChip.findExit(current_cord)
    myChip.exitBox()
    print("Done")