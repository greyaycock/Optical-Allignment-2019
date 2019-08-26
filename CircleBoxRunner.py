from CircleBox import *

testObj = CircleArea()

print('--tiny box inside circle--')
try:
    result = testObj.area_in_circle(2.0, 2.0, 2.0, 2.01, 1.99, 2.01, 1.99)
    print('Overlap area should be: 0.000400')
    print('Overlap area is:' , result , '\r\n')
except:
    print('Error' , '\r\n')
    
################################################################################    
print('--box with 1/4 circle--')
try:
    result = testObj.area_in_circle(2.0, 2.0, 2.0, 1000.0, -1000.0, -1000.0, 1000.0)
    print('Overlap area should be: 12.566371')
    print('Overlap area is:' , result , '\r\n')
except:
    print('Error' , '\r\n')
    
################################################################################    
print('--huge box contains circle--')
try:
    result = testObj.area_in_circle(2.0, 2.0, 2.0, 2.0, -50.0, -50.0, 2.0)
    print('Overlap area should be: 3.141593')
    print('Overlap area is:' , result , '\r\n')
except:
    print('Error' , '\r\n')
    
################################################################################    
print('--box splits circle--')
try:
    result = testObj.area_in_circle(2.0, 2.0, 2.0, 4.1, 0.0, -1.0, 2.0)
    print('Overlap area should be: 6.283185')
    print('Overlap area is:' , result , '\r\n')
except:
    print('Error' , '\r\n')
    
################################################################################    
print('--again, bigger box--')
try:
    result = testObj.area_in_circle(2.0, 2.0, 2.0, 4.1, -0.1, -1.0, 2.0)
    print('Overlap area should be: 6.283185')
    print('Overlap area is:' , result , '\r\n')
except:
    print('Error' , '\r\n')
    
################################################################################    
print('--1/2 box in circle--')
try:
    result = testObj.area_in_circle(2.0, 2.0, 2.0, 2.001, 0.0, -2.0, 2.0)
    print('Overlap area should be: 0.00400')
    print('Overlap area is:' , result , '\r\n')
except:
    print('Error' , '\r\n')
    
################################################################################    
print('--all but a sliver of circle--')
try:
    result = testObj.area_in_circle(2.0, 2.0, 2.0, -3.999, 0.0, -1.0, 5.0)
    print('Overlap area should be: 12.566286')
    print('Overlap area is:' , result , '\r\n')
except:
    print('Error' , '\r\n')
    
################################################################################    
print('--close to 1/4 circle--')
try:
    result = testObj.area_in_circle(2.0, 2.0, 2.0, 1.99, 0.001, -0.001, 1.99)
    print('Overlap area should be: 3.101628')
    print('Overlap area is:' , result , '\r\n')
except:
    print('Error' , '\r\n')
    

    


