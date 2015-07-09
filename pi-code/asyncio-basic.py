from os import environ
import trollius as asyncio
from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner

class MyComponent(ApplicationSession):

    @asyncio.coroutine
    def onJoin(self, details):
        print("Session Joined.")


if __name__ == '__main__':
    print "IM TRYING"
    runner = ApplicationRunner(url = u"ws://10.33.92.126:18080/ws", realm = u"realm1")
    runner.run(MyComponent)