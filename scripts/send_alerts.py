#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import smtplib
from email.mime.text import MIMEText

def send_alerts(report_path, recipients):
    with open(report_path, 'r') as file:
        report = file.read()

    msg = MIMEText(report)
    msg['Subject'] = 'SOC Threat Alert'
    msg['From'] = 'your-email@gmail.com'
    msg['To'] = ', '.join(recipients)

    # Configuring email server
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  
            server.login('your-email@gmail.com', 'your-password')  #Email and password
            server.sendmail(msg['From'], recipients, msg.as_string())
            print("Alerts sent successfully.")
    except Exception as e:
        print(f"Failed to send alerts: {e}")

if __name__ == "__main__":
    report_path = '../report/threat_report.csv'
    recipients = ['telesameer@gmail.com']
    send_alerts(report_path, recipients)

