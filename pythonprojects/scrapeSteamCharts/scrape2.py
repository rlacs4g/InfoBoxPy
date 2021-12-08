import smtplib, ssl, requests
from bs4 import BeautifulSoup


port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "leaftest1118@gmail.com"  # Enter your address
receiver_email = "throwaway062@gmail.com"  # Enter receiver address
password = input("Type your password and press enter: ")
message = "pop"
# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)

