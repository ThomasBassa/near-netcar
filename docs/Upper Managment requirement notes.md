# Requirements

*no payload requirments*
*3 lb 1 ft cubed*

### Sound and Lights:
1. The vehicle shall be mounted with a light *Ambiguous*
2. The light shall be on while the vehicle is powered
3. The light shall be visible to any sighted person in the forward path of the vehicle with an unobstructed view of the light source
4. The vehicle shall be mounted with a noise device *Ambiguous*
5. The noise device shall sound when an obstacle is detected 20 m from the vehicle's front bumper *Always beeping*
6. The noise device shall generate between 60 and 80 decibels when sounding *Shorten*
*300 lumens*

### Vehicle Motion:
1. The vehicle shall be able to move forward
2. The vehicle shall be able to move backwards
3. The vehicle shall be able to turn left
4. The vehicle shall be able to turn right
5. The vehicle's speed shall not exceed 30mph
6. The vehicle's motion shall be controlled by ground control when in manual mode
7. The vehicle shall stop all movement after communication with ground control is interrupted *Go back to last waypoint*
8. The vehicle shall be able to remotely reconnect with ground control upon signal loss
9. The vehicle shall be able to operate for at least an hour at a time
*control at least 1-2 miles away*

### Obstacle Avoidance
1. The vehicle shall be able to detect objects that are up to 20 m in front of it
2. The vehicle shall stop a minimum of 5 m from a detected object 
3. The vehicle shall be able to navigate around detected obstacles after stopping

### Water- and Dust-Proofing
1. The vehicle shall be IP 66 compliant
2. The vehicle shall be able to operate in temperatures between 0 and 40 degrees Celsius *upper to low up to surface of a real car* 

### HD Camera
1. The vehicle shall be equipped with a functioning HD camera
2. The HD camera shall have a minimum of a 120 degree viewing area *may budge*
3. The HD camera shall have a minimum resolution of 720p at 30 (or slightly less, aboe 24) fps
4. The HD camera shall stream to ground control while the vehicle is powered
5. The HD camera shall face directly forward from the front of the vehicle
6. The HD camera shall be unobstructed by other components of the vehicle

### Ground Station
1. The ground station shall show a live HD camera feed from the vehicle
2. The ground station shall send instructions for waypoint navigation to the vehicle while it is in autonomous mode 
3. The ground station shall be able to switch the vehicle between manual and autonomous mode
4. The ground station shall be able to cease vehicle movement
5. The ground station shall display the vehicle's position on a map
6. The ground station shall display the vehicle's current speed
7. The user shall be able to place waypoints on the map
8. The ground station shall be able to provide help regarding use of the system *training system*
*A lot more status info, battery voltage, water status, direction, etc.

### Communications
1. The vehicle shall communicate with the ground station at a rate of at least 30 Hz while connected *30 Hz is a lot, just make it responsive*
2. The vehicle shall receive movement instructions from the ground station
3. The vehicle shall respond to commands within 10* -> 150 ms *how do we test*

### Autonomous Navigation
1. The vehicle shall stay on top of and within the bounds of sidewalks while moving autonomously
2. The vehicle shall be able to navigate among user-specified waypoints
3. The vehicle shall travel along the shortest possible safe path between waypoints
4. The vehicle shall have the option to be autonomous
5. The vehicle shall move only along sidewalks while moving autonomously
6. The vehicle shall stop when it detects itself as being off-path *how to test* *also it should just get back on the path*  
7. The vehicle shall have the option to be manually controlled
