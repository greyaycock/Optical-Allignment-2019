import pyfits
import numpy as np

class Image:
    height, width = 0, 0
    
    def __init__(self, heightInput, widthInput, pixelValue):
        self.height = heightInput
        self.width = widthInput
        self.pixelValue = pixelValue
        
        n = np.full((self.width, self.height), self.pixelValue)        #Creates a numpy object and creates the specified array
        hdu = pyfits.PrimaryHDU(n)                      #PrimaryHDU object to encapsulate the data
        self.hdulist = pyfits.HDUList([hdu])                 #Creating an HDUList to contain the newly created primary HDU
    
    def readPixel(self):
        print('')
    def writePixel(self):
        print('')
        
    def saveImage(self, imageName):
        self.hdulist.writeto(imageName)                      #Should save file (and did in previous versions),
                                                        #yet is now not due to the saveImage method not having access to 'hdulist'



###Just the code I've been using to test as I go###
obj = Image(50, 50, 100.0)
obj.saveImage('test.fits')
print(obj.height, obj.width)

        
    

