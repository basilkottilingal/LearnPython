#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


# In[14]:


# triangles =  [
# ((1,1,1),(2,2,2),(1,3,4)),
# ((2,3,4),(9,9,9),(3,4,5)),
# ]
triangles =  [
[[1,1,1],[2,2,2],[1,3,4]],
[[2,3,4],[9,9,9],[3,4,5]],
]


ax = plt.gca(projection="3d")

ax.add_collection(Poly3DCollection(triangles))

ax.set_xlim([0,10])
ax.set_ylim([0,10])
ax.set_zlim([0,10])

plt.show()


# In[4]:


np.shape(triangles)


# In[27]:


f = open('triangles.dat', 'r')
data = np.genfromtxt(f, delimiter=',')
f.close()
l, = np.shape(data);
p = (int) (l/9); q = 3 ; r =3;
triangles = np.reshape(data, (p,q,r))


# In[31]:


#interactive  (To rotate and zoom plot use following command)
get_ipython().run_line_magic('matplotlib', 'notebook')

ax = plt.gca(projection="3d")

ax.add_collection(Poly3DCollection(triangles))

ax.set_xlim([0.6,0.8])
ax.set_ylim([0.6,0.8])
ax.set_zlim([0.6,0.8])

plt.show()


# In[ ]:




