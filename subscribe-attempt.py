from os import environ
from twisted.internet.defer import inlineCallbacks

from autobahn.wamp.types import CallResult
from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner

class Component(ApplicationSession):

    def onJoin(self, details):
        res = yield self.call('com.myapp.addNumbers', 2, 3)
        print("Got result: {}".format(res))
