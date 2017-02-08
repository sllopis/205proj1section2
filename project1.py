#Sergio Llopis Donate
#Project 1
#02/07/2017
#CST 205

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

#Opening the images
for i in range(1,10):
    Image.open("images/" + str(i) + ".png")
    
    
# Size of the Images (Width and Height)
pictureWidth = 495
pictureHeight = 557

#Array for adding images to the List
imgList = []
for i in range(1,10):
    imgList.append(Image.open("images/" + str(i) + ".png"))
    
    
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
    
        

#median
#clear
#output

#newimg.putpixel((x,y), (myred, mygreen, myblue)) 

#canvas.putpixel()

# newimage.save()

#Calling for the function
#print medianoper(greenpx)





#medianoper((redpx,greenpx,bluepx))
































# canvas.putpixel

# canvas.save()

# range(im1,im2,im3,im4,im5,im6,im7,im8,im9)

# for x in range(9):
#     print (range)

# for x in xrange(495):
#     for y in xrange (557):
#         px = im1.getpixel()
    
#px = []

#px = im.load()
#print (px[4,4])

#print (im.format)

#class PIL.ImageFilter.MedianFilter(size=3)

#pix_val is the list that contains all
#the pixel values which can be printed to see those values

#im = array(Image.open('empire.jpg'))
#print im.shape, im.dtype


#im.new(RGB, (495, 557), color=0)

#px = im.load()

#array
#loop to check
#calculate the median
#info put back into the new image
#for x range (10):
    

# images = Image.open('images/1.png',
#           'images/2.png',
#           'images/3.png',
#           'images/4.png',
#           'images/5.png',
#           'images/6.png',
#           'images/7.png',
#           'images/8.png',
#           'images/9.png',)







