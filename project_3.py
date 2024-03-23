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
    def __init__(self):
        # Create the window
        self.window = tk.Tk()
        self.window.title("Robot face")
        self.window.geometry('850x700') # Sets the width x height of the window
        # Create the canvas that sits ontop the window
        self.canvas = tk.Canvas(self.window, bg='gray', height=700, width=850)
        create_circle(425, 350, 300, self.canvas, 4, 'light gray') # Head
        create_circle(325, 325, 100, self.canvas, 3)  # eye 1
        self.pupil1 = create_circle(325, 325, 40, self.canvas, 3, "black")  # Pupil 1
        create_circle(525, 325, 100, self.canvas, 3)  # eye 2
        self.pupil2 = create_circle(525, 325, 40, self.canvas, 3, "black")  # Pupil 2
        #  Mouth if we need
        # self.mouth = create_circle(425, 500, 80, self.canvas, 2, "red")
        # self.canvas.create_oval(425, 500, 80, 80, width=2, fill="red")
        self.canvas.pack()

    def lookUp(self):
        self.canvas.coords(self.pupil1, 275, 225, 375, 325)
        self.canvas.coords(self.pupil2, 475, 225, 575, 325)

    def lookDown(self):
        self.canvas.coords(self.pupil1, 275, 325 , 375, 525)
        self.canvas.coords(self.pupil2, 475, 325, 575, 525)

    def lookleft(self):
        x0, y0, x1, y1 = get_circle_coords(250, 325, 40, self.canvas)
        self.canvas.coords(self.pupil1, x0, y0, x1, y1)
        x0, y0, x1, y1 = get_circle_coords(450, 325, 40, self.canvas)
        self.canvas.coords(self.pupil2, x0, y0, x1, y1)

    def lookRight(self):
        x0, y0, x1, y1 = get_circle_coords(400, 325, 40, self.canvas)
        self.canvas.tag_raise(self.pupil1)
        self.canvas.coords(self.pupil1, x0, y0, x1, y1)
        x0, y0, x1, y1 = get_circle_coords(600, 325, 40, self.canvas)
        self.canvas.coords(self.pupil2, x0, y0, x1, y1)

class RobotBody:
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.title("Robot body")
        self.window.geometry('850x700') # Sets the width x height of the window
        # Create the canvas that sits ontop the window
        self.canvas = tk.Canvas(self.window, bg='gray', height=700, width=850)
        # Create the initial body
        self.canvas.create_line(100,600,200,350, width=5)
        self.canvas.pack()


def main():
    body = RobotBody()
    body.window.mainloop()
    # face = RobotFace()
    # face.window.after(1000, face.lookleft)
    # face.window.after(2000, face.lookRight)
    # face.window.after(3000, face.lookDown)
    # face.window.after(4000, face.lookUp)
    # face.window.mainloop()
    

if __name__ == "__main__":
    main()

