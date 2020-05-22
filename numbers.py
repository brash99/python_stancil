#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 16:56:36 2020

@author: brash
"""

def addnum(x,y):
    z = x + y
    return z

a = [1.2,2.4,1.5,3.1,4.9]
b = [2.2,1.8,-1.4,6.5,-2]
c = []

for i in range(5):
    c.append(addnum(a[i],b[i]))
    
print (c)


 



