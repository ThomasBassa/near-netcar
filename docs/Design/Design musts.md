# Glossary (A001)

* Ground Station (GS) - User interface. The website and the joystick.
  Everything on the operator's end.
* Vehicle - The RC car and its onboard Pi

# Musts

## System Design (A002)
This is the set of subsystems necessary in this system.
* Joystick - The way the user will control the vehicle
* Camera (Hardware overlap) - What the user will use to see in front of the vehicle
* Website Frontend - The way the user will see the camera feed, map, and various other statistics about the vehicle 

## Use Cases (A003)

### Manual Vehicle Movement (A004)
1. User moves joystick
2. System sends information to vehicle accordingly
3. Vehicle moves

## Subsystem Design (B001)

### Website Frontend (B002)

#### Behaviour (B003)
The website contains a 720p video feed from the camera next to a Google map
of the area surrounding the vehicle that both refresh at 30 Hz.
There is also a Stop button that causes the vehicle to stop moving as quickly as possible, to be used
in an emergency situation. There will also be some vehicle statistics 
displayed below the camera feed, such as heading, which will aid in navigation, 
and the speed of the vehicle, to tell the user how fast he/she is going.

#### Role (B004)
The website frontend is used to display vehicle status information.
It allows the user to see through the vehicle's eyes via the onboard camera.
It also shows where the vehicle is in geographic space
so that the user is also able to plan where he or she wants to go.
It provides directional instructions to take the user wherever
they want to go on campus as well.
It also enables emergency stops through the stop button.
The website frontend will show important information about the current status of the car 
such as the cardinal direction the vehicle is facing,
and the vehicle's current speed.

#### Major components, location, interaction (B005)
* Google Map: Top 3/4ths of the screen. Left half of the screen.
  Is used to update the user on the vehicle's location.
* Video Feed: Top 3/4ths of the screen. Right half of the screen.
  Is used to provide the user with a visual of what is in front of the vehicle and aid in navigation.
* Stop Button: Below the video stream.
  When clicked, it will command the vehicle to stop moving as fast as possible.
  It calls an RPC named emergStop to tell the robot to begin slowing down and eventually stop.
  It can stop the robot from 30 mph in 15 meters, to be used in emergencies.
* Data: Below the camera feed.
  Will display the current heading to the user
  and the vehicle's current speed.

### Joystick (B006)

#### Behaviour (B007)

Joystick produces outputs based on the current position using Pygame.
These outputs should be tuples of two floats passed through RPC protocol to the vehicle using Autobahn.
The vehicle-mounted pi runs code that maps the joystick's current position to servo commands,
turning the wheels of the vehicle accordingly.
The joystick will continue sending data, even when not moving, at 30 Hz (every .0333 seconds).

#### Physical (B008)
The system consists entirely of the joystick and the computer that it's plugged into via USB.
The joystick will be physically next to the computer,
and its code will be on the computer as well.
The user interacts by operating the joystick to control the vehicle's movement.

#### Software Components (B009)
The initial function onJoin runs when the session begins. onJoin then runs the function joyUpdate, which picks up the
joystick movement, converts it into a tuple of floats, and passes is to another function, joyMonitor, 30 times a
second. joyMonitor runs	directly on the pi, and tells the servos to turn.

##### Function - onJoin() (F001)
* Args - self, details (WAMP stuff) <!-- These should be explained, but it's okay...-->
* Returns - n/a
* Behaviour - Runs the functions within when the session connects

##### Function - joyUpdate() (F002)
* Args - n/a
* Returns - Tuple of floats called val, -1.1 <= vals <= 1.1
* Behaviour - Picks up the movements of the joystick 30 times a second,
converts the position to a tuple of two floats, and calls the function 	joyMonitor() with vals.

##### Function - joyMonitor(put) (F003)
* Args - put
 <!-- get put range from hardware team -->
* Returns - int passed to the servos
* Behaviour - Takes in val from joyUpdate and uses it to control the servos through the setPWM function.

### Vehicle Camera (C001)

#### Behaviour (C002)
An HD camera will be mounted to the front of the vehicle so that it faces forward.
The camera's onboard components capture shots of the vehicle's front-facing view and converts that view to video. The resulting video is then sent to the ground station in real time and displayed in a window on the ground station webpage.

#### Physical (C003)
The sensors will be taken from a Ubiquiti Aircam Mini camera, and attached to the strut at the front end of the vehicle.

#### Software Components (C004)
The camera's sensor captures shots of what it sees at a rate of 30 hz.
Default software in the camera converts the frames that are captured
into a 30fps video at 720p resolution. That video is then sent to the UI
that is controlled by the ground station and displayed in real time.  

Ubiquiti Aircam
http://www.newegg.com/Product/Product.aspx?Item=9SIA0ZX20N9128&cm_re=ubiquiti-_-0ED-0005-00022-_-Product

### Training System (Z011)
The training system will be a printed manual describing all the features of the website frontend and the joystick.
The training system is for new users to the vehicle, instructing them so they will know how to handles the vehicle, especially in case of emergencies. 

### Hardware Design (C005)

The vehicle will communicate with the ground station.
A user at the ground station controls the vehicle using a joystick.
The vehicle shall be able to send live HD feed from a camera while the vehicle is powered.
The vehicle will have a light and a buzzer to warn pedestrians while the vehicle is on.
The vehicle will conform to IP54 standards, protecting it from water, dust, and touch.
The vehicle will contain a gps to transmit its location

### Vehicle Design (C006)

### Ground Station Communication (C007)
Application components connect to Crossbar.io and can then talk to each other using two patterns:
Remote Procedure Calls and Publish & Subscribe. Crossbar.io directs and transmitts messages to the proper components ("message routing").

#### Remote Procedure Calls (C008)
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

#### Publish & Subscribe (C009)
With the Publish & Subscribe pattern, any component can subscribe to receive events published from other components and 
publish events which other subscribed components will receive. Crossbar.io routes event published to all components that have 
subscribed to receive events for the topic.

#### Methods (C010)
To PUBLISH an event - session.publish('join.session', 'Session joined')

To REGISTER a procedure for remote calling - session.register(Horizontal(param)), 'com.myapp.add2')

### Sound and Lights (Z022)
An active buzzer 65db will be used, and will sound every 2 seconds. The buzzer will be contained in the waterproof box. 
The buzzer will be wired to the Pi in the following way:

The GPIO library for Raspberry Pi will be used in the program. The method GPIO.write(pin, power) will be used with the 
parameters of the pin and GPIO.on/GPIO.off. Pin 11 on the Raspberry Pi will be used for 's'.

A 4" x 2" oblong amber LED marker light will be mounted on the top of the vehicle. The light will be on while the vehicle is 
powered. The light will be powered by a battery connected by two bare end lead wires with two pins, power and ground.
The GPIO library will again be used.

DC 24V Electronic Amber LED Flashing Alarm Siren 100dB BJ-3
http://www.amazon.com/OBLONG-SURFACE-CLEARANCE-MARKER-EL-114303CA/dp/B00N54AT54/ref=sr_1_13?s=electronics&ie=UTF8&qid=1433356800&sr=1-13&keywords=amber+LEDs

### Servo/Motor Control (D001)

#### Behavior (D002)
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

#### Physical (D003)
This system consists of two servos, two motors, a servo controller,
and a speed controller. The two servos are directly connected to the vehicle
and wired to a Raspberry Pi that connects to a website using crossbar.io.
This website uses RPC, passing joystick data over the Wi-Fi by calling
the method Horizontal() to the Pi which controls the rotation of the servos.
The Evx-2 speed controller will be mounted onto the robot and wired to
the motors and Raspberry Pi. Like the servos, the data from the joystick
is transferred using RPC over the internet using crossbar.io
to call the method Vertical() and sent to the Pi which feeds the speed controller data.

Evx-2 speed controller
https://traxxas.com/products/parts/escs/3019Revx2lvd

#### Software Components (D004)
The Pi connects to the ground station through crossbar.io.
Ground control calls methods Horizontal(param) and Vertical(param)
with the data from the joystick to control speed and direction of the robot.
The motor's PWM frequency is 1700 Hz, and the Pi controls the speed controller with I2C.

### Battery (Z069)
The battery will power the whole vehicle, and needs to have enough voltage output to power all the sensors. 
The battery needs to be large enough for all the sensors and the vehicle to run for a half hour.

### Mounting Container (D006)
A flat 3D printed platform will hold cargo and act as a landing pad.
The vehicle suspension can hold three pounds. 

### Video Feed (D007)
The casing will be removed from a Ubiquiti Aircam H.264 1Megapixel/720P 
camera, and it will be mounted on the top of the vehicle, facing forward. The 
camera requires 24V, and has 30fps. First the camera’s IP is determined using 
its provided software. The IP address will be fixed. The port used will be 8080. 
The port and IP will be used to contact the camera from the ground station. 

### Vehicle Location Tracking (D008)

The vehicle's location will be tracked using a GPS module. The GPS module will talk to the Pi with serial communication. The Pi will read string messages from the GPS module. Then the program will interpret the message to find the latitude and longitude of the vehicle. This information will be published over crossbar.io to the ground station. This will happen every main loop iteration. Pin 1 on the module goes to 3.3 V power. Pin 2 is RX and goes to RDX on the Pi. Pin 3 is TX and goes to TDX on the Pi. Pin 4 is ground.

Adafruit Ultimate GPS HAT for Raspberry Pi
http://www.adafruit.com/products/2324?gclid=CjwKEAjwwN-rBRD-oMzT6aO_wGwSJABwEIkJCAMYJyy6h1IrAPDdW4B7pWDP0m-PBwPz1TAtpNVDnxoCcenw_wcB

### Waterproofing (D009)
To meet IP54 specifications, the vehicle will be enclosing the GPS, Raspberry Pi, and the breakout board in a tupperware 
container, which will be fixed to the chassis of the vehicle. Holes will be drilled through the side for wires that need to 
come out and attach to components on the vehicle's exterior. The components of the vehicle will be able to withstand temperatures as low as 0 degrees Celsius, and up to 50 degrees Celsius
