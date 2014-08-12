from SimpleCV import Display, Image, Color

winsize = (1300,750)
display = Display(winsize) 
img = Image(winsize) #No image default black background of size same as display
img.save(display) # Putting on display

while not display.isDone(): # Display will b on till you close it
	if display.mouseLeft: # When left mouse button is pressed
		
		# Draw circles
		# dl() means accessing drawing layer and all the drawing function like the "Circle()"
		img.dl().circle((display.mouseX, display.mouseY), 4,
			Color.GREEN, filled=True) 
		
		#update the window
		img.save(display)

		#Save as image as you close the window
		img.save("painting.png")
