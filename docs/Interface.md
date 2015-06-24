# Interface
<!-- Don't delete comments until AFTER you address them! -->

## Remote Procedure Calls

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
* Behavior - Honks the horn for .5  when called

## Publish/Subscribe Topics
<!-- The PubSub components need a different format:
	###Name of topic ("offical" name)
	* Data type, range
	* Frequency of updates -->

### aero.near.showBattery
* int, ranging 0 to 100 inclusive (integer percent)
* frequency - to be determined

### aero.near.showTemp
* an integer representing the temperature of the device in degrees Farenheit
* frequency - to be determined

### aero.near.carPos
* The latitude and longitude of the vehicle, formatted as a tuple in that order, **and explain the datatype & units**
* frequency - to be determined
