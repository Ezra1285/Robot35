import maestro

class robot:
    
    def __init__(self):
        self.robot_controll = maestro.Controller()
        self.robot_controll.setAccel(0,60)
        self.robot_controll.setSpeed(0, 10)
        self.robot_controll.setTarget(0, 6000)
        self.waist = 6000
        self.headTurn = 6000
        self.headTilt = 6000
        self.turn = 6000

    #  Handle body movement
    def move_forward(self):
        # self.robot_controll.setTarget(0, 6000)
        # self.robot_controll.setTarget(1, 6000)
        self.robot_controll.setTarget(0, 4500)
        self.robot_controll.setTarget(1, 7500)
        # print("forward")

    def reverse(self):
        self.robot_controll.setTarget(0, 6000)
        self.robot_controll.setTarget(0, 6000)
        self.robot_controll.setTarget(1, 5500)
        # print("forward")

    def fullyStop(self):
        self.robot_controll.setAccel(0,60)
        self.robot_controll.setSpeed(0, 10)
        self.robot_controll.setAccel(1,60)
        self.robot_controll.setSpeed(1, 10)
        self.robot_controll.setTarget(2, 6000)
        self.robot_controll.setTarget(0, 6000)
        self.robot_controll.setTarget(1, 6000)
        # print("Full stop")

    def stop(self):
        self.robot_controll.setTarget(2, 6000)
        self.robot_controll.setTarget(0, 6000)
        # print("Stop")

    def right_forward(self):
        self.robot_controll.setTarget(0, 5200)
        self.robot_controll.setTarget(2, 7000)
        # print("left foward")

    def left_forward(self):
        self.robot_controll.setTarget(0, 5200)
        self.robot_controll.setTarget(2, 5000)
        # print("right forward")

    def right(self):
        self.robot_controll.setTarget(0, 5500)
        self.robot_controll.setTarget(2, 7000)
        # print("left")

    def left(self):
        self.robot_controll.setTarget(1, 5500)
        self.robot_controll.setTarget(2, 5000)
        # print("right")

    def spinInCircle(self):
        self.robot_controll.setSpeed(2, 5)
        self.robot_controll.setSpeed(2, 5)
        self.robot_controll.setTarget(2, 6800)

    def startSpin(self, speed=7000):
        self.robot_controll.setSpeed(2, 3)
        self.robot_controll.setAccel(2, 3)
        self.robot_controll.setTarget(2, speed)
        # print("Start spin")
        
    def stopSpin(self):
        self.robot_controll.setSpeed(2, 0)
        self.robot_controll.setAccel(2, 0)
        self.robot_controll.setTarget(2, 6000) 
        # print("Stop spin")

    #  handle waist movement
    def waistRight(self):
        self.waist += 200
        if(self.waist > 7900):
            self.waist = 7900
        # print("waist ", self.waist)
        self.robot_controll.setTarget(2, self.waist)

    def waistLeft(self):
        self.waist -= 200
        if(self.waist < 1510):
            self.waist = 1510
        self.robot_controll.setTarget(2, self.waist)

    #  handle head movement(Working)
    def headRight(self):
        self.headTurn += 200
        if(self.headTurn > 7900):
            self.headTurn = 7900
        self.robot_controll.setTarget(3, self.headTurn)

    def headLeft(self):
        self.headTurn -= 200
        if(self.headTurn < 1510):
            self.headTurn = 1510
        self.robot_controll.setTarget(3, self.headTurn)
    
    def headFullyLeft(self):
        self.robot_controll.setTarget(3, 1510)

    def headUp(self):
        self.headTilt += 200
        if(self.headTilt > 7900):
            self.headTilt = 7900
        self.robot_controll.setTarget(4, self.headTilt)

    def centerHead(self):
        self.robot_controll.setTarget(4, 5750)

    def headDown(self):
        self.headTilt -= 200
        if(self.headTilt < 1510):
            self.headTilt = 1510
        self.robot_controll.setTarget(4, self.headTilt)

    def headFullyDown(self):
        self.robot_controll.setTarget(4, 1510)

    def headFullyUp(self):
        self.robot_controll.setTarget(4, 7900)

    def headstraight(self):
        self.headTilt = 1800
        self.robot_controll.setTarget(4, self.headTilt)

    def rightShoulder(self):
        self.robot_controll.setTarget(5, 6000)

    def rightBicep(self):
        self.robot_controll.setTarget(6, 6000)

    def rightElbow(self):
        self.robot_controll.setTarget(7, 6000)

    def rightUpperForearm(self):
        self.robot_controll.setTarget(8, 6000)

    def rightWrist(self):
        self.robot_controll.setTarget(9, 6000)

    def rightGripperClose(self):
        self.robot_controll.setTarget(10, 6000)

    def leftShoulder(self):
        self.robot_controll.setTarget(11, 6000)

    def leftBicep(self):
        self.robot_controll.setTarget(12, 6000)

    def leftElbow(self):
        self.robot_controll.setTarget(13, 6000)

    def leftUpperForearm(self):
        self.robot_controll.setTarget(14, 6000)

    def leftWrist(self):
        self.robot_controll.setTarget(15, 6000)

    def leftGripperClose(self):
        self.robot_controll.setTarget(16, 6000)
    
    def resetRight(self):
        self.robot_controll.setTarget(5, 5900)
    
    def resetLeft(self):
        self.robot_controll.setTarget(11, 5900)

    def close(self):
        self.robot_controll.close()
