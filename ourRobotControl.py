from maestro import Controller   
import random                                                  

MOTORS = 0
TURN = 1
BODY = 2
HEADTILT = 4
HEADTURN = 3


class RobotControl():
    def __init__(self):
        self.tango = Controller()
        self.body = 6000
        self.headTurn = 6000
        self.headTilt = 6000
        self.motors = 6000
        self.turn = 6000

    def lookDown(self,val=200):
        self.headTilt -= val
        if(self.headTilt < 1510):
            self.headTilt = 1510
        self.tango.setTarget(HEADTILT, self.headTilt)
        print("Look down")

    def lookUp(self, amount=200):
        self.headTilt += amount
        if(self.headTilt > 7900):
            self.headTilt = 7900
        self.tango.setTarget(HEADTILT, self.headTilt)
        print("Look up")

    def lookRight(self, amount=200):
        self.headTurn += amount
        if(self.headTurn > 7900):
            self.headTurn = 7900
        self.tango.setTarget(HEADTURN, self.headTurn)
        print("Look Right")

    def defaultHead(self):
        self.headTilt = 6000
        self.headTurn = 6000
        self.tango.setTarget(HEADTURN, self.headTurn)
        self.tango.setTarget(HEADTILT, self.headTilt)

    def lookLeft(self, amount=200):
        self.headTurn -= amount
        if(self.headTurn < 1510):
            self.headTurn = 1510
        self.tango.setTarget(HEADTURN, self.headTurn)
        print("Look left")
        
    def waistLeft(self, amount=200):
        self.body -= amount
        if(self.body < 1510):
            self.body = 1510
        self.tango.setTarget(BODY, self.body)
        print ('waist left')

    def waistRight(self, amount=200):    
        self.body += amount
        if(self.body > 7900):
            self.body = 7900
        self.tango.setTarget(BODY, self.body)
        print("waist right")
        
            
    def moveFoward(self, amount=200):
        self.motors += amount
        if(self.motors > 7900):
            self.motors = 7900
        self.tango.setTarget(MOTORS, self.motors)
        print("Foward")
    
    def moveBackwards(self, amount=200):
        self.motors -= amount
        if(self.motors < 1510):
            self.motors = 1510
        self.tango.setTarget(MOTORS, self.motors)

    def turnRight(self, amount=200):
        self.turn += amount
        if(self.turn > 7400):
            self.turn = 7400
        self.tango.setTarget(TURN, self.turn)
        print("Turning Right")

    def slowTurnRight(self, amount=200):
        self.tango.setSpeed(TURN, 3)
        self.tango.setAccel(TURN, 3)
        self.turn += amount
        if(self.turn > 7400):
            self.turn = 7400
        self.tango.setTarget(TURN, self.turn)
        print("Turning Right")

    def turnLeft(self, amount=200):
        self.turn -= amount
        if(self.turn <2110):
            self.turn = 2110
        self.tango.setTarget(TURN, self.turn)
        print("Turning left")

    def defualtMotors(self):
        self.motors = 6000
        self.turn = 6000
        self.tango.setTarget(MOTORS, self.motors)
        self.tango.setTarget(TURN, self.turn)
        print("Defaulting motors")

    def defualtEverything(self):
        self.motors = 6000
        self.turn = 6000
        self.body = 6000
        self.headTilt = 6000
        self.headTurn = 6000
        self.rightShoulder = 6000
        self.rightBicep = 6000
        self.rightElbow = 6000
        self.rightUpperforarm = 6000
        self.rightWrist = 6000
        self.rightGripper = 6000
        self.leftShouler = 6000
        self.leftBicep = 6000
        self.leftElbow = 6000
        self.leftUpperForearm = 6000
        self.leftWrist = 6000
        self.leftGripper = 6000
        self.tango.setTarget(MOTORS, self.motors)
        self.tango.setTarget(TURN, self.turn)
        self.tango.setTarget(BODY, self.body)
        self.tango.setTarget(HEADTILT, self.headTilt)
        self.tango.setTarget(HEADTURN, self.headTurn)
        self.tango.setTarget(5, self.rightShoulder)
        self.tango.setTarget(6, self.rightBicep)
        self.tango.setTarget(7, self.rightElbow)
        self.tango.setTarget(8, self.rightUpperforarm)
        self.tango.setTarget(9, self.rightWrist)
        self.tango.setTarget(10, self.rightGripper)
        self.tango.setTarget(11, self.leftShouler)
        self.tango.setTarget(12, self.leftBicep)
        self.tango.setTarget(13, self.leftElbow)
        self.tango.setTarget(14, self.leftUpperForearm)
        self.tango.setTarget(15, self.leftWrist)
        self.tango.setTarget(16, self.leftGripper)
        print("Defaulting everything")

    def getRandomMovement(self):
        random_num = random.randint(1, 15)
        if random_num == 1:
            self.lookUp(800)
        elif random_num == 2:
            self.lookDown(800)
        elif random_num == 3:
            self.lookRight(800)
        elif random_num == 4:
            self.lookLeft(800)
        elif random_num == 5:
            self.defaultHead()
        elif random_num == 6:
            self.rightShoulderMove(7100)
        elif random_num == 7:
            self.leftShoulderMove(7100)
        elif random_num == 8:
            self.rightBicepMove(7000)
        elif random_num == 9:
            self.rightElbowMove(7000)
        elif random_num == 10:
            self.rightUpperForearmMove(7000)
        elif random_num == 11:
            self.rightUpperForearmMove(6000)
        elif random_num == 12:
            self.rightElbowMove(5000)
        elif random_num == 13:
            self.rightShoulderMove(5000)
        elif random_num == 14:
            self.waistRight(800)
        elif random_num == 15:
            self.waistLeft(800)
        # Maybe do the movement then defualt back after a second 
        #  OR add a third third that randomly defaults everything

    def rightShoulderMove(self, amount):
        self.rightShoulder = amount
        if(self.rightShoulder < 2110):
            self.rightShoulder = 2110
        if(self.rightShoulder > 7400):
            self.rightShoulder = 7400
        self.tango.setTarget(5, self.rightShoulder)

    def rightBicepMove(self, amount):
        self.rightBicep = amount
        if(self.rightBicep < 2110):
            self.rightBicep = 2110
        if(self.rightBicep > 7400):
            self.rightBicep = 7400
        self.tango.setTarget(6, self.rightBicep)

    def rightElbowMove(self, amount):
        self.rightElbow = amount
        if(self.rightElbow < 2110):
            self.rightElbow = 2110
        if(self.rightElbow > 7400):
            self.rightElbow = 7400
        self.tango.setTarget(7, self.rightElbow)
        
    def rightUpperForearmMove(self, amount):
        self.rightUpperforarm = amount
        if(self.rightUpperforarm < 2110):
            self.rightUpperforarm = 2110
        if(self.rightUpperforarm > 7400):
            self.rightUpperforarm = 7400
        self.tango.setTarget(8, self.rightUpperforarm)
        
    def rightWristMove(self, amount):
        self.rightWrist = amount
        if(self.rightWrist < 2110):
            self.rightWrist = 2110
        if(self.rightWrist > 7400):
            self.rightWrist = 7400
        self.tango.setTarget(9, self.rightWrist)

    def rightGripperMove(self, amount):
        self.rightGripper = amount
        if(self.rightGripper < 2110):
            self.rightGripper = 2110
        if(self.rightGripper > 7400):
            self.rightGripper = 7400
        self.tango.setTarget(10, self.rightGripper)

    def leftShoulderMove(self, amount):
        self.leftShouler = amount
        if(self.leftShouler < 2110):
            self.leftShouler = 2110
        if(self.leftShouler > 7400):
            self.leftShouler = 7400
        self.tango.setTarget(11, self.leftShouler)

    def leftBicepMove(self, amount):
        self.leftBicep = amount
        if(self.leftBicep < 2110):
            self.leftBicep = 2110
        if(self.leftBicep > 7400):
            self.leftBicep = 7400
        self.tango.setTarget(12, self.leftBicep)

    def leftElbowMove(self, amount):
        self.leftElbow= amount
        if(self.leftElbow < 2110):
            self.leftElbow = 2110
        if(self.leftElbow > 7400):
            self.leftElbow = 7400
        self.tango.setTarget(13, self.leftElbow)

    def leftUpperForearmMove(self, amount):
        self.leftUpperForearm= amount
        if(self.leftUpperForearm < 2110):
            self.leftUpperForearm = 2110
        if(self.leftUpperForearm > 7400):
            self.leftUpperForearm = 7400
        self.tango.setTarget(14, self.leftUpperForearm)

    def leftWristMove(self, amount):
        self.leftWrist= amount
        if(self.leftWrist < 2110):
            self.leftWrist = 2110
        if(self.leftWrist > 7400):
            self.leftWrist = 7400
        self.tango.setTarget(15, self.leftWrist)

    def leftGripperMove(self, amount):
        self.leftGripper = amount
        if(self.leftGripper < 2110):
            self.leftGripper = 2110
        if(self.leftGripper > 7400):
            self.leftGripper = 7400
        self.tango.setTarget(16, self.leftGripper)

    def resetRight(self):
        self.robot_controll.setTarget(5, 5900)
    
    def resetLeft(self):
        self.robot_controll.setTarget(11, 5900)

    def close(self):
        self.robot_controll.close()
