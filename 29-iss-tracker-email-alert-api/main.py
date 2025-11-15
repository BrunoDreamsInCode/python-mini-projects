import smtplib
import requests, time
from datetime import datetime

# Set your own latitude and longitude here.
# You can find your coordinates using this tool:
# https://www.latlong.net/convert-address-to-lat-long.html
MY_LAT = -23.187080
MY_LNG = -46.884048
TIME_FORMAT = 0

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": TIME_FORMAT
}

def check_iss_position():
    # Fetch current ISS coordinates
    response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
    response_iss.raise_for_status()
    data_iss = response_iss.json()

    iss_lat = float(data_iss["iss_position"]["latitude"])
    iss_long = float(data_iss["iss_position"]["longitude"])

    return iss_lat, iss_long

def iss_near(iss_lat, iss_lng):
    # Check if ISS is within +/-5 degrees of your location
    if (MY_LAT - 5 <= iss_lat <= MY_LAT + 5) and (MY_LNG - 5 <= iss_lng <= MY_LNG + 5):
        return True
    return False

def is_dark():
    # Determine if it's currently dark at your location
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour

    return time_now >= sunset or time_now <= sunrise

run_time = 0
while True:
    iss_lat, iss_lng = check_iss_position()

    # Trigger email only when ISS is near AND it's dark
    if iss_near(iss_lat, iss_lng) and is_dark():
        my_email = "YOUR_EMAIL_HERE"
        my_password = "YOUR_APP_PASSWORD_HERE"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="bruno.dreams.in.code@gmail.com",
                msg=(
                    "Subject:Look at Sky🌃!\n\n"
                    "The International Space Station is passing near your location right now!\n"
                    "Look up at the sky and enjoy the view!"
                )
            )

    run_time += 1
    print(f"This application runs every 60s\nRun times: {run_time}")
    time.sleep(60)
