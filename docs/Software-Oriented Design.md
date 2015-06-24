# Glossary
* Ground Station (GS) - User interface. The website and the joystick.
  Everything on the operator's end.
* Vehicle - The RC car and its onboard Pi

# System Design
This is the set of subsystems we believe are necessary in this system.
* Joystick - The way the user will control the vehicle
* Navigation - How the user will know where to go
* Camera (Hardware overlap) - What the use will use to see in front of the vehicle
* Website Frontend - The way the user will see the camera feed, map, and various other statistics about the vehicle 

# Use Cases 

## Manual Vehicle Movement
1. User moves joystick
2. System sends information to vehicle accordingly.
3. Vehicle moves


## Obstacle Detection
1. Vehicle detects an obstacle (with Lidar)
2. The vehicle stops
![Use Case: Obstacle Detection](https://raw.githubusercontent.com/ThomasBassa/near-netcar/master/docs/Diagrams/Use%20Cases_%20Obstacle%20stopping%20-%20New%20Page.png)

# Subsystem Design

## Website Frontend

### Behaviour
The website contains a 720p video feed from the camera next to a Google map
of the area surrounding the vehicle that both refresh at 30 Hz.
Below the map and video feed is a toggleable switch to change the mode of
the vehicle between manual and autonomous navigation. There is also a Stop button
that causes the vehicle to stop moving as quickly as possible, to be used
in an emergency situation. These directional instructions will also be used 
to help the vehicle navigate autonomously. There will also be some vehicle statistics 
displayed below the camera feed,such as temperature of the vehicle, 
which will be used to tell when the vehicle is about to overheat. 
Heading, which will aid in navigation, and battery level, to tell when the vehicle will lose power.

### Role
The website frontend is used to display vehicle status information.
It allows the user to see through the vehicle's eyes via the onboard camera and
enables the vehicle's course to be set in automatic mode.
It also shows where the vehicle is in geographic space
so the user is also able to plan where he or she wants to go.
It provides directional instructions to take the user wherever
they want to go on campus as well.
It also enables emergency stops through the stop button.

The website frontend will show important information about the current status of the car 
such as the battery life of the car, the vehicle's temperature, the cardinal direction the vehicle is facing,
the camera's framerate, and the vehicle's current speed.

### Major components, location, interaction
* Google Map: Top 3/4ths of the screen. Left half of the screen.
  Is used to provide waypoints, give directions while navigating, and update the user on the vehicle's location.
* Video Feed: Top 3/4ths of the screen. Right half of the screen.
  Is used to provide the user with a visual of what is in front of the vehicle and aid in navigation.
* Assisted Mode Checkbox: Below the map.
  When clicked, it will swap the vehicle from manual to assisted mode and vice versa.
  It operates on PubSub. The vehicle subscribes to what the ground station publishes on the channel modeSwitch.
  The ground station publishes when the state of the checkbox changes. This causes the vehicle to switch modes.
* Stop Button: Below the video stream.
  When clicked, it will command the vehicle to stop moving as fast as possible.
  It calls an RPC named emergStop to tell the robot to begin slowing down and eventually stop.
  It can stop the robot from 30 mph in 15 meters, to be used in emergencies.
* Data: Below the camera feed.
  Will display the current heading and battery level to the user.
  It will also show the vehicle's temperature, the camera's framerate, and the vehicle's current speed.

## Joystick

### Behaviour

Joystick produces outputs based on the current position using Pygame.
These outputs should be tuples of floats passed through RPC protocol to the vehicle using Autobahn.
The vehicle-mounted pi runs code that maps the joystick's current position to servo commands,
turning the wheels of the vehicle accordingly.
The joystick will continue sending data, even when not moving, at 30 Hz (every .0333 seconds).

### Physical
The system consists entirely of the joystick and the computer that it's plugged it into via USB.
The joystick will be physically next to the computer,
and its code will be on the computer as well.
The user interacts by operating the joystick to control the vehicle movement.

### Software Components
The initial function onJoin runs when the session begins. onJoin then runs the function joyUpdate, which picks up the
joystick movement, converts it into a tuple of floats, and passes is to another function, joyMonitor, 30 times a
second. joyMonitor runs	directly on the pi, and performs some sort of hardware magic to make the servos turn.

#### Function - onJoin(detials)
* Args - 
* Returns - none
* Behavior - Runs the functions within when the session connects

#### Function - joyUpdate()
* Returns - Tuple of floats called val, -1.1 <= vals <= 1.1
* Behavior - Picks up the movements of the joystick 30 times a second,
converts the position to a tuple of floats, and calls the function 	joyMonitor() with vals.

#### Function - joyMonitor(put)
* Args - the float that contains the 1 to -1 range of the joystick axis
* Returns - int passed to the servos
* Behavior - Takes in val from joyUpdate and uses it to control the servos through the setPWM function.

## Vehicle Camera

### Behaviour
An HD camera will be mounted to the front of the vehicle so that it faces forward.

### Physical
The sensors will be taken from a Ubiquiti Aircam camera, and attached to the strut at the front end of the vehicle.

### Software Components
The camera's sensor captures shots of what it sees at a rate of 30 hz.
Default software in the camera converts the frames that are captured
into a 30fps video at 720p resolution. That video is then sent to the UI
that is controlled by the ground station and displayed in real time.  
