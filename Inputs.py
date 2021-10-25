import sys

import pygame

pygame.init()

clock = pygame.time.Clock()

pygame.joystick.init()

joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]


while True:
    for event in pygame.event.get():
        if event.type == pygame.JOYAXISMOTION:
            if event.axis == 5:
                print("Forward", event.value)
            if event.axis == 4:
                print("Backward ", event.value)
        if event.type == pygame.JOYHATMOTION:
            if event.value == (1, 0):
                print("Right")
            if event.value == (-1, 0):
                print("Left")

            
            
    


