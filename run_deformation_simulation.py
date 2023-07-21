#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 15:23:24 2023

@author: D.Brueckner
"""

import numpy as np
from deformation_simulation import simulate

def viscosity(x,L):
    return 1+amplitude*np.cos(np.pi+np.pi*x/L)

#define parameters
L0 = 500 #in microns
time = 100 #in mins
v = 1.5 # in microns per min

N_bins = 100
dt = 0.1
N_t = int(time/dt)
N_t_plot = 10

ratio = 1/5
amplitude = (1-ratio)/(1+ratio)

xx_initial = np.linspace(-L0,L0,N_bins)

eta = viscosity(xx_initial,L0)
h,l,x = simulate(eta,L0,v,N_bins,N_t,dt)


import matplotlib.pyplot as plt
plt.close('all')
fs = 12
fs2 = 12   
params = {
          'font.size':   fs,
          'xtick.labelsize': fs2,
          'ytick.labelsize': fs2,
          }
plt.rcParams.update(params)
file_suffix = '.pdf'

divider_time = int(N_t/N_t_plot)

import matplotlib as mpl
cmap = mpl.cm.get_cmap('inferno')
colors_time = cmap(list(np.linspace(0,0.8,N_t_plot)))


fig_size = [4,3]
fs = 12
fs2 = 12   
params = {
          'figure.figsize': fig_size,
          }
plt.rcParams.update(params)


plt.figure()
xx = np.linspace(-L0,L0,100)
plt.plot(xx,viscosity(xx,L0),color='grey',lw=3)

plt.xlabel(r'Initial position $x$')
plt.ylabel(r'Viscosity $\eta(x)$')

plt.ylim([0,2])

plt.tight_layout()


plt.figure()
tt = np.arange(N_t)*dt
i = 0
plt.plot(tt,h[i,:],color='royalblue',label='Lateral',lw=4)
i = int(N_bins/2)
plt.plot(tt,h[i,:],color='gold',label='Animal',lw=4)

plt.ylim([0.2,1.2])
plt.xlabel(r'Time [min]')
plt.ylabel(r'Thickness [ratio to $t_0$]')
plt.legend(frameon=False)

plt.tight_layout()


plt.figure()
count = 0
for t in range(0,N_t,divider_time):
    plt.plot(x[:,t],h[:,t],color=colors_time[count])
    count+=1 
    
plt.ylim([0.2,1.2])
plt.xlabel(r'Distance from animal pole [$\mu$m]')
plt.ylabel(r'Thickness $h(x,t)/h_0$')

plt.tight_layout()


N_bins_plot = int(N_bins/2)
cmap = mpl.cm.get_cmap('YlGnBu')
colors_space = np.flipud(cmap(list(np.linspace(0,1,N_bins_plot))))
plt.figure()
for i in range(N_bins_plot-1,-1,-1):
    plt.plot(tt,h[i,:],color=colors_space[i])

plt.xlabel(r'Time [min]')
plt.ylabel(r'Thickness $h(t)/h_0$')

plt.tight_layout()
