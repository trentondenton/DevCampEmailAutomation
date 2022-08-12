import smtplib
from dotenv import load_dotenv
from os.path import join, dirname, isdir
from os import environ
import string
dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

gmail_user = environ.get("user")
gmail_password = environ.get("pass")
subject = 'Weekly mentor session'
sent_from = "Bottega University"
cc = environ.get("cc")
file = environ.get("file")

with open(file) as f:
    f_read = f.read().split('\n')
    for student in f_read:
        s = student.split(',')
        name = s[1]
        hour = s[2]
        to = s[0].split()
        body = 'Hi {0}! this is Trenton from Bottega, just to remind you that tomorrow you have your mentoring session scheduled at {1} MST, if you want to reschedule please let us know sending an email to advisor@bottega.edu '.format(
            name, hour)
        
        
        
        message = 'From: {}\r\nCC: {}\r\nSubject: {}\n\n{}'.format(sent_from,cc,subject, body)


        try:
            to = [to] + cc.split(",") 
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(gmail_user, gmail_password)
            server.sendmail(sent_from, to, message)
            server.close()

            print('Email sent to '+name)
        except:
            print('Something went wrong...')
