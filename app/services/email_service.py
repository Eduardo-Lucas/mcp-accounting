# app/services/email_service.py

def send_email(to: str, subject: str, body: str):
    # Replace later with SendGrid / SES
    print(f"[EMAIL] To: {to}")
    print(f"Subject: {subject}")
    print(body)
