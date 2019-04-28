# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 14:31:58 2019

@author: AN389897
"""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

print('please provide the below details to send an email')
host = 'smtp.gmail.com'
port = 587
username = str(input('Email id: '))
password = str(input('Password: '))
to_details = str(input('Send Email To: ')).split(',')
subject = str(input('Subject: '))
base_message = str(input('Body in HTML:'))
attachment = str(input('Provide file name to be attached in the mail:')).split(',')

def send_email(user, password, to, subject, body, files):
    try:
        email_conn =smtplib.SMTP(host, port)
        email_conn.ehlo()
        email_conn.starttls()
        email_conn.login(user, password)
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = user
        part_1 = MIMEText(body,'Html')
        msg.attach(part_1)
        for file in files:
            attaching = MIMEBase('application', 'octet-stream')
            attaching.set_payload(open(str(file),'rb').read())
            encoders.encode_base64(attaching)
            attaching.add_header('Content-Disposition', 'attachment; filename = %s' %file)
            msg.attach(attaching)
        print(msg)
        email_conn.sendmail(user, to, msg.as_string())
        email_conn.quit()
    except Exception as e:
        print('Message Could not be send ', e)
    
send_email(username, password, to_details, subject, base_message, attachment)