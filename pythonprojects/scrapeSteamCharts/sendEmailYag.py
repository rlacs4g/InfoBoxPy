import yagmail
import smtplib
conn = smtplib.SMTP('imap.gmail.com',587)
conn.ehlo()
conn.starttls()
conn.login('youremail@gmail.com', 'your_password')

conn.sendmail('from@gmail.com','to@gmail.com','Subject: What you like? \n\n Reply Reply Reply')
conn.quit()

receiver = "throwaway062@gmail.com"
body = "Hello there from Yagmail"
filename = "document.pdf"

yag = yagmail.SMTP("leaftest1118@gmail.com")
yag.send(
    to=receiver,
    subject="Yagmail test with attachment",
    contents=body, 
    attachments=filename,
)
