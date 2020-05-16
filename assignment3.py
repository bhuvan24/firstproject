#!/usr/bin/env python
# coding: utf-8

# In[12]:


#Assignment 2 - create data frame - Pandas
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
id_list =[1001,1002,1003,1004,1005]
name_list = ['Anathan','Ashok','Babul','Rajsekar','Zaheer']
age_list = [28,25,24,22,39]
salary_list = [10000,12000,15000,9000,30000]
staff_detail_1 = {'Person ID':id_list,'Name':name_list,'Age':age_list,'Salary':salary_list}
s_df_1=pd.DataFrame(staff_detail_1)
s_df_1


# In[13]:


id_list2=[2001,2002,2003,2004,2005]
name_list2=['Ravi','Guru','Bhasha','Raju','Malik']
age_list2=[25,28,21,28,31]
salary_list2=[13000,12500,17000,8500,40000]

staff_detail_2 = {'Person ID':id_list2,'Name':name_list2,'Age':age_list2,'Salary':salary_list2}
s_df_2=pd.DataFrame(staff_detail_2)
s_df_2


# In[21]:


#convert multi dataframe into panel - panel is depreciated in pandas 0.25.3
panel_data ={'Data1':s_df_1,'Data2':s_df_2}
#panel_1 = pd.Panel.from_dict(panel_data)
pd.Panel()


# In[41]:


#using pickle compare data -- Pickle
import pickle
fileobj = open('filee','wb')
pickle.dump(s_df_1,fileobj)
fileobj.close()
fileobj = open('filee','rb')
bf=pickle.load(fileobj)
bf


# In[43]:


#check datas
bf==s_df_1


# In[55]:


#file import csv through pandas
filecsv = "E:\\Machine_Learning_Classworks\\csvfiles\\sample.csv"
ds=pd.read_csv(filecsv,names=['SNo','Name','Age','City','Salary'],index_col=['SNo'])
ds


# In[69]:


#prints only particular column
ds=pd.read_csv(filecsv,names=['SNo','Name','Age','City','Salary'],index_col=['SNo'],usecols=['SNo','Name','Age'])
ds


# In[70]:


#prints datas after 3 rows
ds=pd.read_csv(filecsv,names=['SNo','Name','Age','City','Salary'],index_col=['SNo'],skiprows=3)
ds

