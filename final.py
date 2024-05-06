import tkinter as tk
import time
import _thread, threading
import pyttsx3
import RPi.GPIO as GPIO
from project_8 import LocationChip
from ourRobotControl import RobotControl

def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command) 
    engine.runAndWait()

def run(location):
    not_done = True
    asked = False
    user = ""
    last_cord = ""
    while not_done:
        dist = get_distance()
        closest_cord = location.findQuadrant()
        if closest_cord == "a0" and last_cord != "a0":
            SpeakText("I am in the starting quadrant")
        if closest_cord == "a1" and last_cord != "a1":
            SpeakText("I am in the charging station")
        if closest_cord == "a2" and last_cord != "a2":
            SpeakText("I am in hunters office ")
        if closest_cord == "a3" and last_cord != "a3":
            SpeakText("I am in restrooms")
        last_cord = closest_cord
        if dist < 120 and not asked:
            SpeakText("Greetings Human")
            user = input("Where do you want to go? ")
            closest_cord = findSquare(user, location)
            asked = True
        if closest_cord == user:
            SpeakText("I need to talk")
            findSquare("a1", location)
            not_done = True

def findSquare(quadrant, location):
    robot_cotrol = RobotControl()
    while True:
        robot_cotrol.turnRight(1500)
        time.sleep(2)
        robot_cotrol.defualtMotors()
        t2 = threading.Thread(target=robot_cotrol.moveBackwards(1000))
        t2.start()
        t2.join()
        time.sleep(1)
        robot_cotrol.defualtEverything()
        closest_cord = location.findQuadrant()
        if closest_cord == quadrant:
            return closest_cord
        else:
            continue
def get_distance():
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


def main():
    myChip = LocationChip()
    t1 = threading.Thread(target=run(myChip))
    t1.start()
    t1.join()
    
    print("We are done")
    

if __name__ == "__main__":
    main()
