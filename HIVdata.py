#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author:    Edward Brash
Created:   Mon Jun 24 09:02:22 2019
Modified:  Mon Jun 24 09:02:22 2019

Description:
------------
"""

import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

home_dir = "/Users/brash/Documents/python_stancil/PMLSdata/"
data_dir = home_dir + "01HIVSeries/"
data_file = data_dir + "HIVseries.csv"

print(data_file)

my_file = open(data_file)

xdata = []
ydata = []
for line in my_file:
    #print (line)
    x,y = line.split(",")
    xdata += [(float(x))]
    ydata += [(float(y))]
    
my_file.close()

xdata = np.array(xdata)
ydata = np.array(ydata)

def fitfunction(x,a,b,c):
    return a*x*x + b*x + c

plt.xlabel('Time since adminstration of drug (days)')
plt.ylabel('Viral Concentration (mg/dL)')
plt.title("HIV Series")
plt.scatter(xdata,ydata,label='Experimental Data')
plt.legend()


popt,pcov = curve_fit(fitfunction,xdata,ydata)

perr = np.sqrt(np.diag(pcov))
print (popt,perr)

plt.plot(xdata,fitfunction(xdata,*popt),'r-',
         label='fit: a=%5.3f +/- %5.3f,\n     b=%5.3f +/- %5.3f,\n     c=%5.3f +/- %5.3f' % 
         (popt[0],perr[0],popt[1],perr[1],popt[2],perr[2]))

plt.legend()

