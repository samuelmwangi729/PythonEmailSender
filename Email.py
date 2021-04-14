import smtplib
from  email.message import EmailMessage
import CONFIG
#create an instance of Email Message class
message=EmailMessage()
#Sender email, receiver, subject content 
message['From']=CONFIG.EMAIL
message['To']="born2hack001@gmail.com"
message['Subject']="Password reset Notification"
content="Hello, hope this email find you safe.Someone has requested a password reset for the account registered under this email. IF THIS IS NOT YOU, KINDLY IGNORE THE EMAIL"
message.set_content(content)
with smtplib.SMTP_SSL('smtp.gmail.com',465) as server:
    #login your google account 
    server.login(CONFIG.EMAIL,CONFIG.PASS)
    server.send_message(message)