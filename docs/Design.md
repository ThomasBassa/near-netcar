#Design
The vehicle will be able to communicate with the ground station.  The vehicle shall also be able to navigate sidewalks autonomously between waypoints determined by a user at the ground station while avoiding obstacles.  In addition, the vehicle will be controlled by motion given by the joystick when in manual mode.  The vehicle shall be able to send live HD feed of camera while the vehicle is on. The vehicle will have a light and a buzzer to warn pedestrians while the vehicle is on and in motion. The vehicle will conform to IP66 standards, making it water, dust, and touch resistant.  

![BlockDiagram](https://github.com/ThomasBassa/near-netcar/blob/master/docs/BlockDiagram.png)

<Figure 1.> # (<h1>)Figure 1: Block Diagram of vehicle systems

![HardwareConnection](https://github.com/ThomasBassa/near-netcar/blob/master/docs/HardwareConnection.png)

<Figure 2.> ## (<h2>)Figure 2: Block diagram of Hardware Connections

![screenshot 2015-06-17 13 10 21](https://cloud.githubusercontent.com/assets/11369623/8214167/55704aae-14f5-11e5-9748-e12c572fcc7e.png)

![screenshot 2015-06-17 13 10 21](https://cloud.githubusercontent.com/assets/11369623/8214167/55704aae-14f5-11e5-9748-e12c572fcc7e.png)

<!---
It might be a good idea to label the figures in here so that you can refer to them as Figure 1, Figure 2, etc.
--> 

###Car Design

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

###Obstacle Avoidance

The car will be mounted with a lidar on a rotating servo. The servo will sweep back and forth, giving the lidar a 180 degree range of 'vision'. The results of the lidar scanning will be used to create a map of the world around the car, which will be constantly updated as the lidar continues to scan, and the car drives around. When the lidar detects an obstacle in the car's path, the obstacle will have a repulsion factor based on its distance; the closer the object, the more the car is repelled. Likewise, the waypoint to which the car is traveling will have an attraction factor of some value. The car will avoid the obstacle in its path while at the same time moving towards the objective in the most efficient way possible.

###Sound and Lights

An active buzzer <dB level> will be used, and will sound every 2 seconds. The buzzer will be contained in the waterproof box. The buzzer will be wired to the Pi in the following way:

<!---
Add pinout screen shot
--> 

Raspberry Pi                            Active buzzer module

    GND   ------------------------------------- ‘-’ 
    GPIO11 ------------------------------------- ‘s’

The method GPIO.write(pin, power) will be used with the parameters of the pin and GPIO.on/GPIO.off. Pin 11 on the Raspberry Pi will be used for 's'. The GPIO library for Raspberry Pi will be used in the program.

A 4" x 2" oblong amber LED marker light will be mounted on the top of the vehicle. The LED will be on whenever the vehicle is powered. The light will be powered by a battery connected by two bare end lead wires- two pins, power and ground. The GPIO library will again be used.

#Servo/Motor Control
###Behavior 
•	Uses the output from the joystick to control speed and direction of the vehicle.  This output is produced into two different methods, horizontal and vertical.  Horizontal output controls the direction of the vehicle (rotational degrees of the servos) and Vertical output controls the speed of the vehicle (negative output = positive acceleration, positive output = negative acceleration).  
•	Servo control method --> Horizontal(param)
o	This method changes the PWM signal to the servo using I2C library.
•	Motor control method--> Vertical(param)
##o	Figure out what code we need to talk to the motor controller
###Physical
•	This system consists of two servo motors, two motors, a servo controller, and an Evx-2 speed controller.  The two servo motors are directly connected to the vehicle and wired to a raspberry pi which connects to a website using crossbar.io.  This website uses RPC, passing joystick data over the Wi-Fi by calling the method Horizontal to the Pi which controls the rotation of the servos.  The Evx-2 speed controller will be mounted onto the robot and wired to the motors and raspberry pi.  Like the servos, the data from the joystick is transferred using RPC over the internet using crossbar.io to call the method Vertical and sent to the pi which feeds the speed controller data. 
###Software Components
•	Pi connects to the website through crossbar.io.  Ground control calls methods Horizontal(param) and Vertical(param) with the data from the joystick to control speed and direction of the robot.  
•	PWM Frequency- 1700Hz
•	Pi controls with i2c
###Function Horizontal(param)
•	This function controls the direction of the servos
•	Param is the input form the joystick and is a number between -1 and 1 on the x-axis
•	This function is called by the ground station using RPC 
###Function Vertical(param)
•	This function controls the acceleration and speed of the motors.
•	Param is the input from the joystick and is a number between -1 and 1 on the y-axis
•	This function is called by the ground station using RPC

