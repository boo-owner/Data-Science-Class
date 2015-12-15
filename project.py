# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 13:35:18 2015
This python file:

Reads in excel data from edx
processes the data
analyzes the data

    @boo-owner
@author: arthurkolios
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
# read in the drinks data
mooc_cols = ['course_id', 'userid_di', 'registered', 'viewed', 'explored', 'certified', 'final_cc_cname_di', 'loe_di', 'yob', 'gender', 'grade', 'start_time_di', 
'last_event_di', 'nevents', 'ndays_act', 'nplay_video', 'nchapters', 'nforum_posts', 'roles', 'incomplete_flag']
mooc = 'HMXPC13_DI_v2_5-14-14.csv'
mooc_data = pd.read_csv(mooc, header=0, names=mooc_cols, na_values='NAN')

mooc_data.describe()

mooc_data.head()


#average grade for students with certificates
'''    
mooc_data[mooc_data.certified==1].grade.mean()
'''
# create age variable

mooc_data['yob'].dtype
mooc_data['new_yob']=mooc_data.yob.convert_objects(convert_numeric=True)

mooc_data['age'] = 2013 - mooc_data['new_yob']

# create time elapsed variable

mooc_data['nstart_time_di']=pd.to_datetime(mooc_data['start_time_di'])
mooc_data['nlast_event_di']=pd.to_datetime(mooc_data['last_event_di'])

mooc_data['time_elapse'] = mooc_data['nlast_event_di'] - mooc_data['nstart_time_di']

#create outcome category variable to enable groupby operations


pd.crosstab(mooc_data['viewed'], [mooc_data['explored'], mooc_data['certified']], margins = True)
weird = mooc_data[(mooc_data['viewed'] == 0) & (mooc_data['explored'] == 1) & (mooc_data['certified'] == 0)]
print weird

mooc_data['outcome']=''

mooc_data['outcome'][(mooc_data['viewed'] == 1) & (mooc_data['explored'] == 0) & (mooc_data['certified'] == 0)] = 1
mooc_data['outcome'][(mooc_data['viewed'] == 1) & (mooc_data['explored'] == 1) & (mooc_data['certified'] == 0)] = 2
mooc_data['outcome'][(mooc_data['viewed'] == 0) & (mooc_data['explored'] == 1) & (mooc_data['certified'] == 0)] = 2
mooc_data['outcome'][(mooc_data['viewed'] == 1) & (mooc_data['explored'] == 1) & (mooc_data['certified'] == 1)] = 3
mooc_data['outcome'][(mooc_data['viewed'] == 1) & (mooc_data['explored'] == 0) & (mooc_data['certified'] == 1)] = 3
mooc_data['outcome'][(mooc_data['viewed'] == 0) & (mooc_data['explored'] == 0) & (mooc_data['certified'] == 0)] = 0

counts = mooc_data['outcome'].value_counts(sort = False)  

# pie chart for outcomes

counts.plot(kind='pie', labels = ['registered only','viewed', 'explored', 'certified'], colors=['r', 'g', 'b', 'c'],
            title = 'Student Outcomes', autopct='%1.1f%%', shadow=True)

# describe sample
#box plot age

mooc_data['age'].plot(kind='box', title = 'Age distribution')
fig = plt.figure(1, figsize=(9, 6))

# Create an axes instance
ax = fig.add_subplot(111)

labels = ['registered only','viewed', 'explored', 'certified']
mooc_data.boxplot(column='age', by='outcome')


#calculate average age by outcome category

mooc_data[mooc_data.certified==1].age.mean()
mooc_data[mooc_data.viewed==1].age.mean()
mooc_data[mooc_data.explored==1].age.mean()
mooc_data[mooc_data.explored==0].age.mean()


#pie chart gender
#fill in missing values
import numpy as np
mooc_data.gender.replace('o', np.nan, inplace = True)
counts_gender = mooc_data.gender.value_counts(dropna=False)
counts_gender.plot(kind='pie', labels = ['Male', 'Female', 'Missing'], autopct='%1.1f%%', shadow=True, title = "Gender distribution")


#pie chart highest degree
counts_hdeg = mooc_data['loe_di'].value_counts(dropna=False).sort_index(1)

counts_hdeg.plot(kind='pie', autopct='%1.1f%%', shadow=True, title = 'Highest degree earned: Whole Sample')


counts_hdeg_out0 = mooc_data['loe_di'][mooc_data['outcome']==0].value_counts(dropna=False).sort_index(1)
counts_hdeg_out1 = mooc_data['loe_di'][mooc_data['outcome']==1].value_counts(dropna=False).sort_index(1)
counts_hdeg_out2 = mooc_data['loe_di'][mooc_data['outcome']==2].value_counts(dropna=False).sort_index(1)
counts_hdeg_out3 = mooc_data['loe_di'][mooc_data['outcome']==3].value_counts(dropna=False).sort_index(1)

counts_hdeg_out0.plot(kind='pie', autopct='%1.1f%%', shadow=True, title = 'Highest degree earned: registered only')

counts_hdeg_out1.plot(kind='pie', autopct='%1.1f%%', shadow=True, title = 'Highest degree earned: viewed')

counts_hdeg_out2.plot(kind='pie', autopct='%1.1f%%', shadow=True, title = 'Highest degree earned: explored')

counts_hdeg_out3.plot(kind='pie', autopct='%1.1f%%', shadow=True, title = 'Highest degree earned: certified')

test = mooc_data[:7]

for index, rows in test.iterrows():
    print rows['loe_di']

# look at courses
mooc_data.course_id.value_counts()   
cs50 = mooc_data[mooc_data.course_id == "HarvardX/CS50x/2012"]
# Look at class interaction variables
 #'start_time_di', 'last_event_di', 'nevents', 'ndays_act', 'nplay_video', 'nchapters', 'nforum_posts', 'roles', 'time_elapse',  

mooc_datac = DataFrame.copy(mooc_data)
active = mooc_datac[mooc_datac['outcome']!=0]
active.nevents[active.nevents>100000]=8000
active.describe
plt.xlabel("Total # of events")
active.nevents.plot(kind='hist' , bins = 120, title='histogram of # events')

active.nplay_video.plot(kind='hist' , bins = 120, title='density plot of # play video')

active.nchapters.plot(kind='hist' , title='density plot of # chapters')

active.nforum_posts.plot(kind='hist' , bins = 20, title='histogram of # forum posts')
mooc_data.index.values
active.index.values
active.dtypes
active.ix[9]
from pandas import DataFrame

from sklearn.cluster import KMeans

#all active classes
active['nevents'].fillna(0, inplace = True)

activec = DataFrame.copy(active)
neven = activec[(activec['nevents']>0)]


print pd.isnull(neven['nevents']).value_counts()
print pd.isnull(neven['ndays_act']).value_counts()
print pd.isnull(neven['nplay_video']).value_counts()
print pd.isnull(neven['nchapters']).value_counts()
print pd.isnull(neven['nforum_posts']).value_counts()

# remove outliers

neven['nplay_video'].describe()
neven.nplay_video.replace(98517, 65, inplace = True)

neven['nevents'].describe()
neven.nevents.replace(197757, 586, inplace = True)
#replace NaNs to 0s
neven['nplay_video'].fillna(0, inplace = True)
neven['nchapters'].fillna(0, inplace = True)
neven['nforum_posts'].fillna(0, inplace = True)

cs50 = neven[mooc_data.course_id == "HarvardX/CS50x/2012"]


# run model
feature_cols = ['nevents', 'ndays_act', 'nplay_video', 'nchapters', 'nforum_posts']
X = neven[feature_cols]
k_means = KMeans(n_clusters=3)
k_means.fit(X) 
labels = k_means.labels_
centroids = k_means.cluster_centers_
pd.value_counts(labels)
neven_pr = neven.copy()
neven_pr['Cluster Class'] = pd.Series(labels, index=neven.index)


#plot results

for i in range(k):
    # select only data observations with cluster label == i
    ds = neven_pr[]
    # plot the data observations
    pyplot.plot(ds[:,0],ds[:,1],'o')
pyplot.show()

r = neven_pr['Cluster Class']
fig = pylab.figure()
ax = Axes3D(fig)
x=neven_pr['nchapters']
y=neven_pr['nplay_video']
z=neven_pr['nforum_posts']

color = [str(item/255.) for item in r]
ax.scatter(x,y,z, c=color)
pyplot.show()

#run model on CS50 course dataset
cs50 = active[active.course_id == "HarvardX/CS50x/2012"]
#preprocessing
#replace NaNs to 0s

list = ['nevents', 'ndays_act', 'nplay_video', 'nchapters', 'nforum_posts']
for what in range(0,5):
    print cs50[list[what]].value_counts()

for what in range(0,3):
    print pd.isnull(cs50[list[what]]).value_counts()

for what in range(0,3):
    cs50[list[what]].fillna(0, inplace = True)
from sklearn import preprocessing

listz = ['znevents', 'zndays_act', 'znplay_video']
for what in range(0,3):
    cs50[listz[what]] = preprocessing.scale(cs50[list[what]])

feature_cols = ['znevents', 'zndays_act', 'znplay_video']
X = cs50[feature_cols]
k_means = KMeans(n_clusters=3)
k_means.fit(X) 
labels = k_means.labels_
centroids = k_means.cluster_centers_
pd.value_counts(labels)

cs50_pr = cs50.copy()
cs50_pr['Cluster Class_KM'] = pd.Series(labels, index=cs50.index)

ms = MeanShift()
ms.fit(X)
labels = ms.labels_
cluster_centers = ms.cluster_centers_
pd.value_counts(labels)

cs50_pr['Cluster Class_MS'] = pd.Series(labels, index=cs50.index)

#plot results

rkm = cs50_pr['Cluster Class_KM']
rms = cs50_pr['Cluster Class_MS']
x=cs50_pr['znevents']
y=cs50_pr['znplay_video']
z=cs50_pr['znchapters']

fig = pylab.figure()
ax = Axes3D(fig)
ax.scatter(x,y,z, c=rkm, cmap=plt.cm.Accent, title = 'Scatter Plot CS50 - Kmeans (3)')
pyplot.show()

fig = pylab.figure()
ax = Axes3D(fig)
ax.scatter(x,y,z, c=rms, cmap=plt.cm.Accent, title = 'Scatter Plot CS50 - Mean Shift')
pyplot.show()

#run model on Justice course dataset
justice = active[mooc_data.course_id == "HarvardX/ER22x/2013_Spring"]
#preprocessing
#replace NaNs to 0s

list = ['nevents', 'ndays_act', 'nplay_video', 'nchapters']

for what in range(0,4):
    print pd.isnull(justice[list[what]]).value_counts()

for what in range(0,4):
    justice[list[what]].fillna(0, inplace = True)
from sklearn import preprocessing

listz = ['znevents', 'zndays_act', 'znplay_video', 'znchapters']
for what in range(0,4):
    justice[listz[what]] = preprocessing.scale(justice[list[what]])

#scale data

feature_cols = ['znevents', 'zndays_act', 'znplay_video', 'znchapters']

X = justice[listz]

#kmeans
k_means = KMeans(n_clusters=3)
k_means.fit(X) 
labels = k_means.labels_
centroids = k_means.cluster_centers_
pd.value_counts(labels)
justice_pr = justice.copy()
justice_pr['Cluster Class_KM'] = pd.Series(labels, index=justice.index)
#plot results

r = justice_pr['Cluster Class_KM']
fig = pylab.figure()
ax = Axes3D(fig)
x=justice_pr['znevents']
y=justice_pr['znplay_video']
z=justice_pr['znchapters']

ax.scatter(x,y,z, c=r, cmap=plt.cm.Accent, title='Scatter Plot Justice Course - KMeans (3)')
pyplot.show()
#meanshift
ms = MeanShift()
ms.fit(X)
labels = ms.labels_
cluster_centers = ms.cluster_centers_

justice_pr = justice.copy()
justice_pr['Cluster Class_MS'] = pd.Series(labels, index=justice.index)

#plot results

r = justice_pr['Cluster Class']
fig = pylab.figure()
ax = Axes3D(fig)
x=justice_pr['znevents']
y=justice_pr['znplay_video']
z=justice_pr['znchapters']

ax.scatter(x,y,z, c=r, cmap=plt.cm.Accent, title='Scatter Plot Justice Course - Mean Shift')
pyplot.show()

#Prediction

