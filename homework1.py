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
    robot_instance.move_forward()
    time.sleep(1)
    robot_instance.fullyStop()
    robot_instance.close()