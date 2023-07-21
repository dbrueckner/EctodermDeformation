#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 15:23:24 2023

@author: D.Brueckner
"""

import numpy as np

def calc_positions(l_here,N_bins):
    length = np.sum(l_here)
    x_here = np.zeros(l_here.shape)
    for i in range(0,N_bins):
        if i == 0:
            x_here[i] = l_here[i]/2
        else:
            x_here[i] = np.sum(l_here[:i]) + l_here[i]/2
    return x_here - length/2

def simulate(eta,L0,v,N_bins,N_t,dt):
    
    h = np.zeros((N_bins,N_t))
    l = np.zeros((N_bins,N_t))
    x = np.zeros((N_bins,N_t))

    h[:,0] = np.ones(N_bins)

    l0 = (2*L0/N_bins)
    l[:,0] = np.ones(N_bins)*l0
    x[:,0] = calc_positions(l[:,0],N_bins)


    for t in range(0,N_t-1):
        
        sum_term = 0
        for i in range(0,N_bins):
            sum_term += l[i,t]/(h[i,t]*eta[i])
        f_ext = 8*v/sum_term
        
        for i in range(0,N_bins): 
            l[i,t+1] = l[i,t] + ( l[i,t]/(4*h[i,t]*eta[i]) )*f_ext*dt
            h[i,t+1] = h[i,t] + ( -1/(4*eta[i]) )*f_ext*dt
            
        x[:,t+1] = calc_positions(l[:,t+1],N_bins)
        
    return h,l,x
