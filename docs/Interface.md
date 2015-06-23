# Interface

## Movement commands

### near.aero.joyUpdate()
* Behavior - Picks up the movements of the joystick 30 times a second,
converts the position to a tuple of floats, and calls the function 	joyMonitor() with vals.

### near.aero.joyMonitor(servoAxis, motorAxis)
* Args - servoAxis: float used in the joystick-servo code. Range 1 to -1. 
motorAxis: float used in the joystick-motor code. Range 1 to -1
* Behavior - Takes in val from joyUpdate and uses it to control the servos and motors through the Ground System.
Sends joystick forward, backward, left, and right movement through the Ground System to the vehicle

## Assisted Mode

### near.aero.switchMode()
* Behavior - Switches the obstacle avoidance system on and off, in obediance to the time-out requirment

## Horn

### near.aero.honkHorn()
* Behavior - Every time an obtacle is detected or when the user requests, the horn will sound

## Battery

### near.aero.showBattery(batlevel)
* Args - int that show the percantage of battery left. Range 0 to 100
* Returns - batlevel
* Behavior - The vehicle sends its battery level to the Ground System, which will display the information on the webpage

## Temperature

### near.aero.showTemp(temp)
* Args - int that shows the temperature of the vehicle interior range 0 to 2 million
* Returns - temp
* Behavior - The vehicle sends its temperature to the Ground System, which will display the information on the webpage
