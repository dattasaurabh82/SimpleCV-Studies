from SimpleCV import Camera, Display, Image
import time

#initialize the camera
cam = Camera() #take sthe default in built webcam
               #If not that the a UVC(USB Video Class : ext web cam)
               #using the default camera resolution, 
               #without special calibration, etc

#initialize the display
display = Display()

#snap a picture using the camera
img = cam.getImage()

#display the image
img.save(display)

# Wait 10 seconds so the window doesn't close right away
time.sleep(10)