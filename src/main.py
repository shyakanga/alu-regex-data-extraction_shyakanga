import re
import json
import os


def extract_emails(content):
    #This regex checks that: 
    # - the email has atleast a letter at the username part and after the @
    # - for the domain, it can have characters separated with - and can have multiple subdomains
    email_pattern = r"\w+-?\.?[a-z0-9]+?-?[0-9]?\.?[A-Za-z0-9]?@\w+-?(?:[\.?\w+-?]+)?[A-Za-z+][0-9]?"
    return re.findall(email_pattern, content, re.MULTILINE)


def extract_hashtags(content):
    #This regex uses a lookbehind to check a space before a # that can eb follwoed by multpiple characters
    hashtag_pattern = fr"(?<=\s)#\w+"
    return re.findall(hashtag_pattern, content)


def extract_locations(content):
    #This regex searchees for [loc:] and then groups everything in there to get the final result as the location
    location_pattern = fr"\[loc:(.+?)\]"
    return re.findall(location_pattern, content)


def extract_times(content):
    #This regex checks for 2 grouped digits separated by a : three times to get a 24h formatted date
    time_pattern = r"\d{2}:\d{2}:\d{2}"
    return re.findall(time_pattern, content)


def extract_phone_numbers(content):
    #This regex checks for a phone number with these creteria: it must must start with a +, then the following number should between 1 to 9 because there is no country code of 0, then there is an optional whitespace, then what follows allows to use braces to format the phone number's region between 1 to 3 digits, then the rest are digits that can have spaces between them, ad they must not exceed 14 but not less than 6 to be inclusive for all countries
    phone_pattern = r"^\+[1-9]{1,3}\s?(\([0-9]{1,3}\))?(\s?\d){6,14}$"
    return re.findall(phone_pattern, content, re.MULTILINE)


def extract_credit_cards(content):
    #This regex checks for 16 digits that are grouped in 4s and can be separated by either a space or a -, and they are optional
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
