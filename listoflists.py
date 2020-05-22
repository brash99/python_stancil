#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 16:57:46 2020

@author: brash
"""


Edward = ["Edward","Brash","800","West Princess Anne Road","Norfolk","VA","23517"]
Alice = ["Alice","Wonderland","123","Main Street","Beverly Hills","CA","90210"]
Freddy = ["Frederick","Kruger","111","Elm Street","Amityville","MA","66666"]

People = [Edward,Alice,Freddy]

print (People)

print (" ")

print ([People[i][0] for i in range(len(People))])


