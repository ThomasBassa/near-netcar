class MyComponent(ApplicationSession):

   @inlineCallbacks
   def onJoin(self, details):

      # 1) subscribe to a topic
      def onevent(msg):
         print("Got event: {}".format(msg))

      yield self.subscribe(onevent, 'com.myapp.hello')

      # 2) publish an event
      self.publish('com.myapp.hello', 'Hello, world!')

      # 3) register a procedure for remoting
      def add2(x, y):
         return x + y

      self.register(add2, 'com.myapp.add2');

      # 4) call a remote procedure
      res = yield self.call('com.myapp.add2', 2, 3)
      print("Got result: {}".format(res))
