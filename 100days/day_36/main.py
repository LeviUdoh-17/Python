import requests
import smtplib

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://api.marketaux.com/v1/news/all"

API_KEY = "GB10NMQO4FWH59BW"
NEWS_API_KEY = "NpTplpTbMXkwpIpkl1LJ5t7a5a9NtDaG7l97RE6v"
password = "awydkdsgjgvtjzam"
my_email = "ukaraobong15@gmail.com"
    
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

params={
    "function": "TIME_SERIES_INTRADAY",
    "symbol": STOCK_NAME,
    "apikey": API_KEY,
    "interval": "60min"
}
news_params={
    "api_token": NEWS_API_KEY,
    "symbols": STOCK_NAME,
    "filter_entities": True
}
data = requests.get(STOCK_ENDPOINT, params=params)
stocks = data.json()
closing_stock_price = []
for i, r in stocks.items():
    if i == "Time Series (60min)":
        for key, values in r.items():
            closing_stock_price.append(values["4. close"])
company = ""
news_highlight = ""
yesterday_closing_stock = float(closing_stock_price[1])
today_closing_stock = float(closing_stock_price[0])
difference =abs(yesterday_closing_stock-today_closing_stock)
news_data = requests.get(NEWS_ENDPOINT, params=news_params)
news = news_data.json()
print((difference/yesterday_closing_stock)*100)
if (difference/yesterday_closing_stock)*100 > 4: 
    print("Good News")
    for i, r in news.items():
        if i == "data":
            for item in r:
                news_highlight = item['description']
                for key, value in r[2].items():
                    if key == "entities":
                        for b, c in value[0].items():
                            if b == "name":
                                company = c                
    with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
        # connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="leviudoh17@gmail.com", msg=f"Subject: Stock News\n\n{company}\n{news_highlight}")


    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
# """
# TSLA: 🔺2%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
# or
# "TSLA: 🔻5%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
# """