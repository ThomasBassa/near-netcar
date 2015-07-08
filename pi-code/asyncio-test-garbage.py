from os import environ
import asyncio
from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner

class MyComponent(ApplicationSession):

    @asyncio.coroutine
    def onJoin(self, details):
        print("Session Joined.")


if __name__ == '__main__':
    runner = ApplicationRunner(
        environ.get("AUTOBAHN_DEMO_ROUTER", "ws://192.168.1.30:8080/ws"),
        u"crossbardemo",
        debug_wamp=False,  # optional; log many WAMP details
        debug=False,  # optional; log even more details
    )
    runner.run(MyComponent)