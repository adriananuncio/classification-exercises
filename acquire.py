#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from env import host, user, password
import os


# In[2]:


def get_connection(schema,
                  user=user,
                  host=host,
                  password=password):
    return f'mysql+pymysql://{user}:{password}@{host}/{schema}'


# In[14]:


def get_titanic_data():
    if os.path.exists('titanic.csv'):
        df = pd.read_csv('titanic.csv', index_col=0)
    else: 
        query = 'SELECT * FROM passengers'
        connection = get_connection('titanic_db')
        df = pd.read_sql(query, connection)
        df.to_csv('titanic.csv')    
    return df 


# In[15]:


df = get_titanic_data()


# ##### 

# ### get_iris_data

# In[16]:


query = '''SELECT measurement_id,
sepal_length,
sepal_width,
petal_width,
species_name
FROM measurements
LEFT JOIN species USING(species_id)'''
connection = get_connection('iris_db')


# In[17]:


def get_iris_data():
    if os.path.exists('iris.csv'):
        df = pd.read_csv('iris.csv', index_col=0)
    else:
        query = '''SELECT measurement_id,
        sepal_length,
        sepal_width,
        petal_width,
        species_name
        FROM measurements
        LEFT JOIN species USING(species_id)'''
        connection = get_connection('iris_db')
        df = pd.read_sql(query, connection)
        df.to_csv('iris.csv')
    return df


# In[18]:


df_iris = get_iris_data()


# ##### 

# ### get_telco_data

# In[19]:


query = '''SELECT * FROM customers
LEFT JOIN contract_types USING(contract_type_id)
LEFT JOIN internet_service_types USING (internet_service_type_id)
LEFT JOIN payment_types USING (payment_type_id)'''
connection = get_connection('telco_churn')


# In[20]:


def get_telco_data():
    if os.path.exists('telco_churn.csv'):
        df = pd.read_csv('telco_churn.csv', index_col=0)
    else: 
        query = '''SELECT * FROM customers
        LEFT JOIN contract_types USING(contract_type_id)
        LEFT JOIN internet_service_types USING (internet_service_type_id)
        LEFT JOIN payment_types USING (payment_type_id)'''
        connection = get_connection('telco_churn')
        df = pd.read_sql(query, connection)
        df.to_csv('telco_churn.csv')
    return df


# In[21]:


telco = get_telco_data


# ##### 
