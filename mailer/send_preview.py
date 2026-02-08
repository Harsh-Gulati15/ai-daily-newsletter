import smtplib
from email.mime.text import MIMEText

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

SENDER_EMAIL = "harshgulati0511@gmail.com"
SENDER_PASSWORD = "veot bjql zvmj jrdc"
RECEIVER_EMAIL = "harshgulati0511@gmail.com"

def send_preview_email(content):
    msg = MIMEText(content)
    msg["Subject"] = "🧪 AI Newsletter Preview — Approval Needed"
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
