#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import pandas as pd

def audit_report(filename):
    df=pd.read_excel(filename)
    print("**************************AUDIT REPORT***********************")
    print ("-----------------Number of Columns--------------------------")
    print(len(df.columns))
    print ("-----------------Number of Records--------------------------")
    print(len(df.index))
    print ("-----------------Columns Data Types-------------------------")
    print(df.dtypes)
    print ("-----------------Number of Missing cells--------------------")
    print(df.isnull().sum())
    print ("-----------------Number of duplicate rows--------------------")    
    print(df.duplicated().sum())
    print ("-----------------Memory Taken By Dataframe-------------------") 
    print((df.memory_usage(deep=True).sum())/1048576, "MB" )
    print ("-----------------------Warning-------------------------------")
    print("Max missing values are in column:",df.count().idxmin())
    print ("-------------------Range of columns--------------------------")
    print(df.describe().loc[['max','min']])
    return;

audit_report("C:/Users/Zohran/Documents/R/sec_b.xlsx")