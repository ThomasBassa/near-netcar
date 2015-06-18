#Design

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
