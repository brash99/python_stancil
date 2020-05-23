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

def quadfunction(x,a,b,c):
    return a*x*x + b*x + c

def expfunction(x,c,d):
    return c*np.exp(-d*x)

plt.xlabel('Time since adminstration of drug (days)')
plt.ylabel('Viral Concentration (mg/dL)')
plt.title("HIV Series")
plt.scatter(xdata,ydata,label='Experimental Data')
plt.legend()


popt,pcov = curve_fit(quadfunction,xdata,ydata)

popt2,pcov2 = curve_fit(expfunction,xdata,ydata)

perr = np.sqrt(np.diag(pcov))
print ("Fit1: ",popt,perr)
perr2 = np.sqrt(np.diag(pcov2))
print ("Fit2: ",popt2,perr2)

xmax = 12.5
xfit = np.arange(0.0,xmax,0.1)

plt.plot(xfit,quadfunction(xfit,*popt),'r-',
         label='quad fit: a=%5.3f +/- %5.3f,\n b=%5.3f +/- %5.3f,\n c=%5.3f +/- %5.3f' % 
         (popt[0],perr[0],popt[1],perr[1],popt[2],perr[2]))

xii = np.linspace(0.0,xmax,100)
psi = np.random.multivariate_normal(popt,pcov,10000)
ysamplei=np.asarray([quadfunction(xii,*pi) for pi in psi])
loweri = np.percentile(ysamplei,16.0,axis=0)
upperi = np.percentile(ysamplei,84.0,axis=0)
plt.plot(xii,loweri,'r--')
plt.plot(xii,upperi,'r--')

#plt.plot(xfit,expfunction(xfit,*popt2),'g-',
#         label='exp fit: a=%5.3f +/- %5.3f,\n b=%5.3f +/- %5.3f' % 
#         (popt2[0],perr2[0],popt2[1],perr2[1]))
#
#xi = np.linspace(0.0,xmax,100)
#ps = np.random.multivariate_normal(popt2,pcov2,10000)
#ysample=np.asarray([expfunction(xi,*pi) for pi in ps])
#lower = np.percentile(ysample,16.0,axis=0)
#upper = np.percentile(ysample,84.0,axis=0)
#plt.plot(xi,lower,'g--')
#plt.plot(xi,upper,'g--')




plt.legend()

