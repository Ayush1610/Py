

# {
#    "cmd": ["C:\\Users\\nEW u\\AppData\\Local\\Programs\\Python\\Python35\\python.exe", "-u", "$file"],
#     "file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
#     "selector": "source.python"
# }


#items = ["Mic","Phone",323.12,3123.123,"Justin","Bag",
#"Cliff bars",134]


#int_items = []


# for i in items:
#     if isinstance(i, float) or isinstance(i, int):
#         int_items.append(i)
#     elif isinstance(i, str):
#         str_items.append(i)
#     else:
#         pass


# print(str_items)

# print(int_items)  



# def new_sum(new_num_lists):
#     total = 0
#     for i in new_num_lists:
#       if isinstance(i,float) or isinstance (i,int):
#               total += 1
#   return total


#new_sum(items)








import datetime


class msg():

    user_details = []
    messages = []
    basic_msg = """Hi {name}!

                Thank you for the purchase on {date}
                of worth {price}.
                Have a great day!

                Regards,
                Ayush
"""
    
    def user_new(self,name,price):
        name = name[0].upper() + name[1:].lower()
        price = "%.2f" %(details["price"])
        details = {
    	    "name": name,
    	    "price": price,
    	}
        today = datetime.time.today()
        date_text = '{today.date}/{today.month}/{today.year}'.format(today=today)
        details['date'] = date_text
        self.user_details.append(details)
    
    def get_details(self):
    	return self.user_details

    def new_msg(self):
        if len(self.user_details) > 0:
            for details in self.get_details():
                name = details["name"]
                price = detail["price"]
                date = details["date"]
                messages = self.basic_msg
                new_msg = basic_msg.format(
             	    name = name,
            	    date = date,
            	    price = price 
            	)
            self.messages.append(new_msg)
        return self.messages
    return []	    

            
            	
instance = msg()
instance.user_new("Rahul",345.56)
instance.user_new("gaurAv",300.00)
instance.user_new("marwadi",800.00)
instance.get_details()

