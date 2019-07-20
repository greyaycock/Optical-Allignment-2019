import pyfits
import numpy as np
import time

class Image:
    
    def __init__(self, heightInput, widthInput, pixelValue):                         #Constructor
        self.height = heightInput
        self.width = widthInput
        self.pixelValue = pixelValue
        self.n = np.full((self.width, self.height), self.pixelValue)                 #Creates a numpy object and creates the specified array
        
    def openImage(self, imageInput):
        self.hdulist = pyfits.open(imageInput)                                       #Opens a FITS image as a pyfits object
        self.n = self.hdulist[0].data                                                #Reads the first (and only) HDU, which contains the pixel array
    
    def readPixel(self, pixelX, pixelY):                                             #Work in progress
        return self.n[pixelX, pixelY]
        
    def writePixel(self, pixelY, pixelX, newValue):
        self.n[pixelX, pixelY] = newValue                                            #SHOULD just change the pixel at [pixelX, pixelY] to newValue
        print("Pixel at (" , pixelX , "," , pixelY , ") changed to " , newValue , ".")
      
#######################Circle Drawing############################      
        
    def drawCircle(self, centerX, centerY, x, y):                                    #Method responsible for the actual pixel writing
        
        self.writePixel(centerX + x, centerY - y, 50.0)                              #These 6 writePixel() calls create 6/8 of the circle outline,
        self.writePixel(centerX - x, centerY - y, 50.0)                              #with each call being responsible for one octile of the circle.
        self.writePixel(centerX + y, centerY + x, 50.0)                              #The result is a "bowl" shape, leaving the top two octile
        self.writePixel(centerX - y, centerY + x, 50.0)                              #empty so that the loops following can go through and fill in the rest.
        self.writePixel(centerX + y, centerY - x, 50.0)
        self.writePixel(centerX - y, centerY - x, 50.0)
        
        for xx in range(centerX - x, centerX + x + 1):                               #This loop filles in the top and bottom quarters of the circle.
            self.writePixel(xx, centerY + y, 50.0)
            self.writePixel(xx, centerY - y, 50.0)
        for xx in range(centerX - y, centerX + y):                                   #This loop fills in the middle quarters of the circle.
            self.writePixel(xx, centerY + x, 50.0)
            self.writePixel(xx, centerY - x, 50.0)

    def generateCircle(self, xc, yc, r):                                   #Method based on Bresenham's circle-generation algorithm
        x = 0                                                              #Takes parameters for center (xc, yc) coordinate, as well as the radius (r)
        y = r
        d = 3 - (2*r)
        self.drawCircle(xc, yc, x, y)
        while(y>=x):
            x+=1
            if(d>0):                                                       #Updates d and y values
                y-=1
                d = d+4*(x-y)+10
            else:
                d = d + 4 * x + 6
            self.drawCircle(xc, yc, x, y)
            time.sleep(.06)                                                #Delay helps program run smoother
            
################File Manipulation##########################        
    def saveImage(self, imageName):
        hdu = pyfits.PrimaryHDU(self.n)                                    #PrimaryHDU object to encapsulate the data
        self.hdulist = pyfits.HDUList([hdu])                               #Creating an HDUList to contain the newly created primary HDU
        self.hdulist.writeto(imageName)                                    #Saves file as imageName parameter (MUST INCLUDE '.fits' extension!)
        
################Test Code##################################
obj = Image(50, 50, 51.0)
obj.generateCircle(35, 35, 10)
obj.saveImage('circleTest13.fits')
