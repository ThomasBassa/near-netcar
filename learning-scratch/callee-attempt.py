'''registers the function addNumbers, gives it a URI. Based on the register-attempt.py code that Alex fixed'''

from twisted.internet.defer import inlineCallbacks
from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner

class MyComponent(ApplicationSession):

    @inlineCallbacks
    def onJoin(self, details):
	print("session ready")


        def addNumbers(x, y):
           return x + y
        
	try:
            yield self.register(addNumbers, u'aero.near.addNumbers')
            print("Procedure registered.")
        except Exception as e:
            print("Could not register procedure: {0}".format(e))

if __name__ == '__main__':
    runner = ApplicationRunner(url = u"ws://104.197.76.36:8080/ws", realm = u"realm1")
    runner.run(MyComponent)
