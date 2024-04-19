from new_keyboard_control import KeyControl
import serial
import time
# data = b"$KT1,NULL,0.91,2.68,NULL,LO=[no soultion]\r\n"

# data = data.decode('utf-8').split(",")

class myTest:

    def __init__(self):
        self.chip = serial.Serial() 
        self.chip.port = '/dev/ttyUSB0' 
        self.chip.baudrate = 115200 
        self.chip.bytesize = serial.EIGHTBITS 
        self.chip.parity = serial.PARITY_NONE 
        self.chip.stopbits = serial.STOPBITS_ONE 
        self.chip.timeout = self.chip.open()
        self.robot_contol = KeyControl()

    def readData(self):
        line1 = self.chip.readline()
        line2 = self.chip.readline()
        data = line2.decode('utf-8').split(",")
        print("Text 1 found: ", line1)
        print("Text 2 found: ", line2)
        return data


    def spinCycle(self):
        self.robot_contol.lookUp('a', 800)
        time.sleep(1)
        self.cords = self.readData()
                
        # self.robot_contol.turnRight('a', 400)
        # time.sleep(1)
        # self.robot_contol.defualtMotors()
        # self.cords = self.readData()


t = myTest()
t.spinCycle()
t.robot_contol.defaultHead()
t.robot_contol.defualtMotors()