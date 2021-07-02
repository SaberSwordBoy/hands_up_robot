import os
import soundPlayer
import serial
from threading import Timer, Thread
from time import time

serial = serial.Serial("/dev/ttyACM0", 9600)

hands_down = True
delay_interval = 500

def on_hands_down():
    t = Thread(target=soundPlayer.playSound)
def on_hands_up():
    pass


vulgar = False
loop = True
while True:
    line = serial.readline().encode("UTF-8").rstrip()
    print(line)

    if line == "handsdown":
        hands_down = True
    elif line == 'handsup':
        hands_down = False
    else:
        pass
    if hands_down:
        timer = Timer(interval=delay_interval, function=on_hands_down)
        timer.start()
        print(timer)

