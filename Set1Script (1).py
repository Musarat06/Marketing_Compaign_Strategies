# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 00:19:59 2021
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np
from matplotlib import cm

file = r'D:\Freelancing\Pure_Data_Science\USA_business_stat\Set 1.xlsx'

df = pd.read_excel(file)

# =============================================================================
# Splitting the time into more columns to get more detailed insights and Cleaning the data
# =============================================================================
dayList = []
for i, row in df.iterrows():
    dayList.append(row['funded date'].split(',')[0])    
df['funded date - day'] = dayList

dateList = []
for i, row in df.iterrows():
    dateList.append(row['funded date'][5:7])
df['funded date - date'] = dateList

monthList = []
for i, row in df.iterrows():
    monthList.append(row['funded date'][8:11])
df['funded date - month'] = monthList

timeList = []
for i, row in df.iterrows():
    timeList.append(row['funded date'][17:19])
df['funded date - time'] = timeList

df.category[df.category== 'Film &amp; Video']  = 'Film & Video'

# Project Statuses Overview
successfulProjects = df[df['status'] == 'successful']
cancelledProjects = df[df['status'] == 'cancelled']
failedProjects = df[df['status'] == 'failed']
liveProjects = df[df['status'] == 'live']
suspendedProjects = df[df['status'] == 'suspended']

labels = ['Successful', 'Live', 'Cancelled', 'Failed', 'Suspended']
values = np.array([len(successfulProjects), len(liveProjects), len(cancelledProjects), len(failedProjects), 
                   len(suspendedProjects)])

colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'pink', 'orange']

plt.pie(values,labels=labels,autopct='%1.1f%%',startangle=90, colors = colors, pctdistance=0.8,
        textprops={'fontsize': 13})
plt.legend(loc='upper right', prop={'size': 9})
plt.axis('equal')
plt.tight_layout()
plt.title('Project Statuses Overview\n')
plt.show()


# Idealnesss in Months

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

cumsumMonthMaxValues = []
for month in months:
    maxValue = df[df['funded date - month'] == month]['funded percentage'].cumsum().max()
    cumsumMonthMaxValues.append(maxValue)
    
colors = cm.inferno_r(np.linspace(.85, .2, 12))
fig, ax = plt.subplots(figsize=(8,6))
plt.barh(months, cumsumMonthMaxValues, align='center', color=colors)
plt.xlabel('Funded Percentage')
plt.ylabel('Funded Month')
plt.title('Percentage Funding for Different Months')


# Idealnesss in Date

dates = np.asarray(np.unique(dateList)).tolist()

cumsumMaxValuesDates = []
for date in dates:
    maxValue = df[df['funded date - date'] == date]['funded percentage'].cumsum().max()
    cumsumMaxValuesDates.append(maxValue)
      
colors = cm.inferno_r(np.linspace(.2, .85, 31))
fig, ax = plt.subplots(figsize=(9,6))
plt.barh(dates, cumsumMaxValuesDates, align='center', color=colors)
plt.xlabel('Funded Percentage')
plt.ylabel('Funded Dates')
plt.title('Percentage Funding for Different Dates During a Month')


# Check successfulness in Days

days = np.asarray(np.unique(dayList)).tolist()

cumsumMaxValuesDays = []
for day in days:
    maxValue = df[df['funded date - day'] == day]['funded percentage'].cumsum().max()
    cumsumMaxValuesDays.append(maxValue)
    
colors = cm.inferno_r(np.linspace(.2, .85, 7))
fig, ax = plt.subplots(figsize=(9,4))
plt.barh(days, cumsumMaxValuesDays, align='center', color=colors)
plt.xlabel('Funded Percentage')
plt.ylabel('Funded Days')
plt.title('Percentage Funding for Different Days')


# Check successfulness in Time

times = np.asarray(np.unique(timeList)).tolist()

cumsumMaxValuesTimes = []
for time in times:
    maxValue = df[df['funded date - time'] == time]['funded percentage'].cumsum().max()
    cumsumMaxValuesTimes.append(maxValue)
    
colors = cm.inferno_r(np.linspace(.85, .2, 12))
fig, ax = plt.subplots(figsize=(12,6))
plt.barh(times, cumsumMaxValuesTimes, align='center', color=colors)
plt.xlabel('Funded Percentage')
plt.ylabel('Funded Timings')
plt.title('Percentage Funding for Different Times in a Day')



# =============================================================================
# What type of projects would be most successful at getting funded
# =============================================================================

categories = np.unique(np.asarray(df['category'])).tolist()

highestFundedPercentCategory = []

for category in categories:
    maxValue = df[df['category'] == category]['funded percentage'].cumsum().max()
    highestFundedPercentCategory.append(maxValue)
    
colors = cm.copper(np.linspace(.95, .2, 13))
fig, ax = plt.subplots(figsize=(8,6))
plt.xlabel('Funded Percentage')
plt.ylabel('Categories')
plt.title('Percentage Funding for Different Categories')
plt.barh(categories, highestFundedPercentCategory, align='center', color=colors)




