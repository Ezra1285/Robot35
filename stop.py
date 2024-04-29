import tkinter as tk
from ourRobotControl import RobotControl
import threading
import pyttsx3
from tkinter import simpledialog
from tkinter import messagebox
import time
import speech_recognition as sr
robot = RobotControl()
robot.defualtEverything()