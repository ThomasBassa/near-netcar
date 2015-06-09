from twisted.internet.defer import inlineCallbacks

from autobahn.wamp.types import CallResult
from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner

class MyComponent(ApplicationSession):

    def onJoin(self, details):
        res = yield self.call('aero.near.addNumbers', 2, 3)
        print("Got result: {}".format(res))

if __name__ == '__main__':
    runner = ApplicationRunner(url = u"ws://104.197.76.36:8080/ws", realm = u"realm1")
    runner.run(MyComponent)
