from SimpleCV import Display, Image
import time

#initiate display
display = Display()

#display pygame logo
img = Image("logo")
img.save(display)

print "I launched a window"

# Helps in interacting with the window
# This while loop will keep looping until the window is closed
while not display.isDone():
    time.sleep(0.1)

print "You closed the window"
