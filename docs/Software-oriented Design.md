# Software

## Glossary
* Ground Station (GS) - User interface. The website and the joystick. Everything on the operator's end.
* 

## System Design
* Joystick Code
* Navigation (Autonomous and otherwise)
* Camera (Hardware overlap)
* Website Frontend
* 







## Subsystem Design

### Website Frontend
#### Behavior
  The website contains a 720p video feed from the camera next to a Google map of the area surrounding the vehicle that both refresh at 30 Hz. Below the map and video feed is a toggleable switch to change the mode of the vehicle between manual and autonomous navigation. There is also a "Stop" button that causes the vehicle to stop moving as quickly as possible, to be used in an emergency situation. In order to aid in navigation, there will also be buttons to begin directional instructions. These directional instructions will also be used to help the vehicle navigate autonomously. Waypoints are able to be placed on the map to give instructions on where the vehicle needs to go in both manual and autonomous mode.
  
#### Role
  The website frontend is used by the user to aid in their use of the vehicle. It allows the user to see through the vehicle's eyes, enabling effective navigation. It also shows where the vehicle is in geographic space so the user is also able to plan where he or she wants to go. It provides directional instructions to take the user wherever they want to go on campus as well. It also enables emergency stops through the stop button. Finally, it allows the user to put the vehicle into autonomous mode so it can navigate on its own if the user does not want to control it any more.
  
#### Major components, location, interaction
* Google Map: Top 3/4ths of the screen. Left half of the screen. Is used to drop waypoints, give directions while navigating, and update the user on the vehicle's location.
* Video Feed: Top 3/4ths of the screen. Right half of the screen. Is used to provide the user with a visual of what is in front of the vehicle.
* Autonomous Mode Checkbox (AMC): Below the map. When clicked, it will swap the vehicle from manual to autonomous mode and vice versa. 
* Stop Button: Below the video stream. When clicked, it will command the vehicle to stop moving as fast as possible. To be used in emergencies.
* Navigational Buttons: Between the Stop Button and the AMC. They will cause navigations to start between waypoints chosen by the user.
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
