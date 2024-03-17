#  Project 1 (part 6): Some code working on PI to move one servo with code. Proving the serial port is on.
#  We show the head moving up and down in this program.
import control_robot
import time


def main():
    robot_instance = control_robot.robot()
    robot_instance.headUp()
    time.sleep(3)
    robot_instance.centerHead()
    time.sleep(3)
    robot_instance.headDown()
    time.sleep(3)
    robot_instance.centerHead()
    time.sleep(3)
    robot_instance.close()

if __name__ == "__main__":
    main()