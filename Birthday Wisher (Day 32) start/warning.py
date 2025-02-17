import smtplib
from email.mime.text import MIMEText
import os

def send_challenge_email(sender_email, sender_password, recipient, subject, template_file):
    """
    Sends an email to a recipient with a challenge message from an HTML template.

    Args:
        sender_email: The sender's email address.
        sender_password: The sender's email password.
        recipient: The recipient's email address.
        subject: The subject of the email.
        template_file: Path to the HTML template file.
    """
    try:
        # Reading the HTML template
        with open(template_file, "r") as file:
            html_template = file.read()

        # Extracting the recipient's name from their email address
        recipient_name = recipient.split("@")[0]

        # Replace the name placeholder in the template
        html_content = html_template.replace("[Friend's Name]", recipient_name)

        # Create the email message
        msg = MIMEText(html_content, 'html')
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = recipient

        # Connect to the SMTP server and send the email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
            connection.login(sender_email, sender_password)
            connection.sendmail(sender_email, recipient, msg.as_string())

        print(f"Challenge email sent to {recipient} successfully!")

    except Exception as e:
        print(f"Error sending email to {recipient}: {e}")

# --- Your Information ---
sender_email = "fill yours"
sender_password = "fill yours"
friends_emails = ["fill yours", "fill yours", "fill yours", "fill yours"]

# --- Challenge Message ---
subject = "Coding Challenge! Activated"
friend_warning = os.path.join("C:/Users/prave/Downloads/Birthday+Wisher+(Day+32)+start/Birthday Wisher (Day 32) start/Warning.html")
friend_warning2 = os.path.join("C:/Users/prave/Downloads/Birthday+Wisher+(Day+32)+start/Birthday Wisher (Day 32) start/Warning1.html")

# --- Send emails to each friend ---
for friend_email in friends_emails:
    if friend_email == "fill yours":  # Checking if it's Friend 3
        template_file = friend_warning2
    else:
        template_file = friend_warning

    send_challenge_email(sender_email, sender_password, friend_email, subject, template_file)