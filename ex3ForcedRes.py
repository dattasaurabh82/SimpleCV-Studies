from SimpleCV import Camera
import time
cam = Camera(0, { "width": 1200, "height": 1024 })
img = cam.getImage()
img.drawText("Ello Punk", 160, 120)
img.show()
time.sleep(5)