from twisted.internet.defer import inlineCallbacks
from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner
import pygame
from twisted.internet import reactor, task
import os
from time import sleep

class MyComponent(ApplicationSession):

    def read_joystick(self):
        print("reading joystick")
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
                    print("event value axis 1: {}".format(event.value))
                elif event.axis == 1:
                    self.verticalPosition = event.value
        os.system('cls' if os.name == 'nt' else 'clear')            
        try:
            #call function here
            joyvalues = {'horizontal':(self.horizPosition), 'vertical': (self.verticalPosition / 2)}
            #json_joyvalues = json.dumps(joyvalues)
            self.publish('aero.near.joystream', joyvalues)
            print("sent stuff: {}".format(joyvalues))
        except Exception as e:
            print("Error: {}".format(e))

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