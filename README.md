# HCaptcha Motion Data Generator


## How it works

The generator uses the format that HCaptcha uses in there post request:
 
    answers = {
            "235f50e0-c797-4122-b7f9-fefe3fc73839": "true",
            "64b5aae2-e513-4fa9-aca3-5e7c6dcca2f9": "false",
            "467573c1-9100-4527-84d8-a359c96a84e3": "true",
            "cd91a2ba-a9b0-4705-83bc-f449c9065efd": "true",
            "fd046c90-ca04-4d22-93ad-4c2eed9dbcfe": "false",
            "6d49241d-d4e2-4293-88a4-71992d99099f": "true",
            "00de96ab-423c-469c-bf63-6beb9eee7344": "true",
            "594d4f15-d741-47fc-ac8a-ce558cc28241": "true",
            "609eba26-d160-4188-837e-597070b3e2cf": "false",
        }

hCaptcha.py converts generates a random point, in a certain area, that would be clicked, as if the captcha was on screen.
These generated points are then used to create Bezier curves. The curves are realistic, as the middle point is not randomly generated, and is generated by creating a "box" between the two points.
This makes it so the curves are not sharp, and look human.

![Points](https://github.com/detectivevoke/hcaptcha-motion-data/blob/main/images/points.PNG)

Motion Data is then generated, from all these curves, using timestamps and the co-ordinates. TopLevel.py creates the payload within the motion data, and makes the payload seem legit.

This only works as the images from the response are all in order. If HCaptcha change this, it will stop working.

![Keys](https://github.com/detectivevoke/hcaptcha-motion-data/blob/main/images/keypad.PNG)

If this gets changed, the points will have to be inputted manually.




## Current Problems

A useragent is generated in main.py, and the gen has to use that useragent, otherwise it will get flagged. It only generates a Chrome useragent, as that is what the topLevel.py payload is set to.

The "box" created in Bezier.py, _box(), is shifted by one pixel, which doesnt change anything, just makes the box uneven, but will not flag the data.

Fairly slow, in comparrison to what it could be, as its generating thousands of possible coordinates into 2d arrays.

Unable to change useragent, working on it, able to input your own.


## Update 1 

Changed topLayer.py to actually make the payload correct
Timestamps now are correct, giving a default of 20 seconds to move the mouse to all the curves, to make it look more realistic, as it used to simply move within milliseconds of each point, so it is now more realistic
Moved most motion data creation itself into timeStamp.py

If anything else needs explaining, please DM @ Detective Voke#9720

Releasing ASAP :)
