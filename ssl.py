import ssl
import socket
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def check_ssl_expiry(domain):
    context = ssl.create_default_context()
    with socket.create_connection((domain, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=domain) as ssock:
            cert = ssock.getpeercert()
            expires_on = datetime.datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
            return expires_on

def send_email(to_email, website_expiries):
    sender_email = 'ssl@gravityafrica.co.ke'  # Replace with your email address
    password = 'EMAIL PASSWORD'  # Replace with your email password

    message = MIMEMultipart()
    message['Subject'] = 'SSL Certificate Expiry Reminder'
    message['From'] = sender_email
    message['To'] = to_email

    body = "SSL certificates for the following websites are expiring soon:\n\n"
    for website, expiry_date in website_expiries.items():
        remaining_days = (expiry_date - datetime.datetime.now()).days
        body += f"{website}: {expiry_date.strftime('%Y-%m-%d')} (in {remaining_days} days)\n"

    message.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP_SSL('gravityafrica.co.ke', 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, to_email, message.as_string())

websites = ['google.com', 'youtube.com']  # Replace with your list of websites
recipient_email = 'yourmail'  # Replace with the recipients email address

website_expiries = {}
for website in websites:
    expiry_date = check_ssl_expiry(website)
    website_expiries[website] = expiry_date

send_email(recipient_email, website_expiries)
