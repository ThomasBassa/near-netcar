# Glossary (A001)
* Ground Station (GS) - User interface. The website and the joystick.
  Everything on the operator's end.
* Vehicle - The RC car and its onboard Pi

# System Design (A002)
This is the set of subsystems we believe are necessary in this system.
* Joystick - The way the user will control the vehicle
* Navigation - How the user will know where to go
* Camera (Hardware overlap) - What the use will use to see in front of the vehicle
* Website Frontend - The way the user will see the camera feed, map, and various other statistics about the vehicle 

# Use Cases (A003)

## Manual Vehicle Movement (A004)
1. User moves joystick
2. System sends information to vehicle accordingly.
3. Vehicle moves

## Obstacle Avoidance (A005)
1. Vehicle detects an obstacle (with Lidar)
2. The vehicle stops

# Subsystem Design (B001)

## Website Frontend (B002)

### Behaviour (B003)
The website contains a 720p video feed from the camera next to a Google map
of the area surrounding the vehicle that both refresh at 30 Hz.
Below the map and video feed is a toggleable switch to change the mode of
the vehicle between manual and autonomous navigation. There is also a Stop button
that causes the vehicle to stop moving as quickly as possible, to be used
in an emergency situation. These directional instructions will also be used 
to help the vehicle navigate autonomously. There will also be some vehicle statistics 
displayed below the camera feed,such as heading, which will aid in navigation, 
battery level, to tell the user when the vehicle will lose power,
and the speed of the vehicle, to tell the user how fast he/she is going.

### Role (B004)
The website frontend is used to display vehicle status information.
It allows the user to see through the vehicle's eyes via the onboard camera and
enables the vehicle's course to be set in automatic mode.
It also shows where the vehicle is in geographic space
so the user is also able to plan where he or she wants to go.
It provides directional instructions to take the user wherever
they want to go on campus as well.
It also enables emergency stops through the stop button.

The website frontend will show important information about the current status of the car 
such as the battery life of the car, the cardinal direction the vehicle is facing,
and the vehicle's current speed.

### Major components, location, interaction (B005)
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
  It will also show the camera's framerate and the vehicle's current speed.

## Joystick (B006)

### Behaviour (B007)

Joystick produces outputs based on the current position using Pygame.
These outputs should be tuples of two floats passed through RPC protocol to the vehicle using Autobahn.
The vehicle-mounted pi runs code that maps the joystick's current position to servo commands,
turning the wheels of the vehicle accordingly.
The joystick will continue sending data, even when not moving, at 30 Hz (every .0333 seconds).

### Physical (B008)
The system consists entirely of the joystick and the computer that it's plugged it into via USB.
The joystick will be physically next to the computer,
and its code will be on the computer as well.
The user interacts by operating the joystick to control the vehicle movement.

### Software Components (B009)
The initial function onJoin runs when the session begins. onJoin then runs the function joyUpdate, which picks up the
joystick movement, converts it into a tuple of floats, and passes is to another function, joyMonitor, 30 times a
second. joyMonitor runs	directly on the pi, and performs some sort of hardware magic to make the servos turn.

#### Function - onJoin() (F001)
* Args - self, details (WAMP stuff) <!-- These should be explained, but it's okay...-->
* Returns - n/a
* Behavior - Runs the functions within when the session connects

#### Function - joyUpdate() (F002)
* Args - n/a
* Returns - Tuple of floats called val, -1.1 <= vals <= 1.1
* Behavior - Picks up the movements of the joystick 30 times a second,
converts the position to a tuple of two floats, and calls the function 	joyMonitor() with vals.

#### Function - joyMonitor(put) (F003)
* Args - put
 <!-- get put range from hardware team -->
* Returns - int passed to the servos
* Behavior - Takes in val from joyUpdate and uses it to control the servos through the setPWM function.

## Vehicle Camera (C001)

### Behaviour (C002)
An HD camera will be mounted to the front of the vehicle so that it faces forward.
The camera's onboard components capture shots of the vehicle's front-facing view and converts that view to video. The resulting video is then sent to the ground station in real time and displayed in a window on the ground station webpage.

### Physical (C003)
The sensors will be taken from a Ubiquiti Aircam camera, and attached to the strut at the front end of the vehicle.

### Software Components (C004)
The camera's sensor captures shots of what it sees at a rate of 30 hz.
Default software in the camera converts the frames that are captured
into a 30fps video at 720p resolution. That video is then sent to the UI
that is controlled by the ground station and displayed in real time.  

Ubiquiti Aircam
http://www.newegg.com/Product/Product.aspx?Item=9SIA0ZX20N9128&cm_re=ubiquiti-_-0ED-0005-00022-_-Product

## Training system (Z011)
The training system will be a printed manual describing all the features of the website frontend and the joystick.
The training system is for new users to the vehicle, instructing them so they will know how to handle emergencies. 

## Hardware Design (C005)

The vehicle will communicate with the ground station.
The vehicle shall have two modes: assisted manual mode and manual mode.
In manual mode, a user at the ground station controls the vehicle using a joystick.
In assisted manual mode, the vehicle intervenes when an obstacle is detected and
keeps the vehicle on the sidewalk. The user can switch between the two modes.
The vehicle shall be able to send live HD feed from a camera while the vehicle is powered.
The vehicle will have a light and a buzzer to warn pedestrians while the vehicle is on.
The vehicle will conform to IP54 standards, protecting it from water, dust, and touch.

![BlockDiagram](https://github.com/ThomasBassa/near-netcar/blob/master/docs/Diagrams/MainBlockDiagram.png)

**Figure 1.** Block Diagram of Vehicle Components

![HardwareConnection](https://github.com/ThomasBassa/near-netcar/blob/master/docs/Diagrams/HardwareDiagram.png)

**Figure 2.** Block diagram of Hardware Connections

## Vehicle Design (C006)

![screenshot 2015-06-17 13 10 21](https://cloud.githubusercontent.com/assets/11369623/8214167/55704aae-14f5-11e5-9748-e12c572fcc7e.png)

**Figure 3.** Strut design to be 3D printed

This strut design was printed using the TAZ 5 printer.
The vehicle has one strut mounted onto the front and one onto back of the chassis to give suport for the suspension.

![screenshot 2015-06-17 13 06 49](https://cloud.githubusercontent.com/assets/11369623/8214178/5cb7feec-14f5-11e5-985d-d3d6e6b22ce7.png)

**Figure 4.** Cube for the strut

We have 8 of these printed, 4 per strut, attached to struts with acetone-glue; shocks are screwed into these.
This block was printed to give suport for the shocks.
Four blocks were used to glue: one block to each side of the top 2 holes on each strut,
to support the nails we later used to prop up the spings on the strut. They were glued using acetone.

## Ground Station Communication (C007)
Application components connect to Crossbar.io and can then talk to each other using two patterns:
Remote Procedure Calls and Publish & Subscribe. Crossbar.io directes and transmitts messages to the right components ("message routing").

### Remote Procedure Calls (C008)
Remote Procedure Call (RPC) is a messaging pattern involving peers of three roles:
Caller, Callee, and Dealer. A Caller issues calls to remote procedures by providing the procedure URI
and any arguments for the call. The Callee will execute the procedure using the supplied arguments to the call
and return the result of the call to the Caller. Callees register procedures they provide with Dealers.
Callers initiate procedure calls first to Dealers. Dealers route calls incoming from Callers to Callees
implementing the procedure called, and route call results back from Callees to Callers.
The Caller and Callee will usually run application code, while the Dealer works
as a generic router for remote procedure calls decoupling Callers and Callees.

With the Remote Procedure Call pattern, any component can register a procedure that other components can call and call all 
procedures registered by other components. Crossbar.io routes calls to the component that registered the respective procedure 
and returns the result to the caller: RPC pattern - registering a procedure with the Crossbar.io router, PRC pattern - 
calling a remote procedure and receiving the result, routed via Crossbar.io.

### Publish & Subscribe (C009)
With the Publish & Subscribe pattern, any component can subscribe to receive events published from other components and 
publish events which other subscribed components will receive. Crossbar.io routes event published to all components that have 
subscribed to receive events for the topic.

### Methods (C010)
To PUBLISH an event - session.publish('join.session', 'Session joined')

To REGISTER a procedure for remote calling - session.register(Horizontal(param)), 'com.myapp.add2')

![CommunicationBlock](https://github.com/ThomasBassa/near-netcar/blob/master/docs/Diagrams/CommunicationsBlocks.png)

**Figure 5.** Block diagram of server communications

## Obstacle Avoidance (C011)
The vehicle will be mounted with a lidar laser rangefinder.
The vehicle will have two modes (assisted manual/manual). When the vehicle is powered on,
it will start in manual mode and after 20 seconds elapse (timer),
it will switch to assisted manual mode. In assisted manual mode,
the servo will sweep back and forth constantly, on an axis that will
establish a 1.2373 degree field of vision which will detect obstacles.
This was determined using Figure <>. If an obstacle is detected, the vehicle will
cease motion and alert the user (by publishing an obstacle detection event)
that an obstacle is obstructing its path.
The user will then have an option to override the alert and control the vehicle manually.
Choosing to switch it to manual mode will only last 20 seconds before automatically switching back to assisted manual mode.

LIDAR-Lite Laser Rangefinder
http://www.robotshop.com/en/lidar-lite-laser-rangefinder-pulsedlight.html?gclid=CjwKEAjwwN-rBRD-oMzT6aO_wGwSJABwEIkJ7oTmUTfX6Yse7cnXtwcMd9URNekiWv3NAlCizliooBoChQ_w_wcB

![AssistManual](https://github.com/ThomasBassa/near-netcar/blob/master/docs/Diagrams/AssistManualState.png)

**Figure 6.** State diagram of manual assisted and manual mode

### Use Case - Obstacle Detection (C012)

1. press button on website to switch to assisted mode
2. calls method on vehicle
3. assisted manual comes on
  - Lidar comes on, servo begins rotating
4. if an obstacle is detected
  - vehicle stops
  - alerts user by publishing event
5. user has option for a 20 sec override
6. if override option is not taken
  - wait until obstacle has moved
7. if override option taken
  - start a timer
  - switch to manual mode
  - switch back to assisted after 20 sec

![AssistManual](https://github.com/ThomasBassa/near-netcar/blob/master/docs/Diagrams/ServoRotationDiagram.png)

**Figure 7.** Diagram showing how the servo's rotation angle was determined

![AssistManual](https://github.com/ThomasBassa/near-netcar/blob/master/docs/Diagrams/MainSeq.png)

**Figure 8.** The main sequence diagram for the vehicle code

![AssistManual](https://github.com/ThomasBassa/near-netcar/blob/master/docs/Diagrams/ObstacleDetection.png)

**Figure 9.** Sequence diagram for obstacle detection

## Sound and Lights
An active buzzer 65db will be used, and will sound every 2 seconds. The buzzer will be contained in the waterproof box. 
The buzzer will be wired to the Pi in the following way:

    Raspberry Pi                            Active buzzer module

    GND   ------------------------------------- ‘-’
    GPIO11 ------------------------------------- ‘s’

The GPIO library for Raspberry Pi will be used in the program. The method GPIO.write(pin, power) will be used with the 
parameters of the pin and GPIO.on/GPIO.off. Pin 11 on the Raspberry Pi will be used for 's'.

A 4" x 2" oblong amber LED marker light will be mounted on the top of the vehicle. The light will be on while the vehicle is 
powered. The light will be powered by a battery connected by two bare end lead wires with two pins, power and ground.
The GPIO library will again be used.

DC 24V Electronic Amber LED Flashing Alarm Buzzer Siren 100dB BJ-3
http://www.amazon.com/OBLONG-SURFACE-CLEARANCE-MARKER-EL-114303CA/dp/B00N54AT54/ref=sr_1_13?s=electronics&ie=UTF8&qid=1433356800&sr=1-13&keywords=amber+LEDs

## Servo/Motor Control (D001)

### Behavior (D002)
This system uses the output from the joystick to control speed and direction of the vehicle.
This output is produced into two different vehicle methods, horizontal and vertical.
Horizontal output controls the direction of the vehicle (rotational degrees of the servos)
and Vertical output controls the speed of the vehicle
(negative output = positive acceleration, positive output = negative acceleration). Actions shall be processed within 150 ms. 
- Servo control method --> Horizontal(param): This method changes the PWM signal
to the servo using I2C library.
Turning to the right is 150. Changing to the left is 600.
The last value received is saved in a variable to be used for sidewalk detection.

- Motor control method--> Vertical(param): This method changes the I2C output to the motors using I2C library.

### Physical (D003)
This system consists of two servos, two motors, a servo controller,
and an Evx-2 speed controller. The two servos are directly connected to the vehicle
and wired to a Raspberry Pi that connects to a website using crossbar.io.
This website uses RPC, passing joystick data over the Wi-Fi by calling
the method Horizontal() to the Pi which controls the rotation of the servos.
The Evx-2 speed controller will be mounted onto the robot and wired to
the motors and Raspberry Pi. Like the servos, the data from the joystick
is transferred using RPC over the internet using crossbar.io
to call the method Vertical() and sent to the Pi which feeds the speed controller data.

Evx-2 speed controller
https://traxxas.com/products/parts/escs/3019Revx2lvd

###Software Components (D004)
The Pi connects to the ground station through crossbar.io.
Ground control calls methods Horizontal(param) and Vertical(param)
with the data from the joystick to control speed and direction of the robot.
The motor's PWM frequency is 1700 Hz, and the Pi controls the speed controller with I2C.

### Use Case - Sidewalk Lost (D005)
1. press button on website to switch to assisted mode
2. calls method on vehicle
3. assisted manual comes on
  - colour sensor comes on
4. if colour sensor detects no sidewalk
  - use last joystick input (left/right) and turn opposite direction for 1 second

![AssistManual](https://github.com/ThomasBassa/near-netcar/blob/master/docs/Diagrams/ColorSensorSeq.png)

**Figure 11.** Sequence diagram for the color sensor readings

## Battery (Z069)
The battery will power the whole vehicle, and needs to have enough voltage output to power all the sensors. 
The battery needs to be large enough for all the sensors and the vehicle to run for a half hour.

## Mounting Container (D006)
A 28 Qt. Latch Box with dimensions 23" x 16" x 6" will be used.
Holes will be drilled into the container around the struts and
attached to the struts with zip ties. The holes at the bottom of the container will
be sealed with rubber cement to prevent water from entering the container.
The container has a lid for protection. The vehicle suspension can hold three pounds. 

Storage bin
http://www.homedepot.com/p/Sterilite-28-Qt-Latch-Box-16551010/100671079?MERCH=REC-_-NavPLPHorizontal1_rr-_-NA-_-100671079-_-N

![AssistManual](https://github.com/ThomasBassa/near-netcar/blob/master/docs/Diagrams/VehicleContainer.png)

**Figure 12.** Diagram of the container's placement on the vehicle with measurements

Alternatively container:

A 20” x 20” x 12” vinyl insulated pizza deliver bag will be mounted on the vehicle. There will be a straight sheet of plastic inserted into the bottom on the bag (dimensions 18” x 16”) to keep it from sturdy. The bag will be kept folded down when empty.

Pizza bag http://www.webstaurantstore.com/choice-20-x-20-x-12-vinyl-insulated-pizza-delivery-bag/124PIBAG5VNL.html

<Diagram here>

## Video Feed (D007)
The casing will be removed from a Ubiquiti Aircam H.264 1Megapixel/720P 
camera, and it will be mounted on the top of the vehicle, facing forward. The 
camera requires 24V, and has 30fps. First the camera’s IP is determined using 
its provided software. The IP address will be fixed. The port used will be 80. 
The port and IP will be used to contact the camera from the ground station. 

![Camera](https://github.com/ThomasBassa/near-netcar/blob/master/docs/Diagrams/CameraSeq.png)

**Figure 13.** The sequence diagram for the camera HD feed

## Vehicle Location Tracking (D008)

The vehicle's location will be tracked using a GPS module. The GPS module will talk to the Pi with serial communication. The Pi will read string messages from the GPS module. Then the program will interpret the message to find the latitude and longitude of the vehicle. This information will be published over crossbar.io to the ground station. This will happen every main loop iteration. Pin 1 on the module goes to 3.3 V power. Pin 2 is RX and goes to RDX on the Pi. Pin 3 is TX and goes to TDX on the Pi. Pin 4 is ground.

Adafruit Ultimate GPS HAT for Raspberry Pi
http://www.adafruit.com/products/2324?gclid=CjwKEAjwwN-rBRD-oMzT6aO_wGwSJABwEIkJCAMYJyy6h1IrAPDdW4B7pWDP0m-PBwPz1TAtpNVDnxoCcenw_wcB

![AssistManual](https://github.com/ThomasBassa/near-netcar/blob/master/docs/Diagrams/GPS_Module.png)

**Figure 14.** Picture of the GPS module to be used

![AssistManual](https://github.com/ThomasBassa/near-netcar/blob/master/docs/Diagrams/GPSSeqDiagram.png)

**Figure 15.** Sequence diagram for GPS reading and publishing

## Waterproofing (D009)
To meet IP54 specifications, the vehicle will be enclosing the GPS, Raspberry Pi, and the breakout board in a tupperware 
container, which will be fixed to the chassis of the vehicle. Holes will be drilled through the side for wires that need to 
come out and attach to components on the vehicle's exterior, and then sealed with rubber cement.
