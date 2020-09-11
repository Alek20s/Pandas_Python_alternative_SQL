# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 18:19:40 2020

@author: Aleks
"""
import pandas as pd
import csv

f = open('who.csv')
reader = csv.reader(f)
header = next(reader)
print('Headers:', header)
data = []
for r in reader:
    data.append(r)


f1 = open('generation.csv')
reader = csv.reader(f1)
header = next(reader)
print('Headers:', header)
gen = []
for q in reader:
    gen.append(q)
    
    
f3 = open('continent_mapping.csv')
reader = csv.reader(f3)
header = next(reader)
print('Headers:', header)
continents = []
for q in reader:
    continents.append(q)
    
    
# Cleaning data - transferming strings and spaces  into integers
for i in range(0,len(data)):
    data[i][1] = int(data[i][1])
    data[i][5] = int(data[i][5])
    data[i][7] = int(data[i][7])
    
for i in range(0,len(data)):
    if data[i][4].isdigit() == True:
        data[i][4] = int(data[i][4])
    else:
        data[i][4] = 0

for i in range(0,len(data)):
    if data[i][3] == '5-14 years':
        data[i][3] = '05-14 years'
        
for i in range(0,len(data)):
    data[i].append(data[i][4]*100000/data[i][5])
    
for i in range(0,len(data)):
    for n in range(0, len(gen)):         
        dob = data[i][1] - int(data[i][3][0:2])
        if  (dob >= int(gen[n][1]) and dob <=int(gen[n][2])):    
            data[i].append(gen[n][0])
            
########################################################### 
          
for i in range(0,len(data)):
    for n in range(0, len(continents)):         
        if  data[i][0] == continents[n][0]:    
            data[i].append(continents[n][1])
            
############################################################

df1= pd.DataFrame(data) # PANDAS DATA FRAME

df1.columns= ['country', 'year','sex', 'age','suicide_no','population', 'HDI', 'gdp_for_year','suicide_person','gen', 'continent']
 
 ##################################################################     
"""
TASK_6
"""
# Just selecting a year, for example year = 2002   
year= 2002
year = df1[df1['year']== year]


# pop is for calculating population and suicide number for the year,
pop= year.groupby(['country'],as_index=False)['suicide_no','population'].sum()

# gdp is for finding a mean gdp_per_year for each year
gdp =year.groupby(['country'],as_index=False)['gdp_for_year'].mean()

#creating a new database which has the same dimension as pop and gdp
table =pd.DataFrame(pop)

# adding a new collumn 'gdp_for_year, $' and filling this column
table['gdp_for_year, $'] = gdp['gdp_for_year']

# adding a new column 'gdp_per_capita_per_year,$' and filling it.
table['gdp_per_capita_per_year,$'] = gdp['gdp_for_year']/pop['population']

#sorting data according 'gdp_per_capita' or a required parametor.
table.sort_values(by = ['gdp_for_year, $'])

# printing data and writing to a csv file
print(table)
table.to_csv('task_6.csv')






