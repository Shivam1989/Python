
# coding: utf-8

# In[2]:

#Import packages
import os
import pandas as pd



# In[3]:

# get current working directory
direct = os.getcwd()

# read csv file from location
df = pd.read_csv(direct+"/"+"Assignment 3/vehicle_collisions.csv", usecols=[0,3,19,20,21,22,23])
df.head()


# In[5]:

location = df[['UNIQUE KEY','BOROUGH']]
vehicle = df[['VEHICLE 1 TYPE','VEHICLE 2 TYPE','VEHICLE 3 TYPE','VEHICLE 4 TYPE','VEHICLE 5 TYPE']]
df_type = vehicle.notnull()
df_type = df_type.applymap(lambda x:1 if x else 0)
df_type = pd.concat([df_location, df_type], axis=1)
df_type.head()


# In[7]:

result = df_type.groupby(df_type['BOROUGH']).sum()


# In[13]:

columns = ['Borough', 'One_Vehicle_Involved', 'Two_Vehicle_Involved', 'Three_Vehicle_Involved', 'More_Vehicle_Involved']
finalResult = pd.DataFrame({'Borough' : result.index, 'One_Vehicle_Involved' : result['VEHICLE 1 TYPE']-result['VEHICLE 2 TYPE'], 
                           'Two_Vehicle_Involved' : result['VEHICLE 2 TYPE']-result['VEHICLE 3 TYPE'], 'Three_Vehicle_Involved' : result['VEHICLE 3 TYPE']-result['VEHICLE 4 TYPE'],
                           'More_Vehicle_Involved' : result['VEHICLE 4 TYPE'] })
finalResult[columns].head()


# In[14]:

#function to check is directory exists
def CheckDir(path):
    directory = os.path.dirname(path) # defining directory path
    if not os.path.exists(directory): # checking if directory already exists
        os.makedirs(directory) # making a directory
        
Path =direct+'\Q1_Part_2.csv'
CheckDir(resultsPath)

# Saving our dataFrame to csv file.
finalResult[columns].to_csv(Path, index=False, encoding='utf-8')


# In[ ]:



