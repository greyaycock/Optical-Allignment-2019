import pyfits
import numpy as np
import time

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
        
    def drawCircle(self, centerX, centerY, x, y):
        self.writePixel(centerX + x, centerY + y, 50.0)
        self.writePixel(centerX - x, centerY + y, 50.0)
        self.writePixel(centerX + x, centerY - y, 50.0)
        self.writePixel(centerX - x, centerY - y, 50.0)
        self.writePixel(centerX + y, centerY + x, 50.0)
        self.writePixel(centerX - y, centerY + x, 50.0)
        self.writePixel(centerX + y, centerY - x, 50.0)
        self.writePixel(centerX - y, centerY - x, 50.0)
        
    def circleBres(self, xc, yc, r):
        x = 0
        y = r
        d = 3 - (2*r)
        self.drawCircle(xc, yc, x, y)
        while(y>=x):
            x+=1
            
            if(d>0):
                y-=1
                d = d+4*(x-y)+10
            else:
                d = d + 4 * x + 6
            self.drawCircle(xc, yc, x, y)
            time.sleep(.06)
        
    def saveImage(self, imageName):
        hdu = pyfits.PrimaryHDU(self.n)                                     #PrimaryHDU object to encapsulate the data
        self.hdulist = pyfits.HDUList([hdu])                                #Creating an HDUList to contain the newly created primary HDU
        self.hdulist.writeto(imageName)                                     #Saves file as imageName parameter (MUST INCLUDE '.fits' extension!)



###Just the code I've been using to test as I go###
obj = Image(50, 50, 51.0)
obj.circleBres(35, 35, 10)
obj.saveImage('circleTest.fits')
