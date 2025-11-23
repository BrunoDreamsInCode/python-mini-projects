# Stock Price Alert -- Automated Email Notifier

> Python project that monitors stock price changes and sends news alerts
> via email.

This project is a **Stock Price Alert System** built with Python.\
It checks the daily percentage change of a given stock using a financial
API and sends an email alert with **relevant news articles** when the
stock rises or falls beyond a defined threshold.

Ideal for learning automation, APIs, and email handling in Python.

------------------------------------------------------------------------

## 📌 Features

-   Monitors daily price changes of any stock\
-   Pulls the latest related news articles\
-   Sends formatted email alerts via Gmail SMTP\
-   Error handling for API inconsistencies\
-   Clear and readable logic for beginners\
-   Easily hostable on services like PythonAnywhere

------------------------------------------------------------------------

## 📸 Example Email Alert

```{=html}
<!-- Add screenshot if available -->
```
<img width="1919" height="582" alt="img_1" src="https://github.com/user-attachments/assets/f97018a7-9598-45e7-999d-f854277aaaab" />



------------------------------------------------------------------------

## 🧠 Learning Goals

-   Consuming REST APIs\
-   Parsing JSON data\
-   Sending emails with `smtplib`\
-   Automating tasks\
-   Working with environment variables\
-   Deploying on PythonAnywhere

------------------------------------------------------------------------

## ⚙️ How It Works

1.  Fetch daily stock prices\
2.  Calculate percentage movement\
3.  If change exceeds threshold:
    -   Get related news\
    -   Compose formatted text\
    -   Send email alert

------------------------------------------------------------------------

## ▶️ How to Run

1.  Configure environment variables:

```{=html}
<!-- -->
```
    STOCK_API_KEY=your_stock_api_key
    NEWS_API_KEY=your_news_api_key
    MY_EMAIL=your_email@gmail.com
    MY_PASSWORD=your_email_password
    TO_EMAIL=destination_email

2.  Run the script:
```bash
  python3 main.py
```

------------------------------------------------------------------------

## 📁 File Structure

-   `main.py` --- main script with stock and news logic\
-   `README.md` --- project documentation\
-   `images/` --- optional folder for screenshots

------------------------------------------------------------------------

## 📝 Example Output

    TSLA: 🔻-4.12%

    Article 1 title
    Article 1 description
    Article 1 link

    Article 2 title
    Article 2 description
    Article 2 link

------------------------------------------------------------------------

## 🧰 Requirements

    requests
    smtplib  (built‑in)
    datetime (built‑in)
    os       (built‑in)

------------------------------------------------------------------------

## 📄 License

Free to use and modify for educational purposes.
