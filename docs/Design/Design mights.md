
# Mights

## Use Cases (D021) 

###  Assisted Mode (A005)
1. User clicks switch on Website Frontend
2. Ground Station sends a boolean to the PubSub server
3. Vehicle turns off assisted mode for 20 seconds 
4. Assisted mode turns back on automatically

### Obstacle Detection (C012)
1. Lidar comes on, servo begins rotating
2. If an obstacle is detected, the vehicle stops and alerts user by publishing event
3. User has option for a 20 sec override
4a. If override option is not taken, vehicle will wait until obstacle has moved
4b. If override option is taken, the vehicle will start a 20sec timer, switch to manual mode, switch back to assisted after 20 sec

### Sidewalk Lost (D005)
1. One of the color sensors detects vehicle on grass
2. Vehicle moves backwards and in the direction of the sensor which did not detect grass

## Obstacle Avoidance (C011)
The vehicle will be mounted with a lidar laser rangefinder.
The vehicle will have two modes (assisted manual/manual). When the vehicle is powered on,
it will start in manual mode and after 20 seconds elapse (timer),
it will switch to assisted manual mode. In assisted manual mode,
the servo will sweep back and forth constantly, on an axis that will
establish a 1.2373 degree field of vision which will detect obstacles.
This was determined using Figure 6. If an obstacle is detected, the vehicle will
cease motion and alert the user (by publishing an obstacle detection event)
that an obstacle is obstructing its path.
The user will then have an option to override the alert and control the vehicle manually.
Choosing to switch it to manual mode will only last 20 seconds before automatically switching back to assisted manual mode.