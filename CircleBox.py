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
    
    def find_point_vert(self, circle_x, circle_y, circle_radius, x_in):
        delta_x = (x_in - circle_x)   
        disc = circle_radius*circle_radius - delta_x*delta_x
        if (disc >= 0.0):
            y_sq = math.sqrt(disc)
            return (y_sq+circle_y, circle_y-y_sq)
        else:
            return (np.nan,np.nan)
    
    def find_point_horiz(self, circle_x, circle_y, circle_radius, y_in):
        delta_y = (y_in - circle_y)
        disc = circle_radius*circle_radius - delta_y*delta_y
        if (disc >= 0.0):
            x_sq = math.sqrt(disc)
            return (x_sq+circle_x, circle_x - x_sq)
        else:
            return (np.nan, np.nan)

    def circle_intersects_vertical(self, circle_x, circle_y, circle_radius, x, y_low, y_high):
        intersect1, intersect2 = self.find_point_vert(circle_x, circle_y, circle_radius, x)
        if (intersect1 != None):
            if (intersect1 >= y_low and intersect1 <= y_high):
                return True

        if (intersect2 != None):
            if (intersect2 >= y_low and intersect2 <= y_high):
                return True
                
        return False
    
    def chord_area(self, chord, radius):
        theta = 2.0 * math.asin(chord/(2*radius))
        area = radius*radius*0.5*(theta - math.sin(theta))
        return area
        
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
            dummy, intersect1 = self.find_point_horiz(circle_x, circle_y, circle_radius, box_top)
            intersect2, dummy = self.find_point_vert(circle_x, circle_y, circle_radius, box_left)
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
        
    def area_in_circle(self, circle_x, circle_y, circle_radius, box_top, box_bottom, box_left, box_right):
    # Check the circle extreme points, see if they're in the box
        top_is_in = self.point_in_box(box_left, box_right, box_top, box_bottom, circle_x, circle_y + circle_radius)
        bottom_is_in = self.point_in_box(box_left, box_right, box_top, box_bottom, circle_x, circle_y - circle_radius)
        left_is_in = self.point_in_box(box_left, box_right, box_top, box_bottom, circle_x - circle_radius, circle_y)
        right_is_in = self.point_in_box(box_left, box_right, box_top, box_bottom, circle_x + circle_radius, circle_y)
        center_is_in = self.point_in_box(box_left, box_right, box_top, box_bottom, circle_x, circle_y)
        #count number of box corners inside the circle
        top_left_inside = self.point_in_circle(circle_x, circle_y, circle_radius, box_left, box_top)
        top_right_inside = self.point_in_circle(circle_x, circle_y, circle_radius, box_right, box_top)
        bottom_left_inside = self.point_in_circle(circle_x, circle_y, circle_radius, box_left, box_bottom)
        bottom_right_inside = self.point_in_circle(circle_x, circle_y, circle_radius, box_right, box_bottom)
    
        num_inside = 0
        box_area = (box_top - box_bottom)*(box_right - box_left)
    
        if (top_left_inside):
            num_inside+=1
        if (top_right_inside):
            num_inside+=1
        if (bottom_left_inside):
            num_inside+=1
        if (bottom_right_inside):
            num_inside+=1

        num_circle_extremes_outside = np.nan
        if (not top_is_in):
            num_circle_extremes_outside+=1
        if (not bottom_is_in):
            num_circle_extremes_outside+=1
        if (not left_is_in):
            num_circle_extremes_outside+=1
        if (not right_is_in):
            num_circle_extremes_outside+=1

    #all corners inside the circle: easy
        if (num_inside == 4):
            return (box_top-box_bottom)*(box_right-box_left)

        do_inversion = False
        if (num_inside == 3):
    #turn this into a version of case 1
            do_inversion = True
            top_left_inside = not top_left_inside
            top_right_inside = not top_right_inside
            bottom_left_inside = not bottom_left_inside
            bottom_right_inside = not bottom_right_inside

    #case 12
        if (num_inside == 1 and num_circle_extremes_outside == 4 and mcenter_is_in):
            return self.do_clipped_corners(box_top, box_bottom, box_left, box_right, circle_radius, circle_x, circle_y, top_left_inside, top_right_inside, bottom_left_inside, bottom_right_inside)


    #one corner inside the circle
        if (num_inside == 1 or num_inside == 3): 
            top_intersect, bottom_intersect, left_intersect, right_intersect = 0.0, 0.0, 0.0, 0.0
    #always < 180-deg chord
            if (top_left_inside or top_right_inside):
                '''if(letter_debug): 
                    fprintf(stderr, "A")'''
                right_intersect, left_intersect = self.find_point_horiz(circle_x, circle_y, circle_radius,box_top)
            
            if (bottom_left_inside or bottom_right_inside): 
                '''if (letter_debug):
                    fprintf(stderr, "B")'''
                right_intersect, left_intersect = self.find_point_horiz(circle_x, circle_y, circle_radius, box_bottom)
    
            if (top_left_inside or bottom_left_inside): 
                '''if (letter_debug):
                    fprintf(stderr, "C")'''
                top_intersect, bottom_intersect = self.find_point_vert(circle_x, circle_y, circle_radius, box_left)
    
            if (top_right_inside or bottom_right_inside): 
                '''if (letter_debug):
                    fprintf(stderr, "D")'''
                top_intersect, bottom_intersect = self.find_point_vert(circle_x, circle_y, circle_radius, box_right)
    

            if (do_inversion):
                temp = np.nan
                temp = left_intersect
                left_intersect = right_intersect
                right_intersect = temp

                temp = bottom_intersect
                bottom_intersect = top_intersect
                top_intersect = temp


            if (top_left_inside): 
                '''if (letter_debug):
                    fprintf(stderr, "a");'''
                return self.do_case_1(box_area, circle_radius, box_left, box_top, right_intersect, bottom_intersect, do_inversion)
            elif (top_right_inside): 
                '''if (letter_debug):
                    fprintf(stderr, "b")'''
                return self.do_case_1(box_area, circle_radius, box_right, box_top, left_intersect, bottom_intersect, do_inversion)
            elif (bottom_left_inside): 
                '''if (letter_debug):
                    fprintf(stderr, "c")'''
                return self.do_case_1(box_area, circle_radius, box_left, box_bottom,right_intersect, top_intersect, do_inversion)
            elif (bottom_right_inside): 
                '''if (letter_debug):
                    fprintf(stderr, "d")'''
                return self.do_case_1(box_area, circle_radius, box_right, box_bottom, left_intersect, top_intersect, do_inversion)
            else: 
                '''fprintf(stderr, "three_part_model: impossible #1\n");'''
                return 0
        elif (num_inside == 2):                                   #else two corners inside the circle: opposite sides, still four cases
            '''if top/bottom sides intersect, top_bottom will be TRUE. If
            left/right sides intersect, top_bottom will be FALSE.'''
            top_bottom = ((top_left_inside and bottom_left_inside) or (top_right_inside and bottom_right_inside))
            '''if circle is to the right or to the top, high_side will be
            TRUE. If circle is to the left or to the bottom, high_side will
            be FALSE.'''
            high_side = ((top_right_inside and bottom_right_inside) or (top_left_inside and top_right_inside))
    
            intersect1, intersect2, intersect3, intersect4 = np.nan, np.nan, np.nan, np.nan
            box_full_width = np.nan

            if (top_bottom):
                intersect1, intersect2 = self.find_point_horiz(circle_x, circle_y, circle_radius, box_top)
                intersect3, intersect4 = self.find_point_horiz(circle_x, circle_y, circle_radius, box_bottom)
                box_full_width = box_top - box_bottom
            else:
                intersect1, intersect2 = self.find_point_vert(circle_x, circle_y, circle_radius, box_left)
                intersect3, intersect4 = self.find_point_vert(circle_x, circle_y, circle_radius, box_right)
                box_full_width = box_right - box_left
    

            if (top_bottom and high_side): 
                if (not self.circle_intersects_vertical(circle_x, circle_y, circle_radius, box_left, box_bottom, box_top)): 
                    '''if (letter_debug):
                        fprintf(stderr, "E");'''
                    return self.do_case_9(circle_radius, box_full_width, box_right - intersect2, box_right - intersect4)
      
            elif(top_bottom and not high_side): 
                if (not self.circle_intersects_vertical(circle_x, circle_y, circle_radius, box_right, box_bottom, box_top)): 
                    '''if (letter_debug):
                        fprintf(stderr, "F");'''
                    return self.do_case_9(circle_radius, box_full_width,intersect1 - box_left, intersect3 - box_left)
      
            elif((not top_bottom) and high_side):
                if (not self.circle_intersects_horizontal(circle_x, circle_y, circle_radius, box_bottom, box_left, box_right)): 
                    '''if (letter_debug):
                        fprintf(stderr, "G");'''
                    return self.do_case_9(circle_radius, box_full_width,box_top - intersect2, box_top - intersect4)
      
            elif ((not top_bottom) and (not high_side)): 
                if (not self.circle_intersects_horizontal(circle_x, circle_y, circle_radius, box_top, box_left, box_right)):
                    '''if (letter_debug):
                        fprintf(stderr, "H");'''
                    return self.do_case_9(circle_radius, box_full_width, intersect1 - box_bottom, intersect3 - box_bottom)
            '''getting here means we have the odd case where the entire box is
            inside the circle except for two adjacent corners (case 11)'''
            return self.do_clipped_corners(box_top, box_bottom, box_left, box_right, circle_radius, circle_x, circle_y, top_left_inside, top_right_inside, bottom_left_inside, bottom_right_inside)
       
        elif (num_inside == 0): 
            if (circle_y - circle_radius > box_top or circle_y + circle_radius < box_bottom or circle_x - circle_radius > box_right or circle_x + circle_radius < box_left):
                return 0.0
    
            '''if none of the sides of the circle are in the box and the
               center is not in the box, then nothing is in the box'''
            if (not (top_is_in or bottom_is_in or left_is_in or right_is_in or center_is_in)):
                return 0.0


            circle_area = math.pi * circle_radius * circle_radius
            #now subtract off any chords that fall outside the box
            intercept1, intercept2 = np.nan, np.nan                   #were just normal declarations 

            if (center_is_in):
                if (not top_is_in): 
                    intercept1, intercept2 = self.find_point_horiz(circle_x, circle_y, circle_radius, box_top)
                    assert(not math.isnan(intercept1))
                    chord = abs(intercept1 - intercept2)
                    '''if (letter_debug):
                        fprintf(stderr, "P")'''
                    circle_area -= self.chord_area(chord, circle_radius)
      
                if (not bottom_is_in): 
                    intercept1, intercept2 = self.find_point_horiz(circle_x, circle_y, circle_radius, box_bottom)
                    assert(not math.isnan(intercept1))
                    chord = abs(intercept1 - intercept2)
                    '''if (letter_debug):
                        fprintf(stderr, "Q");'''
                    circle_area -= self.chord_area(chord, circle_radius)
      
                if (not left_is_in): 
                    intercept1, intercept2 = self.find_point_vert(circle_x, circle_y, circle_radius, box_left)
                    assert(not math.isnan(intercept1))
                    chord = abs(intercept1 - intercept2)
                    '''if (letter_debug):
                        fprintf(stderr, "R");'''
                    circle_area -= self.chord_area(chord, circle_radius)
      
                if (not right_is_in): 
                    intercept1, intercept2 = self.find_point_vert(circle_x, circle_y, circle_radius, box_right)
                    '''if (math.isnan(intercept1)): {
                        fprintf(stderr, "circle_box: err:\n");
                        fprintf(stderr, "circle_x = %lf, circle_y = %lf\n", circle_x, circle_y);
                        fprintf(stderr, "circle_radius = %lf, box_right = %lf\n", circle_radius, box_right);'''
        
                    assert(not math.isnan(intercept1))
                    chord = abs(intercept1 - intercept2)
                    '''if (letter_debug):
                        fprintf(stderr, "S");'''
                    circle_area -= self.chord_area(chord, circle_radius)
      
                return circle_area
            else: 
            #center is not inside
                if(top_is_in): 
                    intercept1, intercept2 = self.find_point_horiz(circle_x, circle_y, circle_radius, box_bottom)
                    if (not (math.isnan(intercept1) or math.isnan(intercept2))): 
                        if (intercept1 >= box_left and intercept1 <= box_right and intercept2 >= box_left and intercept2 <= box_right): 
                            chord = abs(intercept1 - intercept2)
                            '''if (letter_debug):
                                fprintf(stderr, "I");'''
                        return self.chord_area(chord, circle_radius)
          
        
      
    
                if (bottom_is_in): 
                    intercept1, intercept2 = self.find_point_horiz(circle_x, circle_y, circle_radius, box_top)
                    if (not(math.isnan(intercept1) or math.isnan(intercept2))): 
                        if (intercept1 >= box_left and intercept1 <= box_right and intercept2 >= box_left and intercept2 <= box_right): 
                            chord = abs(intercept1 - intercept2)
                            '''if (letter_debug):
                                fprintf(stderr, "J");'''
                            return self.chord_area(chord, circle_radius)
          
        
      
    
                if (left_is_in): 
                    intercept1, intercept2 = self.find_point_vert(circle_x, circle_y, circle_radius, box_right)
                    if (not(math.isnan(intercept1) or isnan(intercept2))): 
                        if (intercept1 >= box_bottom and intercept1 <= box_top and intercept2 >= box_bottom and intercept2 <= box_top): 
                            chord = abs(intercept1 - intercept2)
                            '''if (letter_debug)
                            fprintf(stderr, "K");'''
                            return self.chord_area(chord, circle_radius)
          
        
      
    
                if (right_is_in): 
                    intercept1, intercept2 = self.find_point_vert(circle_x, circle_y, circle_radius, box_left)
                    if (not(math.isnan(intercept1) or math.isnan(intercept2))): 
                        if (intercept1 >= box_bottom and intercept1 <= box_top and intercept2 >= box_bottom and intercept2 <= box_top): 
                            chord = abs(intercept1 - intercept2)
                            '''if (letter_debug):
                                fprintf(stderr, "L")'''
                            return self.chord_area(chord, circle_radius)
          
        
      
                '''fprintf(stderr, "three_part_model: impossible #7\n");'''
    
        else: 
            #fprintf(stderr, "three_part_model: impossible #5\n");
            return 0
  
        ###NOTREACHED###
        #fprintf(stderr, "three_part_model: impossible #6\n");
        #return 0

        
       



    
    
    
    

