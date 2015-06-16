# Software

Autobahn will be used for its RPC and PubSub functions throughout the project

[Documentation](http://autobahn.ws/python/)

## UI
* The vehicle camera's operating system streams data to the UI
* The vehicle will use Djikstra's algorithm to plot a path between intersections
* The UI will utilize RPC to continuously update the vehicle on the joystick position
* The UI will have a button that uses RPC to stop all vehicle movement
* The UI will have a button that uses RPC to switch between manual and automatic mode
* The vehicle will use PubSub to communicate its location to the UI 
* The vehicle will use PubSub to communicate its speed to the UI 
* The UI will display the location and speed of the vehicle
* 
