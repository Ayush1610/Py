{
   "cmd": ["C:\\Users\\nEW u\\AppData\\Local\\Programs\\Python\\Python35\\python.exe", "-u", "$file"],
    "file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
    "selector": "source.python"
}

from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

host = "smtp.gmail.com"
port = 587
username = "harsh161097@gmail.com"
password = "flamehurts"
from_email = username
to_list = ['golwalker.pratikshit@gmail.com','1604086@kiit.ac.in','nishit.k1002@gmail.com']


class msg():

	user_details = []
	messages = []
	email_messages = []
	
	basic_msg = """ Hi, {name}!!!
	greetings for your purchase on {date}
	of worth {price}
	Regards,
	Ayush
	"""
	

	def user_new(self, name, price, email=None):
		name = name[0].upper() + name[1:].lower()
		price = "%.2f" %(price)
		details = {
			"name" : name,
			"price": price,
		}
		today = datetime.today()
		date_text = '{today.date}/{today.month}/{today.year}'.format(today=today)
		details['date'] = date_text
		self.user_details.append(details)

	def get_details(self):
		return self.user_details

	def new_msg(self):
		if len(self.user_details) > 0:
			for details in self.get_details():
				name = details["name"]
				price = details["price"]
				date = details["date"]


				new_msg = self.basic_msg.format(
					name = name,
					date = date,
					price = price
				)
				# print(new_msg)
				user_email = details.get('email')
				if user_email:
					user_data = {
						"email": user_email,
						"basic_msg": new_msg
					}
					
					self.email_details.append(user_data)
				else:
					self.messages.append(new_msg)
				return self.messages
			return[]
	def send_emails(self):
		self.new_msg()
		if len(self.email_messages) > 0:
			for details in self.email_messages:
				user_email = detail['email']
				user_message = detail['messages']
				
				try:
					email.conn = smtplib.SMTP(host,port)
					email_conn.ehlo()

					email_conn.starttls()
					email_conn.login(username, password)


					the_msg = MIMEMultipart("alternative")
					the_msg["Subject"] = "THE INTERNSHIP CAMP"
					the_msg["From"] = "from_email"
					the_msg["To"] = "user_email"

					part_1 = MIMEText(user_message, 'plain')
					the_msg.attach(part_1)


					email_conn.sendmail(from_email, [user_email], the_msg.as_string())
					email_conn.quit()
				except Exception as e:
					raise e
			return True
		return False


instance = msg()
instance.user_new("sammy",float(150.00),email="golwalkerpratikshit@gmail.com")
instance.user_new("gaurAv",float(350.567),email="1604086@kiit.ac.in")
instance.user_new("Nishit",float(250.879),email="nishit.k1002@gmail.com")
instance.get_details()
instance.new_msg()
instance.send_emails()