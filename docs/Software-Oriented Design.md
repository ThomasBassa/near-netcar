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

## Obstacle Avoidance
1. Vehicle detects an obstacle (with Lidar)
2. The vehicle stops

# Subsystem Design

## Website Frontend

### Behaviour
The website contains a 720p video feed from the camera next to a Google map
of the area surrounding the vehicle that both refresh at 30 Hz.
Below the map and video feed is a toggleable switch to change the mode of
the vehicle between manual and autonomous navigation. There is also a Stop button
that causes the vehicle to stop moving as quickly as possible, to be used
in an emergency situation. In order to aid in navigation, there will also
be buttons to begin directional instructions for manual mode.
These directional instructions will also be used to help the vehicle
navigate autonomously. Waypoints are able to be placed on the map to give
instructions on where the vehicle needs to go in both manual and autonomous mode.
<<<<<<< HEAD
There will also be some vehicle statistics displayed below the camera feed,
such as temperature of the vehicle, which will be used to tell when the vehicle is about to overheat. 
Heading, which will aid in navigation, and battery level, to tell when the vehicle will lose power.
=======
There will also be some data displayed below the camera feed,
such as temperature of the vehicle, heading, and battery level.
>>>>>>> origin/master

### Role
The website frontend is used to display vehicle status information.
It allows the user to see through the vehicle's eyes via the onboard camera and
enables the vehicle's course to be set in automatic mode.
It also shows where the vehicle is in geographic space
so the user is also able to plan where he or she wants to go.
It provides directional instructions to take the user wherever
they want to go on campus as well.
It also enables emergency stops through the stop button.
Finally, it allows the user to put the vehicle into autonomous mode,
so it can navigate on its own if the user does not want to control it.
<<<<<<< HEAD
The website frontend will show important information about the current status of the car 
such as the battery life of the car, the vehicle's temperature, the ardinal direction the vehicle is facing,
the camera framerate, and the vehicle's current speed.
=======
The website frontend will show important information about the current status
of the car such as the battery life of the car or the vehicle's temperature.
>>>>>>> origin/master

### Major components, location, interaction
* Google Map: Top 3/4ths of the screen. Left half of the screen.
  Is used to provide waypoints, give directions while navigating, and update the user on the vehicle's location.
* Video Feed: Top 3/4ths of the screen. Right half of the screen.
  Is used to provide the user with a visual of what is in front of the vehicle and aid in navigation.
* Autonomous Mode Checkbox: Below the map.
  When clicked, it will swap the vehicle from manual to autonomous mode and vice versa.
  <!-- There should be a list of all of the Pi-related calls near the end of the doc -->
  It operates on PubSub. The vehicle subscribes to what the ground station publishes on the channel modeSwitch.
  The ground station publishes when the state of the checkbox changes. This causes the vehicle to switch modes.
* Stop Button: Below the video stream.
  When clicked, it will command the vehicle to stop moving as fast as possible.
  It calls an RPC named emergStop to tell the robot to begin slowing down and eventually stop.
  It can stop the robot from 30 mph in 15 meters, to be used in emergencies.
* Navigational Buttons: Between the Stop Button and the AMC.
  They will cause navigations to start between waypoints chosen by the user.
* Data: Below the camera feed.
<<<<<<< HEAD
  Will display the current heading and battery level to the user.
=======
  Will display important information such as heading and battery level to the user.
>>>>>>> origin/master
  It will also show the vehicle's temperature, the camera's framerate, and the vehicle's current speed.

## Joystick

### Behaviour

Joystick produces outputs based on the current position using Pygame.
<!-- The exact type & format of the tuples needs to show later -->
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

#### Function - onJoin()
* Args - salf, details (WAMP stuff) <!-- These should be explained, but it's okay...-->
* Returns - n/a
* Behavior - Runs the functions within when the session connects

#### Function - joyUpdate()
* Args - n/a
* Returns - Tuple of floats called val, -1.1 <= vals <= 1.1
* Behavior - Picks up the movements of the joystick 30 times a second,
converts the position to a tuple of floats, and calls the function 	joyMonitor() with vals.

#### Function - joyMonitor(put)
* Args - put
 <!-- get put range from hardware team -->
* Returns - int passed to the servos
* Behavior - Takes in val from joyUpdate and uses it to control the servos through the setPWM function.

## Vehicle Camera

### Behaviour
An HD camera will be mounted to the front of the vehicle so that it faces forward.
<!-- The following line/paragraph is useless, how do I build it? -->
The camera's onboard components capture shots of the vehicle's front-facing view and converts that view to video. The resulting video is then sent to the ground station in real time and displayed in a window on the ground station webpage.

### Physical
The sensors will be taken from a Ubiquiti Aircam camera, and attached to the strut at the front end of the vehicle.

### Software Components
The camera's sensor captures shots of what it sees at a rate of 30 hz.
Default software in the camera converts the frames that are captured
into a 30fps video at 720p resolution. That video is then sent to the UI
that is controlled by the ground station and displayed in real time.  
