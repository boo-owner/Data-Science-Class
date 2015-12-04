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
import seaborn as sns
# read in the drinks data
mooc_cols = ['course_id', 'userid_di', 'registered', 'viewed', 'explored', 'certified', 'final_cc_cname_di', 'loe_di', 'yob', 'gender', 'grade', 'start_time_di', 'last_event_di', 'nevents', 'ndays_act', 'nplay_video', 'nchapters', 'nforum_posts', 'roles', 'incomplete_flag']
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
'''

'''
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


counts = mooc_data['outcome'].value_counts().sort_index(1)      

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
mooc_data.gender.replace('o', np.nan, inplace = True)
counts_gender = mooc_data.gender.value_counts(dropna=False)
counts_gender.plot(kind='pie', labels = ['Male', 'Female', 'Missing'], autopct='%1.1f%%', shadow=True)


#pie chart highest degree
counts_hdeg = mooc_data['loe_di'].value_counts(dropna=False).sort_index(1)

counts_hdeg.plot(kind='pie', autopct='%1.1f%%', shadow=True, title = 'Highest degree earned')


counts_hdeg_out0 = mooc_data['loe_di'][mooc_data['outcome']==0].value_counts(dropna=False).sort_index(1)
counts_hdeg_out1 = mooc_data['loe_di'][mooc_data['outcome']==1].value_counts(dropna=False).sort_index(1)
counts_hdeg_out2 = mooc_data['loe_di'][mooc_data['outcome']==2].value_counts(dropna=False).sort_index(1)
counts_hdeg_out3 = mooc_data['loe_di'][mooc_data['outcome']==3].value_counts(dropna=False).sort_index(1)
