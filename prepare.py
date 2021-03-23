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
# In [ ]:
def Robust_Scaler(X_train, X_validate, X_test):
    """
    Takes in X_train, X_validate and X_test dfs with numeric values only
    Returns scaler, X_train_scaled, X_validate_scaled, X_test_scaled dfs 
    """
    scaler = sklearn.preprocessing.RobustScaler().fit(X_train)
    X_train_scaled = pd.DataFrame(scaler.transform(X_train), index = X_train.index, columns = X_train.columns)
    X_validate_scaled = pd.DataFrame(scaler.transform(X_validate), index = X_validate.index, columns = X_validate.columns)
    X_test_scaled = pd.DataFrame(scaler.transform(X_test), index = X_test.index, columns = X_test.columns)
    
    return scaler, X_train_scaled, X_validate_scaled, X_test_scaled

# In[ ]:
def model_zillow ():
    '''This function takes in the clean data, drops the tax amount for modeling purposes and drops the not as good features as chosen by rfe and selectkbest.'''
    df= clean_zillow()
    df= df.drop(columns=['tax_amount','county','lot_size','fips'])
    
    train_validate, test = train_test_split(df, test_size=.2, random_state=123)
    train, validate = train_test_split(train_validate, test_size=.3, random_state=123) 
    
    X_train2 = train.drop(columns=['tax_value'])
    X_validate2 = validate.drop(columns=['tax_value'])
    X_test2 = test.drop(columns=['tax_value'])

    y_train2 = train[['tax_value']]
    y_validate2 = validate[['tax_value']]
    y_test2 = test[['tax_value']]
    return X_train2, X_validate2, X_test2, y_train2, y_validate2, y_test2


