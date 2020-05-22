#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 19:43:32 2020

@author: brash
"""

import math

radius = float(input("Enter the radius of the circle: "))

circumference = 2*math.pi*radius
area = math.pi*radius**2

print("For a circle of radius",radius,
      ", the circumference is ",circumference,
      ", and the area is ",area,".")