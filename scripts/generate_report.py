#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

def generate_report(threats, output_path):
    
    #Generating a summary report for identified threats.
    
    report = threats[['srcip', 'sport', 'dstip', 'dsport', 'attack_cat', 'label']]
    report.to_csv(output_path, index=False)
    print(f"Report generated and saved to {output_path}")

if __name__ == "__main__":
    data_path = '../data/UNSW_NB15_training-set.csv'
    df = pd.read_csv(data_path)
    threats = df[df['label'] == 1]
    generate_report(threats, '../report/threat_report.csv')

