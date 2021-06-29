# hands_up_robot
Code for the raspi and arduino for a custom karate helmet that yells at you when your hands are down

## About
This project uses the hardware listed below:

* [Raspberry Pi 0 W](https://raspberrypi.org/products)
* [Arduino Uno](https://store.arduino.cc)
* [Elegoo Arduino Kit](https://www.amazon.com/ELEGOO-Project-Tutorial-Controller-Projects/dp/B01D8KOZF4/ref=sr_1_1_sspa?dchild=1&gclid=CjwKCAjwieuGBhAsEiwA1Ly_nRVXU7gvjTrQ3-CqXilhhYByVTwrCBprHiMRavElYcfAI-rEBF8OsBoCsyQQAvD_BwE&hvadid=182609996783&hvdev=c&hvlocphy=9004859&hvnetw=g&hvqmt=e&hvrand=12822772681615992111&hvtargid=kwd-198539702654&hydadcr=18008_9812099&keywords=elegoo+arduino+kit&qid=1624977713&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExNjZDM0dQU0ZaRVMzJmVuY3J5cHRlZElkPUEwNDg4NDc0MktaOVk4RDJVRjE0RCZlbmNyeXB0ZWRBZElkPUEwOTE1MDY2MzhLWVhQOVdMOVNVQiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=)


## How it works: 

On a (modified) karate helmet there are two pushbuttons that send signals down to an Arduino Uno.
if none of the buttons have been pressed for a set amount of time (changes from 3-5 depending on difficulty level), then the arduino sends
a signal to the Raspberry Pi via Serial, where the Raspi plays a random audio file from internal memory and sends a signal back when it's finished,
restarting the arduino timer, for the same thing to run again
