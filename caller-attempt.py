'''finally works'''

from os import environ
from twisted.internet.defer import inlineCallbacks

from autobahn.wamp.types import CallResult
from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner

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
    runner = ApplicationRunner(
        environ.get("AUTOBAHN_DEMO_ROUTER", "ws://104.197.76.36:8080/ws"),
        u"realm1",
        extra=dict(
            max_events=5,  # [A] pass in additional configuration
        ),
        debug_wamp=False,  # optional; log many WAMP details
        debug=False,  # optional; log even more details
    )
    runner.run(MyComponent)
