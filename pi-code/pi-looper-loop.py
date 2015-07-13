    def looper():
     for startUp in range(0,8):
       rotor(2,startUp)
       checkGPS()
       checkColour()
     #this doesn't work yet
     #while(true = true):
       for downCount in range(0,16):
         rotor(2,downCount)
         checkGPS()
         checkColour()
       for upCount in range(0,16):
         rotor(2,upCount)
         checkGPS()
         checkColour()


