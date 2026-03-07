
#============================================================
#Program :Simple Gmail Mail Sender
#Author  : Chaitany Dilip Belambkar
#Purpose : Send mail using Python SMTP
#============================================================

import smtplib
from email.message import  EmailMessage
#----------------------------------------------------------
#Function : Chaitany_send_mail
#Description: send email using Gmail SMTP server 
#----------------------------------------------------------

def send_mail(sender,app_password,reciever,subject,body):

    #Step1 : Create  Email Object
    msg = EmailMessage()

    #step 2: set mail headers
    msg["From"] = sender
    msg["To"] = reciever
    msg["Subject"] = subject

    #step 3 : Add mail body
    msg.set_content(body)

    #step 4 : Create SMTP SSL connection manually
    smtp = smtplib.SMTP_SSL("smtp.gmail.com",465)

    #step 5 : Login Using Gmail + App Password 
    smtp.login(sender,app_password)

    #step 6 : send the mail
    smtp.send_message(msg)

    #step 7 : close connection manually
    smtp.quit()

    #------------------------------------------------------
    #Function :    main
    #Description : Driver code
    #------------------------------------------------------

def main():

    #Always use separate temporary /testing account
    sender_email = "pythonsript9689@gmail.com"

    #App password generated  from google account 
    app_password = "upqp qlcu wxqk oixx"

    #Your secod email for testing
    reciever_email = "chaitanyabelambkar@gmail.com"
    subject = "Test mail from Python Script"
    body = """Jay Ganesh, 
    This is test email sent 
    using Chaitany Python. 
    
    Regards,
    Chaitany InfoSystems
    """ 
    send_mail(sender_email,app_password,reciever_email,subject,body)

    print("Chaitany Mail Sent Successfully")

#-------------------------------------------------------
#Program Entry Point
#-------------------------------------------------------

if __name__ == "__main__":
    main()


