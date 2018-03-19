{
   "cmd": ["C:\\Users\\nEW u\\AppData\\Local\\Programs\\Python\\Python35\\python.exe", "-u", "$file"],
    "file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
    "selector": "source.python"
}
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

host = "smtp.gmail.com"
port = 587
username = "harsh161097@gmail.com"
password = "flamehurts"
from_email = username
to_email = ["ayushh4u@gmail.com,golwalkerpratikshit@gmail.com,nishit.k1002@gmail.com,1604086@gkiit.ac.in,1604097@kiit.ac.in"]

email_conn = smtplib.SMTP(host,port)
email_conn.ehlo()

email_conn.starttls()
email_conn.login(username, password)


the_msg = MIMEMultipart("alternative")
the_msg["Subject"] = "New mail"
the_msg["From"] = "from_email"


plain_text = "Holla, people! Something good is awaiting for you. The Internship camp.Dates: 23-25 March 2018. Register now!!!"

part_1 = MIMEText(plain_text,'plain')

the_msg.attach(part_1)


email_conn.sendmail(from_email, to_email, the_msg.as_string())
email_conn.quit()
