from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner
from twisted.internet.defer import inlineCallbacks




class MyComponent(ApplicationSession):

    def debug1(self, stuff):
        print (stuff)
    def onJoin(self, details):
        print ('Session Joined')
        
        self.register(self.debug1, "joystream")
        #self.register(self.debug, 'aero.near.joystream')
        #self.subscribe(self.debug, 'pubtest')
        print ('regged')
    

if __name__ == '__main__':
    print ("I'M TRYING.")
    runner = ApplicationRunner(url = u"ws://104.197.24.18:8080/ws", realm = u"realm1")
    runner.run(MyComponent)