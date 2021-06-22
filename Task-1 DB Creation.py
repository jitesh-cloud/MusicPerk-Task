#!/usr/bin/env python
# coding: utf-8

# In[7]:


# Database Creation
# Importing libraries pandas and sqlalchemy
# Sqlalchemy - gives power and flexibility of SQL
import pandas as pd
from sqlalchemy import create_engine

# Creation of dataframe and accessing excel file
df = pd.read_excel('D:\\FreeCodeCamp\\Python Projects\\Internshala_Tasks\\MusicPerk_Tasks\\HINDALCO_1D.xlsx')

# Operating SQL and storing into database
engine = create_engine('mysql://root:@localhost/hindalco')

# dataframe's data stored into mysql server
df.to_sql('hindalco', con=engine)


# In[ ]:




