import os
import smtplib
from email.mime.text import MIMEText

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

SENDER_EMAIL = os.getenv("GMAIL_ADDRESS")
SENDER_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")
RECEIVER_EMAIL = os.getenv("GMAIL_ADDRESS")

def send_preview_email(content):
    if not SENDER_EMAIL or not SENDER_PASSWORD:
        raise RuntimeError("Email credentials not set")

    msg = MIMEText(content)
    msg["Subject"] = "🧪 AI Newsletter Preview — Approval Needed"
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
