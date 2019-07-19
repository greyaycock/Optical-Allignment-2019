import pyfits
import numpy as np
import time
import math

class Image:
    
    def __init__(self, heightInput, widthInput, pixelValue):
        self.height = heightInput
        self.width = widthInput
        self.pixelValue = pixelValue
        self.n = np.full((self.width, self.height), self.pixelValue)                 #Creates a numpy object and creates the specified array
        
    def openImage(self, imageInput):
        self.hdulist = pyfits.open(imageInput)                                       #Opens a FITS image as a pyfits object
        self.n = self.hdulist[0].data                                                #Reads the first (and only) HDU, which contains the pixel array
    
    def readPixel(self, pixelX, pixelY):                                             #Work in progress
        print(self.n[pixelX, pixelY])
        
    def writePixel(self, pixelY, pixelX, newValue):
        self.n[pixelX, pixelY] = newValue                                            #SHOULD just change the pixel at [pixelX, pixelY] to newValue
        print("Pixel at (" , pixelX , "," , pixelY , ") changed to " , newValue , ".")
        
    def drawCircle(self, centerX, centerY, radius):
        sin45 = 0.70710678118                                               #Only trig needed, so I just created a variable with the needed value
        distance = radius/(2*sin45)
        for i in range(int(radius),int(distance),-1):
            j = math.sqrt(radius*radius - i*i)
            for k in range(int(-j), int(j), 1):
                self.writePixel(centerX - k, centerY + i, 50)
                self.writePixel(centerX - k, centerY - i, 50)
                self.writePixel(centerX + i, centerY + i, 50)
                self.writePixel(centerX - i, centerY - i, 50)

        
    def saveImage(self, imageName):
        hdu = pyfits.PrimaryHDU(self.n)                                     #PrimaryHDU object to encapsulate the data
        self.hdulist = pyfits.HDUList([hdu])                                #Creating an HDUList to contain the newly created primary HDU
        self.hdulist.writeto(imageName)                                     #Saves file as imageName parameter (MUST INCLUDE '.fits' extension!)



###Just the code I've been using to test as I go###
obj = Image(50, 50, 51.0)
obj.drawCircle(35.0, 35.0, 3)
obj.saveImage('circleTest.fits')

