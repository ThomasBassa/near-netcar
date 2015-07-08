from twisted.internet.defer import inlineCallbacks
from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner
import pygame
from twisted.internet import reactor, task
import os
from time import sleep


pygame.init()
clock = pygame.time.Clock()
pygame.joystick.init()

joystick_count = pygame.joystick.get_count()
for i in range(joystick_count):
    joystick = pygame.joystick.Joystick(i)
    joystick.init()
    name = joystick.get_name()
val = None
oldval = None
class MyComponent(ApplicationSession):
    global val
    global oldval
    global maxTurn
    global horizPosition
    global verticalPosition
    horizPosition = 0.0
    verticalPosition = 0.0
    maxTurn = .05


    def onJoin(self, details):
        global val
        global oldval
        global horizPosition
        global verticalPosition
        val = (0.0,0.0)
        oldval = (0.0, 0.0)
        done = False
        print('Session Ready')

        def interpolate():
            global val
            global oldval
            global horizPosition
            global verticalPosition
#            ifPositive = True
#            if val[0] - oldval[0] <= 0:
#                ifPositive = False
#            print(ifPositive)
            diff = oldval[0] - val[0]
            if diff > maxTurn:
                diff = maxTurn
            elif diff < (maxTurn*-1):
                diff = maxTurn*-1
#            if ifPositive == False:
#                diff = diff * -1
            print("diff: {}".format(diff))
            axiszeroold = val[0]
            val = (axiszeroold + diff, verticalPosition)
            if val[0] >  1:
                val = (1,verticalPosition)
            elif val[0] < -1:
                val = (-1,verticalPosition)
            oldval = (horizPosition,verticalPosition)
            print("val set")
            print("Axis 0 at {}".format(val[0]))
            print("Axis 1 at {}".format(val[1]))
            print("Old 0: {}".format(oldval[0]))
            print("Old 1: {}".format(oldval[1]))
            self.call('aero.near.joyMonitor', val[0], val[1])

        @inlineCallbacks
        def update():
            global val
            global oldval
            global horizPosition
            global verticalPosition

            print("updating")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.JOYBUTTONDOWN:
                    button = event.button
                    print("Button {} on".format(button))
                if event.type == pygame.JOYBUTTONUP:
                    button = event.button
                    print("Button {} off".format(button))
                if event.type == pygame.JOYAXISMOTION:
                    if event.axis == 0:
#                        val = (event.value, oldval[1])
                        horizPosition = event.value
                        print("event value axis 1: {}".format(event.value))
                    elif event.axis == 1:

                        verticalPosition = event.value
            os.system('cls' if os.name == 'nt' else 'clear')            
            try:
                #call function here
                print("trying to interpolate")
                yield interpolate()
                yield self.call('aero.near.joyMonitor', val[0], val[1])		
            except Exception as e:
                print("Error: {}".format(e))
            
        
        print("Jimmy's a big 'ole butthead!")
        print("Axis {} at {}".format(0, val[0]))
        print("Axis {} at {}".format(1, val[1]))
#            print("Axis {} at {}".format(2, val[2]))
        l = task.LoopingCall(update)
        l.start(.03333)
#        l.start(.033333)
#        reactor.run()
if __name__ == '__main__':
    print("Main running")
    val = (0.0, 0.0)
    try:
        runner = ApplicationRunner(url = u"ws://10.33.92.126:18080/ws", realm = u"realm1")
        runner.run(MyComponent)
    except Exception as e:
        print("Error {}".format(e))