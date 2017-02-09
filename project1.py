#Sergio Llopis Donate
#Project 1
#02/07/2017
#CST 205

#github link: https://github.com/sllopis

from PIL import Image

#GETTING THE MEDIAN + SORTING FUNCTION

def medianoper(myList):
    
    # Store list length in the variable listLength
    listLength = len(myList)
    # Sort the list
    sortedValues = sorted(myList)
    # Location of middle value. Subtract one because of zero index
    middleIndex = (listLength + 1)/2 - 1
    # Return the object located at that index
    return sortedValues[middleIndex]

#Array for adding images to the List + Opening the images
imgList = []
for i in range(1,10):
    imgList.append(Image.open("images/" + str(i) + ".png"))

pictureWidth, pictureHeight = imgList[0].size
    
#Creating new image blue color
newimg = Image.new("RGB", ((pictureWidth,pictureHeight)), color=None)

#Creating a list for the colors (9 colors)
redpx = []
greenpx = []
bluepx= []

for x in range(0, pictureWidth - 1):
    for y in range(0, pictureHeight - 1):
        for myImage in imgList:
            
            myred, mygreen, myblue = myImage.getpixel((x,y))
            
            redpx.append(myred)
            greenpx.append(mygreen)
            bluepx.append(myblue)
            
        myred = medianoper(redpx)
        mygreen = medianoper(greenpx)
        myblue = medianoper(bluepx)

        newimg.putpixel(((x,y)), ((myred, mygreen, myblue)))
        
        redpx = []
        greenpx = []
        bluepx = []
    
newimg.save("canvas.png")
    
  