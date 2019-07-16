import pyfits
import numpy as np

class Image:
    
    def __init__(self, heightInput, widthInput, pixelValue):
        self.height = heightInput
        self.width = widthInput
        self.pixelValue = pixelValue
        self.n = np.full((self.width, self.height), self.pixelValue)                 #Creates a numpy object and creates the specified array
        
    def __init__(self, imageInput):
        self.hdulist = pyfits.open(imageInput)                                       #Opens a FITS image as a pyfits object
        self.n = self.hdulist[0].data                                                #Reads the first (and only) HDU, which contains the pixel array
    
    def readPixel(self, pixelX, pixelY):                                             #Work in progress
        print(self.n[pixelX, pixelY])
        
    def writePixel(self, pixelX, pixelY, newValue):
        self.n[pixelX, pixelY] = newValue                                            #SHOULD just change the pixel at [pixelX, pixelY] to newValue
        print("Pixel at (" , pixelX , "," , pixelY , ") changed to " , newValue , ".")
        
        
    def saveImage(self, imageName):
        hdu = pyfits.PrimaryHDU(self.n)                                     #PrimaryHDU object to encapsulate the data
        self.hdulist = pyfits.HDUList([hdu])                                #Creating an HDUList to contain the newly created primary HDU
        self.hdulist.writeto(imageName)                                     #Saves file as imageName parameter (MUST INCLUDE '.fits' extension!)



###Just the code I've been using to test as I go###
#obj = Image(50, 50, 100.0)
obj = Image('image016.fits')
obj.readPixel(3, 3)
obj.writePixel(35, 35, 50.0)
obj.saveImage('test19.fits')
#print(obj.height, obj.width)

        
    

