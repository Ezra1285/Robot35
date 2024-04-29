import tkinter as tk
from ourRobotControl import RobotControl
import threading
import pyttsx3
from tkinter import simpledialog
from tkinter import messagebox
import time
import speech_recognition as sr
class Main(tk.Tk):
    def __init__(self): 
        super().__init__()
        self.canvas = tk.Canvas(self, width=500, height=500)
        #self.attributes("-fullscreen", True)
        self.canvas.grid(row=0,column=0)
        self.boxes = []
        self.icons = []
        self.orders = []
        self.motors_forward = {"Speed" : 200, "Distance" : 1, "Direction" : "Forward"}
        self.motors_turn = {"Distance" : 1, "Direction" : "Right"}
        self.head_tilt = {"Direction" : "Right"}
        self.head_pan = {"Direction" : "Up"}
        self.waist_turn = {"Direction" : "Right"}
        self.talking = {"Speech" : "Hello"}
        self.create_boxes()
        self.update()
        self.create_canvas()


    def create_duplicate(self, original_label):
        x0, y0 = self.canvas.winfo_pointerxy()
        x0 -= self.canvas.winfo_rootx()
        y0 -= self.canvas.winfo_rooty()
        # Check if the label is within any of the boxes
        for box in self.boxes:
            if box.coords_inside(x0, y0):
                # Create a new label at the released position
                new_label = tk.Label(self.canvas, text=original_label.cget('text'), bg=original_label.cget('bg'))
                new_label.config(image=original_label.image)
                new_label.image = original_label.image
                if original_label.cget('text') == "motors_forward":
                    self.orders.append(1)
                    new_label.bind("<Button-3>", lambda event, label=new_label: self.motors_forward_dialog(label))
                elif original_label.cget('text') == "motors_turn":
                    self.orders.append(2)
                    new_label.bind("<Button-3>", lambda event, label=new_label: self.motors_turn_dialog(label))
                elif original_label.cget('text') == "head_pan_label":
                    self.orders.append(3)
                    new_label.bind("<Button-3>", lambda event, label=new_label: self.head_pan_dialog(label))
                elif original_label.cget('text') == "head_tilt_label":
                    self.orders.append(4)
                    new_label.bind("<Button-3>", lambda event, label=new_label: self.head_tilt_dialog(label))
                elif original_label.cget('text') == "talking_label":
                    self.orders.append(5)
                    new_label.bind("<Button-3>", lambda event, label=new_label: self.talking_dialog(label))
                elif original_label.cget('text') == "waist_turn_label":
                    self.orders.append(6)
                    new_label.bind("<Button-3>", lambda event, label=new_label: self.waist_turn_dialog(label))
                elif original_label.cget('text') == "wait_for_input_label":
                    self.orders.append(7)
                    new_label.bind("<Button-3>", lambda event, label=new_label: self.wait_for_input_dialog(label))

                self.canvas.create_window(x0, y0, window=new_label, tags="motion_bound")
                self.icons.append(new_label)

    def motors_forward_dialog(self, label):
        if label in self.icons:
            menu = tk.Menu(self, tearoff=False)
            speed_menu = tk.Menu(menu, tearoff=False)
            speed_menu.add_command(label="Slow", command=lambda: self.set_motors_forwards(speed=200))
            speed_menu.add_command(label="Medium", command=lambda: self.set_motors_forwards(speed=500))
            speed_menu.add_command(label="Fast", command=lambda: self.set_motors_forwards(speed=800))

            distance_menu = tk.Menu(menu, tearoff=False)
            distance_menu.add_command(label="Short", command=lambda: self.set_motors_forwards(distance=1))
            distance_menu.add_command(label="Medium", command=lambda: self.set_motors_forwards(distance=2))
            distance_menu.add_command(label="Long", command=lambda: self.set_motors_forwards(distance=3))

            direction_menu = tk.Menu(menu, tearoff=False)
            direction_menu.add_command(label="Forward", command=lambda: self.set_motors_forwards(direction="Forward"))
            direction_menu.add_command(label="Left", command=lambda: self.set_motors_forwards(direction="Left"))
            direction_menu.add_command(label="Right", command=lambda: self.set_motors_forwards(direction="Right"))

            menu.add_cascade(label="Speed", menu=speed_menu)
            menu.add_cascade(label="Distance", menu=distance_menu)
            menu.add_cascade(label="Direction", menu=direction_menu)

            menu.post(label.winfo_rootx(), label.winfo_rooty())
        else:
            print("Icon must be dragged to the timeline before opening properties.")
    def motors_turn_dialog(self, label):
        if label in self.icons:
            menu = tk.Menu(self, tearoff=False)

            distance_menu = tk.Menu(menu, tearoff=False)
            distance_menu.add_command(label="Short", command=lambda: self.set_motors_turn(distance=1))
            distance_menu.add_command(label="Medium", command=lambda: self.set_motors_turn(distance=2))
            distance_menu.add_command(label="Long", command=lambda: self.set_motors_turn(distance=3))

            direction_menu = tk.Menu(menu, tearoff=False)
            direction_menu.add_command(label="Left", command=lambda: self.set_motors_turn(direction="Left"))
            direction_menu.add_command(label="Right", command=lambda: self.set_motors_turn(direction="Right"))

            menu.add_cascade(label="Distance", menu=distance_menu)
            menu.add_cascade(label="Direction", menu=direction_menu)

            menu.post(label.winfo_rootx(), label.winfo_rooty())
        else:
            print("Icon must be dragged to the timeline before opening properties.")
    def head_tilt_dialog(self, label):
        if label in self.icons:
            menu = tk.Menu(self, tearoff=False)

            direction_menu = tk.Menu(menu, tearoff=False)
            direction_menu.add_command(label="Left", command=lambda: self.set_head_tilt(direction="Left"))
            direction_menu.add_command(label="Right", command=lambda: self.set_head_tilt(direction="Right"))

            menu.add_cascade(label="Direction", menu=direction_menu)

            menu.post(label.winfo_rootx(), label.winfo_rooty())
        else:
            print("Icon must be dragged to the timeline before opening properties.")
    def head_pan_dialog(self, label):
        if label in self.icons:
            menu = tk.Menu(self, tearoff=False)

            direction_menu = tk.Menu(menu, tearoff=False)
            direction_menu.add_command(label="Up", command=lambda: self.set_head_pan(direction="Up"))
            direction_menu.add_command(label="Down", command=lambda: self.set_head_pan(direction="Down"))

            menu.add_cascade(label="Direction", menu=direction_menu)

            menu.post(label.winfo_rootx(), label.winfo_rooty())
        else:
            print("Icon must be dragged to the timeline before opening properties.")
    def waist_turn_dialog(self, label):
        if label in self.icons:
            menu = tk.Menu(self, tearoff=False)

            direction_menu = tk.Menu(menu, tearoff=False)
            direction_menu.add_command(label="Left", command=lambda: self.set_waist_turn(direction="Left"))
            direction_menu.add_command(label="Right", command=lambda: self.set_waist_turn(direction="Right"))

            menu.add_cascade(label="Direction", menu=direction_menu)

            menu.post(label.winfo_rootx(), label.winfo_rooty())
        else:
            print("Icon must be dragged to the timeline before opening properties.")

    def wait_for_input_dialog(self, label):
        if label in self.icons:
            menu = tk.Menu(self, tearoff=False)
            speed_menu = tk.Menu(menu, tearoff=False)
            speed_menu.add_command(label="Slow", command=lambda: print("Speed: Slow"))
            speed_menu.add_command(label="Medium", command=lambda: print("Speed: Medium"))
            speed_menu.add_command(label="Fast", command=lambda: print("Speed: Fast"))

            distance_menu = tk.Menu(menu, tearoff=False)
            distance_menu.add_command(label="Short", command=lambda: print("Distance: Short"))
            distance_menu.add_command(label="Medium", command=lambda: print("Distance: Medium"))
            distance_menu.add_command(label="Long", command=lambda: print("Distance: Long"))

            direction_menu = tk.Menu(menu, tearoff=False)
            direction_menu.add_command(label="Forward", command=lambda: print("Direction: Forward"))
            direction_menu.add_command(label="Left", command=lambda: print("Direction: Left"))
            direction_menu.add_command(label="Right", command=lambda: print("Direction: Right"))

            menu.add_cascade(label="Speed", menu=speed_menu)
            menu.add_cascade(label="Distance", menu=distance_menu)
            menu.add_cascade(label="Direction", menu=direction_menu)

            menu.post(label.winfo_rootx(), label.winfo_rooty())
        else:
            print("Icon must be dragged to the timeline before opening properties.")

    def talking_dialog(self, label):
        if label in self.icons:
            menu = tk.Menu(self, tearoff=False)
            speed_menu = tk.Menu(menu, tearoff=False)
            speed_menu.add_command(label="Hello", command=lambda: self.set_talking(speech="Hello my name is Robot 35"))
            speed_menu.add_command(label="Name", command=lambda: self.set_talking(speech="What is your name?"))
            speed_menu.add_command(label="Language", command=lambda: self.set_talking(speech="What is your favorite programming language?"))
            speed_menu.add_command(label="Class", command=lambda: self.set_talking(speech="What is your favorite class?"))

            menu.add_cascade(label="Speech", menu=speed_menu)
            menu.post(label.winfo_rootx(), label.winfo_rooty())
        else:
            print("Icon must be dragged to the timeline before opening properties.")

    def create_boxes(self):
        box_width = 50
        box_height = 50
        for i in range(3):
            for j in range(3):
                x = 200 + i * 200
                y = 70 + j * 120
                box = Box(self.canvas, x, y, box_width, box_height)
                self.boxes.append(box)
        
    def set_motors_forwards(self, speed = None, distance = None, direction = None):
        if speed != None:
            self.motors_forward.update(Speed = speed)
        if distance != None:
            self.motors_forward.update(Distance = distance)
        if direction != None:
            self.motors_forward.update(Direction = direction)

    def set_motors_turn(self, distance = None, direction = None):
        if distance != None:
            self.motors_turn.update(Distance = distance)
        if direction != None:
            self.motors_turn.update(Direction = direction)

    def set_head_tilt(self, direction = None):
        if direction != None:
            self.head_tilt.update(Direction = direction)

    def set_head_pan(self, direction = None):
        if direction != None:
            self.head_pan.update(Direction = direction)

    def set_waist_turn(self, direction = None):
        if direction != None:
            self.waist_turn.update(Direction = direction)

    def set_talking(self, speech = None):
        if speech != None:
            self.talking.update(Speech = speech)

    def create_canvas(self):
        # motors forward label
        motors_forward_label = tk.Label(self.canvas, text="motors_forward")
        image = tk.PhotoImage(file="motors_forward.png")
        motors_forward_label.config(image=image)
        motors_forward_label.image = image
        id_cLabel = self.canvas.create_window(50, 50, window=motors_forward_label)
        motors_forward_label.bind("<ButtonRelease-1>", lambda event: self.create_duplicate(motors_forward_label))

        # motors turn label
        motors_turn_label = tk.Label(self.canvas, text="motors_turn")
        image = tk.PhotoImage(file="motors_turn.png")
        motors_turn_label.config(image=image)
        motors_turn_label.image = image
        id_cLabel = self.canvas.create_window(50, 150, window=motors_turn_label)
        motors_turn_label.bind("<ButtonRelease-1>", lambda event: self.create_duplicate(motors_turn_label))

        # head pan label
        head_pan_label = tk.Label(self.canvas, text="head_pan_label")
        image = tk.PhotoImage(file="head_pan.png")
        head_pan_label.config(image=image)
        head_pan_label.image = image
        id_cLabel = self.canvas.create_window(50, 250, window=head_pan_label)
        head_pan_label.bind("<ButtonRelease-1>", lambda event: self.create_duplicate(head_pan_label))

        # head tilt label
        head_tilt_label = tk.Label(self.canvas, text="head_tilt_label")
        image = tk.PhotoImage(file="head_tilt.png")
        head_tilt_label.config(image=image)
        head_tilt_label.image = image
        id_cLabel = self.canvas.create_window(50, 350, window=head_tilt_label)
        head_tilt_label.bind("<ButtonRelease-1>", lambda event: self.create_duplicate(head_tilt_label))

        # Talking label
        talking_label = tk.Label(self.canvas, text="talking_label")
        image = tk.PhotoImage(file="talking.png")
        talking_label.config(image=image)
        talking_label.image = image
        id_cLabel = self.canvas.create_window(50, 450, window=talking_label)
        talking_label.bind("<ButtonRelease-1>", lambda event: self.create_duplicate(talking_label))

        # Waist turn label
        waist_turn_label = tk.Label(self.canvas, text="waist_turn_label")
        image = tk.PhotoImage(file="waist_turn.png")
        waist_turn_label.config(image=image)
        waist_turn_label.image = image
        id_cLabel = self.canvas.create_window(50, 550, window=waist_turn_label)
        waist_turn_label.bind("<ButtonRelease-1>", lambda event: self.create_duplicate(waist_turn_label))

        # Wait for input label
        wait_for_input_label = tk.Label(self.canvas, text="wait_for_input_label")
        image = tk.PhotoImage(file="wait_for_input.png")
        wait_for_input_label.config(image=image)
        wait_for_input_label.image = image
        id_cLabel = self.canvas.create_window(50, 650, window=wait_for_input_label)
        wait_for_input_label.bind("<ButtonRelease-1>", lambda event: self.create_duplicate(wait_for_input_label))

        # execute button
        execute_button_label = tk.Label(self.canvas, text="Execute", bg="green", fg="white", font=("Arial", 12), padx=10, pady=5, relief=tk.RAISED)
        image = tk.PhotoImage(file="wait_for_input.png")
        wait_for_input_label.config(image=image)
        wait_for_input_label.image = image
        execute_button_label.bind("<Button-1>", lambda event: self.execute())
        execute_button_id = self.canvas.create_window(150, 20, window=execute_button_label)


    def execute(self):
        t1 = threading.Thread(target=self.final)
        t1.start()
        t1.join()
    
    def final(self):
        robot_cotrol = RobotControl()
        for x in self.orders:
            if x == 1:
                if (self.motors_forward.get("Direction") == "Forward"):
                    robot_cotrol.moveBackwards(self.motors_forward.get("Speed"))
                    time.sleep(self.motors_forward.get("Distance"))
                if (self.motors_forward.get("Direction") == "Right"):
                    robot_cotrol.turnLeft(self.motors_forward.get("Speed"))
                    time.sleep(self.motors_forward.get("Distance"))
                if (self.motors_forward.get("Direction") == "Left"):
                    robot_cotrol.turnRight(self.motors_forward.get("Speed"))
                    time.sleep(self.motors_forward.get("Distance"))
            elif x == 2:
                if (self.motors_turn.get("Direction") == "Right"):
                    robot_cotrol.turnLeft(self.motors_turn.get("Speed"))
                    time.sleep(self.motors_turn.get("Distance"))
                if (self.motors_turn.get("Direction") == "Left"):
                    robot_cotrol.turnRight(self.motors_turn.get("Speed"))
                    time.sleep(self.motors_turn.get("Distance"))
            elif x == 3:
                if (self.motors_turn.get("Direction") == "Right"):
                    robot_cotrol.lookRight()
                    time.sleep(1)
                if (self.motors_turn.get("Direction") == "Left"):
                    robot_cotrol.lookLeft()
                    time.sleep(1)
            elif x == 4:
                if (self.motors_turn.get("Direction") == "Up"):
                    robot_cotrol.lookUp()
                    time.sleep(1)
                if (self.motors_turn.get("Direction") == "Down"):
                    robot_cotrol.lookDown()
                    time.sleep(1)
            elif x == 5:
                self.SpeakText(self.talking.get("Speech"))
            elif x == 6:
                if (self.motors_turn.get("Direction") == "Right"):
                    robot_cotrol.waistRight()
                    time.sleep(1)
                if (self.motors_turn.get("Direction") == "Left"):
                    robot_cotrol.waistLeft()
                    time.sleep(1)
            elif x == 7 :
                with sr.Microphone() as source:
                    r= sr.Recognizer()
                    r.adjust_for_ambient_noise(source)
                    r.dyanmic_energythreshhold = 3000
                    try:
                        print("Human: ", end="")
                        user_input = r.listen(source)            
                        user_input = r.recognize_google(user_input)
                        print(user_input)
                    except sr.UnknownValueError:
                        print("Don't know that word")
                print(user_input)
                
    def SpeakText(self, command):
        # Initialize the engine
        engine = pyttsx3.init()
        engine.say(command) 
        engine.runAndWait()

class Box:
    def __init__(self, canvas, x, y, width, height):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect_id = canvas.create_rectangle(x, y, x + width, y + height, outline="black", fill="")

    def coords_inside(self, x, y):
        return self.x < x < self.x + self.width and self.y < y < self.y + self.height


if __name__ == "__main__":
    main = Main()
    main.mainloop()
