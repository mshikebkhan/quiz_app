import requests
import json
import os

parameters = {
    "amount": 10,
    "type": "boolean",
    "category": 27
}

# ✅ Use Documents folder (always writable by user)
json_file_path = os.path.join(os.path.expanduser("~"), "Documents", "question_data_file.json")

def get_response():
    try:
        # Try to fetch fresh data from API
        response = requests.get(url="https://opentdb.com/api.php", params=parameters)
    except:
        try:
            with open(json_file_path, 'r') as question_data_file:
                question_data = json.load(question_data_file)
        except FileNotFoundError:
            print("No offline data found, please connect to internet.")
            question_data = []
    else:
        response.raise_for_status()
        question_data = response.json()["results"]
        # Save to user Documents folder for offline use
        try:
            with open(json_file_path, 'w') as question_data_file:
                json.dump(question_data, question_data_file)
        except PermissionError:
            print("❌ Cannot write offline data. Permission denied.")
    return question_data
