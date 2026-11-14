
#importing libraries
import datetime as dt
import smtplib
import pandas as pd
import random
import os
#my_data
my_email=os.environ.get("MY_EMAIL")
my_password=os.environ.get("MY_PASSWORD")

#today
now = dt.datetime.now()
month = now.month
day = now.day
today = (month, day)
#opening file
data=pd.read_csv("birthdays.csv")
#creating dictionary
birthdays_dict={(data_row["month"],data_row["day"]):data_row for (index,data_row) in data.iterrows()}
#condition
if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path=f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents=letter_file.read()
        contents=contents.replace("[NAME]",birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email,my_password)
        connection.sendmail(my_email,birthday_person["email"],f"Subject:Happy Birthday!!\n\n{contents}")




