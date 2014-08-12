from SimpleCV import Camera, Display, Color
import time

# Initialize the camera
cam = Camera()
# Initialize the display
display = Display()
# Take an initial picture
img = cam.getImage() 
# Write a message on the image
img.drawText("Left click to save a photo.", 
 50, 50, color=Color().getRandom()) 
# Show the image on the display
img.save(display)

time.sleep(3)

counter = 0

while not display.isDone(): # for window handling
	
## Pseudo live view
   img = cam.getImage() # get image
   # Update the display with the latest image
   img.save(display)
   # Since it's in while, It'll keep on rolling
   # and displaying making it appear
   # as live view. 
####################

   if display.mouseLeft:
      # Save image to the current directory
      img.save("photobooth" + str(counter) + ".jpg") 
      img.drawText("Photo saved.", 50, 50, color=Color().getRandom()) 
      img.save(display)
      time.sleep(1)
      counter = counter + 1
