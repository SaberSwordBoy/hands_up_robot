import os
import soundPlayer
import serial
from threading import Timer, Thread
from time import time

serial = serial.Serial("/dev/ttyACM0", 9600)

hands_down = True
delay_interval = 500

strings = ['handsup', 'handsdown']

def on_hands_down():
    soundPlayer.playSound()

loop = True
while loop:
    line = serial.readline()
    
