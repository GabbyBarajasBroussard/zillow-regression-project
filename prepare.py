#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import os
import env
from acquire import get_zillow_data
from sklearn.model_selection import train_test_split
import sklearn.preprocessing
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, MinMaxScaler
from sklearn.feature_selection import SelectKBest, f_regression

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
    df['lotsizesquarefeet'].fillna(df['lotsizesquarefeet'].mode()[0], inplace=True)
    # make new column for county names
    rating = []
    for row in df['fips']:
        if row == 6037.0:    rating.append('los_angeles_county')
        elif row == 6059.0:   rating.append('orange_county')
        elif row == 6111.0:  rating.append('ventura_county')
        else:           rating.append('no_county')
    df['county']= rating
    #rename columns to make it easier to call later
    df= df.rename(columns={"bedroomcnt": "bedroom_count","bathroomcnt": "bathroom_count",  "lotsizesquarefeet": "lot_size",
                      "calculatedfinishedsquarefeet": "square_feet", "taxamount": "tax_amount", "taxvaluedollarcnt": "tax_value"
                      })
    # drop unneeded columns
    df= df.drop(columns=["Unnamed: 0", "parcelid", 'latitude','longitude'])
    # return the clean dataframe
    return df


# In[4]:


def prep_zillow_data():
    '''This function takes in the cleaned zillow data and returns a train, validate, and test data sets.'''
    df= clean_zillow()
    train_validate, test = train_test_split(df, test_size=0.2, random_state=123)
    train, validate = train_test_split(train_validate, test_size=0.3, random_state=123) 
    return train, validate, test

def prep_split_zillow_data():
    '''This function takes in the clean data, drops the tax amount for modeling purposes and then splits the data into X/Y Train, Validate/Test.'''
    df= clean_zillow()
    df= df.drop(columns=['tax_amount','county'])
    
    train_validate, test = train_test_split(df, test_size=.2, random_state=123)
    train, validate = train_test_split(train_validate, test_size=.3, random_state=123) 
    
    X_train = train.drop(columns=['tax_value'])
    X_validate = validate.drop(columns=['tax_value'])
    X_test = test.drop(columns=['tax_value'])

    y_train = train[['tax_value']]
    y_validate = validate[['tax_value']]
    y_test = test[['tax_value']]
    return X_train, X_validate, X_test, y_train, y_validate, y_test


# In[ ]:
def select_kbest(x, y, k):
    
    # parameters: f_regression stats test, give me 8 features
    f_selector = SelectKBest(f_regression, k=k)
    
    # find the top 8 X's correlated with y
    f_selector.fit(x, y)
    
    # boolean mask of whether the column was selected or not. 
    feature_mask = f_selector.get_support()
    
    f_feature = X_train_scaled.iloc[:,feature_mask].columns.tolist()
    
    return f_feature

# In [ ]:
def rfe(x, y, k):
    
    lm = LinearRegression()
    
    rfe = RFE(lm, k)
    
    # Transforming data using RFE
    X_rfe = rfe.fit_transform(X_train_scaled,y_train)  
    
    mask = rfe.support_
    
    rfe_features = X_train_scaled.loc[:,mask].columns.tolist()
    
    print(str(len(rfe_features)), 'selected features')
    
    return  rfe_features



