# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 18:19:40 2020

@author: Aleks
"""
#Importing python moduls
import pandas as pd
import csv

# downloaded csv  the file in python code
f = open('who.csv')
reader = csv.reader(f)
header = next(reader)
print('Headers:', header)
data = []
for r in reader:
    data.append(r)

# downloaded data from generation.csv file in python code.
f1 = open('generation.csv')
reader = csv.reader(f1)
header = next(reader)
print('Headers:', header)
gen = []
for q in reader:
    gen.append(q)
   
# Cleaning data - transferming strings and spaces  into integers
for i in range(0,len(data)):
    data[i][1] = int(data[i][1])
    data[i][5] = int(data[i][5])
    data[i][7] = int(data[i][7])
    
# replacing strings, empty spaces and text by  0 and integers    
for i in range(0,len(data)):
    if data[i][4].isdigit() == True:
        data[i][4] = int(data[i][4])
    else:
        data[i][4] = 0

for i in range(0,len(data)):
    if data[i][3] == '5-14 years':
        data[i][3] = '05-14 years'

# adding a new column and filling data 'suicide_person'       
for i in range(0,len(data)):
    data[i].append(data[i][4]*100000/data[i][5])

#  creating a new column "generation" and filling data,
# dob is just additional variable, when a person was born
# append is python method
#gen is data fro generation.csv file    
for i in range(0,len(data)):
    for n in range(0, len(gen)):         
        dob = data[i][1] - int(data[i][3][0:2])
        if  (dob >= int(gen[n][1]) and dob <=int(gen[n][2])):    
            data[i].append(gen[n][0])
            
df1= pd.DataFrame(data) # PANDAS DATA FRAME

# names of columns
df1.columns= ['country', 'year','sex', 'age','suicide_no','pop', 'HDI', 'gdp_for_year','suicide_person','generation']

print(df1)    # printing and checking data      
    
df1.to_csv('task_5.csv') # writing result to  a csv file
    