# Interface
<!-- Don't delete comments until AFTER you address them! -->

## Remote Procedure Calls

### aero.near.joyMonitor(servoAxis, motorAxis)
* Args - servoAxis: float used in the joystick-servo code. Range 1 to -1. Taken from the axes values, where -1 is left, 1 is right
		 motorAxis: float used in the joystick-motor code. Range 1 to -1. Taken from the axes values, where -1 is forward, 1 is backward
* Behavior - Takes in val from joyUpdate and uses it to control the servos and motors through the Ground System.
Sends joystick forward, backward, left, and right movement through the Ground System to the vehicle.
* Return - none

### aero.near.override()
<!-- Is this actually "on and off" or just off? What happens if sent multiple times quickly? -->
* Behavior - Switches the obstacle avoidance override on and off, in obedience to the time-out requirement

### aero.near.honkHorn()
* Behavior - Honks the horn for .5  when called

### aero.near.emergStop()
* Behavior - Stops the vehicle as quickly as possible

## Publish/Subscribe Topics

### aero.near.carPos
* The latitude and longitude of the vehicle, formatted as a tuple of floats in that order. The latitude and longitude will be represented in degrees. 
* frequency - 33ms

### aero.near.carSpeed
* The speed of the vehicle formatted as a float.
* frequency - 33ms

### aero.near.carHeading
* The heading of the vehicle formatted as a string.
* frequency - 33ms
