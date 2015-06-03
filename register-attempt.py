from os import environ
from twisted.internet import reactor
from twisted.internet.defer import inlineCallbacks

from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner

class MyComponent(ApplicationSession):

    def onJoin(self, details):

        def addNumbers(x, y):
           return x + y
           self.register(addNumbers, 'aero.near.addNumbers');

