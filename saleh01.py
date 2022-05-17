#!/usr/bin/env python
# coding: utf-8

# Data Visualization using Python
# 

# Basic plotting in matplotlib

# In[2]:


get_ipython().system('pip install matplotlib==3.4')


# In[6]:


from matplotlib import pyplot as plt
plt.style.use('seaborn-whitegrid')

import numpy as np






from matpltlib import pyplot as plt 


# For: all Matplotlib plots, we start by creating a figure and an axes. In their simplest form, a figure and axes can be created as follows:

# In[7]:


fig = plt.figure()
ax = plt.axes()
# ax.grid()


# In Matplotlib, the figure (an instance of the class plt.Figure) can be thought of as a single container that contains all the objects representing axes, graphics, text, and labels. The axes (an instance of the class plt.Axes) is what we see above: a bounding box with ticks and labels, which will eventually contain the plot elements that make up our visualization.
# 

# Line Plots 

# We'll commonly use the variable name fig to refer to a figure instance, and ax to refer to an axes instance or group of axes instances.
# Once we have created an axes, we can use the ax.plot function to plot some data. Let's start with a simple sinusoid:
# 
# 
# 

# In[9]:


fig = plt.figure()
ax = plt.axes()

x = np.linspace(0, 12, 1100)
ax.plot(x, np.sin(x));


# In[17]:


# Lets add a title and labels to the plot

fig = plt.figure()
ax = plt.axes()

x = np.linspace(0, 10, 1000)
ax.plot(x, np.sin(x))
ax.set_title('Today Class')   # Add a title
ax.set_xlabel('Day label')          # Add x label
ax.set_ylabel('Calss label');         # Add y label


# Multiple lines on same plot

# In[11]:


# Lets add a title to the plot above
fig = plt.figure()
ax = plt.axes()

x = np.linspace(0, 12, 1100)
ax.plot(x, np.sin(x))
ax.plot(x, np.cos(x))
ax.set_title('Multiple Lines');
ax.set_xlabel('xx label')          
ax.set_ylabel('yy label')         
plt.show()


# Adding a legend

# In[12]:


fig = plt.figure()
ax = plt.axes()

x = np.linspace(0, 15, 1100)
ax.plot(x, np.sin(x), label = 'sin')
ax.plot(x, np.cos(x), label = 'cos')
ax.set_title('Multiple Lines');
ax.set_xlabel('x label')          
ax.set_ylabel('y label')
ax.legend()
# ax.legend(loc=1)           
plt.show()


# Line colors

# In[13]:


fig = plt.figure()
ax = plt.axes()

x = np.linspace(0, 9, 1150)
ax.plot(x, np.sin(x), label = 'sin', color = 'red')   # specify color by name
ax.plot(x, np.cos(x), label = 'cos', color = 'g')    # short color code (rgbcmyk)
ax.set_title('Multiple Lines');
ax.set_xlabel('xx label')          
ax.set_ylabel('yy label')
ax.legend();       


# Line Styles

# In[14]:


fig = plt.figure()
ax = plt.axes()
# ax.grid(linestyle = '--')

x = np.linspace(0, 9, 1300)
ax.plot(x, np.sin(x), label = 'sin', linestyle = 'dashed')   
ax.plot(x, np.cos(x), label = 'cos', linestyle = 'dotted')
ax.plot(x, np.sin(x+1), label = 'cos', linestyle = 'dashdot')
ax.set_title('Multiple Lines');
ax.set_xlabel('x label')          
ax.set_ylabel('y label')
ax.legend();


# This is my task today 

# In[ ]:




