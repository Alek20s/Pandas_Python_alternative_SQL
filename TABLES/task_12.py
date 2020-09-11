# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 18:19:40 2020

@author: Aleks
"""
import pandas as pd
import csv
import matplotlib.pyplot as plt

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
            
          
for i in range(0,len(data)):
    for n in range(0, len(continents)):         
        if  data[i][0] == continents[n][0]:    
            data[i].append(continents[n][1])
            
############################################################

"""
TASK 8
"""

df1= pd.DataFrame(data) # PANDAS DATA FRAME

df1.columns= ['country', 'year','sex', 'age','suicide_no','pop', 'HDI', 'gdp_for_year','suicide_person','gen', 'continent']

# grouping by  a generation  to sort on an age group
sort_a= df1.groupby(['age'], as_index=False)['suicide_no'].sum()
print(sort_a)

# plotting and visualising the results
plt.bar(sort_a['age'], sort_a['suicide_no'], color='red')
plt.setp(plt.gca().get_xticklabels(), rotation= 60, horizontalalignment='right')
plt.xlabel("Age group", fontsize = 16)
plt.ylabel("Number of  suicides", fontsize = 15)
plt.title("Number of Suicides on age group  for all generations.", fontsize = 12)
plt.grid(which='major')
plt.show()

# writing the result to a csv file
sort_a.to_csv('task_12_a.csv')

# grouping by age group  to sort on a generation
sort_a= df1.groupby(['gen'], as_index=False)['suicide_no'].sum()

# plotting and visualising the results
plt.bar(sort_a['gen'], sort_a['suicide_no'], color='green')
plt.setp(plt.gca().get_xticklabels(), rotation= 60, horizontalalignment='right')
plt.xlabel("Generation", fontsize = 16)
plt.ylabel("Number of  suicides", fontsize = 15)
plt.title("Number of suicides on generation  for all ages.", fontsize = 13)
plt.grid(which='major')
plt.show()

# writing the result to a csv file
sort_a.to_csv('task_12_g.csv')

# calculating on visualisng on generation and age group
sort_1= df1.groupby(['gen', 'age'], as_index= True)['suicide_no'].sum()
sort_1.to_csv('task_12_1.csv')
print(sort_1)

# Sorting in a different order- on visualisng on age and then
# generation
sort_2= df1.groupby([ 'age','gen'], as_index= True)['suicide_no'].sum()
sort_2.to_csv('task_12_2.csv')
print(sort_2)

# finding age group and generation commited suicides the most.
sort_max = df1.groupby([ 'gen','age'], as_index= False)['suicide_no'].sum()
maks = sort_max.sort_values(by=['suicide_no'])
print(maks)
maks.to_csv('task_12_3.csv')