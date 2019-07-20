import pyfits
import numpy as np

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
        
    def drawCircle(self, centerX, centerY):
        self.writePixel(centerX, centerY, 50.0)
        self.writePixel(centerX + 10, centerY, 50.0)
        self.writePixel(centerX + 10, centerY+1, 50.0)                                    #Method to draw a circle with a radius 10 on the image
        self.writePixel(centerX + 9, centerY+2, 50.0)
        self.writePixel(centerX + 9, centerY+3, 50.0)
        self.writePixel(centerX + 8, centerY+4, 50.0)
        self.writePixel(centerX + 8, centerY+5, 50.0)
        self.writePixel(centerX + 7, centerY+6, 50.0)
        self.writePixel(centerX + 6, centerY+7, 50.0)
        self.writePixel(centerX + 5, centerY+7, 50.0)
        self.writePixel(centerX + 4, centerY+8, 50.0)
        self.writePixel(centerX + 3, centerY+8, 50.0)       
        self.writePixel(centerX + 2, centerY+9, 50.0)
        self.writePixel(centerX + 1, centerY+9, 50.0)
        self.writePixel(centerX + 0, centerY+9, 50.0)
        self.writePixel(centerX + -1, centerY+9, 50.0)
        self.writePixel(centerX + -2, centerY+8, 50.0)
        self.writePixel(centerX + -3, centerY+8, 50.0)
        self.writePixel(centerX + -4, centerY+7, 50.0)
        self.writePixel(centerX + -5, centerY+7, 50.0)
        self.writePixel(centerX + -6, centerY+6, 50.0)
        self.writePixel(centerX + -7, centerY+5, 50.0)
        self.writePixel(centerX + -7, centerY+4, 50.0)
        self.writePixel(centerX + -8, centerY+3, 50.0)
        self.writePixel(centerX + -8, centerY+2, 50.0)
        self.writePixel(centerX + -9, centerY+1, 50.0)
        self.writePixel(centerX + -9, centerY, 50.0)
        self.writePixel(centerX + -9, centerY-1, 50.0)
        self.writePixel(centerX + -9, centerY-2, 50.0)
        self.writePixel(centerX + -8, centerY-3, 50.0)
        self.writePixel(centerX + -8, centerY-4, 50.0)
        self.writePixel(centerX + -7, centerY-5, 50.0)
        self.writePixel(centerX + -7, centerY-6, 50.0)
        self.writePixel(centerX + -6, centerY-7, 50.0)
        self.writePixel(centerX + -5, centerY-8, 50.0)
        self.writePixel(centerX + -4, centerY-8, 50.0)
        self.writePixel(centerX + -3, centerY-9, 50.0)
        self.writePixel(centerX + -2, centerY-9, 50.0)
        self.writePixel(centerX + -1, centerY-10, 50.0)
        self.writePixel(centerX + 0, centerY-10, 50.0)
        self.writePixel(centerX + 1, centerY-10, 50.0)
        self.writePixel(centerX + 2, centerY-10, 50.0)
        self.writePixel(centerX + 3, centerY-9, 50.0)
        self.writePixel(centerX + 4, centerY-9, 50.0)
        self.writePixel(centerX + 5, centerY-8, 50.0)
        self.writePixel(centerX + 6, centerY-8, 50.0)
        self.writePixel(centerX + 7, centerY-7, 50.0)
        self.writePixel(centerX + 8, centerY-6, 50.0)
        self.writePixel(centerX + 8, centerY-5, 50.0)
        self.writePixel(centerX + 9, centerY-4, 50.0)
        self.writePixel(centerX + 9, centerY-3, 50.0)
        self.writePixel(centerX + 10, centerY-2, 50.0)
        self.writePixel(centerX + 10, centerY-1, 50.0)
        
           
        
    def saveImage(self, imageName):
        hdu = pyfits.PrimaryHDU(self.n)                                     #PrimaryHDU object to encapsulate the data
        self.hdulist = pyfits.HDUList([hdu])                                #Creating an HDUList to contain the newly created primary HDU
        self.hdulist.writeto(imageName)                                     #Saves file as imageName parameter (MUST INCLUDE '.fits' extension!)



###Just the code I've been using to test as I go###
obj = Image(50, 50, 51.0)
obj.drawCircle(35, 35)
obj.saveImage('test43.fits')

