# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 19:31:31 2021

@author: Ammad
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np

file = r'D:\Freelancing\24-10-21 (Business Analytics\Set 2.xlsx'


# =============================================================================
# 1st Sheet
# =============================================================================
df1 = pd.read_excel(file, sheet_name= "Nielsen - Total US" ,header = 1)

xpoints = df1['Distribution As Of Date:']
ypoints = df1['Jim Beam Honey']
zpoints = df1['Jack Daniels Honey']
wpoints = df1['Wild Turkey Honey']

figure(figsize = (10, 8))

plt.plot(xpoints, ypoints, color = 'green' )
plt.plot(xpoints, zpoints, color = 'orange')
plt.plot(xpoints, wpoints, color = 'red')

plt.xticks(xpoints, rotation = 45)
plt.locator_params(axis='x', nbins=10)

plt.ylabel('% of Stores with Each Brand')

plt.legend(["Jim Beam Honey", "Jack Daniels Honey", 'Wild Turkey Honey'])
plt.show()


# =============================================================================
# 2nd Sheet
# =============================================================================

df1 = pd.read_excel(file, sheet_name= "Nielsen - By Market",header = 2)

xpoints = df1['Market'][0:12]
ypoints = df1['Jim Beam Honey'][0:12]
zpoints = df1['Jack Daniels Honey'][0:12]
wpoints = df1['Wild Turkey Honey'][0:12]

x = np.arange(len(xpoints))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots(figsize = (20,15))
rects1 = ax.bar(x - width/2, ypoints, width, label='Jim Beam Honey', color = 'lightcoral')
rects2 = ax.bar(x + width/2, zpoints, width, label='Jack Daniels Honey', color = 'yellowgreen')
rects3 = ax.bar(x + width/2, wpoints, width, label='Wild Turkey Honey', color = 'lightskyblue')

ax.set_ylabel('% of Stores with Each Brand')
ax.set_xticks(x)
ax.set_xticklabels(xpoints)
ax.legend()

ax.bar_label(rects1, padding=3, fontsize=7.5)
ax.bar_label(rects2, padding=3, fontsize=7.5)
ax.bar_label(rects3, padding=3, fontsize=7.5)

fig.tight_layout()
plt.show()

xpoints = df1['Market'][12:]
ypoints = df1['Jim Beam Honey'][12:]
zpoints = df1['Jack Daniels Honey'][12:]
wpoints = df1['Wild Turkey Honey'][12:]

x = np.arange(len(xpoints))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots(figsize = (20,15))
rects1 = ax.bar(x - width/2, ypoints, width, label='Jim Beam Honey', color = 'lightcoral')
rects2 = ax.bar(x + width/2, zpoints, width, label='Jack Daniels Honey', color = 'yellowgreen')
rects3 = ax.bar(x + width/2, wpoints, width, label='Wild Turkey Honey', color = 'lightskyblue')

ax.set_ylabel('% of Stores with Each Brand')
ax.set_xticks(x)
ax.set_xticklabels(xpoints)
ax.legend()

ax.bar_label(rects1, padding=3, fontsize=7.5)
ax.bar_label(rects2, padding=3, fontsize=7.5)
ax.bar_label(rects3, padding=3, fontsize=7.5)

fig.tight_layout()
plt.show()


# =============================================================================
# 4th Sheet
# =============================================================================

df4 = pd.read_excel(file, sheet_name= "Illinois Store List", header = 5)

df4.head()

offPremise = df4[df4['Premise Type'] == 'Off Premise']
onPremise = df4[df4['Premise Type'] == 'On Premise']


# ACCOUNTS GROWTH
accounts = ['Jim Beam Honey Volume', 'Jim Beam White Label Volume', 'Knob Creek Volume',
            "Maker's Mark Volume", 'Pinnacle Original Volume', 'Pinnacle Whipped Volume']

cumsumTotalAccounts = []
for account in accounts:
    maxValue = df4[account].cumsum().max()
    cumsumTotalAccounts.append(maxValue)

colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'pink', 'orange']

fig, ax = plt.subplots(figsize=(10,10))

x = np.arange(len(accounts))  # the label locations
rects1 = ax.bar(x - 0.3/2, cumsumTotalAccounts, color=colors)
ax.set_ylabel('Cumulative Sum of Accounts')
ax.set_title('Accounts Growth Based on Volume')
ax.set_xticks(x)
ax.set_xticklabels(accounts)
ax.bar_label(rects1, padding=3)
plt.xticks(rotation = 45, fontsize = 13)
fig.tight_layout()
plt.show()




# OFF CHANNEL GROWTH
channelOffPremise = np.unique(np.asarray(offPremise['Store Channel'])).tolist()
channelOffPremise = ['Large Format Liquor', 'Other Off-Premise',
                     'Grocery, Mass Merchandised, Club & Drug', 'Small Format, Convenience, Urban']

cumsumTotalValueOff = []
for channel in channelOffPremise:
    maxValue = offPremise[offPremise['Store Channel'] == channel]['Total Volume'].cumsum().max()
    cumsumTotalValueOff.append(maxValue)

channelOffPremise = ['Large Format Liquor\n', 'Other Off-Premise\n',
                     '\nGrocery, Mass \nMerchandised, Club & Drug', '\nSmall Format, Convenience, Urban']

colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
fig1, ax1 = plt.subplots()
ax1.pie(cumsumTotalValueOff, colors = colors, labels=channelOffPremise, autopct='%1.1f%%', startangle=90,
        textprops={'fontsize':12}, pctdistance = 0.85, labeldistance = 1.2)
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
ax1.axis('equal')  
plt.title('Off-Premise Channels Growth Based on Total Volume\n',fontsize=15)
plt.tight_layout()
plt.show()


# ON CHANNEL GROWTH
channelOnPremise = np.unique(np.asarray(onPremise['Store Channel'])).tolist()
channelOnPremise = ['Casual Bar & Dining', 'Other On-Premise','Luxury Accounts']

cumsumTotalValueOn = []
for channel in channelOnPremise:
    maxValue = onPremise[onPremise['Store Channel'] == channel]['Total Volume'].cumsum().max()
    cumsumTotalValueOn.append(maxValue)
    
fig1, ax1 = plt.subplots()
ax1.pie(cumsumTotalValueOn, colors = colors, labels=channelOnPremise, autopct='%1.1f%%', startangle=90,
        textprops={'fontsize':12}, pctdistance = 0.85, labeldistance = 1.05)
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.title('On-Premise Channels Growth Based on Total Volume\n',fontsize=15)
ax1.axis('equal')  
plt.tight_layout()
plt.show()
