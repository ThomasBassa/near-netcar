from twisted.internet.defer import inlineCallbacks
from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner
import pygame
from twisted.internet import reactor, task

pygame.init()
clock = pygame.time.Clock()
pygame.joystick.init()

joystick_count = pygame.joystick.get_count()
for i in range(joystick_count):
    joystick = pygame.joystick.Joystick(i)
    joystick.init()
    name = joystick.get_name()
val = None
class MyComponent(ApplicationSession):

    def onJoin(self, details):
        global val
        val = (0.0,0.0)
        done = False
        print("Session Ready")
        @inlineCallbacks
        def update():
            global val
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
                        oldvalue = val[1]
                        val = (event.value, oldvalue)
                    elif event.axis == 1:
                        oldvalue = val[0]
                        val = (oldvalue, event.value)
            try:
                yield self.call('aero.near.joyMonitor', val[0], val[1])
#                yield self.call('aero.near.joyMonitor', val[1])
            except Exception as e:
                print("Error {}".format(e))
            print("Axis {} at {}".format(0, val[0]))
            print("Axis {} at {}".format(1, val[1]))
#            print("Axis {} at {}".format(2, val[2]))
        l = task.LoopingCall(update)
        l.start(.033333)
#        reactor.run()
if __name__ == '__main__':
    print("Main running")
    val = (0.0, 0.0)
    try:
        runner = ApplicationRunner(url = u"ws://104.197.76.36:8080/ws", realm = u"realm1")
        runner.run(MyComponent)
    except Exception as e:
        print("Error {}".format(e))