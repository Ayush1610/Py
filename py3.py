{
   "cmd": ["C:\\Users\\nEW u\\AppData\\Local\\Programs\\Python\\Python35\\python.exe", "-u", "$file"],
    "file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
    "selector": "source.python"
}

import smtplib

host = "smtp.gmail.com"
port = 587
username = "ayushh4u@gmail.com"
password = "itsme"
from_email = username
to_email = ["ayushh4u@gmail.com"]

email_conn = smtplib.SMTP(host,port)
email_conn.ehlo()

email_conn.starttls()
email_conn.sendmail(from_email,to_email,"Holla! there. Something good awaiting.")
email_conn.quit()