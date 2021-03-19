#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import os
import env
import acquire
from sklearn.model_selection import train_test_split
import sklearn.preprocessing
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, MinMaxScaler


# In[3]:


def clean_zillow():
    #get the zillow data
    df= get_zillow_data()
    #handle the nan's
    df['bedroomcnt'].fillna(df['bedroomcnt'].mode()[0], inplace=True)
    df['bathroomcnt'].fillna(df['bathroomcnt'].mode()[0], inplace=True)
    df['calculatedfinishedsquarefeet'].fillna(df['calculatedfinishedsquarefeet'].mode()[0], inplace=True)
    df['fips'].fillna(df['fips'].mode()[0], inplace=True)
    df['taxamount'].fillna(df['taxamount'].mode()[0], inplace=True)
    df['taxvaluedollarcnt'].fillna(df['taxvaluedollarcnt'].mode()[0], inplace=True)
    #rename columns to make it easier to call later
    df= df.rename(columns={"parcelid": "parcel_id", "bedroomcnt": "bedroom_count","bathroomcnt": "bathroom_count",
                      "calculatedfinishedsquarefeet": "square_feet", "taxamount": "tax_amount", "taxvaluedollarcnt": "tax_value"
                      })
    # drop unneeded columns
    df= df.drop(columns=["Unnamed: 0"])
    # return the clean dataframe
    return df


# In[4]:


def prep_zillow_data():
    '''This function takes in the cleaned zillow data and returns a train, validate, and test data sets.'''
    df= clean_zillow()
    train_validate, test = train_test_split(df, test_size=.2, random_state=123)
    train, validate = train_test_split(train_validate, test_size=.3, random_state=123) 
    return train, validate, test

def prep_split_zillow_data():
    '''This function takes in the clean data, drops the tax amount for modeling purposes and then splits the data into X/Y Train, Validate/Test.'''
    df=clean_zillow()
    df= df.drop(columns='taxamount')
    X_train = train.drop(columns='tax_value')
    X_validate = validate.drop(columns='tax_value')
    X_test = test.drop(columns='tax_value')

    y_train = train['tax_value']
    y_validate = validate['tax_value']
    y_test = test['tax_value']
    return X_train, X_validate, X_test, y_train, y_validate, y_test


# In[ ]:




