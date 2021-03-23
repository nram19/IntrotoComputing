
list = [2,4,6,8,4,5,2,1,9,0,4,6,7,4,3,2,1,9,10,3,7,9,6,0,1,3,5,6,7,8,9,10,2,3,6,8,9,10,6,7,4,3]


freq = {}
for i in list:
    freq[i] = list.count(i)
print(freq)


import matplotlib
import matplotlib.pyplot as plt
import numpy as np

x = freq.keys()
y = freq.values()
plt.title("List Element Frequencies")
plt.xlabel("Element")
plt.ylabel("Frequency")

plt.bar(x,y, color = "green", width = 0.5)
plt.show


import json

with open("./freq.json", "w") as out:
    json.dump(freq, out)

f = open("freq.json", "r")
f.read()





import pandas as pd
import numpy as np

df = pd.read_csv('MidtermDS.csv')
df.shape




#See first 5 rows
df.head()




#Drop unnecessary columns
df = df.drop(['Profile Name', 'Attributes', 'Supplemental Video Type', 'Device Type', 'Bookmark',//
              'Latest Bookmark','Country'], axis = 1)

#See data types
df.dtypes



#Check new data
df.head(1)




#Convert Data Types
df['Start Time'] = pd.to_datetime(df['Start Time'], utc = True)
df.dtypes



#Change Start Time column  to dataframe index
df = df.set_index('Start Time')



#Convert from UTC to EST
df.index = df.index.tz_convert('US/Eastern')
#Reset index
df = df.reset_index()

df.head(1)




df['Duration'] = pd.to_timedelta(df['Duration'])
df.dtypes


#Analyzing the data, we see that The Office and Star Trek 
#have been watched the most, so now will create new dataframes
#filtering these two shows so we can coompare

office = df[df['Title'].str.contains('The Office (U.S.)', regex=False)]

startrek = df[df['Title'].str.contains('Star Trek: Deep Space Nine', regex=False)]



#Analyzing the Start Time, we see all data comes from one month
df.shape




df.loc[0]




df.loc[199]




#To compare amount of time spent on The Office vs. Star Trek, convert timedelta
office_days_dur = office['Duration'].sum()
print(office_days_dur)



#Convert to hours
office_hours = 24 + 15
print(office_hours)




#Same for Star Trek
st_days_dur = startrek['Duration'].sum()
print(st_days_dur)

#Convert to hours
st_hours = 20 + (2/60)
print(st_hours)


#Graphical Comparison of total time spent watching:

#Calculate Percentages
z = office_hours + st_hours
a = office_hours / z
b = st_hours / z

import matplotlib.pyplot as plt
import numpy as np

c = np.array([a, b])
mylabels = ["The Office", "Star Trek"]

plt.title("Time Spent Watching The Office vs. Star Trek in a Month")
plt.pie(c, labels = mylabels)
plt.show()



#Graphical Comparison of Days of the Week Spent Watching

#Divide data further
office['weekday'] = office['Start Time'].dt.weekday
startrek['weekday'] = startrek['Start Time'].dt.weekday


#Set order so days from Mon-Sun
office['weekday'] = pd.Categorical(office['weekday'], categories=[0,1,2,3,4,5,6], ordered=True)
office_by_day = office['weekday'].value_counts()
office_by_day= office_by_day.sort_index()

#Same for Star Trek
startrek['weekday'] = pd.Categorical(startrek['weekday'], categories=[0,1,2,3,4,5,6], ordered=True)
st_by_day = startrek['weekday'].value_counts()
st_by_day= st_by_day.sort_index()

#Display Multiple Plots using subplots
matplotlib.rcParams.update({'font.size': 22})
#Plot 1: The Office
plt.subplot(1, 2, 1)
plt.xlabel("Day")
plt.ylabel("# of Episodes")
office_by_day.plot(kind='bar', figsize=(20,10), title = 'Office Episodes Watched by Day', color = "blue")

#Plot 2: Star Trek
plt.subplot(1, 2, 2)
plt.xlabel("Day")
plt.ylabel("# of Episodes")
st_by_day.plot(kind = 'bar', figsize = (20, 10), title = 'Star Trek Episodes Watched by Day', color = "orange")

plt.suptitle("Comparing Shows by Day Watched")
plt.show()




