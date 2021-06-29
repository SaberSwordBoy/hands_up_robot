import os
import random
import soundPlayer
import time
import serial

serial = serial.Serial("/dev/ttyACM0", 9600)

vulgar = False
loop = True
while True:
    line = serial.readline().encode("UTF-8").rstrip()
    print(line)
    