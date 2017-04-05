
# coding: utf-8

# In[1]:

#Importing Packages
import os
import pandas as pd


# In[3]:

# get current working directory
direct = os.getcwd()

# read csv file from location
df = pd.read_csv(direct+"/"+"Assignment 3/vehicle_collisions.csv", parse_dates=['DATE'], usecols=[0,1,3])
df.head()


# In[8]:

# Offsetting the warning
pd.options.mode.chained_assignment = None
# Now task is to filter all date for the year 2016
Year = df[df.DATE.dt.year == 2016]


# In[14]:

Year['Month'] = Year['DATE'].dt.strftime('%b')
NY = Year['UNIQUE KEY'].groupby(Year['Month']).count()


# In[17]:

NY.index = pd.CategoricalIndex(NY.index, 
                               categories=['Jan', 'Feb', 'Mar', 'Apr','May','Jun', 'Jul', 'Aug','Sep', 'Oct', 'Nov', 'Dec'], 
                               sorted=True)
NY = NY.sort_index()
Manhattan = Year['UNIQUE KEY'][Year['BOROUGH'] == "MANHATTAN"].groupby(Year['Month']).count()
Manhattan.index = pd.CategoricalIndex(Manhattan.index, 
                               categories=['Jan', 'Feb', 'Mar', 'Apr','May','Jun', 'Jul', 'Aug','Sep', 'Oct', 'Nov', 'Dec'], 
                               sorted=True)
Manhattan = Manhattan.sort_index()


# In[19]:

# Create new Data frame 
Columns = ["Month", "Manhattan", "NYC", "Percentage"]
dataFrame = pd.DataFrame({'Month' : NYC.index, 'Manhattan' : Manhattan, 'NYC' : NYC, 'Percentage' : Manhattan / NYC})



# In[21]:

def CheckDir(path):
    # defining directory path
    directory = os.path.dirname(path)
    # checking if directory already exists
    if not os.path.exists(directory):
        # making a directory
        os.makedirs(directory) 
        
Path = direct+'\Q1_Part_1.csv'
CheckDir(Path)

# Saving our dataFrame to csv file.
dataFrame[Columns].to_csv(Path, index=False, encoding='utf-8')


# In[ ]:



