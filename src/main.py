import re
import json
import os


def extract_emails(content):
    email_pattern = fr"\w*\.\w*@alueducation|alumni.alueducation|si.alueducation.com"
    return re.findall(email_pattern, content, re.MULTILINE)


def extract_hashtags(content):
    hashtag_pattern = fr"(?<=\s)#\w+"
    return re.findall(hashtag_pattern, content)


def extract_locations(content):
    location_pattern = fr"\[loc:(.+?)\]"
    return re.findall(location_pattern, content)


def extract_times(content):
    time_pattern = r"\d{2}:\d{2}:\d{2}"
    return re.findall(time_pattern, content)


def extract_phone_numbers(content):
    phone_pattern = r"^\+[1-9]{1,3}\s?(\([0-9]{1,3}\))?(\s?\d){6,14}$"
    return re.findall(phone_pattern, content, re.MULTILINE)


def extract_credit_cards(content):
    credit_card_pattern = r"\d{4}\-?\s?\d{4}\-?\s?\d{4}\-?\s?\d{4}\-?\s?"
    return re.findall(credit_card_pattern, content)


input_path = "input/raw-text.txt"
output_path = "output/sample-output.json"

with open(input_path, "r", encoding="utf-8") as f:
    content = f.read()

results = {
    "emails": extract_emails(content),
    "hashtags": extract_hashtags(content),
    "locations": extract_locations(content),
    "times": extract_times(content),
    "phone_numbers": extract_phone_numbers(content),
    "credit_cards": extract_credit_cards(content),
}

for key, values in results.items():
    print(f"{key}:")
    for value in values:
        print(f"  - {value}")
    print()

os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)
