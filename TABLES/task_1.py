# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 12:35:50 2020

@author: Aleks
"""
# importing python moduls as formal procesures
import pandas as pd

#   reading the csv file
who= pd.read_csv("who_suicide_statistics_modified3.csv")

df1= pd.DataFrame(who) # PANDAS DATA FRAME

# making a list of all countries
for num, country in enumerate(df1['country'].unique(),1):
    print(num , country)

countries = pd.DataFrame(df1['country'].unique())

countries.columns=['country']  # assigning the column name

countries.to_csv('task_1.csv')   # writing data to a csv file
