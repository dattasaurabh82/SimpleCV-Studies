from SimpleCV import Camera, Image, Display
import time

cam = Camera()
display = Display()
#cam.live()
# Set the number of frames to capture
numFrames = 10

# Loop until we reach the limit set in numFrames
for x in range(0, numFrames):
	img = cam.getImage()
	filename = "image-" + str(x) + ".jpg" 
	img.save(filename) 
	img.save(display)
	print "Saved image as: " + filename
	time.sleep(3)
