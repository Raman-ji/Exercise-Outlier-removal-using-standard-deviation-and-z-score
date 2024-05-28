#!/usr/bin/env python
# coding: utf-8

# In[2]:


""" You are given bhp.csv which contains property prices in the city of banglore, India. You need to examine price_per_sqft column and do following,

1. Remove outliers using percentile technique first. Use [0.001, 0.999] for lower and upper bound percentiles
2. After removing outliers in step 1, you get a new dataframe.
3. On step(2) dataframe, use 4 standard deviation to remove outliers
4. Plot histogram for new dataframe that is generated after step (3). Also plot bell curve on same histogram
5. On step(2) dataframe, use zscore of 4 to remove outliers. This is quite similar to step (3) and you will get exact same result"""


# In[3]:


import pandas as pd


# In[4]:


df=pd.read_csv(r"C:\Users\uniqu\Downloads\archive\bhp.csv")


# In[5]:


df


# In[6]:


df.describe()


# In[7]:


df['price_per_sqft'].quantile(0.001)


# In[8]:


df['price_per_sqft'].quantile(0.999)


# In[9]:


df1=df[(df.price_per_sqft>df['price_per_sqft'].quantile(0.001))& (df.price_per_sqft<df['price_per_sqft'].quantile(0.999))]


# In[10]:


df1

#First step is complete 


# # On step(2) dataframe, use 4 standard deviation to remove outliers

# In[11]:


mean=df1.price_per_sqft.mean()


# In[12]:


std_deviation= df1.price_per_sqft.std()


# In[13]:


std_deviation


# In[14]:


min_std = mean-4*std_deviation


# In[15]:


max_std = mean+4*std_deviation


# In[16]:


df2= df1[(df1.price_per_sqft<max_std) & (df1.price_per_sqft>min_std)]


# In[17]:


df2


# In[18]:


import matplotlib.pyplot as plt


# In[19]:


plt.hist(df2.price_per_sqft, bins=20, rwidth=0.8)
plt.xlabel('Price per square ft')
plt.ylabel('Count')
plt.show()


# In[20]:


from scipy.stats import norm 
import numpy as np


# In[21]:


plt.hist(df2.price_per_sqft, bins=20, rwidth=0.8, density=True)
plt.xlabel('Height (inches)')
plt.ylabel('Count')

rng = np.arange(-5000, df2.price_per_sqft.max(), 100)
plt.plot(rng, norm.pdf(rng,df2.price_per_sqft.mean(),df2.price_per_sqft.std()))


# On step(2) dataframe, use zscore of 4 to remove outliers. This is quite similar to step (3) and you will get exact same result

# In[22]:


df1['zscore']=(df1.price_per_sqft- df1.price_per_sqft.mean())/df.price_per_sqft.std()
df1.sample(10)
df1.shape


# In[23]:


df1['zscore'] = (df1.price_per_sqft-df1.price_per_sqft.mean())/df1.price_per_sqft.std()
df1.sample(10)


# In[29]:


df3=df1[(df1.zscore<4)&(df1.zscore>-4)]


# In[30]:


df3


# In[32]:


outliers_z = df1[(df1.zscore < 4) & (df1.zscore>-4)]
outliers_z.shape


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




