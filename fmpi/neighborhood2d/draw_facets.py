#!/usr/bin/env python
# coding: utf-8

# In[12]:


from matplotlib import pyplot as plt
#from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
import numpy as np


# In[13]:


I_ = 0; J_ = 0; K_= 0;

def bounding_box():
    ax.plot([(I_),(I_+1)], [(J_),(J_)], [(K_),(K_)], color = [0,0,0], alpha=0.1)
    ax.plot([(I_),(I_+1)], [(J_+1),(J_+1)],     [(K_+1),(K_+1)], color = [0,0,0], alpha=0.1)
    ax.plot([(I_),(I_+1)], [(J_),(J_)], [(K_+1),(K_+1)], color = [0,0,0], alpha=0.1)
    ax.plot([(I_),(I_+1)], [(J_+1),(J_+1)],     [(K_),(K_)], color = [0,0,0], alpha=0.1)
    ax.plot([(I_),(I_)], [(J_),(J_+1)], [(K_),(K_)], color = [0,0,0], alpha=0.1)
    ax.plot([(I_+1),(I_+1)], [(J_),(J_+1)],     [(K_+1),(K_+1)], color = [0,0,0], alpha=0.1)
    ax.plot([(I_+1),(I_+1)], [(J_),(J_+1)],     [(K_),(K_)], color = [0,0,0], alpha=0.1)
    ax.plot([(I_),(I_)], [(J_),(J_+1)], [(K_+1),(K_+1)], color = [0,0,0], alpha=0.1)
    ax.plot([(I_),(I_)], [(J_),(J_)],[(K_),(K_+1)], color = [0,0,0], alpha=0.1)
    ax.plot([(I_+1),(I_+1)], [(J_+1),(J_+1)],       [(K_),(K_+1)], color = [0,0,0], alpha=0.1)
    ax.plot([(I_+1),(I_+1)], [(J_),(J_)],   [(K_),(K_+1)], color = [0,0,0], alpha=0.1)
    ax.plot([(I_),(I_)], [(J_+1),(J_+1)],   [(K_),(K_+1)], color = [0,0,0], alpha=0.1)
    
def draw_axi():
    ax.quiver((I_+0.01), (J_+0.01), (K_+0.01), 0.1, 0., 0., color = 'r')
    ax.quiver((I_+0.01), (J_+0.01), (K_+0.01), 0., 0.1, 0., color = 'g')
    
#line segment /edges of cube
seg = [[[0,0,0],[0,0,1]],[[0,0,0],[0,1,0]],
       [[0,0,0],[1,0,0]],[[1,1,0],[1,1,1]],[[0,1,1],[1,1,1]],
       [[1,0,1],[1,1,1]],[[1,0,0],[1,0,1]],[[1,0,0],[1,1,0]],
       [[0,1,0],[0,1,1]],[[0,1,0],[1,1,0]],[[0,0,1],[1,0,1]],
       [[0,0,1],[0,1,1]]] ;


# In[120]:


###################
##  EDGES cells and facets#######

#streams
imgfile = "neighborhood.png" #output .png

#fig handle
fig,ax = plt.subplots()

#colormap
cmap=plt.get_cmap('tab10')  #Only 10 distict colors

#input elements data
file = "facets.dat" #input
dat = np.loadtxt(file);
r,c  = np.shape(dat)
for ir in range(r):
    x = [dat[ir,2*(j%4)] for j in range(2)]
    y = [dat[ir,2*(j%4)+1] for j in range(2)]
    if(dat[ir,4]):
        ax.plot(x,y, c = 'r')
    else:
        ax.plot(x,y, c = 'black')
    
ax.scatter(dat[:, 0], dat[:, 1], s = 4.*np.ones(r), c = 'm', marker = 'o')
    
#input cell data
file = "cells.dat" #input
dat = np.loadtxt(file);
r,c  = np.shape(dat)
for ir in range(r):
    x = [dat[ir,2*(j%4)] for j in range(5)]
    y = [dat[ir,2*(j%4)+1] for j in range(5)]
    if(int(dat[ir,8]) == 2):
        ax.fill(x,y, c = [1,0,0], alpha=0.3)
        ax.plot(x,y, c = [0,0,0], lw = 0.1)
    if(dat[ir,8]):
        ax.fill(x,y, c = [1,0,0], alpha=0.1, edgecolor ='none')
        #ax.plot(x,y, c = [0,0,0], lw = 0.)
    else:
        ax.plot(x,y, c = [0,0,0])

#input element vectors data
file = "vectors.dat" #input
dat = np.loadtxt(file);
r,c  = np.shape(dat)
for ir in range(r):
    x = dat[ir,0]
    y = dat[ir,1]
    u = dat[ir,2]
    v = dat[ir,3] 
    if(int(dat[ir,4]) == 1):
        ax.quiver(x,y, u,v, scale=0.3, color = 'b')
    else:
        ax.quiver(x,y, u,v, scale=0.3, color = 'g')

ax.set_aspect('equal')
ax.set_xlim([0, 0.5])
ax.set_ylim([0, 0.5])
ax.axes.xaxis.set_visible(False)
ax.axes.yaxis.set_visible(False)
plt.savefig(imgfile, dpi=1200)


# In[122]:


###################
##  EDGES cells and facets#######

#streams
imgfile = "neighborhood2.png" #output .png

#fig handle
fig,ax = plt.subplots()

#colormap
cmap=plt.get_cmap('tab10')  #Only 10 distict colors

#input elements data
file = "facets.dat" #input
dat = np.loadtxt(file);
r,c  = np.shape(dat)
for ir in range(r):
    x = [dat[ir,2*(j%4)] for j in range(2)]
    y = [dat[ir,2*(j%4)+1] for j in range(2)]
    ax.plot(x,y, c = 'black')
    
ax.scatter(dat[:, 0], dat[:, 1], s = 4.*np.ones(r), c = 'm', marker = 'o')
    
#input cell data
file = "cells2.dat" #input
dat = np.loadtxt(file);
r,c  = np.shape(dat)
for ir in range(r):
    x = [dat[ir,2*(j%4)] for j in range(5)]
    y = [dat[ir,2*(j%4)+1] for j in range(5)]
    if(int(dat[ir,8]) == 2):
        ax.fill(x,y, c = [1,0,0], alpha=0.3)
        ax.plot(x,y, c = [0,0,0], lw = 0.1)
    if(dat[ir,8]):
        ax.fill(x,y, c = [1,0,0], alpha=0.1, edgecolor ='none')
        #ax.plot(x,y, c = [0,0,0], lw = 0.)
    else:
        ax.plot(x,y, c = [0,0,0])

#input element vectors data
file = "vectors2.dat" #input
dat = np.loadtxt(file);
r,c  = np.shape(dat)
for ir in range(r):
    x = dat[ir,0]
    y = dat[ir,1]
    u = dat[ir,2]
    v = dat[ir,3] 
    if(int(dat[ir,4]) == 1):
        ax.quiver(x,y, u,v, scale=10, color = 'g')
    else:
        ax.quiver(x,y, u,v, scale=10, color = 'b')

ax.set_aspect('equal')
ax.set_xlim([0, 0.5])
ax.set_ylim([0, 0.5])
ax.axes.xaxis.set_visible(False)
ax.axes.yaxis.set_visible(False)
plt.savefig(imgfile, dpi=1200)


# In[ ]:




