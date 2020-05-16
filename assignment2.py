#!/usr/bin/env python
# coding: utf-8

# In[12]:


#Assignment 2 - create data frame
import pandas as pd
id_list =[1001,1002,1003,1004,1005]
name_list = ['Anathan','Ashok','Babul','Rajsekar','Zaheer']
age_list = [28,25,24,22,39]
salary_list = [10000,12000,15000,9000,30000]
staff_detail_1 = {'Person ID':id_list,'Name':name_list,'Age':age_list,'Salary':salary_list}
s_df_1=pd.DataFrame(staff_detail_1)
s_df_1


# In[14]:


id_list2=[2001,2002,2003,2004,2005]
name_list2=['Ravi','Guru','Bhasha','Raju','Malik']
age_list2=[25,28,21,28,31]
salary_list2=[13000,12500,17000,8500,40000]

staff_detail_2 = {'Person ID':id_list2,'Name':name_list2,'Age':age_list2,'Salary':salary_list2}
s_df_2=pd.DataFrame(staff_detail_2)
s_df_2


# In[18]:


#convert multi dataframe into panel
panel_data ={'Data1':s_df_1,'Data2':s_df_2}
panel_1 = pd.Panel(panel_data)
panel_1

