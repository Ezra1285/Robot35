import tkinter as tk
from maestro import Controller                                                     

# MOTORS = 1
# TURN = 2
# BODY = 0
# HEADTILT = 4
# HEADTURN = 3

MOTORS = 0
TURN = 1
BODY = 2
HEADTILT = 4
HEADTURN = 3


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
        self.body = 6000
        self.headTilt = 6000
        self.headTurn = 6000
        self.rightShoulder = 6000
        self.rightBicep = 6000
        self.rightElbow = 6000
        self.rightUpperforarm = 6000
        self.rightWrist = 6000
        self.rightGripper = 6000
        self.leftShouler = 6000
        self.leftBicep = 6000
        self.leftElbow = 6000
        self.leftUpperForearm = 6000
        self.leftWrist = 6000
        self.leftGripper = 6000
        self.tango.setTarget(MOTORS, self.motors)
        self.tango.setTarget(TURN, self.turn)
        self.tango.setTarget(BODY, self.body)
        self.tango.setTarget(HEADTILT, self.headTilt)
        self.tango.setTarget(HEADTURN, self.headTurn)
        self.tango.setTarget(5, self.rightShoulder)
        self.tango.setTarget(6, self.rightBicep)
        self.tango.setTarget(7, self.rightElbow)
        self.tango.setTarget(8, self.rightUpperforarm)
        self.tango.setTarget(9, self.rightWrist)
        self.tango.setTarget(10, self.rightGripper)
        self.tango.setTarget(11, self.leftShouler)
        self.tango.setTarget(12, self.leftBicep)
        self.tango.setTarget(13, self.leftElbow)
        self.tango.setTarget(14, self.leftUpperForearm)
        self.tango.setTarget(15, self.leftWrist)
        self.tango.setTarget(16, self.leftGripper)
        print("Defaulting everything")


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
