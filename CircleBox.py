import math
import numpy as np


class CircleArea:

    def point_in_circle(self, circle_x, circle_y, circle_radius, x, y):
        delta_x = (x - circle_x)
        delta_y = (y - circle_y)
        return (delta_x * delta_x + delta_y * delta_y) <= circle_radius*circle_radius
        
    def point_in_box(self, left, right, top, bottom, x, y):
        x_ok = (x >= left and x <= right)
        y_ok = (y >= bottom and y <= top)
        return (x_ok and y_ok)
        
    def point_in_square(self, box_top, box_bottom,  box_left,  box_right, x, y):
        return (x >= box_left and x <= box_right and y >= box_bottom and y <= box_top)
    
    def find_point_vert(self, circle_x, circle_y, circle_radius, x_in, y_out1,  y_out2):                                #Work in progress, need to figure out 
        delta_x = (x_in - circle_x)                                                                                     #how to pass by reference in Python
        y_sq = math.sqrt(circle_radius*circle_radius - delta_x*delta_x)
        y_out1 = y_sq + circle_y                                                                                        
        y_out2 = circle_y - y_sq
    
    def find_point_horiz(self, circle_x, circle_y, circle_radius, y_in, x_out1, x_out2):
        delta_y = (y_in - circle_y)
        x_sq = math.sqrt(circle_radius*circle_radius - delta_y*delta_y)
        self.x_out1 = x_sq + circle_x
        self.x_out2 = circle_x - x_sq

    def chord_area(self, chord, radius):
        theta = 2.0 * math.asin(chord/(2*radius))
        area = radius*radius*0.5*(theta - math.sin(theta))
        return area
        
    '''def circle_intersects_vertical(self, circle_x, circle_y, circle_radius, x, y_low, y_high):
        intersect1, intersect2 = 0, 0
        self.find_point_vert(circle_x, circle_y, circle_radius, x, intersect1, intersect2)
        if (not math.isnan(intersect1)):                                                                             #Work in progress, trying to figure out
            if (intersect1 >= y_low and intersect1 <= y_high):                                                       #the syntax of isnan in Python
                return True

        if (not math.isnan(intersect2)):
            if (intersect2 >= y_low and intersect2 <= y_high):
                return True
                
        return False'''
        
        #############Insert circle_intersects_horizontal###################
        
    def do_case_1(self, box_area, circle_radius, x_coord, y_coord, x_intercept, y_intercept, invert):    #invert is a bool
        del_x = x_coord - x_intercept
        del_y = y_coord - y_intercept
        height = abs(del_x)
        width  = abs(del_y)
        triangle = (height * width)/2.0
        chord = math.sqrt(del_x*del_x + del_y*del_y)

        area = self.chord_area(chord, circle_radius)
        #The "chord area" is subtracted if "invert" is true
        if (invert):
            return box_area - (triangle - area)
        else:
            return triangle + area
        '''NOTREACHED'''
        
    def do_clipped_corners(self, box_top, box_bottom, box_left, box_right, circle_radius, circle_x, circle_y, top_left_inside, top_right_inside, bottom_left_inside, bottom_right_inside):
        upper_left = 0.0                        #These four are the amount of 
        upper_right = 0.0                               #loss due to clipping of each of the
        lower_left = 0.0                                #four corners by the circle
        lower_right = 0.0

        if (not top_left_inside):
            intersect1, intersect2, dummy = 0, 0, 0
            self.find_point_horiz(circle_x, circle_y, circle_radius, box_top, dummy, intersect1)
            self.find_point_vert(circle_x, circle_y, circle_radius, box_left, intersect2, dummy)
            '''by setting the first argument (box_area) to 0.0, we set up
               do_case_1 to return a negative value, which is the area of
               the chunk cut off at the top_left corner.              '''
            upper_left = -self.do_case_1(0.0, circle_radius, box_left, box_top, intersect1, intersect2, True)
            #if (letter_debug):
                #fprintf(stderr, "z")

        if (not top_right_inside):
            intersect1, intersect2, dummy = 0, 0, 0      #Were originally just declared, could be wrong to set to 0
            self.find_point_horiz(circle_x, circle_y, circle_radius, box_top, intersect1, dummy)
            self.find_point_vert(circle_x, circle_y, circle_radius, box_right, intersect2, dummy)
            upper_right = -self.do_case_1(0.0, circle_radius, box_right, box_top, intersect1, intersect2, True)
            #if (letter_debug):
                #fprintf(stderr, "y")
                
        if (not bottom_left_inside):
            intersect1, intersect2, dummy = 0, 0, 0
            self.find_point_horiz(circle_x, circle_y, circle_radius,box_bottom, dummy, intersect1)
            self.find_point_vert(circle_x, circle_y, circle_radius,box_left, dummy, intersect2)
            lower_left = -self.do_case_1(0.0, circle_radius, box_left, box_bottom, intersect1, intersect2, True)
            #if (letter_debug):
                #fprintf(stderr, "x")

        if (not bottom_right_inside):
            intersect1, intersect2, dummy = 0, 0, 0
            self.find_point_horiz(circle_x, circle_y, circle_radius, box_bottom, intersect1, dummy)
            self.find_point_vert(circle_x, circle_y, circle_radius, box_right, dummy, intersect2)
            lower_right = -self.do_case_1(0.0, circle_radius, box_right, box_bottom, intersect1, intersect2, True)
            #if (letter_debug):
                #fprintf(stderr, "w")


        return (box_right - box_left)*(box_top - box_bottom) - (upper_left + upper_right + lower_left + lower_right)
        
    def do_case_9(self, radius, box_width, box_side1, box_side2):
        
    #three parts: one is a triangle, one a rectangle, and the other is a chord area
        rect_side = 0
        if box_side1 < box_side2:
            rect_side = box_side1
        else:
            rect_side = box_side2
        rect_area = rect_side * box_width
        triangle_side = abs(box_side1 - box_side2)
        triangle_area = (triangle_side * box_width)/2
        chord = math.sqrt(box_width * box_width + triangle_side * triangle_side)
        third_area = self.chord_area(chord, radius)
        return rect_area + triangle_area + third_area
        
    
    

        
        
        
        
       
############Test code######################       
g = CircleArea()
print(g.point_in_circle(1, 1, 1, -7, 1))
print(g.point_in_box(1, 1, 1, 1, 1, 1))         
print(g.point_in_square(1, 1, 1, 1, 1, 1))
#g.find_point_vert(1, 1, 1, 1, 1, 1)
#print(g.y_out1)
#g.find_point_horiz(1, 1, 1, 1, 1, 1)
#print(g.x_out1)
#print(g.chord_area(1, 1))
#print(g.circle_intersects_vertical(1, 1, 1, 1, 1, 1))
print(g.do_case_1(1, 1, 1, 1, 1, 1, True))
print(g.do_clipped_corners(1, 1, 1, 1, 1, 1, 1, False, False, True, True))
print(g.do_case_9(1,1,1,2))





    
    
    
    

