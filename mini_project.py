import smtplib
from email.mime.text import MIMEText

def send_rent_reminder_email():
    rent = input("Hey, User! Please enter an amount for the rent: \n")
    roomies = input("Please enter the number of people who stay in the apartment: \n")
    
    # Validating rent
    if rent.isdigit() and int(rent) <= 2000:
        Total_Rent = float(rent)
        print("Thanks for entering a valid amount.")
        
        # Validating roommates
        if roomies.isdigit() and int(roomies) <= 6:
            print("Thanks for entering a valid number of people.")
            try:
                rent_due = Total_Rent / int(roomies)
                
                # setting up my Emails
                sender_email = "enter_your_email"
                # i'm using app password here whic is helping to sign in to my Google Account on older apps and services that don’t support modern security standards.
                sender_password = "Please enter your app_password"
                recipients = ["roomie_1", "roomie_2", "roomie_3", "roomie_4", "roomie_5"]
                subject = "Hey Roomies! Rent is Due Soon 😊"
                message = f"""Hey Roomies! Just a reminder—rent is due soon! The total rent is {Total_Rent}, so each person's share is {rent_due}. If you can send it by November 1st, that would be great!

Thanks,  
Praveen"""
                
                # MIMEText is a class and i'm passing by arguments to it and then storing in msg variable
                msg = MIMEText(message)
                msg['From'] = sender_email
                msg['To'] = ', '.join(recipients)
                msg['Subject'] = subject
                
                # i'm connecting to the Gmail SMTP server, from where we can send emails.
                server = smtplib.SMTP('smtp.gmail.com', 587)
                # starting a secure connection with the server.
                server.starttls()
                # logs in to your email account and sending email to the roomies
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, recipients, msg.as_string())
                server.quit()
                
                print("Email sent successfully!")
            
            except Exception as e:
                print(f"Error sending email: {e}")
        else:
            print("Please enter a valid number of people (1-6).")
    else:
        print("Please enter a valid rent amount (up to $2000).")

send_rent_reminder_email()
