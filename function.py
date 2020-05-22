#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 16:56:36 2020

@author: brash
"""

def addnum(x,y):
    result = x + y
    return result


for i in range(10):
    a = 4*i
    b = 5*i
    c = addnum(a,b)

    if (c != 0):
        print ("%2d + %2d = %2d" % (a,b,c))
    
    