import os
import random
import pygame
import time

pygame.mixer.init()
def get_random_voice(vulgar=False):
    files = []
    for _, _, f in os.walk("sounds"):
        for file in f:
            files.append(file)
    print(files)
    return random.choice(files)

def playSound():
    sound = pygame.mixer.Sound("sounds/" + get_random_voice())
    sound.set_volume(1)
    print(sound.get_volume())
    sound.play(0)
    time.sleep(sound.get_length())
