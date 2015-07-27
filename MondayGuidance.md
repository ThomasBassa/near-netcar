VEHICLE TESTING

I'm sure there's more testing that needs to be done to smooth out the vehicle's driving. That is important. Test test test test. Make sure you keep an eye on the temperature of the battery stick (assuming the battery stick isn't replaced by Monday). Also remember to test the LiPo's voltage frequently. If it gets below 11.5, we need to charge it probably. All 3 LiPos are in the LiPo safe bag downstairs. All three are fully charged. The red LiPo is for the remote. Make sure you don't switch red and black wires when you plug it into the remote control.

If you get the I2C error, it's coming from the servo driver (blue stick). There might be some partial connections between it and the T-shaped Pi connector or between the T-shaped Pi connector and the Pi. Jiggle things around until the error goes away or carefully disconnect one wire at a time (involved in the I2C) and reconnect it to see which connection is bad.



CODE STUFF

Make sure files are organized based on functionality. You guys know how to import files that are in the same directory and call methods written in those files. Implementing those initialization functions you guys wrote would be good. Determine what we need for error handling to be done properly. 



HARDWARE STUFF

You guys did a good job on Wednesday arranging everything. We should TRY to find an alternative to the ribbon cable and the T-shaped Pi thing. All the pins on the T-shaped Pi thing are exposed. That is bad. And the ribbon cable is far too long for what we're doing. Which is also bad. This alternative might involve a breakout board or it might involve a shorter cable.



EVERYTHING

Record all your tests in Excel and push code to github when you know it works.

We have time to add in additional functionality. We don't have Lidar, so we can't do anything there. It's possible we have something in our sensor box that will be usable. Ultrasonic probably won't be helpful because it is so short range. I can't find the GPS module at all. Please locate it if you can. GPS would be easy to implement without breaking anything!!!!! Which is great.

Do whatever you think needs to be done. This file just contains some ideas.

