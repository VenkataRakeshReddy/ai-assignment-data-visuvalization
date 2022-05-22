#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[3]:


sns.set(style="darkgrid")


# In[4]:


#sns.get_dataset_names()
sns.get_dataset_names()


# In[6]:


tips=sns.load_dataset('tips')


# In[7]:


tips.head()


# In[8]:


#relplot with the orgument x,y,data
sns.relplot(x='total_bill',y='tip',data=tips)


# In[11]:


#relplot with the orugument x,y,data,hue
sns.relplot(x='total_bill',y='tip',data=tips,hue="smoker")


# In[12]:


sns.scatterplot(x='total_bill',y='tip',data=tips,hue="sex")


# In[13]:


sns.relplot(x='total_bill',y='tip',data=tips,col="time",hue="day",style="day",kind="scatter")


# In[16]:


fmri=sns.load_dataset('fmri')


# In[17]:


fmri.head()


# In[18]:


sns.relplot(x='timepoint',y='signal',data=fmri,kind='line',ci=False)


# In[19]:


sns.relplot(x='timepoint',y='signal',data=fmri,kind='line',ci=True)


# In[20]:


sns.relplot(x='timepoint',y='signal',data=fmri,kind='line',hue='region')


# In[21]:


tips.head()


# In[22]:


sns.regplot(x='total_bill',y='tip',data=tips)


# In[ ]:




