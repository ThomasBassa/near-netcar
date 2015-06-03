from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner

class MyComponent(ApplicationSession):

   def onJoin(self, details):
      print("session joined")
      print("Jimmy's a big 'ole butthead")	

if __name__ == '__main__':
   runner = ApplicationRunner(url = u"ws://104.197.76.36:8080/ws", realm = u"realm1")
   runner.run(MyComponent)	
