import tkinter as tk
from maestro import Controller                                                     

MOTORS = 1
TURN = 2
BODY = 0
HEADTILT = 4
HEADTURN = 3


##def sendCommand(x):
##    if(x == '8'):
##        tango.setTarget(MOTOR, 6800)
class KeyControl():
    def __init__(self,win):
        self.root = win
        self.tango = Controller()
        self.body = 6000
        self.headTurn = 6000
        self.headTilt = 6000
        self.motors = 6000
        self.turn = 6000
        
    def head(self,key):
        print(key.keycode)
        if key.keycode == 38:
            self.headTurn += 200
            if(self.headTurn > 7900):
                self.headTurn = 7900
            self.tango.setTarget(HEADTURN, self.headTurn)
        elif key.keycode ==40:
            self.headTurn -= 200
            if(self.headTurn < 1510):
                self.headTurn = 1510
            self.tango.setTarget(HEADTURN, self.headTurn)
        elif key.keycode == 25:
            self.headTilt += 200
            if(self.headTilt > 7900):
                self.headTilt = 7900
            self.tango.setTarget(HEADTILT, self.headTilt)
        elif key.keycode == 39:
            self.headTilt -= 200
            if(self.headTilt < 1510):
                self.headTilt = 1510
            self.tango.setTarget(HEADTILT, self.headTilt)
                


    def waist(self, key):
        print(key.keycode)
        
        if key.keycode == 54:
            self.body += 200
            if(self.body > 7900):
                self.body = 7900
            self.tango.setTarget(BODY, self.body)
            print("waist right")
        elif key.keycode == 52:
            self.body -= 200
            if(self.body < 1510):
                self.body = 1510
            self.tango.setTarget(BODY, self.body)
            print ('waist left')
   
    
    def arrow(self, key):
        print(key.keycode)
        if key.keycode == 116:
            self.motors += 200
            if(self.motors > 7900):
                self.motors = 7900
            print(self.motors)
            self.tango.setTarget(MOTORS, self.motors)
        elif key.keycode == 111:
            self.motors -= 200
            if(self.motors < 1510):
                self.motors = 1510
            print(self.motors)
            self.tango.setTarget(MOTORS, self.motors)
        elif key.keycode == 114:
            self.turn += 200
            if(self.turn > 7400):
                self.turn = 7400
            print(self.turn)
            self.tango.setTarget(TURN, self.turn)
        elif key.keycode == 113:
            self.turn -= 200
            if(self.turn <2110):
                self.turn = 2110
            print(self.turn)
            self.tango.setTarget(TURN, self.turn)
        
        elif key.keycode == 65:
            self.motors = 6000
            self.turn = 6000
            self.tango.setTarget(MOTORS, self.motors)
            self.tango.setTarget(TURN, self.turn)

import tkinter as tk
from maestro import Controller                                                     

MOTORS = 1
TURN = 2
BODY = 0
HEADTILT = 4
HEADTURN = 3


##def sendCommand(x):
##    if(x == '8'):
##        tango.setTarget(MOTOR, 6800)
class KeyControl():
    def __init__(self,win):
        self.root = win
        self.tango = Controller()
        self.body = 6000
        self.headTurn = 6000
        self.headTilt = 6000
        self.motors = 6000
        self.turn = 6000

    def lookDown(self,key):
        self.headTilt -= 200
        if(self.headTilt < 1510):
            self.headTilt = 1510
        self.tango.setTarget(HEADTILT, self.headTilt)
        print("Look down")

    def lookUp(self,key):
        self.headTilt += 200
        if(self.headTilt > 7900):
            self.headTilt = 7900
        self.tango.setTarget(HEADTILT, self.headTilt)
        print("Look up")

    def lookRight(self,key):
        self.headTurn += 200
        if(self.headTurn > 7900):
            self.headTurn = 7900
        self.tango.setTarget(HEADTURN, self.headTurn)
        print("Look Right")


    def lookLeft(self,key):
        self.headTurn -= 200
        if(self.headTurn < 1510):
            self.headTurn = 1510
        self.tango.setTarget(HEADTURN, self.headTurn)
        print("Look left")
        

    def waistLeft(self, key):
        self.body -= 200
        if(self.body < 1510):
            self.body = 1510
        self.tango.setTarget(BODY, self.body)
        print ('waist left')

    def waistRight(self, key):    
        self.body += 200
        if(self.body > 7900):
            self.body = 7900
        self.tango.setTarget(BODY, self.body)
        print("waist right")
        
            
    def moveFoward(self, key):
        self.motors += 200
        if(self.motors > 7900):
            self.motors = 7900
        self.tango.setTarget(MOTORS, self.motors)
        print("Foward")
    
    def moveBackwards(self, key):
        self.motors -= 200
        if(self.motors < 1510):
            self.motors = 1510
        self.tango.setTarget(MOTORS, self.motors)

    def turnRight(self, key):
        self.turn += 200
        if(self.turn > 7400):
            self.turn = 7400
        self.tango.setTarget(TURN, self.turn)
        print("Turning Right")

    def turnLeft(self, key):
        self.turn -= 200
        if(self.turn <2110):
            self.turn = 2110
        self.tango.setTarget(TURN, self.turn)
        print("Turning left")

    def defualtMotors(self, key):
        self.motors = 6000
        self.turn = 6000
        self.tango.setTarget(MOTORS, self.motors)
        self.tango.setTarget(TURN, self.turn)
        print("Deafulting motors")

win = tk.Tk()
keys = KeyControl(win)

win.bind('<Up>', keys.moveFoward)
win.bind('<Left>', keys.turnLeft)
win.bind('<Down>', keys.moveBackwards)
win.bind('<Right>', keys.turnRight)
win.bind('<space>', keys.defualtMotors)
win.bind('<z>', keys.waistLeft)
win.bind('<c>', keys.waistRight)
win.bind('<w>', keys.lookUp)
win.bind('<s>', keys.lookDown)
win.bind('<a>', keys.lookLeft)
win.bind('<d>', keys.lookRight)
win.mainloop()
keys = KeyControl(win)     
