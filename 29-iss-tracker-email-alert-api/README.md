# ISS Overhead Notifier 🚀  
Exercise from 100 Days of Code Python Course  
https://www.udemy.com/course/100-days-of-code/

A Python script that checks the real-time position of the International Space Station (ISS) and notifies you via email whenever it passes near your location **at night**, allowing you to spot it in the sky.

## Features
- Uses the **Open Notify ISS API** to get live ISS coordinates  
- Uses the **Sunrise–Sunset API** to determine if it's currently dark  
- Sends an email automatically when:
  - The ISS is within ±5° latitude and longitude of your location  
  - It is nighttime at your coordinates  
- Loops every 60 seconds  
- Simple and beginner-friendly Python example of APIs + email + automation

## How the email is received
Below is an example of the notification email you will receive when the ISS is passing near your location at night:
<img width="1653" height="327" alt="img" src="https://github.com/user-attachments/assets/4840f27f-5976-4dfb-bf85-7bd23a313391" />

## Commands
The script runs automatically and continuously checks for:
- ISS proximity  
- Darkness at your location  
- Conditions for email alert  

To execute:

```
python main.py
```

## How to Use
1. Clone the repository:
   ```
   git clone https://github.com/your-username/iss-overhead-notifier
   ```
2. Open the code and set your own email, app password, and coordinates directly in the file:
    ```
    MY_EMAIL = "your_email@gmail.com"
    MY_APP_PASSWORD = "your_app_password"
    MY_LAT = -23.187080
    MY_LNG = -46.884048
    ```

3. Run the script:
   ```
   python main.py
   ```
4. Leave it running.  
You’ll get an email whenever the ISS is overhead *at night.*

## Technical Skills
- API requests
- JSON parsing
- Time and astronomical calculations
- Email automation (SMTP)
- Scheduling with loops

## Requirements
- Python 3.x  
- Packages: `requests`

## Notes
- The script checks every 60 seconds  
- Make sure to use your own email and app password
- Public APIs may have request limits
