import smtplib, ssl, requests
from bs4 import BeautifulSoup

url = "https://steamcharts.com/app/570"

page = requests.get(url)

counter = 0

soup = BeautifulSoup(page.content, "html.parser")

number = soup.find(id="app-heading")
title = soup.find(id="app-title")

chartElements = number.find_all("span", class_="num")
titleElements =  title.find("a", href_="")


fline = titleElements.text, " | Steam Charts Source ", "]\n"
for chartElements in chartElements:

    counter += 1

    if counter == 1:
        oneHour = ("\n1 hour ago     ", chartElements.text)
    elif counter == 2:
        tfPeak = "\n24-hour peak  ", chartElements.text
    elif counter == 3:
        atPeak = ("\nall-time peak  ", chartElements.text )


port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "leaftest1118@gmail.com"  # Enter your address
receiver_email = "throwaway062@gmail.com"  # Enter receiver address
password = input("Type your password and press enter: ")
message = str(fline[0] + "\n") + str(oneHour[0] + oneHour[1]) + str(tfPeak[0] + tfPeak[1]) + str(atPeak[0] + atPeak[1])
# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message) 

# : Colon is tied with the name/nickname of the sender in the mail that is received. It will not send anything if too long. Figure out how to cancel it or escape it