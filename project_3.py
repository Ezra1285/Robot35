import tkinter as tk
import time

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

class RobotFace():
    def __init__(self, window):
        self.window = window
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
        self.canvas.pack()

    def idleEyes(self):
        x0, y0, x1, y1 = get_circle_coords(350, 200, 30, self.canvas)
        self.canvas.coords(self.pupil1, x0, y0, x1, y1)
        x0, y0, x1, y1 = get_circle_coords(500, 200, 30, self.canvas)
        self.canvas.coords(self.pupil2, x0, y0, x1, y1)

    def lookUp(self, button_event):
        self.canvas.coords(self.pupil1, 315, 125, 375, 200)
        self.canvas.coords(self.pupil2, 475, 125, 535, 200)

    def lookDown(self, button_event):
        self.canvas.coords(self.pupil1, 325, 200 , 375, 300)
        self.canvas.coords(self.pupil2, 475, 200, 525, 300)

    def lookleft(self, button_event):
        x0, y0, x1, y1 = get_circle_coords(300, 200, 30, self.canvas)
        self.canvas.coords(self.pupil1, x0, y0, x1, y1)
        x0, y0, x1, y1 = get_circle_coords(450, 200, 30, self.canvas)
        self.canvas.coords(self.pupil2, x0, y0, x1, y1)

    def lookRight(self, button_event):
        print("Buttom:", button_event)
        x0, y0, x1, y1 = get_circle_coords(400, 200, 30, self.canvas)
        self.canvas.tag_raise(self.pupil1)
        self.canvas.coords(self.pupil1, x0, y0, x1, y1)
        x0, y0, x1, y1 = get_circle_coords(550, 200, 30, self.canvas)
        self.canvas.coords(self.pupil2, x0, y0, x1, y1)

    def removeCurrentCanvas(self):
        self.canvas.destroy()

class RobotBody:
    def __init__(self, window) -> None:
        self.window = window
        # Create the canvas that sits ontop the window
        self.canvas = tk.Canvas(self.window, bg='gray', height=480, width=800)
        # Create the initial body
        self.leftLeg = self.canvas.create_line(325,425,400,300, width=4) # Left leg
        self.rightLeg = self.canvas.create_line(475,425,400,300, width=4) # Right leg
        self.back = self.canvas.create_line(400,300,400,150, width=4) # back
        # self.pupil2 = create_circle(500, 200, 30, self.canvas, 3, "black")  # Pupil 2
        self.head = create_circle(400, 100, 50, self.canvas, 3, "gray")
        self.leftEye = create_circle(385, 85, 10, self.canvas, 3, "black")
        self.rightEye = create_circle(415, 85, 10, self.canvas, 3, "black")
        self.leftArm = self.canvas.create_line(325,250,400,175, width=4) # Left arm
        self.rightArm = self.canvas.create_line(475,250,400,175, width=4) # Right arm
        self.canvas.pack()

    def idle(self):
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

    def walkLeft(self, count = 1000):
        while True: # Implement a trigger to break or use some event trigger
            if count > 3000:
                break
            self.window.after(count, self.halfStepLeft)
            count += 1000
            self.window.after(count, self.fullStepLeft)
            count += 1000
        return count

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

    def walkRight(self, count = 1000):
        start_cnt = count
        
        while True: # Implement a trigger to break or use some event trigger
            if count > start_cnt+3000:
                break
            self.window.after(count, self.halfStepRight)
            count += 1000
            self.window.after(count, self.fullStepRight)
            count += 1000
        return count    

    def removeCurrentCanvas(self):
        self.canvas.destroy()

def main():
    window = tk.Tk()
    window.title("Robot 35")
    window.geometry('800x480') # Sets the width x height of the window
    
    face = RobotFace(window)

    #TODO: Key Bindings will need to match what the robot uses
    # i.e.) lookUp will use the same key used in keyboard_control.py to make the robot loop up
    window.bind("w", face.lookUp)
    window.bind("a", face.lookleft)
    window.bind("s", face.lookDown)
    window.bind("d", face.lookRight)

    # window.bind("left", RobotBody.walkLeft)

    window.mainloop()


def test ():
    window = tk.Tk()
    window.title("Robot 35")
    window.geometry('800x480') # Sets the width x height of the window
    


    ###  Test the body animations
    body = RobotBody(window)
    # count = body.walkLeft()
    # window.after(count, body.idle) 
    # count += 1000
    # count = body.walkRight(count)
    # count+=1000

    ###  Test for the face animations using time based queuing
    # window.after(count, body.removeCurrentCanvas)
    face = RobotFace(window)
    # count+=1000
    # window.after(count, face.lookleft)
    # window.after(2000, face.lookRight)
    # window.after(3000, face.lookDown)
    # window.after(4000, face.lookUp)
    # window.after(5000, face.idleEyes)
    
    window.mainloop()
    

if __name__ == "__main__":
    main()

