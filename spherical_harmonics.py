#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 25 12:12:22 2020

@author: brash
"""


import matplotlib.pyplot as plt
from matplotlib import cm, colors
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scipy.special import sph_harm

theta = np.linspace(0, np.pi, 100)
phi = np.linspace(0, 2*np.pi, 100)
theta, phi = np.meshgrid(theta, phi)

# The Cartesian coordinates of the unit sphere
x = np.sin(theta) * np.cos(phi)
y = np.sin(theta) * np.sin(phi)
z = np.cos(theta)

l = 3

nplots = 2*l + 2
nrows = int(np.sqrt(nplots))
ncolumns = int(nplots/nrows)
if (ncolumns*nrows<nplots):
    nrows=nrows+1
if (ncolumns-nrows>1):
    nrows=nrows+1
    ncolumns=ncolumns-1

print(nplots,nrows,ncolumns)

# Set the aspect ratio to 1 so our sphere looks spherical
fig = plt.figure(figsize=plt.figaspect(1.))

for m in range(-l,l+1):
    fcolors = sph_harm(m, l, phi, theta).real*sph_harm(m, l, phi, theta).real + sph_harm(m, l, phi, theta).imag*sph_harm(m, l, phi, theta).imag
    fmax, fmin = fcolors.max(), fcolors.min()
    fcolors = (fcolors - fmin)/(fmax - fmin)
    
    ax = plt.subplot(nrows,ncolumns,m+l+1,projection='3d')
    ax.plot_surface(x, y, z,  rstride=1, cstride=1, facecolors=cm.seismic(fcolors))
    
    if (m == -l):    
        fcolorsum = sph_harm(m, l, phi, theta).real*sph_harm(m, l, phi, theta).real + sph_harm(m, l, phi, theta).imag*sph_harm(m, l, phi, theta).imag
        print (m,fcolors)
    else:
        fcolorsum += sph_harm(m, l, theta, phi).real*sph_harm(m, l, theta, phi).real + sph_harm(m, l, theta, phi).imag*sph_harm(m, l, theta, phi).imag
        print (m,fcolors)
         
        
ax = plt.subplot(nrows,ncolumns,2*l+2,projection='3d')
ax.plot_surface(x, y, z,  rstride=1, cstride=1, facecolors=cm.seismic(fcolorsum))   

plt.show()