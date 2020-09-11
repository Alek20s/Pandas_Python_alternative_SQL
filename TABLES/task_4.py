# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 18:19:40 2020

@author: Aleks
"""
# Importing python moduls
import pandas as pd
import csv

#reading  the csv file, its header and its data
# and writing the data into python   two dimensial list
#  using python method 'append()'
f = open('who.csv')
reader = csv.reader(f)
header = next(reader)
print('Headers:', header)
data = []
for r in reader:
    data.append(r)
    
# Cleaning data - transferming strings and spaces  into integers
for i in range(0,len(data)):
    data[i][1] = int(data[i][1])
    data[i][5] = int(data[i][5])
    data[i][7] = int(data[i][7])
    
# replacing empty spaces and text in integer python type
# in the column 4 ('suicide_no')    
for i in range(0,len(data)):
    if data[i][4].isdigit() == True:
        data[i][4] = int(data[i][4])
    else:
        data[i][4] = 0
# replacing some strings in the same format
for i in range(0,len(data)):
    if data[i][3] == '5-14 years':
        data[i][3] = ' 5-14 years'

#  ADDING THE NEW COLUMN 
# using a method 'append()'
#data[i][4] is num of suicides, data[i][5] is population.        
for i in range(0,len(data)):
    data[i].append(data[i][4]*100000/data[i][5])
                  
df1= pd.DataFrame(data) # PANDAS DATA FRAME

# assigning column names
df1.columns= ['country', 'year','sex', 'age','suicide_no','pop', 'HDI', 'gdp_for_year','suicide_person']

# printing and checking the result.
print(df1)

# writing the results as a csv file.
df1.to_csv('task_4.csv')





