import tkinter as tk
import time
import _thread, threading
import pyttsx3
from maestro import Controller 
import RPi.GPIO as GPIO

MOTORS = 0
TURN = 1
BODY = 2
HEADTILT = 4
HEADTURN = 3

class ThreadExample(): 
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

    # def mainThread(self, window):
        # window.mainloop()

    # def doAction(self):
    #     # robot_animations.talkingMode()
    #     engine = pyttsx3.init() 
    #     # if (speech != " "):
    #     while len(SCRIPT) != 0:    
    #         engine.say(SCRIPT.pop(0))
    #         engine.runAndWait()
    #         time.sleep(1)
        # robot_animations.idleEyes()

    def get_distance(self):
        GPIO.setmode(GPIO.BCM)

        TRIG_PIN = 4
        ECHO_PIN = 17 

        GPIO.setup(TRIG_PIN, GPIO.OUT)
        GPIO.setup(ECHO_PIN, GPIO.IN)

        GPIO.output(TRIG_PIN, False)
        time.sleep(0.1)

        GPIO.output(TRIG_PIN, True)
        time.sleep(0.00001)
        GPIO.output(TRIG_PIN, False)

        timeout = time.time()
        while GPIO.input(ECHO_PIN) == 0:
            if (time.time() - timeout) > 3:
                print('timeout occured while waiting for signal')
                return None
        
        pulse_start = time.time()
        timeout = time.time()
        while GPIO.input(ECHO_PIN) == 1:
            if (time.time() - timeout) > 3:
                print('timeout occured while recieving signal')
                return None
        pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17150
        distance = round(distance, 2)
        print("Dist:", distance)
        return distance


    def contUpdateDist(self):
        print("checking dist")
        while (True):
            print(self.get_distance())

    def timedFunction(self):
        print("                1 seconds is up")

    def tryFoward(self, amount=200):
        print("trying foward")
        self.moveBackwards(amount)
        time.sleep(4)
        self.defualtMotors()

    def doAll(self):
        while True:
            self.moveBackwards(1000)
            time.sleep(4)
            dist = self.get_distance()
            if dist < 50:
                break
        self.defualtMotors()

def speak():
    global speech
    engine = pyttsx3.init() 
    # if (speech != " "):
    while(speech != " "):    
        engine.say(speech)
        engine.runAndWait()
        speech = " "


def main():
    inst = ThreadExample()
    inst.doAll()

def main1():
    global speech
    speech = "Hello World"
    speak()
        
    # robot_animations = RobotControl()
    # sensor =  distSensor()
    inst = ThreadExample()

    t = threading.Timer(200.0, inst.timedFunction)
    t.start()
    ##inst.firstThread()
    ##inst.secondThread()
    try:
        _thread.start_new_thread(inst.tryFoward,(1000))
    except:
        print ("Error: unable to start thread1 ")
    try:
        _thread.start_new_thread(inst.contUpdateDist,())
    except:
        print ("Error: unable to start thread2 ")
    # inst.mainThread()
    print("We are done")




    # window.mainloop()


if __name__ == "__main__":
    main()

