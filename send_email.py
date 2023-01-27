import imghdr
import os
import smtplib
from email.message import EmailMessage

username = f"{os.getenv('USERNAME')}@gmail.com"
password = os.getenv("PASSWORD")


def send_email(image_path):
    email_message = EmailMessage()
    email_message['Subject'] = 'New Customer Showed Up!'
    email_message.set_content("Hey, we just saw a new customer!")

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(username, password)
    gmail.sendmail(username, username, email_message.as_string())
    gmail.quit()
