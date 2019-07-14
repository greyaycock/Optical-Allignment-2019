import pyfits
import numpy as np

class Image:
    height, width = 0, 0
    
    def __init__(self, heightInput, widthInput, pixelValue):
        self.height = heightInput
        self.width = widthInput
        self.pixelValue = pixelValue
        
        n = np.full((self.width, self.height), self.pixelValue)         #Creates a numpy object and creates the specified array
        hdu = pyfits.PrimaryHDU(n)                                      #PrimaryHDU object to encapsulate the data
        self.hdulist = pyfits.HDUList([hdu])                            #Creating an HDUList to contain the newly created primary HDU
    
    def readPixel(self):                                                #Work in progress
        print('')
    def writePixel(self):
        print('')
        
    def saveImage(self, imageName):
        self.hdulist.writeto(imageName)                                 #Saves file as imageName parameter (MUST INCLUDE '.fits' extension!)
                                                        



###Just the code I've been using to test as I go###
obj = Image(50, 50, 100.0)
obj.saveImage('test.fits')
print(obj.height, obj.width)

        
    

