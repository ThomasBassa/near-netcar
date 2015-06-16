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
  TODO
#### Major components, location, interaction
* Google Map: Top 3/4ths of the screen. Left half of the screen. Is used to drop waypoints, give directions while navigating, and update the user on the vehicle's location.
* Video Feed: Top 3/4ths of the screen. Right half of the screen. Is used to provide the user with a visual of what is in front of the vehicle.
* Autonomous Mode Checkbox:
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
