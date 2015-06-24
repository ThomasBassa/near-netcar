#Vehicle Design

The vehicle will communicate with the ground station.
The vehicle shall have two modes: assisted manual mode and manual mode.
In manual mode, a user at the ground station controls the vehicle using a joystick.
In assisted manual mode, the vehicle intervenes when an obstacle is detected and
keeps the vehicle on the sidewalk. The user can switch between the two modes.
The vehicle shall be able to send live HD feed from a camera while the vehicle is powered.
The vehicle will have a light and a buzzer to warn pedestrians while the vehicle is on.
The vehicle will conform to IP54 standards, protecting it from water, dust, and touch. 
The vehicle shall be pretty.

![BlockDiagram](https://github.com/ThomasBassa/near-netcar/blob/master/docs/Diagrams/MainBlockDiagram.png)

**Figure 1.** Block Diagram of Vehicle Components

![HardwareConnection](https://github.com/ThomasBassa/near-netcar/blob/master/docs/Diagrams/HardwareDiagram.png)

**Figure 2.** Block diagram of Hardware Connections

#Car Design

![screenshot 2015-06-17 13 10 21](https://cloud.githubusercontent.com/assets/11369623/8214167/55704aae-14f5-11e5-9748-e12c572fcc7e.png)

**Figure 3.** <>

This strut design was printed using the TAZ 5 printer.
The vehicle has one strut mounted onto the front and one onto back of the chassis to give suport for the suspension.

![screenshot 2015-06-17 13 06 49](https://cloud.githubusercontent.com/assets/11369623/8214178/5cb7feec-14f5-11e5-985d-d3d6e6b22ce7.png)

**Figure 4.** <>

We have 8 of these printed, 4 per strut, attached to struts with acetone-glue; shocks are screwed into these.
This block was printed to give suport for the shocks.
Four blocks were used to glue: one block to each side of the top 2 holes on each strut,
to support the nails we later used to prop up the spings on the strut. They were glued using acetone.

<!-- Thomas: How much of this is necessary when you could link to Autobahn docs... especially if this is copy/paste? -->
#Ground Station Communication
Application components connect to Crossbar.io and can then talk to each other using two patterns:
Remote Procedure Calls and Publish & Subscribe. Crossbar.io directes and transmitts messages to the right components ("message routing").

###Remote Procedure Calls
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

###Publish & Subscribe
With the Publish & Subscribe pattern, any component can subscribe to receive events published from other components and 
publish events which other subscribed components will receive. Crossbar.io routes event published to all components that have 
subscribed to receive events for the topic.

<!-- Thomas: This bit is probably okay though since their documentation for code is kind of thick -->
###Methods
To PUBLISH an event - session.publish('join.session', 'Session joined')

To REGISTER a procedure for remote calling - session.register(Horizontal(param)), 'com.myapp.add2')

![CommunicationBlock](https://github.com/ThomasBassa/near-netcar/blob/master/docs/Diagrams/CommunicationsBlocks.png)

**Figure 3.** Block diagram of server communications

#Obstacle Avoidance
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

![AssistManual](https://github.com/ThomasBassa/near-netcar/blob/master/docs/Diagrams/AssistManualState.png)

**Figure 4.** State diagram of manual assisted and manual mode

###Use Case - Obstacle Detection

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

**Figure 4.** State diagram of manual assisted and manual mode

![AssistManual](https://github.com/ThomasBassa/near-netcar/blob/master/docs/Diagrams/MainSeq.png)

**Figure 4.** State diagram of manual assisted and manual mode

![AssistManual](https://github.com/ThomasBassa/near-netcar/blob/master/docs/Diagrams/ObstacleDetection.png)

**Figure 4.** State diagram of manual assisted and manual mode

#Sound and Lights
An active buzzer <dB level> will be used, and will sound every 2 seconds. The buzzer will be contained in the waterproof box. 
The buzzer will be wired to the Pi in the following way:

    Raspberry Pi                            Active buzzer module

    GND   ------------------------------------- ‘-’
    GPIO11 ------------------------------------- ‘s’

The GPIO library for Raspberry Pi will be used in the program. The method GPIO.write(pin, power) will be used with the 
parameters of the pin and GPIO.on/GPIO.off. Pin 11 on the Raspberry Pi will be used for 's'.

A 4" x 2" oblong amber LED marker light will be mounted on the top of the vehicle. The light will be on while the vehicle is 
powered. The light will be powered by a battery connected by two bare end lead wires with two pins, power and ground.
The GPIO library will again be used.

#Servo/Motor Control
###Behavior
This system uses the output from the joystick to control speed and direction of the vehicle.
This output is produced into two different vehicle methods, horizontal and vertical.
Horizontal output controls the direction of the vehicle (rotational degrees of the servos)
and Vertical output controls the speed of the vehicle
(negative output = positive acceleration, positive output = negative acceleration).  
- Servo control method --> Horizontal(param): This method changes the PWM signal
to the servo using I2C library.
Turning to the right is 150. Changing to the left is 600.
The last value received is saved in a variable to be used for sidewalk detection.

- Motor control method--> Vertical(param): This method changes the I2C output to the motors using I2C library.


<!-- From the ground station team-- look at Interface.md-- this document needs to be consistent with that -->
###Physical
This system consists of two servos, two motors, a servo controller,
and an Evx-2 speed controller. The two servos are directly connected to the vehicle
and wired to a Raspberry Pi that connects to a website using crossbar.io.
This website uses RPC, passing joystick data over the Wi-Fi by calling
the method Horizontal() to the Pi which controls the rotation of the servos.
The Evx-2 speed controller will be mounted onto the robot and wired to
the motors and Raspberry Pi. Like the servos, the data from the joystick
is transferred using RPC over the internet using crossbar.io
to call the method Vertical() and sent to the Pi which feeds the speed controller data.

###Software Components
The Pi connects to the ground station through crossbar.io.
Ground control calls methods Horizontal(param) and Vertical(param)
with the data from the joystick to control speed and direction of the robot.
The motor's PWM frequency is 1700 Hz, and the Pi controls the speed controller with I2C.

###Function Horizontal(param)
This function controls the direction of the servos. Param is the input
from the joystick and is a number between -1 and 1 on the x-axis.
This function is called by the ground station using RPC.

###Function Vertical(param)
This function controls the acceleration and speed of the motors.
Param is the input from the joystick and is a number between -1 and 1 on the y-axis.
This function is called by the ground station using RPC.

#Sidewalk Detection

![AssistManual](https://github.com/ThomasBassa/near-netcar/blob/master/docs/Diagrams/ColorSensor.png)

**Figure 4.** State diagram of manual assisted and manual mode

An RGB sensor will be mounted onto the front bumper of the car, and the Raspberry Pi will communicate with it using I2C 
(address 0x29), with wiring (from the website) VDD to 3-5 V DC, ground to common ground, SCL to I2C Clock and SDA to I2C 
Data. The sensor will keep track of the colour of the ground directly in front of the vehicle; whenever the ground is not 
white or light grey (sidewalk coloured), the car will turn in the opposite direction as the joystick input being given, for 1 
second, before returning control to the user, thereby keeping the vehicle on the sidewalk.

Note on colours: RGB values will be considered 'sidewalk colours' as long as either

1. all values are greater than 200 (very light colours; coloured light or different times of day may result in the sidewalk 
looking tinted a different colour; these are very light and we won't run into any ground coloured like this (ie no roads or 
nature are these colours, well maybe a flower or something but we'd only have an issue if the floor were made entirely of 
pastel flowers, which isn't happening)
2. all values within two of each other, and greater than 160 (accounts of slightly darker sidewalks, with the values very 
close, only greyscale colours will be allowed, and no asphalt will be this light) 

###Use Case - Sidewalk Lost
1. press button on website to switch to assisted mode
2. calls method on vehicle
3. assisted manual comes on
  - colour sensor comes on
4. if colour sensor detects no sidewalk
  - use last joystick input (left/right) and turn opposite direction for 1 second

![AssistManual](https://github.com/ThomasBassa/near-netcar/blob/master/docs/Diagrams/ColorSensorSeq.png)

**Figure 4.** State diagram of manual assisted and manual mode

#Mounting Container
A 28 Qt. Latch Box with dimensions 23" x 16" x 6" will be used.
Holes will be drilled into the container around the struts and
attached to the struts with zip ties. The holes at the bottom of the container will
be sealed with rubber cement to prevent water from entering the container.
The container has a lid for protection.

![AssistManual](https://github.com/ThomasBassa/near-netcar/blob/master/docs/Diagrams/VehicleContainer.png)

**Figure 4.** State diagram of manual assisted and manual mode

#Vehicle Location Tracking

![AssistManual](https://github.com/ThomasBassa/near-netcar/blob/master/docs/Diagrams/GPS_Module.png)

**Figure 4.** State diagram of manual assisted and manual mode

![AssistManual](https://github.com/ThomasBassa/near-netcar/blob/master/docs/Diagrams/GPSSeqDiagram.png)

**Figure 4.** State diagram of manual assisted and manual mode

#Waterproofing
To meet IP54 specifications, the vehicle will be enclosing the GPS, Raspberry Pi, and the breakout board in a tupperware 
container, which will be fixed to the chassis of the vehicle. Holes will be drilled through the side for wires that need to 
come out and attach to components on the vehicle's exterior, and then sealed with rubber cement.
