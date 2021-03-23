#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import os
import env

# creating a connection to connect to the Codeup Student Database
def get_connection(db, user=env.user, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'
def get_zillow_data():
    '''This function will connect to the Codeup Student Database. It will then cache a local copy to the computer to use for later
        in the form of a CSV file. If you want to reproduce the results, you will need your own env.py file and database credentials.'''
    filename = "zillow.csv"
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        # read the SQL query into a dataframe
        df = pd.read_sql('''
SELECT parcelid, fips, latitude, longitude, lotsizesquarefeet, calculatedfinishedsquarefeet, bedroomcnt, bathroomcnt, taxamount, taxvaluedollarcnt FROM properties_2017
JOIN predictions_2017 USING (parcelid) 
WHERE transactiondate BETWEEN '2017-05-01' AND '2017-08-31'
AND (propertylandusetypeid IN (261, 262, 263, 264, 268, 273, 274, 276, 279))
AND (bathroomcnt > 0)
AND (bedroomcnt > 0);
            ''' , get_connection('zillow'))
        # Write that dataframe to disk for later. Called "caching" the data for later.
        df.to_csv(filename)
        # Return the dataframe to the calling code
        return df

