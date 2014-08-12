from SimpleCV import Camera
import time

#initialize the camera
cam = Camera() #take sthe default in built webcam
               #If not that the a UVC(USB Video Class : ext web cam)
               #using the default camera resolution, 
               #without special calibration, etc

# Capture and image and display it
cam.getImage().show() # The show() function simply pops up the image 
                      # from the camera on the screen. It is often 
                      # necessary to store the image in a variable 
                      # for additional manipulation instead
                      # of simply calling show() after getImage(), 
                      # but this is a good block of code for a quick
                      # test to make sure that the camera is properly 
                      # initialized and capturing video.

# Wait 10 seconds so the window doesn't close right away
time.sleep(10)