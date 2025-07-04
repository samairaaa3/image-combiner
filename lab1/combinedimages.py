# MyColourModule.py
#
# Description: Contains functions related to pixels and their colour
#
# Date: 2024

# import necessary (PIL)
from PIL import Image
# import our own colour module
import myColourModule

# main part of our program

# create output image
imageOutput = Image.open("kid-green.jpg").copy()

# get width and height of image
width = imageOutput.width
height = imageOutput.height

# open file containing foreground object with green screen -> A
imageKidOpen = Image.open("kid-green.jpg")

# load its content
imageKidLoaded = imageKidOpen.load()

# open file containing background -> B
# and load its content
imageBeachOpen = Image.open("beach.jpg")
imageBeachLoaded = imageBeachOpen.load()

# go through each pixel of A
# first : for each row
for j in range(height):
  # second : for each cell in each row
  for i in range(width):
    r = imageKidLoaded[i, j][0]
    g = imageKidLoaded[i, j][1]
    b = imageKidLoaded[i, j][2]

    # if pixel is green
    if myColourModule.isPixelGreen(r, g, b):
      # replace it with B's value
      # get coordinates of this pixel
      xy = (i, j)
      # get the color tuple (r,g,b) of the corresponding pixel on B
      colour = imageBeachLoaded[i, j]
      # change the colour in output image
      # to the color tuple (r,g,b) of the pixel on B. NOTE : the putpixel() function 
      # takes two arguments. The first one is coordinates
      # of the pixel in the image you want to change, and the second is the colour to modify it to
      imageOutput.putpixel(xy, colour)

# Save the resulting image
imageOutput.save("combinedImages.png", "PNG")

# Close the image files
imageKidOpen.close()
imageBeachOpen.close()

