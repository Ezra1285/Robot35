#  Project 1 (part 6): Some code working on PI to move one servo with code. Proving the serial port is on.
#  We show the head moving up and down in this program.
import control_robot
import time


def main():
    robot_instance = control_robot.robot()
    robot_instance.move_forward()
    time.sleep(2)
    robot_instance.reverse()
    time.sleep(2)
    robot_instance.fullyStop()
    robot_instance.right()
    time.sleep(2)
    robot_instance.left()
    time.sleep(2)
    robot_instance.waistLeft()
    time.sleep(2)
    robot_instance.waistRight()
    time.sleep(2)
    # robot_instance.headUp()
    # time.sleep(1)
    # robot_instance.headDown()
    # time.sleep(1)
    # robot_instance.headLeft()
    # time.sleep(1)
    # robot_instance.headRight()
    # time.sleep(1)
    # robot_instance.centerHead()
    # time.sleep(1)
    # robot_instance.rightShoulder()
    # time.sleep(2)
    # robot_instance.rightBicep()
    # time.sleep(2)
    # robot_instance.rightElbow()
    # time.sleep(2)
    # robot_instance.rightUpperForearm()
    # time.sleep(2)
    # robot_instance.rightWrist()
    # time.sleep(2)
    # robot_instance.rightGripperClose()
    # time.sleep(2)
    # robot_instance.resetRight()
    # robot_instance.leftShoulder()
    # time.sleep(2)
    # robot_instance.leftBicep()
    # time.sleep(2)
    # robot_instance.leftElbow()
    # time.sleep(2)
    # robot_instance.leftUpperForearm()
    # time.sleep(2)
    # robot_instance.leftWrist()
    # time.sleep(2)
    # robot_instance.leftGripperClose()
    # robot_instance.resetLeft()
    robot_instance.close()

if __name__ == "__main__":
    main()