import requests, smtplib
from datetime import date, timedelta


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
FUNCTION = "TIME_SERIES_DAILY"

API_KEY_STOCK = "your_stock_api_key"
API_KEY_NEWS = "your_news_api_key"

STOCK_ENDPOINT = "https://www.alphavantage.co/query?"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything?"

MY_EMAIL = "your_email@gmail.com"
MY_PASSWORD = "your_email_password"
TO_EMAIL = "destination_email"

DIF_PERCENTAGE = 5


# Returns the last 2 business days from the API data
def get_last_business_days(data):
    available_days = sorted(data["Time Series (Daily)"].keys(), reverse=True)
    day1 = available_days[0]
    day2 = available_days[1]
    return day1, day2


# Percent difference calculation
def change_value(before_yesterday_closing_price, yesterday_closing_price):
    difference = yesterday_closing_price - before_yesterday_closing_price
    final_difference = round((difference / before_yesterday_closing_price) * 100, 2)
    return final_difference


# Sends UTF-8 email (supports emojis)
def sent_email(STOCK, email_body):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)

        msg = (
            f"Subject: News for {STOCK}\n"
            f"Content-Type: text/plain; charset=utf-8\n\n"
            f"{email_body}"
        )

        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=TO_EMAIL,
            msg=msg.encode("utf-8")
        )


# ===== STOCK DATA =====

stock_params = {
    "function": FUNCTION,
    "symbol": STOCK,
    "apikey": API_KEY_STOCK,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()

yesterday, before_yesterday = get_last_business_days(data)

yesterday_closing_price = float(data['Time Series (Daily)'][yesterday]['4. close'])
before_yesterday_closing_price = float(data['Time Series (Daily)'][before_yesterday]['4. close'])

print(f"\n{before_yesterday}, close value: {before_yesterday_closing_price}")
print(f"{yesterday}, close value: {yesterday_closing_price}")

# Artificial boost for testing (optional)
stock_change = change_value(before_yesterday_closing_price, 90)

print(f"Difference: {stock_change}%")


# ===== NEWS DATA =====

news_params = {
    "apiKey": API_KEY_NEWS,
    "q": COMPANY_NAME,
    "sortBy": "publishedAt",
}

response = requests.get(NEWS_ENDPOINT, params=news_params)
json_data = response.json()

articles = json_data.get("articles", [])[:3]


# ===== EMAIL SENDING =====

print(f"\nSTOCK CHANGE = {stock_change}%")
print(f"Minimum threshold = {DIF_PERCENTAGE}%\n")

# Positive movement
if stock_change > DIF_PERCENTAGE:
    email_body = f"{STOCK}: 🔺{stock_change}%\n\n"

    for article in articles:
        desc = article["description"].strip()
        email_body += (
            f"{article['title']}\n"
            f"{desc}\n"
            f"{article['url']}\n\n"
        )

    sent_email(STOCK, email_body)

# Negative movement
elif stock_change < DIF_PERCENTAGE * -1:
    email_body = f"{STOCK}: 🔻{stock_change}%\n\n"

    for article in articles:
        desc = article["description"].strip()
        email_body += (
            f"{article['title']}\n"
            f"{desc}\n"
            f"{article['url']}\n\n"
        )

    sent_email(STOCK, email_body)

else:
    print("Small change — No email sent.")