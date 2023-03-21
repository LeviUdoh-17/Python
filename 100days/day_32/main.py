# import smtplib

# my_email = "ukaraobong15@gmail.com"
# password = "awydkdsgjgvtjzam"
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email, 
#         to_addrs="ukaraobong17@yahoo.com", 
#         msg='Subject:Hello\n\nHello this is Levi, thank you for the cake'
#     )
import datetime as dt
now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year=2003, month=6, day=4)
print(date_of_birth)