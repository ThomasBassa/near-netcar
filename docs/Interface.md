# Interface
<!-- Don't delete comments until AFTER you address them! -->

## Remote Procedure Calls
<!-- All of these need to have returns specified, just say None if there are none -->

<!-- What makes joyUpdate distinct from joyMonitor? Do these need to be separate? -->
### near.aero.joyUpdate()
<!-- How many elements are in the tuple? What are their ranges? What does each value mean at its extremes? -->
* Behavior - Picks up the movements of the joystick 30 times a second,
converts the position to a tuple of floats, and calls the function 	joyMonitor() with vals.
<!-- Still haven't defined what vals is... -->

### near.aero.joyMonitor(servoAxis, motorAxis)
<!-- What does 1 represent? What is -1? For both of these?
This needs to be made super clear so we don't drive the robot backwards -->
* Args - servoAxis: float used in the joystick-servo code. Range 1 to -1.
motorAxis: float used in the joystick-motor code. Range 1 to -1
* Behavior - Takes in val from joyUpdate and uses it to control the servos and motors through the Ground System.
Sends joystick forward, backward, left, and right movement through the Ground System to the vehicle

### near.aero.switchMode()
<!-- Is this actually "on and off" or just off? What happens if sent multiple times quickly? -->
* Behavior - Switches the obstacle avoidance system on and off, in obedience to the time-out requirement

### near.aero.honkHorn()
<!-- Describe only the behavior of this call. Not the obstacle... -->
* Behavior - Every time an obstacle is detected or when the user requests, the horn will sound

## Publish/Subscribe Topics
<!-- The PubSub components need a different format:
	###Name of topic ("offical" name)
	* Data type, range
	* Frequency of updates -->

### near.aero.showBattery(batlevel)
* Args - int that show the percantage of battery left. Range 0 to 100
* Returns - batlevel
* Behavior - The vehicle sends its battery level to the Ground System, which will display the information on the webpage

### near.aero.showTemp(temp)
* Args - int that shows the temperature of the vehicle interior range 0 to 2 million
* Returns - temp
* Behavior - The vehicle sends its temperature to the Ground System, which will display the information on the webpage
