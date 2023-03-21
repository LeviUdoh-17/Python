import pandas as pd
import datetime as dt
from random import randint
import smtplib

now = dt.datetime.now()
now_month = now.month
now_day = now.day
data = pd.read_csv("100days/day_32/birthday-wisher/birthdays.csv")
birthdays_dict = {(row.month, row.day): (row.email, row.first_name) for (index, row) in data.iterrows()}
present = (now_month, now_day)

if present in birthdays_dict.keys():
    my_email = birthdays_dict[present][0]
    password = "awydkdsgjgvtjzam"
    with open(f"100days/day_32/birthday-wisher/letter_templates/letter_{randint(1,3)}.txt", "r") as file:
        name = file.readlines()
    name[0] = name[0].replace("[NAME]", birthdays_dict[present][1])
    letter = ""
    for words in name:
        letter += words
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="ukaraobong15@gmail.com", password=password)
        connection.sendmail(from_addr='ukaraobong15@gmail.com', to_addrs=my_email, msg=f"Subject: Happy Birthday\n\n{letter}")