import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "cgsaw2006@gmail.com"  # Enter your address
receiver_email = "cgsaw2006@icloud.com"  # Enter receiver address
password = input("Type your password and press enter: ")
message = """\
Subject: Hi there

trigger"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)