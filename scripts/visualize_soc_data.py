#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt

def visualize_data(df):
    """
    Visualizing.
    """
    # Plots of attack categories
    attack_categories = df['attack_cat'].value_counts()
    attack_categories.plot(kind='bar')
    plt.title('Distribution of Attack Categories')
    plt.xlabel('Category')
    plt.ylabel('Count')
    plt.show()

if __name__ == "__main__":
    data_path = '../data/UNSW_NB15_training-set.csv'
    df = pd.read_csv(data_path)
    visualize_data(df)

