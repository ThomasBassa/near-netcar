from twisted.internet.defer import inlineCallbacks
from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner
import pygame
from twisted.internet import reactor, task
import os
from time import sleep
import json

class MyComponent(ApplicationSession):

    def read_joystick(self):
        print("reading joystick")
        events = pygame.event.get()
        if events.length == 0:
            self.verticalPosition = self.lastVertical
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.joyloop.stop()
            if event.type == pygame.JOYBUTTONDOWN:
                button = event.button
                print("Button {} on".format(button))
            if event.type == pygame.JOYBUTTONUP:
                button = event.button
                print("Button {} off".format(button))
            if event.type == pygame.JOYAXISMOTION:
                if event.axis == 0:
#                        val = (event.value, oldval[1])
                    self.horizPosition = event.value
                    self.verticalPosition = self.lastVertical
                    print("event value axis 1: {}".format(event.value))
                elif event.axis == 1:
                    self.verticalPosition = event.value
                    self.lastVertical = self.verticalPosition 
        os.system('cls' if os.name == 'nt' else 'clear')           
        try:
            #call function here
            joyvalues = {'horizontal':self.horizPosition, 'vertical': self.verticalPosition}
            #json_joyvalues = json.dumps(joyvalues)
            self.publish('aero.near.joystream', joyvalues)
            
            print("Sending Values - {}".format(joyvalues))
        except Exception as e:
            print("Error: {}".format(e))

    def joygood(self, value):
        print "joygood", value

    def joybad(self, error):
        print "joybad", error

    def onJoin(self, details):
        pygame.init()
        clock = pygame.time.Clock()
        pygame.joystick.init()

        joystick_count = pygame.joystick.get_count()
        for i in range(joystick_count):
            joystick = pygame.joystick.Joystick(i)
            joystick.init()

        self.horizPosition = 0.0
        self.verticalPosition = 0.0
        self.lastVertical = 0
        self.maxTurn = .25
        self.done = False
        print('Session Ready') 
        self.joyloop = task.LoopingCall(self.read_joystick)
        self.joyloop.start(.1)


if __name__ == '__main__':
    print("Main running")
    try:
        runner = ApplicationRunner(url = u"ws://104.197.24.18:8080/ws", realm = u"realm1")
        runner.run(MyComponent)
    except Exception as e:
        print("Error {}".format(e))