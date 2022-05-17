#!/usr/bin/env python
# coding: utf-8

# # Generating visualizations with pyplot is very quick:
# 
# 

# In[11]:


import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()





# You may be wondering why the x-axis ranges from 0-3 and the y-axis from 1-4. If you provide a single list or array to plot, matplotlib assumes it is a sequence of y values, and automatically generates the x values for you. Since python ranges start with 0, the default x vector has the same length as y but starts with 0. Hence the x data are [0, 1, 2, 3].
# 
# plot is a versatile function, and will take an arbitrary number of arguments. For example, to plot x versus y, you can write:
# 
# 

# In[13]:


plt.plot([1, 2, 3, 4], [1, 4, 9, 16])


# # Formatting the style of your plot
# 
# For every x, y pair of arguments, there is an optional third argument which is the format string that indicates the color and line type of the plot. The letters and symbols of the format string are from MATLAB, and you concatenate a color string with a line style string. The default format string is 'b-', which is a solid blue line. For example, to plot the above with red circles, you would issue
# 
# 

# In[14]:


plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.axis([0, 6, 0, 20])
plt.show()


# See the plot documentation for a complete list of line styles and format strings. The axis function in the example above takes a list of [xmin, xmax, ymin, ymax] and specifies the viewport of the axes.
# 
# If matplotlib were limited to working with lists, it would be fairly useless for numeric processing. Generally, you will use numpy arrays. In fact, all sequences are converted to numpy arrays internally. The example below illustrates plotting several lines with different format styles in one function call using arrays.
# 
# 

# In[15]:


import numpy as np

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.4)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()


# # Plotting with keyword strings¶
# There are some instances where you have data in a format that lets you access particular variables with strings. For example, with numpy.recarray or pandas.DataFrame.
# 
# Matplotlib allows you provide such an object with the data keyword argument. If provided, then you may generate plots with the strings corresponding to these variables.
# 
# 

# In[16]:


data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('entry a :')
plt.ylabel('entry b :')
plt.show()


# # Plotting with categorical variables¶
# It is also possible to create a plot using categorical variables. Matplotlib allows you to pass categorical variables directly to many plotting functions. For example:
# 
# 

# In[17]:


names = ['group_a', 'group_b', 'group_c']
values = [1, 9, 97]

plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle('Categorical Plotting')
plt.show()


# 

# In[ ]:





# In[ ]:





# In[ ]:




