# Rain Alert – Weather Forecast Notifier

> Python project that checks the weather forecast and sends an email alert if rain is expected.

This project is a **Weather Forecast Notifier** built with Python.  
It uses the OpenWeatherMap API to check the forecast for a specific location and sends an email alert when rain is predicted.  
It can be hosted on platforms like PythonAnywhere to run automatically.

## Features

- Fetches weather forecast using OpenWeatherMap API  
- Checks multiple upcoming forecast periods  
- Sends email alert if rain is expected  
- Lightweight and easy to configure  
- Can run automatically on cloud platforms like PythonAnywhere  

## Screenshots
### Example Email Alert
<!-- Add screenshot of email -->
![img_1.png](img_1.png)

## Learning Goals

- Practice working with REST APIs in Python  
- Understand JSON data parsing  
- Automate tasks using scripts  
- Send email programmatically using `smtplib`  
- Learn environment variable handling for sensitive data  
- Deploy and run Python scripts on PythonAnywhere  

## How to Run

1. Set your environment variables for API key and email credentials:

```
OWM_API_KEY=your_openweathermap_api_key
MY_EMAIL_ENV=your_email
MY_PASSW_ENV=your_email_password
```

2. Run the script:

```
python main.py
```

## File Structure

- `main.py` — main script for fetching weather and sending emails  
- `requirements.txt` — optional, lists any dependencies (requests, smtplib, etc.)  
- `images/` — store screenshots for README  

## Example Behavior

```
Weather forecast retrieved for Jundiaí, SP  
Forecast shows rain in the next 4 periods  
Email sent: "Don't forget to bring an umbrella"  
```

## Requirements

```
requests
smtplib (built-in)
os (built-in)
```

## License

This project is free to use and modify for educational purposes.

