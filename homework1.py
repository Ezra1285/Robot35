import control_robot
import time


if __name__ == "__main__":
    robot_instance = control_robot.robot()
    robot_instance.headUp()
    time.sleep(3)
    robot_instance.centerHead()
    time.sleep(3)
    robot_instance.headDown()
    robot_instance.centerHead()
    time.sleep(3)