
# coding: utf-8

# In[1]:

#Import Packges
import os
import pandas as pd


# In[2]:

# get current working directory
direct = os.getcwd()

# read csv file from location
df = pd.read_csv(direct+"/"+"Assignment 3/employee_compensation.csv")
df.head()


# In[3]:

comp=df[(df['Year Type']=='Calendar')]
comp=pd.DataFrame(comp.groupby(['Employee Identifier','Job Family']).mean())

comp.drop(['Year', 'Organization Group Code','Union Code'], axis=1, inplace=True)
comp.head()


# In[5]:

overtime=comp[(comp['Overtime']>(.05*comp['Salaries']))]
overtime.head()


# In[6]:

top_family=overtime
top_family=top_family.groupby([top_family.index.get_level_values(1)]).mean()


# In[7]:

top_family=top_family[['Total Benefits','Total Compensation']]
top_family['Percent_Total_Benefit']=100*(top_family['Total Benefits']/top_family['Total Compensation'])
top_family=top_family.sort_values(['Percent_Total_Benefit'], ascending=[False])
top_family.to_csv('Q2_Part_2_Output.csv')
top_family.head(5)


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



