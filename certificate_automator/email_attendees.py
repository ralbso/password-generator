import os
import smtplib, ssl
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

def email_attendees(attendees, filename):
    sender = "ODN (Neuro-RUM)"
    password = input("Type your password and press Enter: ")

    for key,val in attendees.items():
        receiver = val
        subject = "WPRNS Test"

        message = MIMEMultipart("alternative")
        message["From"] = sender
        message["Bcc"] = receiver
        message["Subject"] = subject

        body = "Hello "+str(key.split(" ",1)[0])+""",
        \n\nOur records indicate that you attended the 1st West Puerto Rico Neuroscience Symposium\
        and qualified for this certificate. We are humbled by your support and hope you thoroughly\
        enjoyed this first iteration of many more to come!
        \n\nNote: This certificate was created using a Python algorithm. If there is anything wrong \
        with your certificate, please let us know as soon as possible to correct any mistakes."""

        plain_text = MIMEText(body, "plain")

        # filename = "/Users/Raul/Documents/UPRM/ODN/WPRNS/Certificates/certificate "+str(key)+".pdf"

        with open(filename, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename={os.path.basename(filename)}")
        message.attach(part)
        message.attach(plain_text)

        port = 465
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login("neuro_rum@uprm.edu", password)
            server.sendmail(sender, receiver, message.as_string())
