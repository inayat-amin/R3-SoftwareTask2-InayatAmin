import sys

import pygame

pygame.init()

clock = pygame.time.Clock()

pygame.joystick.init()

joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]


while True:
    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == 0:
                print(event)
                print("A has been pressed")
            if event.button == 1:
                print("B has been pressed")
        if event.type == pygame.JOYHATMOTION:
            if event.value == (1, 0):
                print("Right")
            if event.value == (-1, 0):
                print("Left")
            
            
    


