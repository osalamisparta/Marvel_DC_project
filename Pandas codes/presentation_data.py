#!/usr/bin/env python
# coding: utf-8

# In[151]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



chd = pd.read_csv('Desktop/Sparta global/Homework/Marvel_DC_project/CSVs/charcters_stats.csv')
mcd = pd.read_csv('Desktop/Sparta global/Homework/Marvel_DC_project/CSVs/marvel_characters_info.csv')
# print(chd)
# print(mcd)


# In[37]:


## Read headers
# print(chd.columns)

## Read specefic columns
# print(chd['Name'][0:10])

## Read specefic row
# print(chd.iloc[0:4])

## Read specefic row and columns
# print(chd.iloc[0, 1])

# for i, row in chd.iterrows():
#     print(i, row['Name'])
    
# chd.loc[chd['Alignment'] == 'good'][0:10]

## Sort/Describe data
# print(chd.sort_values('Name'))


    


# In[144]:


## Create a list of Marvel names and a list of DC names
marvel_cname_list = list(mcd.loc[mcd['Publisher'] == 'Marvel Comics']['Name'].values)
dc_cname_list = list(mcd.loc[mcd['Publisher'] == 'DC Comics']['Name'].values)


## Get average speed of Marvel and DC characters
marvel_cstrength_data = chd.loc[chd['Name'].isin(marvel_cn_list)][['Name', 'Strength']]
dc_cstrength_data = chd.loc[chd['Name'].isin(dc_cname_list)][['Name', 'Strength']]

marvel_cstrength_describe_data = marvel_cstrength_data.describe()
dc_cstrength_describe_data = dc_cstrength_data.describe()


# print(type(marvel_cn))
# print(type(chd))


# In[216]:


## Turning data into graphs - BOX PLOTS
a = chd.loc[chd['Name'].isin(marvel_cn_list)]['Strength']
b = chd.loc[chd['Name'].isin(dc_cname_list)]['Strength']

label_names = ['Marvel', 'DC Comics']

plt.figure(figsize=(8,10))
main_bp = plt.boxplot([a, b], labels=label_names)
# plt.title('Marvel vs DC Comics Strength Comparison')
plt.show()


# In[218]:


## Turning data into graphs - HISTOGRAM
plt.figure(figsize=(8,10))
main_hist = plt.hist([a, b])


# In[ ]:





# In[ ]:




