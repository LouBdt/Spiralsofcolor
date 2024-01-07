#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 19:06:47 2024

@author: lou
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 12:32:02 2024

@author: lou
"""
import numpy as np
import matplotlib.pyplot as plt
from colorsys import hls_to_rgb
import warnings
warnings.filterwarnings("ignore")

window = 200
fp = 56
longueur = 50000
offset = 5
repeat =1
nbx = 300
alph = 0.5
desite_spirale = 4.5
colorfactor = 4
qly = 300
trainee =  3.5
th = np.linspace(6*np.pi,0.0001, nbx)
theta = [(t**(1/desite_spirale))*np.log(t+np.e) for t in th]
filenames = []

def rainbow_color_stops(n=nbx, end=1):
    return [ hls_to_rgb(end * i/(n-1), 0.5, 1) for i in range(n) ]

import imageio.v2 as imageio
def makepoints():
    
    xautre = []
    yautre = []
    j = 0
    for i in range(nbx,0,-1):
        print
        if i%offset ==0:
            rj = theta[(j*offset)]**2
            rj1 = theta[(j*offset)+1]**2
            xautre.append([20*rj*np.cos(rj)/((nbx/i)*np.sqrt(rj)),20*rj1*np.cos(rj1)/((nbx/i)*np.sqrt(rj1))])
            yautre.append([20*rj*np.sin(rj)/((nbx/i)*np.sqrt(rj)),20*rj1*np.sin(rj1)/((nbx/i)*np.sqrt(rj1))])
            j+=1 
    return xautre, yautre

def animation(xautre, yautre, w, subtitle):
    coul = rainbow_color_stops()
    x = len(xautre)
    for i in range(x):
        for k in range(int(i/trainee),i-2):
            plt.scatter(xautre[k],yautre[k],c = coul[int(colorfactor*k)], alpha = alph, marker = "o",edgecolor='none')
            plt.scatter([-e for e in xautre[k]],[-e for e in yautre[k]],c = coul[int(colorfactor*k)], alpha = alph, marker = "o",edgecolor='none')
        if i<x-2 and i>x+2:
            plt.scatter(xautre[i+2],yautre[x+2],c = coul[2], alpha = alph*2/3, marker = "o",edgecolor='none')
            plt.scatter([-e for e in xautre[i+2]],[-e for e in yautre[x-2]],c = coul[2], alpha = alph*2/3, marker = "o",edgecolor='none')
        if i<x-1 and i>x+1:
            plt.scatter(xautre[i+1],yautre[i+1],c = coul[x+1], alpha = alph/3, marker = "o",edgecolor='none')
            plt.scatter([-e for e in xautre[i+1]],[-e for e in yautre[x+1]],c = coul[1], alpha = alph/3, marker = "o",edgecolor='none')
        
        
        plt.style.use('dark_background')
        plt.xlim(-window, window)
        plt.ylim(-window, window)
        ax = plt.gca()
        ax.axis('off')
        ax.set_box_aspect(1)
        filename = 'plots/'+str(i)+subtitle+'.png'
        plt.savefig(filename, dpi=qly)
        image = imageio.imread(filename)
        writer.append_data(image)
        i +=1
        plt.pause(0.01) # pause avec duree en secondes
    return xautre,yautre

def reverseanim(xa, ya, writer, subtitle):
    coul = rainbow_color_stops()
    x = len(xa)
    for i in range(x-1,1,-1):
        for k in range(int(i/trainee),i-2):
            plt.scatter(xa[k],ya[k],c = coul[int(colorfactor*k)], alpha = alph, marker = "o",edgecolor='none')
            plt.scatter([-e for e in xa[k]],[-e for e in ya[k]],c = coul[int(colorfactor*k)], alpha = alph, marker = "o",edgecolor='none')
        if i>3:
            plt.scatter(xa[i-2],ya[i-2],c = coul[-i-1], alpha = alph*2/3, marker = "o",edgecolor='none')
            plt.scatter([-e for e in xa[i-2]],[-e for e in ya[i-2]],c = coul[-i-1], alpha = alph*2/3, marker = "o",edgecolor='none')
        if i>2:
            plt.scatter(xa[i-1],ya[i-1],c = coul[-i], alpha = alph/3, marker = "o",edgecolor='none')
            plt.scatter([-e for e in xa[i-1]],[-e for e in ya[i-1]],c = coul[-i], alpha = alph/3, marker = "o",edgecolor='none')
        
        plt.style.use('dark_background')
        plt.xlim(-window, window)
        plt.ylim(-window, window)
        ax = plt.gca()
        ax.axis('off')
        ax.set_box_aspect(1)
        filename = 'plots/'+str(i)+subtitle+'.png'
        plt.savefig(filename, dpi=qly)
        image = imageio.imread(filename)
        writer.append_data(image)
        i +=1
        plt.pause(0.01) # pause avec duree en secondes
with imageio.get_writer('test.mp4', fps=fp)  as writer:
    xa, ya = makepoints()
    animation(xa, ya, writer, "x1x")
    reverseanim(xa, ya,writer, "x2x")
    animation(ya, xa, writer, "x3x")
    reverseanim(ya,xa,writer, "x4x")
    
    