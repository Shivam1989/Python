
# coding: utf-8

# In[1]:

#Import Packges
import os
import pandas as pd


# In[2]:

# get current working directory
direct = os.getcwd()

# read csv file from location
df = pd.read_csv(direct+"/"+"Assignment 3/employee_compensation.csv", usecols=[3,5,21])
df.head()


# In[4]:

comp=pd.DataFrame(df.groupby(['Organization Group','Department']).mean())
comp=comp[['Total Compensation']]
comp.reset_index(level=(0,1), inplace=True)
comp=dept_comp.sort_values(by=['Organization Group','Total Compensation'], ascending=[True,False])
comp.reset_index()
comp.to_csv('Q2_Part_1_Output.csv',  index = False)
comp.head(10)


# In[ ]:



