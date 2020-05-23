#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 09:26:54 2020

@author: brash
"""

import numpy as np

try:
    radius = float(input("Enter the radius of the circle: "))

    circumference = 2.0*np.pi*radius
    area = np.pi*radius**2

    print("For a circle of radius %.2f, the circumference is %.2f and the area is %.2f" % (radius,area,circumference))
    
except ValueError:
    print("The input data must be an integer or a float!!!")
    
    
from PyQt5.QtWidgets import *

app = QApplication([])
label = QLabel("Hello World!")
label.show()
app.exec_()
