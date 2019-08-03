from Image import *
import math 


class OpticalModel:
    
    def __init__(self, width, height, holeSize, xc, yc, starDiameter, tiltOffset, tiltAngle, totalFlux):
        self.width, self.height, self.starDiameter = width, height, starDiameter
        self.holeSize, self.xc, self.yc = holeSize, xc, yc
        self.tiltOffset, self.tiltAngle, self.totalFlux = tiltOffset, tiltAngle, totalFlux
        
        
    def getDonut(self):
        
        image = Image(self.height, self.width, 0.0)                                     #Creates an image object
        image.generateCircle(self.xc,self.yc,self.starDiameter,100.0)                   #Generates outer star-circle

#################Calculations##############
        xoffset = self.tiltOffset * math.sin(self.tiltAngle)                            #Calculates x-direction change based on tilt offset and angle
        yoffset = self.tiltOffset * math.cos(self.tiltAngle)                            #Calculates y-direction change based on tilt offseta and angle

###########Applying calculations###########
        image.generateCircle(self.xc+xoffset, self.yc+yoffset, 5, 0.0)                  #Generates inner star-circle
        
        image.saveImage('OpticalModelTest.fits')
        
####################Test code###############
opti = OpticalModel(90, 90, 10, 50.0, 50.0, 10, 2.7, math.pi, 10)                       #An OpticalModel object with the "typical" values outlined in 
opti.getDonut()                                                                         #ProjectPackageA2, as well as a tilt angle of pi (-y direction)
