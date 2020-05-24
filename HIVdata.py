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


# First, open the data file
# Specify the directory where the file exists, and then use the
# simple Python 'open' method.
#
home_dir = "/Users/brash/Documents/python_stancil/PMLSdata/"
data_dir = home_dir + "01HIVSeries/"
data_file = data_dir + "HIVseries.csv"

print(data_file)

my_file = open(data_file)

# create arrays to hold the data (x,y)
# Then, read the data from the file one line at a time
xdata = []
ydata = []
for line in my_file:
    #print (line)
    x,y = line.split(",")
    xdata += [(float(x))]
    ydata += [(float(y))]
    
# Close the file now that we are done reading
my_file.close()

# Convert the Python lists for data to numpy arrays.
xdata = np.array(xdata)
ydata = np.array(ydata)

# Define a quadratic fitting function
def quadfunction(x,a,b,c):
    return a*x*x + b*x + c

# Define an exponential fitting function
def expfunction(x,c,d):
    return c*np.exp(-d*x)

# Plot the raw data as a scatter plot.  Lavel the axes, 
# give the graph a tiles, and plot the legend.
plt.xlabel('Time since adminstration of drug (days)')
plt.ylabel('Viral Concentration (mg/dL)')
plt.title("HIV Series")
plt.scatter(xdata,ydata,label='Experimental Data')
plt.legend()


# Use the scipy curve_fit utility to fit the data, first with the
# quadratic fitting function, and then with the exponential function.
#
# popt - contains the values of the parameters of the fit (best values)
# pcov - contains the covariance matrix, which can be used to calculate
#        uncertainties in each of the fit parameters
# perr - contains the uncertainties in each of the fit parameters
#
popt,pcov = curve_fit(quadfunction,xdata,ydata)
popt2,pcov2 = curve_fit(expfunction,xdata,ydata)

perr = np.sqrt(np.diag(pcov))
print ("Fit1: ",popt,perr)
perr2 = np.sqrt(np.diag(pcov2))
print ("Fit2: ",popt2,perr2)


# Set the maximum value of the x-axis to plot, which of the two fit
# functions to plot (1 = quad, 2 = exp, 3 = both), and whether to plot
# the +/- one standard deviation of the fit.
#
xmax = 7.5
ichoice = 0
errors = False
xfit = np.arange(0.0,xmax,0.1)

# Plot the fit(s), based upon the choices made above
#
if (ichoice == 1 or ichoice==3):
    plt.plot(xfit,quadfunction(xfit,*popt),'r-',
         label='quad fit: a=%5.3f +/- %5.3f,\n b=%5.3f +/- %5.3f,\n c=%5.3f +/- %5.3f' % 
         (popt[0],perr[0],popt[1],perr[1],popt[2],perr[2]))

    xii = np.linspace(0.0,xmax,100)
    psi = np.random.multivariate_normal(popt,pcov,10000)
    ysamplei=np.asarray([quadfunction(xii,*pi) for pi in psi])
    loweri = np.percentile(ysamplei,16.0,axis=0)
    upperi = np.percentile(ysamplei,84.0,axis=0)
    if (errors):
        plt.plot(xii,loweri,'r--')
        plt.plot(xii,upperi,'r--')

if (ichoice == 2 or ichoice == 3):
    plt.plot(xfit,expfunction(xfit,*popt2),'g-',
             label='exp fit: a=%5.3f +/- %5.3f,\n b=%5.3f +/- %5.3f' % 
             (popt2[0],perr2[0],popt2[1],perr2[1]))
    
    xi = np.linspace(0.0,xmax,100)
    ps = np.random.multivariate_normal(popt2,pcov2,10000)
    ysample=np.asarray([expfunction(xi,*pi) for pi in ps])
    lower = np.percentile(ysample,16.0,axis=0)
    upper = np.percentile(ysample,84.0,axis=0)
    if (errors):
        plt.plot(xi,lower,'g--')
        plt.plot(xi,upper,'g--')

plt.legend()

