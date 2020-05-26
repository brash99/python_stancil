#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 19:43:32 2020

@author: brash
"""

import math

try:
    
    radius = float(input("Enter the radius of the circle: "))

    circumference = 2*math.pi*radius
    area = math.pi*radius**2

    print("For a circle of radius %.2f, the circumference is %.3f, and the area is %.4f." % (radius,circumference,area))
    
except (ValueError):
    
    print("Hey ... the radius must be a number!!")



    