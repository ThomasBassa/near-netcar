# Software Dependencies

## Python 2.7
- https://www.python.org/download/releases/2.7.2/
- v2.7.3
- `python` and `python-dev` apt-get packages

## Autobahn
- http://autobahn.ws/python/
- v0.10.4
- `autobahn` package on pip

## Twisted
- http://autobahn.ws/python/reference/autobahn.twisted.html
- pip package-- most likely installed with Autobahn

## Crossbar
- http://crossbar.io
- Latest version as of the commit for this line (blame)
- `crossbar` package on pip

## Pygame
- http://www.pygame.org/news.html
- Latest version as of the commit for this line (blame)
- `python-pygame` package on apt-get

## Adafruit PWM/Servo controller
- https://learn.adafruit.com/adafruit-16-channel-servo-driver-with-raspberry-pi/using-the-adafruit-library
- https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code
- Clone the above repo, only `Adafruit_PWM_Servo_Driver.py` is relevant

## asyncio
- https://docs.python.org/3.4/library/asyncio.html
- A python library that replaces Twisted on the Pi

## VLC Media Player
- http://www.videolan.org/index.html
- We use the browser plugin from VLC to embed the camera's video into the UI.

## Mozilla Firefox/Internet Explorer/Safari
- https://www.mozilla.org/en-US/firefox/new/
- http://windows.microsoft.com/en-us/internet-explorer/download-ie
- https://support.apple.com/downloads/safari
- These are the only browsers compatible with the VLC plugin natively. 
- Use one of these browsers when accessing the UI.
