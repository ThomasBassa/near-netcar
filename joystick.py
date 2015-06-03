'''
Created by Jayson Clifford
Copyright (c) 2015 Embry-Riddle NextGen Applied Research Lab.
All rights reserved.
'''

import pygame

done = False

pygame.init()
clock = pygame.time.Clock()
pygame.joystick.init()

joystick_count = pygame.joystick.get_count()
for i in range(joystick_count):
    joystick = pygame.joystick.Joystick(i)
    joystick.init()
    name = joystick.get_name()

while done is False:
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            done = True
        if event.type == pygame.JOYBUTTONDOWN:
            button = event.button
            print("Button {} on".format(button))
        if event.type == pygame.JOYBUTTONUP:
            button = event.button
            print("Button {} off".format(button))
        if event.type == pygame.JOYAXISMOTION:
            val = event.value
            axis = event.axis
            print("Axis {} at {}".format(axis, val))
    
        '''
        name = joystick.get_name()
        
        axes = joystick.get_numaxes()
        for i in range( axes ):
            axis = joystick.get_axis( i )

        buttons = joystick.get_numbuttons()    
        for i in range( buttons ):
            button = joystick.get_button( i )

        hats = joystick.get_numhats()
        for i in range( hats ):
            hat = joystick.get_hat( i )
        '''
                                
    clock.tick(20)
