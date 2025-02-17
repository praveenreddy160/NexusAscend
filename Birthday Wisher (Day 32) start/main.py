import smtplib

my_email = "praveenreddy160@gmail.com"
my_password = "fmct hrek mrex nykb"
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=my_password)
connection.sendmail(from_addr=my_email, to_addrs="saiteja.madha@gmail.com", msg="Hello, Madha. Time to Settle This (in Code)")
connection.set_debuglevel(1)
connection.close()