# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 18:19:40 2020

@author: Aleks
"""
# importing python models as a formal procedure
import pandas as pd
import csv

#opening and downloading the csv file into python code
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
    
# replacing empty soaces and text by 0. 
# 4 is the column "suicside_no   
    
for i in range(0,len(data)):
    if data[i][4].isdigit() == True:
        data[i][4] = int(data[i][4])
    else:
        data[i][4] = 0
        
# replacing the string '5-14 years' into '_5-14 years'
for i in range(0,len(data)):
    if data[i][3] == '5-14 years':
        data[i][3] = ' 5-14 years'
                
df1= pd.DataFrame(data) # PANDAS DATA FRAME

# assigning columns names
df1.columns= ['country', 'year','sex', 'age','suicide_no','pop', 'HDI', 'gdp_for_year']

print(df1)

# writing data to a csv file
df1.to_csv('task_3.csv')


