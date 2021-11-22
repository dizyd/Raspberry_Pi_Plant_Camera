from picamera import PiCamera
from time import sleep
import os
from datetime import date
from datetime import datetime





camera = PiCamera()
camera.rotation = 180

camera.start_preview()

for i in range(24):
    
    # get current time
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    camera.annotate_text = now
    today = date.today()

    # take and safe picture
    camera.capture('/home/pi/plant_camera/images/image_%s.jpg' % i)

    # wait for 60 minutes
    sleep(3600)

camera.stop_preview()