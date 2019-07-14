import pyfits
import numpy as np

class Image:
    height, width = 0, 0
    
    def __init__(self, heightInput, widthInput, pixelValue):
        height = heightInput
        width = widthInput
        
        n = np.full((width, height), pixelValue)        #Creates a numpy object and creates the specified array
        hdu = pyfits.PrimaryHDU(n)                      #PrimaryHDU object to encapsulate the data
        hdulist = pyfits.HDUList([hdu])                 #Creating an HDUList to contain the newly created primary HDU
    
    def readPixel(self):
        print('')
    def writePixel(self):
        print('')
        
    def saveImage(self, imageName):
        hdulist.writeto(imageName)                      #Should save file (and was in previous versions),
                                                        #yet is now not due to the saveImage method not having access to 'hdulist'



###Just the code I've been using to test as I go###
obj = Image(50, 50, 100.0)
print(obj.height, obj.width)

        
    

