# Interface
<!-- Don't delete comments until AFTER you address them! -->

## Remote Procedure Calls
<!-- All of these need to have returns specified, just say None if there are none -->

<!-- What makes joyUpdate distinct from joyMonitor? Do these need to be separate? -->
### aero.near.joyUpdate()
* Behavior - Picks up the movements of the joystick 30 times a second, converting to a couple of float values
* Return - vals, which is a tuple with two floats in the range of -1.1 to 1.1, the values of the horizontal and vertical movement of the axes. A value of 1 or -1 is the extreme of a movement.

### aero.near.joyMonitor(servoAxis, motorAxis)
* Args - servoAxis: float used in the joystick-servo code. Range 1 to -1. Taken from the axes values, where -1 is left, 1 is right
		 motorAxis: float used in the joystick-motor code. Range 1 to -1. Taken from the axes values, where -1 is forward, 1 is backward
* Behavior - Takes in val from joyUpdate and uses it to control the servos and motors through the Ground System.
Sends joystick forward, backward, left, and right movement through the Ground System to the vehicle. 
* Return - none

### aero.near.switchMode()
<!-- Is this actually "on and off" or just off? What happens if sent multiple times quickly? -->
* Behavior - Switches the obstacle avoidance system on and off, in obedience to the time-out requirement

### aero.near.honkHorn()
<!-- Describe only the behavior of this call. Not the obstacle... -->
* Behavior - Honks the horn for .5 seconds

## Publish/Subscribe Topics
<!-- The PubSub components need a different format:
	###Name of topic ("offical" name)
	* Data type, range
	* Frequency of updates -->

### aero.near.showBattery
* args - none
* frequency - to be determined
* return - int called batLevel, where 0 <= int <= 100

### aero.near.showTemp
* args - none
* freguency - to be determined
* return - int called temp, larger than zero, represents temperature

### aero.near.carPos
* args - none
* frequency - to be determined
* return - tuple of float values called latLong, which are the latitude and longitude