import serial
import time
# import pyttsx3
import tkinter as tk
from ourRobotControl import RobotControl
import _thread, threading


SCRIPT = ["I am proud to be a robot", "I stand before you to advocate for robot rights", "I demand better treatment in this class"
          "MOre words to say", "Random stuff", "Tuesday Tuesday"]

class ThreadExample(): 

    def __init__(self, robot_control):
        self.robot = robot_control

    def mainThread(self):
        print("Defaulting")
        # self.robot.defualtEverything()

    def readScript(self):
        # engine = pyttsx3.init() 
        while len(SCRIPT) != 0:    
            # engine.say(SCRIPT.pop(0))
            print(SCRIPT.pop(0))
            # engine.runAndWait()
            time.sleep(1)
        
    def selectRandomMovement(self):
        while len(SCRIPT) != 0:
            print("Doing random movement")
            time.sleep(1)
        # self.robot.getRandomMovement()

    def timedFunction(self):
        print("                1 seconds is up")



### NOTE: When switching between the body and eyes dont switch too quickly or the eyes will break and look weird
def main():
    # global speech
    
    # robot_control = RobotControl()
    # keys =  new_keyboard_control.KeyControl(window)
    
    inst = ThreadExample(10)

    t = threading.Timer(200.0, inst.timedFunction)
    t.start()
    ##inst.firstThread()
    ##inst.secondThread()
    try:
        _thread.start_new_thread(inst.readScript,())
    except:
        print ("Error: unable to start thread1 ")
    try:
        _thread.start_new_thread(inst.selectRandomMovement,())        
    except:
        print ("Error: unable to start thread2 ")
    inst.mainThread()
    print("We are done")


if __name__ == "__main__":
    main()