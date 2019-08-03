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

    def generateCircle(self, xc, yc, r, value):
    # need to vary x and y coordinates over broad enough range to
    # catch all pixels that could be in the system
        for x in range(int(xc-r-2), int(xc+r+2)):
            if x < 0:
                continue            # don't fall off the edge
            for y in range(int(yc-r-2), int(yc+r+2)):
                if y < 0:
                    continue        # don't fall off the edge
            # if this pixel is within one radius of the center, then
            # set the pixel
                dx = x-xc
                dy = y-yc
                if r*r >= dx*dx + dy*dy:
                    self.writePixel(x, y, value)
                    
            
################File Manipulation##########################        
    def saveImage(self, imageName):
        hdu = pyfits.PrimaryHDU(self.n)                                    #PrimaryHDU object to encapsulate the data
        self.hdulist = pyfits.HDUList([hdu])                               #Creating an HDUList to contain the newly created primary HDU
        self.hdulist.writeto(imageName)                                    #Saves file as imageName parameter (MUST INCLUDE '.fits' extension!)
        
################Test Code##################################
