from SimpleCV import ImageSet

set = ImageSet(".") # Assumes the image set is in th same folder 
                    # as this script is saved 

for img in set:     # Loop Over all the images in the se(folder)
	oldname = img.filename # This line extracts the original file name of the image.
	newname = oldname[0:-3] + 'png' # This creates the new file name by first finding
	                                # the name of the original file without
                                    # the extension (oldname[0:-3]), and then appending the ".jpg"
                                    # extension

 	print "Converting " + oldname + " to " + newname 
	img.save(newname)