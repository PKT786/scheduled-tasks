import os
import datetime as dt
import smtplib
import pandas
import random
my_email = MY_EMAIL
password = MY_PASSWORD
PLACEHOLDER_NAME = "[NAME]"
##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

now = dt.datetime.now()
print(now.day)

data = pandas.read_csv("birthdays.csv")
birthday_data = data.to_dict(orient="records")
print(birthday_data)

for birthday in birthday_data:
    if now.day == int(birthday["day"]) and now.month == int(birthday["month"]):
       print(birthday["day"], birthday["month"], birthday["name"])
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
       random_num = random.randint(1, 3)
       with open(f"letter_templates/letter_{random_num}.txt") as file:
           file_data = file.read()
           print(file_data)

           new_data = file_data.replace(PLACEHOLDER_NAME, birthday["name"] )
           print(new_data)
           
       # 4. Send the letter generated in step 3 to that person's email address.
       with smtplib.SMTP("smtp.gmail.com", 587) as connection:
           connection.starttls()
           connection.login(user=my_email, password=password)
           connection.sendmail(from_addr=my_email, to_addrs=birthday["email"],
                                  msg=f"Subject:Happy Birthday\n\n{new_data}")







