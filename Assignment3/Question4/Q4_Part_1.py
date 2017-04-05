
# coding: utf-8

# In[30]:

#Import packages
import os
import pandas as pd
import numpy as np
# Offsetting the warning
import warnings
warnings.filterwarnings('ignore')


# In[49]:

# Get current working directory
direct = os.getcwd()

# Read CSV file
df = pd.read_csv(direct+"/"+"Assignment 3/movies_awards.csv", usecols=[15])

df.head()


# In[50]:

# filtering the data frame for which awards is N/A
dfMovies = df.dropna()

dfMovies.head()


# In[51]:

# spliiting data and creating columns 
dfMovies['Awards Wins'] = dfMovies['Awards'].str.extract('(\d+ win)', expand=True)
dfMovies['Awards Nominated'] = dfMovies['Awards'].str.extract('(\d+ nomination)', expand=True)
dfMovies['Primetime Emmys Wins'] = dfMovies['Awards'].str.extract('(Won \d+ Primetime Emmy)', expand=True)
dfMovies['Primetime Emmys Nominations'] = dfMovies['Awards'].str.extract('(Nominated for \d+ Primetime Emmy)', expand=True)
dfMovies['Oscar Nominations'] = dfMovies['Awards'].str.extract('(Nominated for \d+ Oscar)', expand=True)
dfMovies['Oscar Wins'] = dfMovies['Awards'].str.extract('(Won \d+ Oscar)', expand=True)
dfMovies['Golden Globe Nominations'] = dfMovies['Awards'].str.extract('(Nominated for \d+ Golden Globe)', expand=True)
dfMovies['Golden Globe Wins'] = dfMovies['Awards'].str.extract('(Won \d+ Golden Globe)', expand=True)
dfMovies['BAFTA Nominations'] = dfMovies['Awards'].str.extract('(Nominated for \d+ BAFTA)', expand=True)
dfMovies['BAFTA Wins'] = dfMovies['Awards'].str.extract('(Won \d+ BAFTA)', expand=True)


# In[52]:

#taking integers from the split strings
dfMovies['Awards Wins'] = dfMovies['Awards Wins'].str.extract('(\d+)')
dfMovies['Awards Nominated'] = dfMovies['Awards Nominated'].str.extract('(\d+)')
dfMovies['Oscar Nominations'] = dfMovies['Oscar Nominations'].str.extract('(\d+)')
dfMovies['Oscar Wins'] = dfMovies['Oscar Wins'].str.extract('(\d+)')
dfMovies['Primetime Emmys Nominations'] = dfMovies['Primetime Emmys Nominations'].str.extract('(\d+)')
dfMovies['Primetime Emmys Wins'] = dfMovies['Primetime Emmys Wins'].str.extract('(\d+)')
dfMovies['Golden Globe Nominations'] = dfMovies['Golden Globe Nominations'].str.extract('(\d+)')
dfMovies['Golden Globe Wins'] = dfMovies['Golden Globe Wins'].str.extract('(\d+)')
dfMovies['BAFTA Nominations'] = dfMovies['BAFTA Nominations'].str.extract('(\d+)')
dfMovies['BAFTA Wins'] = dfMovies['BAFTA Wins'].str.extract('(\d+)')


# In[53]:

#filling NaN with 0
dfMovies['Awards Wins'] = dfMovies['Awards Wins'].fillna(0)
dfMovies['Awards Nominated'] = dfMovies['Awards Nominated'].fillna(0)
dfMovies['Primetime Emmys Nominations'] = dfMovies['Primetime Emmys Nominations'].fillna(0)
dfMovies['Primetime Emmys Wins'] = dfMovies['Primetime Emmys Wins'].fillna(0)
dfMovies['Oscar Nominations'] = dfMovies['Oscar Nominations'].fillna(0)
dfMovies['Oscar Wins'] = dfMovies['Oscar Wins'].fillna(0)
dfMovies['Golden Globe Nominations'] = dfMovies['Golden Globe Nominations'].fillna(0)
dfMovies['Golden Globe Wins'] = dfMovies['Golden Globe Wins'].fillna(0)
dfMovies['BAFTA Nominations'] = dfMovies['BAFTA Nominations'].fillna(0)
dfMovies['BAFTA Wins'] = dfMovies['BAFTA Wins'].fillna(0)


# In[54]:

#converting the data-type from string to int
dfMovies['Awards Nominated'] = dfMovies['Awards Nominated'].astype(int)
dfMovies['Awards Wins'] = dfMovies['Awards Wins'].astype(int)
dfMovies['Oscar Nominations'] = dfMovies['Oscar Nominations'].astype(int)
dfMovies['Oscar Wins'] = dfMovies['Oscar Wins'].astype(int)
dfMovies['Primetime Emmys Nominations'] = dfMovies['Primetime Emmys Nominations'].astype(int)
dfMovies['Primetime Emmys Wins'] = dfMovies['Primetime Emmys Wins'].astype(int)
dfMovies['Golden Globe Nominations'] = dfMovies['Golden Globe Nominations'].astype(int)
dfMovies['Golden Globe Wins'] = dfMovies['Golden Globe Wins'].astype(int)
dfMovies['BAFTA Nominations'] = dfMovies['BAFTA Nominations'].astype(int)
dfMovies['BAFTA Wins'] = dfMovies['BAFTA Wins'].astype(int)


# In[55]:

#calculating total number of nominations and awards
dfMovies['Awards Nominated'] = dfMovies['Awards Nominated'] + dfMovies['Oscar Nominations'] + dfMovies['Primetime Emmys Nominations'] + dfMovies['Golden Globe Nominations'] + dfMovies['BAFTA Nominations']
dfMovies['Awards Wins'] = dfMovies['Awards Wins'] + dfMovies['Oscar Wins'] + dfMovies['Primetime Emmys Wins'] + dfMovies['Golden Globe Wins'] + dfMovies['BAFTA Wins']


# In[56]:

#columns to be printed on the console
columns = ['Awards','Awards Nominations','Awards Wins','Oscar Nominations','Oscar Wins','Primetime Emmys Nominations','Primetime Emmys Wins','Golden Globe Nominations','Golden Globe Wins','BAFTA Nominations','BAFTA Wins']


# In[58]:

dfMovies.head()


# In[59]:

dfMovies.to_csv(direct+'\Q4_Part_1.csv',index = False, sep=',')


# In[ ]:



