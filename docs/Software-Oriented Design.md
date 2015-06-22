# Glossary
* Ground Station (GS) - User interface. The website and the joystick. Everything on the operator's end.
* Vehicle - The RC car and the onboard Pi 

# System Design
* Joystick Code
* Navigation (Autonomous and otherwise)
* Camera (Hardware overlap)
* Website Frontend

# Subsystem Design

## Website Frontend

### Behaviour
  The website contains a 720p video feed from the camera next to a Google map of the area surrounding the vehicle that both refresh at 30 Hz. Below the map and video feed is a toggleable switch to change the mode of the vehicle between manual and autonomous navigation. There is also a Stop button that causes the vehicle to stop moving as quickly as possible, to be used in an emergency situation. In order to aid in navigation, there will also be buttons to begin directional instructions for manual mode. These directional instructions will also be used to help the vehicle navigate autonomously. Waypoints are able to be placed on the map to give instructions on where the vehicle needs to go in both manual and autonomous mode. There will also be some data displayed below the camera feed, such as temperature of the vehicle, heading, and battery level.
  
### Role
  The website frontend is used by the user to aid in their use of the vehicle. It allows the user to see through the vehicle's eyes via the onboard camera and  enables an effective navigation system. It also shows where the vehicle is in geographic space so the user is also able to plan where he or she wants to go. It provides directional instructions to take the user wherever they want to go on campus as well. It also enables emergency stops through the stop button. Finally, it allows the user to put the vehicle into autonomous mode so it can navigate on its own if the user does not want to control it any more. The website frontend will show important information about the curent status of the car such as the battery life of the car or the vehicle's temperature.
  
### Major components, location, interaction
* Google Map: Top 3/4ths of the screen. Left half of the screen. Is used to drop waypoints, give directions while navigating, and update the user on the vehicle's location.
* Video Feed: Top 3/4ths of the screen. Right half of the screen. Is used to provide the user with a visual of what is in front of the vehicle and aid in navigation.
* Autonomous Mode Checkbox (AMC): Below the map. When clicked, it will swap the vehicle from manual to autonomous mode and vice versa. It operates on PubSub. The vehicle subscribes to what the ground station publishes on the channel modeSwitch. The ground station publishes when the state of the checkbox changes. This causes the vehicle to switch modes.
* Stop Button: Below the video stream. When clicked, it will command the vehicle to stop moving as fast as possible. It calls an RPC named emergStop to tell the robot to begin slowing down and eventually stop. It can stop the robot from 30 mph in 15 meters. To be used in emergencies.
* Navigational Buttons: Between the Stop Button and the AMC. They will cause navigations to start between waypoints chosen by the user.
* Data: Below the camera feed. Will display important information such as heading and battery level to the user. It will also show the vehicle's temperature, the camera's framerate, and the vehicle's current speed.

## Joystick

### Behaviour

Joystick produces outputs based on the current position using Pygame. These ouputs should be tuples of floats passed
through RPC 
protocol to the vehicle using Autobahn. The vehicle-mounted pi runs code that maps the joystick's current position to
servo commands,
turning the wheels of the vehicle accordingly. The joystick will continue sending data, even when not moving, at 30 Hz
(every .0333 seconds).

### Physical

The system consists entirely of the joystick and the computer that it's plugged it into via USB. The joystick will be
physically next to the computer, and it's code will be on the computer as well. The user interacts by operating the
joystick (joysticking) to control the vehicles movement. 

### Software Components 

The initial function onJoin runs when the session begins. onJoin then runs the function joyUpdate, which picks up the
joystick movement, converts it into a tuple of floats, and passes is to another function, joyMonitor, 30 times a
second. joyMonitor runs	directly on the pi, and performs some sort of hardware magic to make the servos turn. 

#### Function - onJoin()
* Args - self, details (WAMP stuff)
* Output - n/a
* Behavior - Runs the functions within when the session connects

#### Function - joyUpdate()
* Args - n/a
* Output - Tuple of floats called val
* Behavior - Picks up the movements of the joystick 30 times a second, converts the position to a tuple of floats, and calls the function 	joyMonitor() with vals.

#### Function - joyMonitor()
* Args - put
* Output - PWM-based servo controls
* Behavior - Takes in val from joyUpdate and uses it to control the servos through the setPWM function.

## Vehicle Camera

### Behaviour
An HD camera will be mounted to the front of the vehicle so that it faces forward. The camera's onboard components capture shots of the vehicle's front-facing view and converts that view to video. The resulting video is then sent to the ground station in real time and displayed in a window on the ground station webpage.

### Physical
The sensors will be taken from a Ubiquiti Aircam camera, and attached to the strut at the front end of the vehicle.             

### Software Components
The camera's sensor captures shots of what it sees at a rate of 30 hz. Default software in the camera converts the frames that are captured into a 30fps video at 720p resolution. That video is then sent to the UI that is controlled by the ground station and displayed in real time.  
  
# Use Cases

## Navigation Activation

1. User asks to put vehicle in auto mode
2. System puts vehicle in auto mode
3. User clicks deisred place on provided map
4. System creates and displays waypoint on map and connects it to previous point. Repeat steps 3 & 4 until User ceases creation of waypoints
5. User tells the system to begin navigation
6. System determines closest path from known sidewalk junctions & transmits to vehicle - nav starts  

## Alternate Flows
1. User indicates a waypoint to remove
2. System removes waypoint from the route and connects the previous and next waypoints
  
## Manual Vehicle Movement
1. User moves joystick
2. System changes vehicle movement accordingly. Repeat steps 1 & 2 as needed

## Obstacle Avoidance
1. Vehicle detects an obstacle (with Lidar)
2. Obstacle registered in map
3. Vehicle is repelled from obstacle, while simultaneously redirecting itself toward the waypoint (objective)
4. Vehicle avoids obstacle.
  
