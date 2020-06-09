#!/usr/bin/env python
# coding: utf-8

# In[4]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
import numpy as np
import sympy

    


# In[5]:


#range of parameter t
t = np.linspace(0, 2*np.pi, 300)

#defining x and y
x = np.sin(t) + 0.5*np.cos(5*t) + 0.25*np.sin(13*t)
y = np.cos(t) + 0.5*np.sin(5*t) + 0.25*np.cos(13*t)
R=(x,y)

#plotting parametric curve
fig, ax = plt.subplots(figsize=(15,15))
plt.title("$PLOT$ $OF$ $PARAMETRIC$ $CURVE:$ \n $x=sin(t)+0.5cos(5t)+0.25sin(13t)$$,$ $y=cos(t)+0.5sin(5t)+0.25cos(13t)$\n ", fontsize="16",fontweight="bold", loc="left")
ax.plot(x, y, color="black", antialiased=True)
ax.grid(color="dimgray", which="major", axis="x", linestyle='-', linewidth=0.65 )
ax.grid(color="dimgray", which="minor", axis="x", linestyle='-', linewidth=0.65 )
ax.grid(color="dimgray", which="major", axis="y", linestyle='-', linewidth=0.65 )
ax.grid(color="dimgray", which="minor", axis="y", linestyle='-', linewidth=0.65 )
ax.set_xlim(-2,2)
ax.set_ylim(-2,2)
ax.set_xlabel("$x$", fontsize="16", weight="bold")
ax.set_ylabel("$y$", fontsize="16", weight="bold")
plt.rcParams.update({'font.size': 15})
plt.show()


# In[10]:


#range which parameters u and v take respectively
range1=np.linspace(0,4*np.pi,150)
range2=np.linspace(0,2*np.pi,150)

#setting parameters u,v
u,v=np.meshgrid(range1, range2)
#defining X,Y,Z
X=(2 + np.sin(v))*np.cos(u)
Y=(2 + np.sin(v))*np.sin(u)
Z=u + np.cos(v)

# Displaying the plot
fig = plt.figure(figsize=(15,15))
ax = fig.gca(projection = '3d')
ax.set_xlim3d(-5,3)
ax.set_ylim3d(-5,3)
ax.set_zlim3d(0, 9)
ax.set_xlabel("$x$", fontsize="16", weight="bold")
ax.set_ylabel("$y$", fontsize="16", weight="bold")
ax.set_zlabel("$z$", fontsize="16", weight="bold")
plt.title("$PLOT$ $OF$ $PARAMETRIC$ $SURFACE:$ \n $x=2+sin(v).cos(u)$$,$ $y=2+sin(v).sin(u)$$,$ $z=u+cos(v)$", fontsize="16",fontweight="bold", loc="left")
plt.rcParams['grid.color']="dimgray"
plt.rcParams.update({'font.size': 15})
ax.plot_surface(X, Y, Z, color = 'c', linewidth=20, alpha=0.8, edgecolors='k',lw=0.3, rstride = 5, cstride = 1)
plt.show()


# In[ ]:





# In[ ]:




