'''finally works'''

from twisted.internet.defer import inlineCallbacks

from autobahn.wamp.types import CallResult
from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner

# TODO There are mixed tabs and spaces in this file-- re-indent WITH SPACES ONLY
class MyComponent(ApplicationSession):

    @inlineCallbacks
    def onJoin(self, details):
        print("Session ready")

        try:
            res = yield self.call(u'aero.near.addNumbers', 2, 3)
            print("Got result: {}".format(res))
        except Exception as e:
            print("call error: {0}".format(e))


if __name__ == '__main__':
    runner = ApplicationRunner(url = u"ws://104.197.76.36:8080/ws", realm = u"realm1")
    runner.run(MyComponent)
