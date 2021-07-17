import os
import random
import pygame
import time

pygame.mixer.init()
def get_random_voice(vulgar=False):
    files = []
    for _, _, f in os.walk("hands_up_robot/hands_up_robot/raspi/sounds"):
        for file in f:
            files.append(file)
    return random.choice(files)

def playSound():
    soundName = get_random_voice()
    sound = pygame.mixer.Sound("hands_up_robot/hands_up_robot/raspi/sounds/" + soundName)
    print(f"[#] Playing {soundName}")
    sound.set_volume(1)

    sound.play(0)
    time.sleep(sound.get_length())

def playShutdownSound():
    sound = pygame.mixer.Sound("hands_up_robot/hands_up_robot/raspi/SHUTDOWN.wav")
    sound.play(0)
    time.sleep(sound.get_length())
