# Requirements

## Hardware

####Sound and Lights:
* The vehicle shall be mounted with a light
* The light shall be on while the vehicle is powered
* The light shall be visible to any sighted person in the forward path of the vehicle with an unobstructed view of the light source
* The vehicle shall be mounted with a noise device
* The noise device shall sound when an obstacle is detected 20 m from the vehicle's front bumper
* The noise device shall generate between 60 and 80 decibels when sounding


##Vehicle Motion:
* The vehicle shall be able to move forward
   - (Note)The vehicle's forward motion shall be controlled by the onboard motors
* The vehicle shall be able to move backwards
   - (Note)The vehicle's backward motion shall be controlled by the onboard motors
* The vehicle shall be able to turn left
   - (Note)The vehicle's turn direction shall be controlled by an onboard servo
* The vehicle shall be able to turn right
   - (Note)The vehicle's turn direction shall be controlled by an onboard servo
* The vehicle's speed shall not exceed 30mph
* The vehicle's motion shall be controlled by ground control
* The vehicle shall stop all movement when communication with ground control is interrupted
* The vehicle shall be able to remotely reconnect with ground control upon signal loss
* The vehicle shall be able to operate for at least an hour at a time###The vehicle shall be able to operate for at least an hour at a time

##Obstacle Avoidance

* The vehicle shall stop after detecting an object in its direct path
* The vehicle shall stop a minimum of 5 m from a detected object
* The vehicle shall switch to manual control when an obstruction has been detected

##Water- and Dust-Proofing

* The vehicle shall be IP 67 compliant
* The vehicle shall be bouyant
* The vehicle shall be able to operate in temperatures between 20 and 30 degrees Celsius

##Communications

* The vehicle shall constantly communicate with ground control while connected
* The vehicle shall respond to commands within 10 ms

### HD Camera

* The vehicle shall be mounted with a functioning HD camera
* The HD camera shall have a minimum of a 120 degree viewing area
* The HD camera shall have a resolution of 720p
* The HD camera shall stream to ground control while the vehicle is powered
* The HD camera shall be facing directly forward from the front of the vehicle
* The HD camera shall maintain an unobstructed view of the area directly in front of the vehicle

### Autonomy

* The vehicle shall have the option to be autonomous
* The vehicle shall move only along sidewalks while moving autonomously
* The vehicle shall stop when it detects itself as being off-path*
* The vehicle shall have the option to be manually controlled

## Software

### UI
* The UI shall show a live HD camera feed from the vehicle
* The UI shall send instructions to the vehicle while it is in autonomous mode
* The UI shall be able to switch the vehicle between manual and autonomous mode
* The UI shall be able to cease vehicle movement
* The UI shall display the vehicle's position on a map
* The UI shall display the vehicle's current speed
* The user shall be able to place waypoints on the map
* The UI shall have a help window to explain functions

### Comms
* The vehicle shall communicate with the ground station at a rate of at least 30 Hz
* The vehicle shall stop itself in the event of a lost connection
* The vehicle shall receive movement instructions from the ground station

### Autonomous Navigation
* The vehicle shall stay on top of and within the bounds of the sidewalks while moving
* The vehicle shall be able to navigate among user-specified waypoints
* The vehicle shall travel along the shortest possible safe path between waypoints
