# R3-SoftwareTask2-InayatAmin
 
I was unable to completely finish the training module as I was overwhelmed with a bunch assignments/design projects and midterms. I sincerely apolagize for this and will make sure that this does not occur in future projects.

What I have done so far is play around with the pygame library and the 'event' object functions, since these were new to me when learning python. 

I used these tools to help detect the inputs from a **controller**.

I have an Xbox one contoller where I detect if "RT" and "LT" are pressed using the pygame.JOYAXISMOTION functions and also detect if the left/right buttons are pressed on the Hat/D-pad using the pygame.JOYHATMOTION functions.

Once pressed I would get the value from the LT/RT as well since these would correspond to the speed of the motors on the rover.

What I would do for my next steps would be to look more into how tcp and socket programming works in python and then apply my knowledge to copy the input values received from the RT/LT as well as the left/right buttons from my program and send it to the server program. 

On the server program, I would take in the inputs of "RT" for forward and "LT" for backward. I would then need to figure out a mathematical formula to map out the range of values from LT/RT and Left/Right to the analog values of 0-255 for the rover motor speeds. Depending on the values received from my client program I would map it out onto the formula to get a value in the 0-255 range. 

This would then allow me to print out the output as a series of 4 arrays where each array would correspond to each of the motors and would have a direction (f or b from LT/RT and Left/Right) as well as its speed (Calculated from the previous step). 

Below is a screenshot of my code and what it prints out:

![image](https://user-images.githubusercontent.com/84003766/138626356-58251ade-dc5f-4a1b-b2ac-176e85f30aaf.png)
