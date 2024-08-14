#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd

def parse_data(file_path):
    """
    Parsing
    """
    df = pd.read_csv(file_path)
    return df

if __name__ == "__main__":
    data_path = '../data/UNSW_NB15_training-set.csv'
    soc_data = parse_data(data_path)
    print(soc_data.head())


# In[ ]:




