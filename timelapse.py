from picamera import PiCamera
from time import sleep
import datetime
from os import system

camera = PiCamera()
global timestamp

camera.rotation = 0
camera.resolution = (2592, 1944)
camera.start_preview()
for i in range(500):
    sleep(10)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    camera.capture('/home/pi/Desktop/images/image%s.jpg' %timestamp)
camera.stop_preview()
