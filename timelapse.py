from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.rotation = 0
camera.resolution = (2592, 1944)
camera.start_preview()
for i in range(500):
    sleep(30)
    camera.capture('/home/pi/Desktop/images/image%s.jpg' % i)
camera.stop_preview()
