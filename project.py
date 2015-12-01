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
import pandas as pd
import matplotlib.pyplot as plt

# read in the drinks data
mooc_cols = ['course_id', 'userid_di', 'registered', 'viewed', 'explored', 'certified', 'final_cc_cname_di', 'loe_di', 'yob', 'gender', 'grade', 'start_time_di', 'last_event_di', 'nevents', 'ndays_act', 'nplay_video', 'nchapters', 'nforum_posts', 'roles', 'incomplete_flag']
mooc = 'HMXPC13_DI_v2_5-14-14.csv'
mooc_data = pd.read_csv(mooc, header=0, names=mooc_cols, na_filter=False)

mooc_data.describe()

mooc_data.head()

#frequencies of outcome categories
categories = ['viewed', 'explored', 'certified']
for X in categories:
    print mooc_data[X].value_counts()
    plt.figure()    
    mooc_data[X].value_counts().plot(kind='bar')




#mooc_data[X].value_counts().plot(kind='bar')
    
#average grade for students with certificates
    
mooc_data[mooc_data.certified==1].grade.mean()

# create age variable

mooc_data['yob'].dtype
mooc_data['new_yob']=mooc_data.yob.convert_objects(convert_numeric=True)

mooc_data['age'] = 2013 - mooc_data['new_yob']

#calculate average age by outcome category

mooc_data[mooc_data.certified==1].age.mean()
mooc_data[mooc_data.viewed==1].age.mean()
mooc_data[mooc_data.explored==1].age.mean()
mooc_data[mooc_data.explored==0].age.mean()

#create outcome category variable to enable groupby operations
'''
mooc_data['outcome']=''
categories = ['viewed', 'explored', 'certified']
for X in categories:
    for Y in range(1,4):
        mooc_data['outcome'][(mooc_data[X] == 1)] = Y

print mooc_data['outcome', 'viewed', 'explored', 'certified'][0:1000]
'''
mooc_data['outcome'][(mooc_data['viewed'] == 1)] = 1
