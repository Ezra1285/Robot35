import tkinter as tk
import time
import _thread, threading
import pyttsx3
import new_keyboard_control

SCRIPT=["Hi","My name is tango", "I am from Canada Aye"]

global speech
def get_circle_coords(x, y, r, canvas): #center coordinates, radius, window/canvas
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return x0, y0, x1, y1

def create_circle(x, y, r, canvas, line_width=2, fill_color="white"): #center coordinates, radius, window/canvas
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvas.create_oval(x0, y0, x1, y1, width=line_width, fill=fill_color)

class RobotAnimations:
    def __init__(self, window):
        self.window = window
        self.count = 500
        # Create the canvas that sits ontop the window
        self.canvas = tk.Canvas(self.window, bg='gray', height=480, width=800) # 700 by 850 
        create_circle(425, 250, 200, self.canvas, 4, 'light gray') # Head
        create_circle(350, 200, 75, self.canvas, 3)  # eye 1
        self.pupil1 = create_circle(350, 200, 30, self.canvas, 3, "black")  # Pupil 1
        create_circle(500, 200, 75, self.canvas, 3)  # eye 2
        self.pupil2 = create_circle(500, 200, 30, self.canvas, 3, "black")  # Pupil 2
        #  Mouth if we need
        # self.mouth = create_circle(425, 500, 80, self.canvas, 2, "red")
        # self.canvas.create_oval(425, 500, 80, 80, width=2, fill="red")
        self.curr_animation = "eyes"
        # self.label = tk.Label(self.window, bg='gray', height=480, width=800, wraplength=500, font='time 20', text="The word is tango and this is a long example to test the length of string that will work",)
        self.canvas.pack()

    # TODO: Delete other canvas if needed and create canvas that will dipslay the words thr robot recives
    def createWordScreen(self, event):
        if self.curr_animation != "text":
            self.removeCurrentCanvas()
        self.label = tk.Label(self.window, bg='gray', height=480, width=800, wraplength=500, font='time 20', text="The word is tango and this is a long example to test the length of string that will work",)
        # self.text = self.canvas.create_text(400, 100, text="The word is tango and this is a long example to test the length of string that will work", fill='black', font='time 20')
        self.curr_animation = "text"
        self.label.pack()

    def createBody(self):
        # Create the canvas that sits ontop the window
        self.canvas = tk.Canvas(self.window, bg='gray', height=480, width=800)
        # Create the initial body
        self.leftLeg = self.canvas.create_line(325,425,400,300, width=4) # Left leg
        self.rightLeg = self.canvas.create_line(475,425,400,300, width=4) # Right leg
        self.back = self.canvas.create_line(400,300,400,150, width=4) # back
        self.head = create_circle(400, 100, 50, self.canvas, 3, "gray")
        self.leftEye = create_circle(385, 85, 10, self.canvas, 3, "black")
        self.rightEye = create_circle(415, 85, 10, self.canvas, 3, "black")
        self.leftArm = self.canvas.create_line(325,250,400,175, width=4) # Left arm
        self.rightArm = self.canvas.create_line(475,250,400,175, width=4) # Right arm
        self.curr_animation = "body"
        self.canvas.pack()

    def switchBodytoEyes(self):
        self.removeCurrentCanvas()
        self.curr_animation = "eyes"
        self.canvas = tk.Canvas(self.window, bg='gray', height=480, width=800) # 700 by 850 
        create_circle(425, 250, 200, self.canvas, 4, 'light gray') # Head
        create_circle(350, 200, 75, self.canvas, 3)  # eye 1
        self.pupil1 = create_circle(350, 200, 30, self.canvas, 3, "black")  # Pupil 1
        create_circle(500, 200, 75, self.canvas, 3)  # eye 2
        self.pupil2 = create_circle(500, 200, 30, self.canvas, 3, "black")  # Pupil 2
        self.canvas.pack()


    def idleEyes(self):
        x0, y0, x1, y1 = get_circle_coords(350, 200, 30, self.canvas)
        self.canvas.coords(self.pupil1, x0, y0, x1, y1)
        x0, y0, x1, y1 = get_circle_coords(500, 200, 30, self.canvas)
        self.canvas.coords(self.pupil2, x0, y0, x1, y1)

    def lookUp(self, button_event):
        if self.curr_animation != "eyes":
            self.switchBodytoEyes()
        self.canvas.coords(self.pupil1, 315, 125, 375, 200)
        self.canvas.coords(self.pupil2, 475, 125, 535, 200)

    def lookDown(self, button_event):
        if self.curr_animation != "eyes":
            self.switchBodytoEyes()
        self.canvas.coords(self.pupil1, 325, 200 , 375, 300)
        self.canvas.coords(self.pupil2, 475, 200, 525, 300)

    def lookleft(self, button_event):
        if self.curr_animation != "eyes":
            self.switchBodytoEyes()
        x0, y0, x1, y1 = get_circle_coords(300, 200, 30, self.canvas)
        self.canvas.coords(self.pupil1, x0, y0, x1, y1)
        x0, y0, x1, y1 = get_circle_coords(450, 200, 30, self.canvas)
        self.canvas.coords(self.pupil2, x0, y0, x1, y1)

    def lookRight(self, button_event):
        if self.curr_animation != "eyes":
            self.switchBodytoEyes()
        x0, y0, x1, y1 = get_circle_coords(400, 200, 30, self.canvas)
        self.canvas.tag_raise(self.pupil1)
        self.canvas.coords(self.pupil1, x0, y0, x1, y1)
        x0, y0, x1, y1 = get_circle_coords(550, 200, 30, self.canvas)
        self.canvas.coords(self.pupil2, x0, y0, x1, y1)

    def bodyIdle(self, key):
        print("Key:", key)
        if self.curr_animation != "body":
            self.removeCurrentCanvas()
            self.createBody()
        x0, y0, x1, y1 = get_circle_coords(385, 85, 10, self.canvas)
        self.canvas.coords(self.leftEye, x0, y0, x1, y1)
        x0, y0, x1, y1 = get_circle_coords(415, 85, 10, self.canvas)
        self.canvas.coords(self.rightEye, x0, y0, x1, y1)
        self.canvas.coords(self.rightLeg, 475,425,400,300,)
        self.canvas.coords(self.leftLeg, 325,425,400,300)
        self.canvas.coords(self.leftArm, 325,250,400,175)
        self.canvas.coords(self.rightArm, 475,250,400,175)

    def halfStepLeft(self):
        self.canvas.coords(self.rightEye, 0, 0, 0, 0)
        x0, y0, x1, y1 = get_circle_coords(365, 85, 10, self.canvas)
        self.canvas.coords(self.leftEye, x0, y0, x1, y1)
        self.canvas.coords(self.rightLeg, 425,425,400,300)
        self.canvas.coords(self.leftLeg, 325,400,400,300)
        self.canvas.coords(self.leftArm, 300,215,400,175)
        self.canvas.coords(self.rightArm, 500,200,400,175)
        
    def fullStepLeft(self):
        self.canvas.coords(self.rightLeg, 425,425,400,300)
        self.canvas.coords(self.leftLeg, 365,420,400,300)
        self.canvas.coords(self.leftArm, 345,275,400,175)
        self.canvas.coords(self.rightArm, 445,265,400,175)

    def walkLeft(self, key):
        #  First remove the other canvas and create a new canvas
        if self.curr_animation != "body":
            self.removeCurrentCanvas()
            self.createBody()
        self.count = 500
        self.window.after(self.count, self.halfStepLeft)
        self.count += 500
        self.window.after(self.count, self.fullStepLeft)
        self.count += 500

    def halfStepRight(self):
        self.canvas.coords(self.leftEye, 0, 0, 0, 0)
        x0, y0, x1, y1 = get_circle_coords(430, 85, 10, self.canvas)
        self.canvas.coords(self.rightEye, x0, y0, x1, y1)
        self.canvas.coords(self.rightLeg, 500,400,400,300)
        self.canvas.coords(self.leftLeg, 375,425,400,300)
        self.canvas.coords(self.leftArm, 325,225,400,175)
        self.canvas.coords(self.rightArm, 500,225,400,175)
        
    def fullStepRight(self):
        self.canvas.coords(self.rightLeg, 485,420,400,300)
        self.canvas.coords(self.leftLeg, 375,425,400,300)
        self.canvas.coords(self.leftArm, 350,275,400,175)
        self.canvas.coords(self.rightArm, 485,235,400,175)

    def walkRight(self, key):
        if self.curr_animation != "body":
            self.removeCurrentCanvas()
            self.createBody()
        self.count = 500
        self.window.after(self.count, self.halfStepRight)
        self.count += 500
        self.window.after(self.count, self.fullStepRight)
        self.count += 500

    def removeCurrentCanvas(self):
        if self.curr_animation == "text":
            self.label.destroy()
        if self.curr_animation == "body" or self.curr_animation == "eyes":
            self.canvas.delete("all")
            self.canvas.destroy()

class ThreadExample(): 

    def mainThread(self, window):
        window.mainloop()

    def readScript(self):
        engine = pyttsx3.init() 
        # if (speech != " "):
        while len(SCRIPT) != 0:    
            engine.say(SCRIPT.pop(0))
            engine.runAndWait()


    def bindKeys(self, window, keys, robot_animations):
        window.bind('<w>', keys.lookUp, add='+')
        window.bind('<a>', keys.lookLeft, add='+')
        window.bind('<s>', keys.lookDown, add='+')
        window.bind('<d>', keys.lookRight, add='+')
        window.bind('<Up>', keys.moveFoward, add='+')  # Turn right
        window.bind('<Left>', keys.turnLeft, add='+') # waist left
        window.bind('<Down>', keys.moveBackwards, add='+') # turn left
        window.bind('<Right>', keys.turnRight, add='+') # waist right
        window.bind('<space>', keys.defualtMotors, add='+') 
        window.bind('<z>', keys.waistLeft) # foward
        window.bind('<c>', keys.waistRight) # backward
                
        #  The add='+' allows us to bind multiple functions
        # window.bind("w", robot_animations.lookUp, add='+')
        # window.bind("w", robot_animations.createWordScreen, add='+')
        window.bind("w", robot_animations.lookUp, add='+')
        window.bind("a", robot_animations.lookleft, add='+')
        window.bind("s", robot_animations.lookDown, add='+')
        window.bind("d", robot_animations.lookRight, add='+')
        window.bind("<Down>", robot_animations.walkLeft, add='+')
        window.bind("<Up>", robot_animations.walkRight, add='+')
        window.bind("<Left>", robot_animations.walkLeft, add='+')
        window.bind("<Right>", robot_animations.walkRight, add='+')
        window.bind("b", robot_animations.createWordScreen)
        window.bind('<space>', robot_animations.idleEyes, add='+')

    def timedFunction(self):
        print("                1 seconds is up")

def speak():
        global speech
        engine = pyttsx3.init() 
        # if (speech != " "):
        while(speech != " "):    
            engine.say(speech)
            engine.runAndWait()
            speech = " "


### NOTE: When switching between the body and eyes dont switch too quickly or the eyes will break and look weird
def main():
    global speech
    speech = "Hello World"
    window = tk.Tk()
    speak()
    window.title("Robot 35")
    window.geometry('800x480') # Sets the width x height of the window
    
    robot_animations = RobotAnimations(window)
    keys =  new_keyboard_control.KeyControl(window)
    
    # readScript()
    # bindKeys(window, keys, robot_animations)

    inst = ThreadExample()

    t = threading.Timer(8.0, inst.timedFunction)
    t.start()
    ##inst.firstThread()
    ##inst.secondThread()
    try:
        _thread.start_new_thread(inst.bindKeys,(window, keys, robot_animations))
    except:
        print ("Error: unable to start thread")
    try:
        _thread.start_new_thread(inst.readScript,())
    except:
        print ("Error: unable to start thread")
    inst.mainThread(window)
    print("We are done")




    # window.mainloop()


if __name__ == "__main__":
    main()

