#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 18:58:27 2020

@author: brash
"""


import numpy as np

x = np.array([[1,2,3],[4,5,6],[7,8,9]])

print (x)

# print (x[row][column])
print(x[2][2])

y = np.zeros(shape=(3,4))

print (y)

for row in range(0,3):
    for column in range(0,4):
        y[row][column] = row*column*column
        
#read data from file and stuff into y
        
print (y)
