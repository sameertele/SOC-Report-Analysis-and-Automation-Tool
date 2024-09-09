# SOC Report Analysis and Automation Tool

## Overview

The SOC Report Analysis and Automation Tool is a Python-based application designed to automate the analysis of Security Operations Center (SOC) reports. The tool parses and visualizes SOC data, identifies potential security threats, generates summary reports, and sends automated alerts for critical vulnerabilities, improving the response time for threat mitigation.

## Features

- **Data Parsing**: Reads and processes SOC report data from CSV files.
- **Data Visualization**: Visualizes various aspects of SOC data, such as attack category distributions.
- **Threat Identification**: Identifies potential security threats based on predefined criteria.
- **Report Generation**: Generates summary reports for identified threats and saves them as CSV files.
- **Automated Alerts**: Sends email alerts to specified recipients based on the generated threat report.

## Dataset

This project utilizes the **UNSW-NB15** dataset, which is a comprehensive dataset for network traffic analysis and intrusion detection.

- **Dataset Link**: [UNSW-NB15 Dataset](https://research.unsw.edu.au/projects/unsw-nb15-dataset)
- **Files Used**: 
  - `UNSW_NB15_training-set.csv`

### Dataset Preparation

1. Download the dataset from the provided link.
2. Place the CSV file in the `data/` directory.
