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
# calculating total number suicedes for bth males and females by year
suic_sex = df1.groupby(['year'],as_index=False)['suicide_no'].sum()
# selecting data only males
male= df1[df1['sex']== 'male']
#  grouping by year
suic_male = male.groupby(['year'],as_index=False)['suicide_no'].sum()
# selecting data only females
female= df1[df1['sex']== 'female']
#  grouping by yea
suic_female = female.groupby(['year'],as_index=False)['suicide_no'].sum()
# adding a new column 'male' and filling it
suic_sex['male']  = suic_male['suicide_no']
# adding a new column 'female' and filling it
suic_sex['female']  = suic_female['suicide_no']
# visualising data and checking it
print(suic_sex)

#  visualising data  via printing using matplotlib
plt.plot(suic_sex['year'], suic_sex['male'],   'b*',  markersize =12)
plt.plot(suic_sex['year'], suic_sex['female'],  'ro',  markersize =8)
plt.xlim((1980, 2020))
plt.ylim((0, 240000))
plt.title ('Number of Suicides',fontsize = 20 )
plt.xlabel ('Time, year', fontsize = 15)
plt.ylabel ('Suicides per year', fontsize =15)
plt.plot (suic_sex['year'], suic_sex['male'], label="Males") 
plt.plot (suic_sex['year'], suic_sex['female'], label="Females")             # plot
plt.legend(loc=1,    prop={'size': 15})
plt.grid(which='major')
plt.show()

# calculating ratio of suicides of males to females
suic_sex['ratio'] = suic_sex['male']/ suic_sex['female']
print(suic_sex)

# printing this ratio
plt.plot(suic_sex['year'], suic_sex['ratio'],  'g-',linewidth=4.0)
plt.xlim((1980, 2020))
plt.ylim((0, 6))
plt.title ('Ratio of suicides males via females',fontsize = 15)
plt.xlabel ('Time, year', fontsize = 18)
plt.ylabel ('Ratio, times', fontsize =18)
plt.grid(which='major')
plt.show()

#writing the data to a csv file
suic_sex.to_csv('task_11.csv')




