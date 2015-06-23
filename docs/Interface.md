# Interface

## Movement commands

<!-- All of these need to be named using their as-close-to-final-as-possible RPC names
e.g. near.aero.functionName(args, moreArgs) -->

### Function - onJoin(details)
* Args - 
* Returns - 
* Behavior - **Is not part of the interface with the vehicle and should be deleted**

<!-- The next four commands should be pared down to JUST what the RPC is going to be. (or plural RPCs...) -->
### Function - joyUpdate()
* Returns - Tuple of floats <!-- What is the range of values of these floats? What do they mean? -->
* Behavior - Picks up the movements of the joystick 30 times a second,
converts the position to a tuple of floats, and calls the function 	joyMonitor() with vals.

### Function - joyMonitor(put)
* Args - int used in the joystick-servo code <!-- Is this "put"? Actually say "put" before this if so. 
  Also, what is the range of this value? What's the high value, and what does it mean? What's the low value and its meaning? -->
* Returns - PWM-based servo controls <!-- This is for literal, in code, return values. Is there a "controls" object? Explain or remove. -->
* Behavior - Takes in val from joyUpdate and uses it to control the servos through the setPWM function.
<!-- "the setPWM function" is not our concern, and should not be mentioned.
     "val" is undefined here -->

### Function - joyMove()
<!-- There are probably arguments for this one? -->
* Returns - The motors moving the tires forwards and backwards <!-- Again, these are CODE returns, vehicle moving is for behavior -->
* Behavior - Sends joystick forward and backward movement through the Ground System to the vehicle


### Function - joyTurn()
* Returns - The servos turning left and right <!-- Again, these are CODE returns, vehicle moving is for behavior -->
* Behavior - Sends joystick left and right movement through the Ground System to the vehicle

## Assisted Mode

### Function - switchMode()
* Args - 
* Returns - None
* Behavior - Switches the obstacle avoidance system on and off <!-- Check requirements-- I want to say that you can only disable 20s -->

## Horn

### Function - honkHorn()
* Returns - 
* Behavior -  


<!-- The PubSub components need a different format:
	###Name of topic ("offical" name)
	* Data type, range
	* Frequency of updates -->
## Battery

### Function - showBattery()
* Args - 
* Returns - The battery status as a percentage float
* Behavior - The vehicle sends its battery level to the Ground System, which will display the information on the webpage

## Temperature

### Function - showTemp()
* Args - 
* Returns - The vehicle's temperature as a percentage float
* Behavior - The vehicle sends its temperature to the Ground System, which will display the information on the webpage
