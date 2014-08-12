from SimpleCV import Camera
import time

# With Windows the camera ID number corresponds to the order
# of the DirectShow devices, which is a bit more complicated to find. So with Windows,
# passing in any number as the camera ID will result in a pop up window that lets you
# map that ID number to a particular device. The ID on a Mac is most easily found with
# trial and error.


# First attached camera
cam0 = Camera(0)
# Second attached camera
cam1 = Camera(1)
# Show a picture from the first camera
img0 = cam0.getImage()
img0.drawText("I am Camera ID 0")
img0.show()
# Show a picture from the first camera
img1 = cam1.getImage()
img1.drawText("I am Camera ID 1")
img1.show()

#hold the image on screen for 5 seconds
time.sleep(5)
