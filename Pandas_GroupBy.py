#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
# Create dataframe
data = {'Batch': ['Morning', 'Morning', 'Morning', 'Morning', 'Afternoon', 'Afternoon', 'Afternoon',
                     'Afternoon', 'Evening', 'Evening', 'Evening', 'Evening'], 
        'Section': ['A', 'A', 'B', 'B', 'A', 'A', 'B', 'B','A', 'A', 'B', 'B'], 
        'Name': ['John', 'Root', 'Ali', 'Scott', 'Mary', 'Jacob', 'Ryaner', 'Arya', 'Elsa', 'Tiger', 'Rose', 'Ryan'], 
        'TestScore': [30, 24, 31, 15, 37, 24, 24, 31, 12, 23, 22, 23]}
df1 = pd.DataFrame(data, columns = ['Batch', 'Section', 'Name', 'TestScore'])
df1


# In[20]:


df_group_by = df1.groupby(by='Section')
df_group_by


# In[21]:


list_groups = list(df_group_by)
list_groups


# In[22]:


group_mean = df1.groupby('Section').mean().add_prefix('mean_')
group_mean


# In[10]:


group_count = df1.groupby('Batch').Batch.count()
group_count


# In[26]:


group_sort_mark = df1.groupby('Batch').mean().sort_values('TestScore',ascending=False)

group_sort_mark


# In[30]:


pivot = pd.pivot_table(df1, index=['Section','Batch'], aggfunc='mean')
pivot


# In[ ]:




