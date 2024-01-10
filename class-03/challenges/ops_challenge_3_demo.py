#!/usr/bin/env python3

# Script:         Ops 401 Class 3 Demo
# Purpose:        Send an Email Message
# Why:            Prep for Ops Challenge


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, receiver_email, subject, body):
    # Set up the MIME
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    # Connect to the SMTP server and send the email
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())

def exit(message='Thank You For Using My Script'):
    print(message)
    sys.exit()

if __name__ == "__main__":
    try:
        # Get user email and password for notifications
        sender_email = input("Enter your email address: ")
        if not sender_email:
            sender_email = 'youremail.com'
        sender_password = input("Enter your email password (App Password for Gmail): ")
        if not sender_password:
            sender_password = "yourpassword from the app in gmail (not login passowrd))"
        receiver_email = input("Enter the administrator's email address: ")

        # Compose the email
        subject = "Test Notification"
        body = "This is a test email notification from your Python script."

        # Send the email notification
        send_email(sender_email, sender_password, receiver_email, subject, body)

        print("Email sent successfully.")
    except KeyboardInterrupt:
        exit("\nExiting the script")
