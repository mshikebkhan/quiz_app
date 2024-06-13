import requests
import json

parameters = {
    "amount": 10,
    "type": "boolean",
    "category": 27
}

def get_response():
    try:
        # First try to get response from API (for fresh data).
        response = requests.get(url="https://opentdb.com/api.php", params=parameters)
    except:
        # Incase there is no internet (OFFLINE!).
        try:
            # Try to load offline data.
            with open("question_data_file.json", 'r') as question_data_file:
                question_data = json.load(question_data_file)
        except FileNotFoundError:
            # If file not found.
            print("No offline data found, please connect to internet.")
    else:
        # Get data from API response.
        response.raise_for_status()
        question_data = response.json()["results"]
        # Save data for offline use.
        with open("question_data_file.json", 'w') as question_data_file:
            json.dump(question_data, question_data_file)
    return question_data


