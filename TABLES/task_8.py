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

# summing up by continent
cont = df1.groupby(['continent'])['suicide_no'].sum()

# plotting the result
cont.plot(kind= 'pie', subplots= True,  figsize = (10, 5), autopct='%1.1f%%')
cont.plot.pie(title="Suicides by continent")
plt.show()

#  adding the column ' suicide_no'
cont.columns = ['suicide_no']
print(cont)

# writing the result to a csv file
cont.to_csv('task_8.csv')


  
