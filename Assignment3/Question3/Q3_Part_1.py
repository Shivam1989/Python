
# coding: utf-8

# In[1]:

#import packages
import os
import pandas as pd


# In[2]:

# Getting current working directory
direct = os.getcwd()

# Reading vehicle_collison file store in Assignment 3 folder in cuurentDirect using pandas read_csv & converting Date Object
# to DATETIME Format

df = pd.read_csv(direct+"/"+"Assignment 3"+"/"+"cricket_matches.csv" , usecols=[6,7,8,12,13,17,18])
df.head()


# In[8]:

sortdf = df.sort_values(['home'], ascending=True)
sortInn1 = sortdf[(sortdf['home'] == sortdf['winner']) & (sortdf['winner'] == sortdf['innings1'])]
sortInn2 = sortdf[(sortdf['home'] == sortdf['winner']) & (sortdf['winner'] == sortdf['innings2'])]
df1 = pd.DataFrame({'home': sortInn1['home'], 'Runs': sortInn1['innings1_runs']})
df2 = pd.DataFrame({'home': sortInn2['home'], 'Runs': sortInn2['innings2_runs']})


# In[9]:

runs = df1.append(df2, ignore_index=True)


# In[10]:

runsGroup = runs['Runs'].groupby(runs['home']).sum()
homeGroup = runs['Runs'].groupby(runs['home']).count()


# In[11]:

columns = ['Home', 'Score']
finalScore = pd.DataFrame({'Home' : homeGroup.index, 'Score' : runsGroup / homeGroup})

finalScore[columns].head(5)


# In[12]:

#function to check is directory exists
def funCheckDir(path):
    directory = os.path.dirname(path) # defining directory path
    if not os.path.exists(directory): # checking if directory already exists
        os.makedirs(directory) # making a directory
        
resultsPath = currentDirect+'\Assignment 3(Results)\Q3_Part_1.csv'
funCheckDir(resultsPath)

# Saving our dataFrame to csv file.
finalScore[columns].to_csv(resultsPath, index=False, encoding='utf-8')


# In[ ]:



