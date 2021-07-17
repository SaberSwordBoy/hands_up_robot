import os
import soundPlayer
import serial
import time
import sys
import datetime

with open("logs.txt", "a") as f:
    f.write(f"[#] STARTED - {time.time()}")

serial = serial.Serial("/dev/ttyACM0", 9600, timeout=0)

hands_up = False
delay_interval = 5
strings = [b"handsup", b"handsdown"]

def on_hands_down():
    print('KEEP YA HANDS UP')
    soundPlayer.playSound()

vulgar = False
loop = True
timer = 0
shutdown_timer = 0
shutdown_time = 20
timer_length = 5
print("[!] Starting Up...")

while loop:
    os.system('clear')
    line = serial.readline()
    print("[~] Read Line: ", end="")
    print(line)
    timer += 0.3
    if shutdown_timer >= shutdown_time:
        print("SHUTTING DOWN")
        soundPlayer.playShutdownSound()
        sys.exit()
    if timer >= timer_length:
        on_hands_down()
        timer = 0
    if strings[0] in line:
        hands_up = True
    elif strings[1] in line:
        hands_up = False
    print(f"[#] hands_up: {hands_up}")
    if hands_up:
        shutdown_timer += 0.3
        timer = 0
    if not hands_up:
        shutdown_timer = 0
    print(f"[#] Timer: {timer}")
    print(f"[#] ShutDown Timer: {shutdown_timer}")

    time.sleep(0.1)
   
