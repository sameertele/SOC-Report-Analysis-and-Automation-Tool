#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

def identify_threats(df):
    """
    Identifying security threats in SOC data.
    """
    # label 1 indicates attack
    threats = df[df['label'] == 1]
    return threats

if __name__ == "__main__":
    data_path = '../data/UNSW_NB15_training-set.csv'
    df = pd.read_csv(data_path)
    threats = identify_threats(df)
    print(f"Identified {len(threats)} potential threats.")

