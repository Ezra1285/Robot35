import tkinter as tk
import time
import _thread, threading
import pyttsx3
import RPi.GPIO as GPIO
from project_8 import LocationChip
def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command) 
    engine.runAndWait()
def run(location):
    closest_cord = location.findQuadrant()
    if closest_cord == "a0":
        SpeakText("I am in the starting quadrant")
    if closest_cord == "a1":
        SpeakText("I am in the charging station")
    if closest_cord == "a2":
        SpeakText("I am in hunters office ")
    if closest_cord == "a3":
        SpeakText("I am in restrooms")
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
