#Vehicle Design

The vehicle will communicate with the ground station.  The vehicle shall have two modes: assisted manual mode and manual mode. In manual mode, a user at the ground station controls the vehicle using a joystick. In assisted manual mode, the vehicle intervenes when an obstacle is detected and keeps the vehicle on the sidewalk. The user can switch between the two modes. The vehicle shall be able to send live HD feed from a camera while the vehicle is powered. The vehicle will have a light and a buzzer to warn pedestrians while the vehicle is on. The vehicle will conform to IP54 standards, protecting it from water, dust, and touch.  

![BlockDiagram](https://github.com/ThomasBassa/near-netcar/blob/master/docs/Diagrams/MainBlockDiagram.png)
**Figure 1.** Figure 1: Block Diagram of Vehicle Components

![HardwareConnection](https://github.com/ThomasBassa/near-netcar/blob/master/docs/Diagrams/HardwareDiagram.png)
**Figure 2.** Figure 2: Block diagram of Hardware Connections

#Car Design

![screenshot 2015-06-17 13 10 21](https://cloud.githubusercontent.com/assets/11369623/8214167/55704aae-14f5-11e5-9748-e12c572fcc7e.png)

<!---
This needs to be more specific. We have struts finished! Which is good. I'd like to see a diagram with the strut's measurements (don't worry, we have this. We just need a pic of our actual design in SolidWorks. Explain the top thingy. That it'll be used to hold the payload up. How will it be used to hold the payload up? Also, use complete sentences. It sounds better.
--> 
<!---
Didn't mention the material used in the print. Specify which material and why. Always talk about why. Talk about how much infill used and why.
--> 
Strut design, we have 2 of these printed and mounted onto the chassis. Used for suspension.

<!---
Is this a duplicate picture? A picture of the actual vehicle might be nice.
--> 
<!---
Why is it tilted in the picture?
--> 
![screenshot 2015-06-17 13 06 49](https://cloud.githubusercontent.com/assets/11369623/8214178/5cb7feec-14f5-11e5-985d-d3d6e6b22ce7.png)

<!---
I'm confused. Where are these attached to the struts? It doesn't say where they're attached.
--> 
We have 8 of these printed, 4 per strut, attached to struts with acetone-glue; shocks are screwed into these.

![screenshot 2015-06-17 13 09 40](https://cloud.githubusercontent.com/assets/11369623/8214180/61576aa0-14f5-11e5-80a5-221eb7742fef.png)

<!---
We need to add more detail to this part. We'll talk about it.
--> 
(Above) lip for waterproofing, we have one of these printed; has been modified after printing to fit. (Below) lip in SolidWorks

![screenshot 2015-06-17 13 11 34](https://cloud.githubusercontent.com/assets/11369623/8214183/6881ce60-14f5-11e5-943d-adec01ff3cb0.png)


##Ground Station Communication
Add text here

![CommunicationBlock](https://github.com/ThomasBassa/near-netcar/blob/master/docs/Diagrams/CommunicationsBlocks.png)

**Figure 3.** Block diagram of server communications

#Obstacle Avoidance
The vehicle will be mounted with a lidar laser rangefinder. The vehicle will have two modes (assisted manual/manual). When the vehicle is powered on, it will start in manual mode and after 20 seconds elapse (timer), it will switch to assisted manual mode. In assisted manual mode, the servo will sweep back and forth constantly, on an axis that will establish a 1.2373 degree field of vision which will detect obstacles. This was determined using Figure <>. If an obstacle is detected, the vehicle will cease motion and alert the user (by publishing an obstacle detection event) that an obstacle is obstructing its path. The user will then have an option to override the alert and control the vehicle manually. Choosing to switch it to manual mode will only last 20 seconds before automatically switching back to assisted manual mode.

![AssistManual](https://github.com/ThomasBassa/near-netcar/blob/master/docs/Diagrams/AssistManualState.png)
**Figure 4.** State diagram of manual assisted and manual mode

###Use Case - Obstacle Detection

1. press button on website to switch to assisted mode
2. calls method on vehicle
3. assisted manual comes on 

    •   Lidar comes on, servo begins rotating
4. if an obstacle is detected

    •   vehicle stops
    •   alerts user by publishing event
5. user has option for a 20 sec override
6. if override option is not taken

    •   wait until obstacle has moved
7. if override option taken

    •   start a timer
    •   switch to manual mode
    •   switch back to assisted after 20 sec

#Sound and Lights
An active buzzer <dB level> will be used, and will sound every 2 seconds. The buzzer will be contained in the waterproof box. The buzzer will be wired to the Pi in the following way:

<!---
Add pinout screen shot
--> 

Raspberry Pi                            Active buzzer module

    GND   ------------------------------------- ‘-’ 
    GPIO11 ------------------------------------- ‘s’

The GPIO library for Raspberry Pi will be used in the program. The method GPIO.write(pin, power) will be used with the parameters of the pin and GPIO.on/GPIO.off. Pin 11 on the Raspberry Pi will be used for 's'. 

A 4" x 2" oblong amber LED marker light will be mounted on the top of the vehicle. The light will be on while the vehicle is powered. The light will be powered by a battery connected by two bare end lead wires with two pins, power and ground. The GPIO library will again be used.

#Servo/Motor Control
###Behavior 
This system uses the output from the joystick to control speed and direction of the vehicle.  This output is produced into two different vehicle methods, horizontal and vertical.  Horizontal output controls the direction of the vehicle (rotational degrees of the servos) and Vertical output controls the speed of the vehicle (negative output = positive acceleration, positive output = negative acceleration).  
•	Servo control method --> Horizontal(param): This method changes the PWM signal to the servo using I2C library. Turning to the right is 150. Changing to the left is 600. The last value received is saved in a variable to be used for sidewalk detection.

•	Motor control method--> Vertical(param): This method changes the I2C output to the motors using I2C library.

<!---
Figure out motor code
--> 

###Physical
This system consists of two servos, two motors, a servo controller, and an Evx-2 speed controller.  The two servos are directly connected to the vehicle and wired to a Raspberry Pi that connects to a website using crossbar.io.  This website uses RPC, passing joystick data over the Wi-Fi by calling the method Horizontal() to the Pi which controls the rotation of the servos.  The Evx-2 speed controller will be mounted onto the robot and wired to the motors and Raspberry Pi.  Like the servos, the data from the joystick is transferred using RPC over the internet using crossbar.io to call the method Vertical() and sent to the Pi which feeds the speed controller data. 

###Software Components
The Pi connects to the ground station through crossbar.io.  Ground control calls methods Horizontal(param) and Vertical(param) with the data from the joystick to control speed and direction of the robot. The motor's PWM frequency is 1700 Hz, and the Pi controls the speed controller with I2C.

###Function Horizontal(param)
This function controls the direction of the servos. Param is the input from the joystick and is a number between -1 and 1 on the x-axis. This function is called by the ground station using RPC.

###Function Vertical(param)
This function controls the acceleration and speed of the motors. Param is the input from the joystick and is a number between -1 and 1 on the y-axis. This function is called by the ground station using RPC.

#Sidewalk Detection
Talk about color sensor.

###Use Case - Sidewalk Lost

1. press button on website to switch to assisted mode
2. calls method on vehicle
3. assisted manual comes on 

    •   colour sensor comes on 
4. if colour sensor detects no sidewalk

    •   use last joystick input (left/right) and turn opposite direction for 1 second


#Mounting Container
A 28 Qt. Latch Box with dimensions 23" x 16" x 6" will be used. Holes will be drilled into the container around the struts and attached to the struts with zip ties. The holes at the bottom of the container will then be sealed with rubber cement to prevent water from entering the container. The container has a lid for protection.

#Vehicle Location Tracking
Add text here
