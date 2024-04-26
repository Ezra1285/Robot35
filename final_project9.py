import tkinter as tk
import time
import _thread, threading
import pyttsx3
from maestro import Controller 
import RPi.GPIO as GPIO
from project_8 import LocationChip, RobotControl


class ThreadExample(): 
    def __init__(self, robot_control, location_chip):
        self.robot = robot_control
        self.chip = location_chip
        self.inBox = True
        GPIO.setmode(GPIO.BCM)
        self.TRIG_PIN = 4
        self.ECHO_PIN = 17 
        GPIO.setup(self.TRIG_PIN, GPIO.OUT)
        GPIO.setup(self.ECHO_PIN, GPIO.IN)
        GPIO.output(self.TRIG_PIN, False)
        time.sleep(0.1)
        GPIO.output(self.TRIG_PIN, True)
        time.sleep(0.00001)
        GPIO.output(self.TRIG_PIN, False)
  
    def mainThread(self):
        print("Starting the thread")
        # self.robot.moveBackwards(1000)

    def get_distance(self):

        timeout = time.time()
        while GPIO.input(self.ECHO_PIN) == 0:
            if (time.time() - timeout) > 3:
                print('timeout occured while waiting for signal')
                return None
        
        pulse_start = time.time()
        timeout = time.time()
        while GPIO.input(self.ECHO_PIN) == 1:
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
        while self.inBox:
            dist = self.get_distance()
            if dist == None:
                continue
            self.object_distance = dist
            time.sleep(2)

    def timedFunction(self):
        print("                1 seconds is up")

    def tryFoward(self):
        while self.inBox:
            print("trying foward")
            # Stops only when distance is closer then 60
            print("Obj dist:", self.object_distance)
            if self.object_distance > 60:
                # if self.robot.motors >= 6000: 
                print("Trying to move")
                self.robot.moveBackwards(1000)
            else:
                print("DEFAULTING")
                self.robot.defualtMotors()
            time.sleep(3)

    def checkInBox(self):
        print("Checking in box")
        if self.inBox:
            self.inBox = self.chip.isInBox()
            time.sleep(1)

def speak(speech):
    engine = pyttsx3.init() 
    if (speech != " "):
        engine.say(speech)
        engine.runAndWait()      


def main():
    myChip = LocationChip()
    # current_cord = myChip.findQuadrant()
    # if current_cord == False:
    #     speak("Range error")
    # else: 
    #     myChip.findExit(current_cord)

    speak("Exit has been found")
    time.sleep(1)
        
    robot_control = RobotControl()
    # sensor =  distSensor()
    inst = ThreadExample(robot_control, myChip)

    t = threading.Timer(200.0, inst.timedFunction)
    t.start()
    ##inst.firstThread()
    ##inst.secondThread()
    # try:
    #     _thread.start_new_thread(inst.checkInBox,())
    # except:
    #     print ("Error: unable to start thread1 ")
    try:
        _thread.start_new_thread(inst.contUpdateDist,())
    except:
        print ("Error: unable to start thread2 ")
    try:
        _thread.start_new_thread(inst.tryFoward,())
    except:
        print ("Error: unable to start thread3 ")
    inst.mainThread()
    print("We are done")


if __name__ == "__main__":
    main()

