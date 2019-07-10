#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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
    
    return;

