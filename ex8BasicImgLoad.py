from SimpleCV import Image, Display
import time

display = Display()

#builtInImg = Image("logo") 

#buildInImg.save(display)

#time.sleep(5)
#webImg = Image("http://simplecv.s3.amazonaws.com/simplecv_lg.png") 
localImg = Image("image-0.jpg") 
localImg.save(display)