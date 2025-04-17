import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import getpass
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def send_mail( recipients, Summary, Plan):
    
    sender_email = os.getenv('SENDER_EMAIL')
    app_password = os.getenv('APP_PASSWORD')
    
    
    # Convert bullets to HTML line breaks
    Plan = Plan.replace("*", "<br>*")

    # Email subject and body
    subject = "Meeting Summary and Plan of Action"
    body = f"""
    Dear Team,<br><br>

    I hope this email finds you well. The purpose of this message is to highlight the key points discussed in today's meeting:<br><br>

    <b>Summary:</b><br>
    {Summary}<br><br>

    <b>Plan of Action:</b><br>
    {Plan}<br>

    Your prompt attention to these matters is appreciated.<br><br>

    Best regards,<br>
    Himanshu Ranjan
    """
    
    # Create MIMEText object
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = ', '.join(recipients)
    message['Subject'] = subject
    message.attach(MIMEText(body, 'html'))

    # Send the email
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email,app_password)
            server.sendmail(sender_email, recipients, message.as_string())
            print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")



