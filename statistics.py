#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# ### statisticsproblem with visualization

# ### 1.A study has shown that males in the UK have steadily grown in height from the 1800s to 1980. Based on the data below, find the mean height for each sixty-year period. Then, choose an appropriate chart or plot to visualize this

# In[2]:


data = [[1810,1820,1830,1840,1850,1860,1870,1880,1890,1900,1910,1920,1930,1940,1950,1960,1970,1980],[169.7,169.1,166.7,166.5,165.6,166.6,167.2,168,167.4,169.4,170.9,171,173.9,174.9,176,176.9,177.1,176.8]]


# In[3]:


pr1 = pd.DataFrame(data).transpose()


# In[4]:


pr1.columns = ['Year','Height in Cm']


# In[5]:


pr1.head(5)


# In[6]:


pr1.info()


# In[7]:


pr1['Year'] = pr1['Year'].astype('int')


# In[8]:


pr1.info()


# In[9]:


pr1


# In[10]:


pr1.shape


# In[11]:


def fining_avg(d):
    averages = []
    interval = 6
    for i in range(0, len(d), interval):
        averages.append(round(sum(d[i:i+interval])/interval,2))
    return averages


# In[12]:


average = fining_avg(pr1['Height in Cm'])


# In[13]:


average


# In[14]:


new_df = pd.DataFrame(average,columns=['Average Heights in Cm'])


# In[15]:


new_df['Year wise Intervals'] = ['1810 - 1860','1870 - 1920','1930 - 1980']


# In[16]:


new_df


# In[17]:


plt.figure(figsize=(12,8))
sns.barplot(x = 'Year wise Intervals', y = 'Average Heights in Cm',data = new_df)
plt.title("Average Height Over Time")
plt.show()


# ### You want to investigate the average amount of time people aged 20 to 40 spend on the phone each week. Interpret the chart below by finding the group mean of the hours spent on the phone.
# 
# Age	   Hours
# 
# 20-22	45
# 
# 23-25	36
# 
# 26-28	25
# 
# 29-31	16
# 
# 32-34	12
# 
# 35-37	8.5
# 
# 38-40	4

# In[18]:


problem = [["20-22","23-25","26-28","29-31","32-34","35-37","38-40"],[45,36,25,16,12,8.5,4]]


# In[21]:


df = pd.DataFrame(problem).transpose()


# In[22]:


df.columns = ['Age','Hours']


# In[23]:


df.head()


# In[26]:


plt.figure(figsize=(12,5))
sns.barplot(x = 'Age', y = 'Hours',data =df)
plt.title("Time Spend on Mobile phone age group")
plt.show()


# In[46]:


def average_mean(x):
    age = x.split("-")
    return (int(age[0]) + int(age[1]))//2


# In[47]:


df['Group_Mean'] = df['Age'].apply(average_mean)


# In[48]:


df


# In[49]:


df['frequency_Group_mean'] = df['Hours'] * df['Group_Mean']


# In[50]:


df


# In[51]:


group_mean = (df['frequency_Group_mean'].sum())/(df['Hours'].sum())


# In[52]:


group_mean


# In[54]:


plt.figure(figsize=(12,5))
sns.barplot(x = 'Age', y = 'Hours',data =df)
plt.title("Time Spend on Mobile phone age group")
plt.show()


# In[ ]:




