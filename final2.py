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
            SpeakText("Goodbye Human")
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
            SpeakText("I need to charge")
            findSquare("a1", location)
            not_done = True

def findSquare(quadrant, location):
    robot_cotrol = RobotControl()
    while True:
        closest_cord = location.findQuadrant()
        if closest_cord == quadrant:
            return closest_cord
        t2 = threading.Thread(target=findQuadrant(location, quadrant))
        t2.start()
        t2.join()
        # robot_cotrol.turnRight(1200)
        # time.sleep(1)
        # robot_cotrol.defualtMotors()
        # t2 = threading.Thread(target=robot_cotrol.moveBackwards(1000))
        # t2.start()
        # t2.join()
        # time.sleep(2.5)
        # robot_cotrol.defualtEverything()
        # time.sleep(1)
        closest_cord = location.findQuadrant()
        print(closest_cord)
        if closest_cord == quadrant:
            return closest_cord
        else:
            continue
def findQuadrant(location, quadrant):
    robot_cotrol = RobotControl()
    data = location.readData()
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
    location.cords = data
    cords_dict = {'a0':float(data[0]), 'a1':float(data[1]), 'a2':float(data[2]), 'a3':float(data[3])} #messing with indexing here
    closest_cord = min(cords_dict, key=cords_dict.get)
    print("Current cord:", closest_cord)
    print(cords_dict)
    robot_cotrol.turnLeft(1000)
    time.sleep(1)
    robot_cotrol.defualtMotors()
    if quadrant == 'a3':
        robot_cotrol.moveBackwards(900)
        time.sleep(1)
    else:
        robot_cotrol.moveBackwards(800)
        time.sleep(1)
    robot_cotrol.defualtMotors()
    data2 = location.readData()
    cords_dict2 = {'a0':float(data2[0]), 'a1':float(data2[1]), 'a2':float(data2[2]), 'a3':float(data2[3])} #messing with indexing here
    print(abs(cords_dict.get(quadrant) - cords_dict2.get(quadrant)))
    if abs(cords_dict.get(quadrant) - cords_dict2.get(quadrant)) < 0.01:
        robot_cotrol.moveFoward(750)
        time.sleep(2)
        robot_cotrol.defualtEverything()
        robot_cotrol.turnRight(700)
        time.sleep(1)
        robot_cotrol.defualtEverything()
        return
    else:
        robot_cotrol.moveBackwards(750)
        time.sleep(3)

        robot_cotrol.defualtEverything()
        


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
    try:
        main()
    except:
        robot_cotrol = RobotControl()
        robot_cotrol.defualtEverything()
