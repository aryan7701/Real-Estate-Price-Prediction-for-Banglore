#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib
matplotlib.rcParams["figure.figsize"]=(20,10)


# In[3]:


#reading the data from the csv file
df1 = pd.read_csv("bengaluru_house_prices.csv")
df1.head()


# In[4]:


#it shows no.of rows and no. of columns
df1.shape


# In[5]:


#I will print account of dataset/data sample in each of these area type categories
df1.groupby('area_type')['area_type'].agg('count')


# In[6]:


# drop/removing certain columns from our dataframe...like area_type,society,balcony,availability,ect.
df2 = df1.drop(['area_type','society','balcony','availability'],axis='columns')
df2.head()


# In[7]:


# bow we are starting the data cleaning fuction to remove the no of rows whose value is NA.
df2.isnull().sum()


# In[8]:


# for dropin we use dropna function
df3 = df2.dropna()
df3.isnull().sum()


# In[9]:


# 
df3.shape


# In[10]:


# we check a particular column and we are calling unique function thus giving us unique values.
df3['size'].unique()


# In[26]:


# creating a new column,thus to avoid duplicate error.
# This column is created based on size column.
df3['bhk']=df3['size'].apply(lambda x:int(x.split(' ')[0]))


# In[27]:


df3.head()


# In[28]:


df3['bhk'].unique()


# In[29]:


df3[df3.bhk>20]


# In[30]:


df3.total_sqft.unique()


# In[31]:


def is_float(x):
    try:
        float(x)
    except:
        return False
    return True


# In[32]:


df3[~df3['total_sqft'].apply(is_float)].head(10)


# In[33]:


def convert_sqft_to_num(x):
    tokens = x.split('-')
    if len(tokens) ==2:
        return(float(tokens[0])+float(tokens[1]))/2
    try:
        return float(x)
    except:
        return None


# In[34]:


convert_sqft_to_num('2166')


# In[35]:


convert_sqft_to_num('2100 - 2850')


# In[36]:


convert_sqft_to_num('34.456Sq. Meter')


# In[37]:


df4 = df3.copy()
df4['total_sqft']= df4['total_sqft'].apply(convert_sqft_to_num)
df4.head(3)


# In[39]:


# check for error if in future any came since in this we should have integer values
df4.loc[30]


# In[ ]:




