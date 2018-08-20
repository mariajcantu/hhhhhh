
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


r = help(np.random.normal)


# In[3]:


r = np.random.normal(0,1e-4,(100,))


# In[4]:


import matplotlib.pyplot as plt


# In[5]:


plt.plot(r)

