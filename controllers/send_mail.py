import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from controllers import email


class SendMail:
    def __init__(self, user, subject, text, html):
        self.sender = email
        self.subject = subject
        self.text = text
        self.html = html
        self.user = user

    def send(self):
        message = MIMEMultipart("alternative")
        message["Subject"] = self.subject
        message["From"] = self.sender['user']
        message["To"] = self.user.email

        # Create the plain-text and HTML version of your message
        text = self.text.format(name=self.user.name, uid=self.user.uid, pwd=self.user.password)
        html = self.html.format(name=self.user.name, uid=self.user.uid, pwd=self.user.password)

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        message.attach(part2)

        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(user=self.sender['user'], password=self.sender['password'])
            server.sendmail(self.sender['user'], self.user.email, message.as_string())

    def send_otp(self):
        message = MIMEMultipart("alternative")
        message["Subject"] = self.subject
        message["From"] = self.sender['user']
        message["To"] = self.user['email']

        # Create the plain-text and HTML version of your message
        text = self.text.format(name=self.user['name'], otp=self.user['otp'])
        html = self.html.format(name=self.user['name'], otp=self.user['otp'])

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        message.attach(part2)

        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(user=self.sender['user'], password=self.sender['password'])
            server.sendmail(self.sender['user'], self.user['email'], message.as_string())
