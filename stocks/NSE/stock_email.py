import smtplib
import os


EMAIL_ADDRESS = os.environ.get('EMAIL_SENDER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

# pprint(os.environ.keys())
print(EMAIL_ADDRESS)
print(EMAIL_PASSWORD)

# SMTP port --> 587
# SMTP_SSL port --> 465
# SMTP LocalHost port --> 1025


with smtplib.SMTP('localhost',1025) as smtp:
# with smtplib.SMTP('smtp.gmail.com',587) as smtp:
# with smtplib.SMTP_SSl('smtp.gmail.com',465) as smtp:
    # way to identify ourselves
    # smtp.ehlo()
    # # encrypt our traffic.
    # smtp.starttls()
    # # reverification after encryption
    # smtp.ehlo()
    
    # smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    
    subject = "stocks analysis"
    
    body = "First report for Stock Analysis"
    
    msg = f'Subject:{subject}\n\n{body}'
    
    smtp.sendmail(EMAIL_ADDRESS,EMAIL_ADDRESS,msg)