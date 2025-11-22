# Import necessary modules for HTTP requests, email sending, and environment variables
import requests, smtplib, os

# Define coordinates for location
MY_LAT = -23.225958
MY_LNG = -46.882988

# Get API key from environment variables
api_key = os.environ.get("OWM_API_KEY")

# OpenWeatherMap forecast endpoint
open_weather = "https://api.openweathermap.org/data/2.5/forecast"

# Email credentials from environment variables
my_email = ("MY_EMAIL_ENV")
my_password = ("MY_PASSW_ENV")

# Number of forecast items to retrieve
cnt_count = 4 # 1=3Hours, so 4= 12Hours.

# List to store weather messages
empty_list = []

# Parameters for the API request
parameters = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "appid": api_key,
    "cnt": cnt_count,
}

# Make the API request
forecast = requests.get(open_weather, params=parameters)
forecast.raise_for_status()  # Raise error if request fails
weather_data = forecast.json()  # Parse JSON response

# Flag to check if it will rain
it_will_rain = False

# Loop through forecast data
for forecast_item in weather_data["list"]:
    weather_id = forecast_item["weather"][0]["id"]  # Weather condition code
    if weather_id < 700:  # Codes <700 indicate rain/snow
        empty_list.append(f"{weather_id} - 🌧️ Don't forget to bring an umbrella 🌧️\n")
        it_will_rain = True
    else:  # Clear or sunny weather
        empty_list.append(f"{weather_id} - ☀️ Don't need an umbrella ☀️\n")

# Send email if rain is expected
if it_will_rain:
    with smtplib.SMTP("smtp.gmail.com", timeout=10) as connection:
        connection.starttls()  # Secure the connection
        connection.login(user=my_email, password=my_password)  # Login to email
        connection.sendmail(
            from_addr=my_email,
            to_addrs="RECIVE_EMAIL_ENV",
            msg=(
                "Subject:It will rain soon!\n\n"
                f"Don't forget to bring an umbrella"
            )
        )
    print("E-mail sent - It will rain")
else:
    print("it won't rain")
