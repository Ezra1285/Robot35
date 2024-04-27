import tkinter as tk
import time
import _thread, threading
import pyttsx3
import RPi.GPIO as GPIO
from project_8 import LocationChip


class ThreadExample(): 
    def __init__(self, location_chip):
        self.chip = location_chip
        self.object_distance = 1000
        self.inBox = True
        # GPIO.setmode(GPIO.BCM)
        # self.TRIG_PIN = 4
        # self.ECHO_PIN = 17 
        # GPIO.setup(self.TRIG_PIN, GPIO.OUT)
        # GPIO.setup(self.ECHO_PIN, GPIO.IN)
        # GPIO.output(self.TRIG_PIN, False)
        # time.sleep(0.1)
        # GPIO.output(self.TRIG_PIN, True)
        # time.sleep(0.00001)
        # GPIO.output(self.TRIG_PIN, False)
  

    def mainThread(self):
        # time.sleep(1)
        # self.chip.fowardMove(4500)
        time.sleep(.5)
        print("Starting the thread")
        # self.robot.moveBackwards(1000)

    def doItAll(self):
        while self.inBox:
            # dist = self.get_distance()           
            dist = 70
            if dist > 60.0:
                print("FOWARD")
                self.chip.robot_contol.moveBackwards(1200)
                time.sleep(1.5)
            else: 
                print("DEFAULTING")
                # self.chip.defaultMove()
            


    # def get_distance(self):
    #     timeout = time.time()
    #     while GPIO.input(self.ECHO_PIN) == 0:
    #         if (time.time() - timeout) > 3:
    #             print('timeout occured while waiting for signal')
    #             return None
        
    #     pulse_start = time.time()
    #     timeout = time.time()
    #     while GPIO.input(self.ECHO_PIN) == 1:
    #         if (time.time() - timeout) > 3:
    #             print('timeout occured while recieving signal')
    #             return None
    #     pulse_end = time.time()

    #     pulse_duration = pulse_end - pulse_start

    #     distance = pulse_duration * 17150
    #     distance = round(distance, 2)
    #     # print("Dist:", distance)
    #     return distance

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
        while self.inBox:
            timeout = time.time()
            while GPIO.input(self.ECHO_PIN) == 0:
                if (time.time() - timeout) > 3:
                    print('timeout occured while waiting for signal')
                    # self.chip.defaultMove()
                    continue            
            pulse_start = time.time()
            timeout = time.time()
            while GPIO.input(self.ECHO_PIN) == 1:
                if (time.time() - timeout) > 3:
                    print('timeout occured while recieving signal')
                    # self.chip.defaultMove()
                    continue
            pulse_end = time.time()
            pulse_duration = pulse_end - pulse_start
            distance = pulse_duration * 17150
            distance = round(distance, 2)
            # print("Dist:", distance)
            # dist = self.get_distance()
            print("Newest dist:", distance)                
            self.object_distance = distance
            time.sleep(1)

    def timedFunction(self):
        print("                1 seconds is up")

    def tryFoward1(self):
        while self.inBox:
            print("trying foward")
            # Stops only when distance is closer then 60
            print("Obj dist:", self.object_distance)
            if self.object_distance > 60.0:
                # if self.robot.motors >= 6000: 
                self.chip.fowardMove(4500)
                time.sleep(.5)
                # self.inBox = self.checkInBox()
                self.inBox = self.checkInBox()
                    
    def tryFoward(self):
        print("Obj dist:", self.object_distance)
        # while self.object_distance > 60.0:
        #     print("FOWARD")
        #     time.sleep(1)
        # print("DEFAULT")
        while self.object_distance > 60.0:
            # if self.robot.motors >= 6000: 
            self.chip.fowardMove(4500)
            time.sleep(1)
            # self.inBox = self.checkInBox()
            # self.inBox = self.checkInBox()
        # print("Deafulkting")
        # self.chip.defaultMove()

            
    def checkInBox(self):
        print("Checking in box")
        if self.inBox:
            self.inBox = self.chip.isInBox()
            time.sleep(1)

def main():
    myChip = LocationChip()
    # current_cord = myChip.findQuadrant()
    # if current_cord == False:
    #     speak("Range error")
    # else: 
    #     myChip.findExit(current_cord)

    # speak("Exit has been found")
        
    # sensor =  distSensor()
    inst = ThreadExample(myChip)
    inst.doItAll()
    # t = threading.Timer(200.0, inst.timedFunction)
    # t.start()

    ##inst.firstThread()
    ##inst.secondThread()
    # try:
    #     _thread.start_new_thread(inst.checkInBox,())
    # except:
    #     print ("Error: unable to start thread1 ")
    # try:
        # _thread.start_new_thread(inst.doItAll,())
    # except:
        # print ("Error: unable to start thread3 ")

    # try:
    #     _thread.start_new_thread(inst.contUpdateDist,())
    # except:
    #     print ("Error: unable to start thread2 ")
    # try:
    #     _thread.start_new_thread(inst.tryFoward,())
    # except:
    #     print ("Error: unable to start thread3 ")

    # inst.mainThread()
    inst.chip.defaultMove()
    print("We are done")
    

if __name__ == "__main__":
    main()

