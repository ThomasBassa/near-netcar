from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner

class MyComponent(ApplicationSession):

    def onJoin(self, details):
        print ('Session Joined')
        self.subscribe(self.got_joy, 'aero.near.joystream')
        #self.subscribe(self.debug, 'pubtest')
        #self.publish("joystream", "hello")
        #self.call("joystream", "hello").addCallback(self.debug)
        print ('subbed')

    def got_joy(self, joyvalues):
        print ("recieved stuff: {}".format(joyvalues))

if __name__ == '__main__':
    print ("I'M TRYING.")
    runner = ApplicationRunner(url = u"ws://104.197.24.18:8080/ws", realm = u"realm1")
    runner.run(MyComponent)


