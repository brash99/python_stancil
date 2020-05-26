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

l = 4

#for m in range(-l,l+1):
#    # Calculate the spherical harmonic Y(l,m) and normalize to [0,1]
#    # fcolors = sph_harm(m, l, theta, phi).real
#    if (m == -l):    
#        fcolors = sph_harm(m, l, phi, theta).real*sph_harm(m, l, phi, theta).real + sph_harm(m, l, phi, theta).imag*sph_harm(m, l, phi, theta).imag
#        print (m,fcolors)
#    else:
#        fcolors += sph_harm(m, l, theta, phi).real*sph_harm(m, l, theta, phi).real + sph_harm(m, l, theta, phi).imag*sph_harm(m, l, theta, phi).imag
#        print (m,fcolors)

m = 0
fcolors = sph_harm(m, l, phi, theta).real*sph_harm(m, l, phi, theta).real + sph_harm(m, l, phi, theta).imag*sph_harm(m, l, phi, theta).imag

fmax, fmin = fcolors.max(), fcolors.min()
fcolors = (fcolors - fmin)/(fmax - fmin)

#print(fcolors)

# Set the aspect ratio to 1 so our sphere looks spherical
fig = plt.figure(figsize=plt.figaspect(1.))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z,  rstride=1, cstride=1, facecolors=cm.seismic(fcolors))
# Turn off the axis planes
#ax.set_axis_off()
plt.show()