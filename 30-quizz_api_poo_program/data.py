import requests

# API parameters (fetch 10 True/False questions)
parameters = {
    "amount": 10,
    "type": "boolean",
}

# Request questions from the Open Trivia DB API
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()

# Parse JSON and extract question list
data = response.json()
question_data = data["results"]