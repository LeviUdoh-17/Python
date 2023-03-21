import datetime as dt
import smtplib
from random import choice

my_email = "ukaraobong15@gmail.com"
password = "analjatfyascjprg"
now = dt.datetime.now()
day_of_the_week = now.weekday()
with open("100days/day_32/quotes.txt", "r") as file:
    quotes = file.readlines()
    quote_of_the_day = choice(quotes)

if day_of_the_week == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="ukaraobong17@yahoo.com", msg=f"Subject: Monday Motivation\n\n{quote_of_the_day}.")
