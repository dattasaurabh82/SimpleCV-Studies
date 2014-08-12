from SimpleCV import Image
import time 

print "Loading img \n..."
time.sleep(3)
img = Image("image-0.jpg")
print "Image loaded"
time.sleep(2)
print "Converting to png"
time.sleep(2)
print "..."
time.sleep(2)

img.save("Converted-1.png")
print "Done successfully"
# img.save() saves the file to the disk
# passing in arguments in the parrenthesis
# confirms/chnages the file type like .jp .png .gif etc etc.
