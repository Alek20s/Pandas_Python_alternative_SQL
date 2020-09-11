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
            

"""
#########################################################################
TASK 10
"""

df1= pd.DataFrame(data) # PANDAS DATA FRAME

df1.columns= ['country', 'year','sex', 'age','suicide_no','pop', 'HDI', 'gdp_for_year','suicide_person','gen', 'continent']
# groupby and sumup for totla suicide numbers over years
suic_year = df1.groupby(['year'],as_index=False)['pop','suicide_no'].sum()
print(suic_year)

#plotting the total numbers  over years
plt.plot(suic_year['year'],suic_year['suicide_no'],  'ro', markersize =8)
plt.xlim((1980, 2020))
plt.ylim((0, 250000))

plt.title ('Total suicide number over years',fontsize = 16 )
plt.xlabel ('Time, year', fontsize = 15)
plt.ylabel ('suicide numbers', fontsize =12)
plt.show()

#calculating total population by year
country_pop = df1.groupby(['year','country' ],as_index=False)['pop'].sum()
year_pop = country_pop.groupby(['year' ],as_index=False)['pop'].sum()

# calculating suicide per 100K of population over years.
suic_year['suicide_per_100k'] = suic_year['suicide_no']*100000/year_pop['pop']

# plotting results
plt.plot(suic_year['year'], suic_year['suicide_per_100k'],  'g^',  markersize =8)
plt.xlim((1980, 2020))
plt.ylim((0, 15))
plt.title ('Suicide numbers per 100K',fontsize = 20 )
plt.xlabel ('Time, year', fontsize = 15)
plt.ylabel ('Suicide per 100K', fontsize =15)
plt.show()

suic_year.to_csv('task_10.csv')
