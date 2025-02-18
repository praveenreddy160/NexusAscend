import smtplib
import datetime as dt
import random
from email.mime.text import MIMEText
import os

def send_challenge_email(sender_email, sender_password, recipient, subject, template_file):
    """
    Sends a motivational email with an HTML template and a random Monday quote.
    """
    try:
        now = dt.datetime.now()
        day = now.weekday()  # 0 = Monday, 6 = Sunday

        # Check if today is Monday
        if day == 0:
            # Read a random quote from quotes.txt
            with open(r"C:/Users/prave/nexusascend/Birthday Wisher (Day 32) start/quotes.txt", "r", encoding="utf-8") as file:
                quotes = file.readlines()
                monday_quote = random.choice(quotes).strip()

            # Read the HTML template
            with open(template_file, "r", encoding="utf-8") as file:
                html_template = file.read()

            # Extract recipient's name from email
            recipient_name = recipient.split("@")[0]

            # Replace placeholders in the template
            html_content = html_template.replace("[Friend's Name]", recipient_name)
            html_content = html_content.replace("[Monday]", monday_quote)

            # Create an HTML email
            msg = MIMEText(html_content, "html")
            msg["Subject"] = "🚀 Inspiration Mode Activated!"
            msg["From"] = sender_email
            msg["To"] = recipient

            # Send email
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
                connection.login(sender_email, sender_password)
                connection.sendmail(sender_email, recipient, msg.as_string())

            print(f"✅ Motivational email sent successfully to {recipient}!")

        else:
            print("⏳ Today is not Monday. No email sent.")

    except Exception as e:
        print(f"❌ Error sending email: {e}")

# --- Sender Information ---
sender_email = "fill here"  # Use environment variables
sender_password = "fill here"

# --- Recipient Information --
recipients = ["fill here"]

# --- Template File Path ---
template_file = r"C:/Users/prave/nexusascend/Birthday Wisher (Day 32) start/monday_motivation.html"

# --- Send Emails ---
for recipient in recipients:
    send_challenge_email(sender_email, sender_password, recipient, "Motivational Monday", template_file)
