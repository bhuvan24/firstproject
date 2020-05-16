#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Assignment- Complaint Report - data manipulation - Task 1
#Library Headers
import pandas as pd
import warnings
import datetime
warnings.filterwarnings('ignore')
ds = pd.read_csv("E:\\Machine_Learning_Classworks\\NYC311\\NYC311.csv")


# In[9]:


#To Prints shape (rows,columns) and size(No.of datas in dataset)
print(ds.shape)
print(ds.size)


# In[11]:


#prints first 5 datas
ds.head(5)


# In[18]:


#convert dtypes of particular column
ds['Created Date'] =ds['Created Date'].apply(pd.to_datetime)
ds['Closed Date'] =ds['Closed Date'].apply(pd.to_datetime)
ds['Due Date'] =ds['Due Date'].apply(pd.to_datetime)
ds.info()


# In[20]:


#to find correlation in dataset
ds.corr()


# In[8]:


#Add to fill NAn with Unknown
ds['Location Type'].fillna('Unknown',inplace=True)
ds['City'].fillna('Unknown',inplace=True)


# In[10]:


#data summary
ds.describe()


# In[41]:


#top 10 and least 10 Complaints
top_complaints = ds['Complaint Type'].value_counts().head(10)
least_complaints = ds['Complaint Type'].value_counts().tail(10)


# In[42]:


top_complaints


# In[44]:


least_complaints


# In[27]:


#Most common complaint type which occurs in max no.of registered City
list_complaints_city_cnts=ds.groupby(['Complaint Type','City']).size().reset_index().groupby('Complaint Type')[[0]].count()
list_complaints_city_cnts.idxmax()


# In[31]:


#Max no.of complaints registered city
list_city_complaints_cnt=ds.groupby(['Complaint Type','City']).size().reset_index().groupby('City')[[0]].count()
list_city_complaints_cnt.idxmax()


# In[14]:


#complaint type above average compliant type mentioned true
ds['Complaint Type'].value_counts() >= ds['Complaint Type'].value_counts().mean()


# In[15]:


#no.of tickets have been breached due date
ds['Closed Date'] =ds['Closed Date'].apply(pd.to_datetime)
ds['Due Date'] =ds['Due Date'].apply(pd.to_datetime)
df1 = ds[(ds['Closed Date'] -ds['Due Date']).dt.days >= 0.0].copy()
len(df1)


# In[77]:


#month wise ticket count
ddscp=ds['Created Date'].dt.month.copy()
mwds=ddscp.drop_duplicates()
nbcase=ddscp.value_counts()
#counter
import matplotlib.pyplot as plt
from matplotlib import style
plt.scatter(mwds,nbcase,marker='o')
plt.show()

