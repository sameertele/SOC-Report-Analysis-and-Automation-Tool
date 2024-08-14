#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from scripts.parse_soc_data import parse_data
from scripts.visualize_soc_data import visualize_data
from scripts.identify_threats import identify_threats
from scripts.generate_report import generate_report
from scripts.send_alerts import send_alerts

def main():
    data_path = 'data/UNSW_NB15_training-set.csv'
    report_path = 'report/threat_report.csv'
    
    # Parsing
    soc_data = parse_data(data_path)
    
    # Visualizing
    visualize_data(soc_data)
    
    # Identifying potential threats
    threats = identify_threats(soc_data)
    
    # Generating a summary report
    generate_report(threats, report_path)
    
    # Sending alerts based on the report
    send_alerts(report_path, ['telesameer@gmail.com'])

if __name__ == "__main__":
    main()

