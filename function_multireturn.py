#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 25 23:57:33 2020

@author: brash
"""

def myalgebra(a,b):
    s = a+b
    d = a-b
    p = a*b
    q = a/b
    return s,d,p,q

# main program
    
x = 7
y = 6

sum,diff,product,quotient = myalgebra(x,y)

print (x,y,":   ",sum,diff,product,quotient)