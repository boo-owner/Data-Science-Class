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
