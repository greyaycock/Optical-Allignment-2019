from Image import *
import math 
import numpy as np


class OpticalModel:
    
    def __init__(self, width, height, holeSize, xc, yc, starDiameter, tiltOffset, tiltAngle, totalFlux):
        self.width, self.height, self.starDiameter = width, height, starDiameter
        self.holeSize, self.xc, self.yc = holeSize, xc, yc
        self.tiltOffset, self.tiltAngle, self.totalFlux = tiltOffset, tiltAngle, totalFlux
        
        
    def getDonut(self):
        
        image = Image(self.height, self.width, 0.0)                                     #Creates an image object
        image.generateCircle(self.xc,self.yc,self.starDiameter/2,100.0)                 #Generates outer star-circle

#################Calculations##############
        xoffset = self.tiltOffset * math.sin(self.tiltAngle)                            #Calculates x-direction change based on tilt offset and angle
        yoffset = self.tiltOffset * math.cos(self.tiltAngle)                            #Calculates y-direction change based on tilt offseta and angle
        innerRadius = self.holeSize*(self.starDiameter/2)
        image.generateCircle(self.xc+xoffset, self.yc+yoffset, innerRadius, 0.0)        #Generates inner circle
        
#######Caclulating and applying flux#######     
        totalValue = 0                                                                  
        for x in range(0, self.width):                                                  #Cycles through every pixel and adds the values up
            for y in range(0, self.height):
                totalValue += image.readPixel(x, y)
                
        fluxRatio = self.totalFlux / totalValue                                         #Calculates the modifier that every element will be multiplied by
        
        for x in range(0, self.width):                                                  #Cycles through every element and applies flux change
            for y in range(0, self.height):
                if (image.readPixel(x, y) != 0.0) and (image.readPixel(x, y) >0.0):
                    newValue = image.readPixel(x, y) * fluxRatio
                    image.writePixel(y, x, newValue)
                
        
        image.saveImage('OpticalModelTest1.fits')
        
####################Test code###############
opti = OpticalModel(90, 90, 0.35, 50.0, 50.0, 20.0, 2.7, math.pi/2, 10000)                  #An OpticalModel object with the "typical" values outlined in 
opti.getDonut()                                                                         #ProjectPackageA2, as well as a tilt angle of pi (-y direction)
