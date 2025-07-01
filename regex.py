import re


# Example 1: Simple match
# pattern = r"\bword\b"
# text = "A wordle in a sentence."
# match = re.search(pattern, text)
# if match:
#     print("Match found:", match.group())  # Match found: word
# else:
#     print("Match not found")


# pattern = r"[0-9]+"
# text = "There are 123 apples and 456 oranges."
# matches = re.findall(pattern, text)
# print("Numbers found:", matches)  # Numbers found: ['123', '456']


# pattern = r"\s+"
# text = "This   is a test."
# new_text = re.sub(pattern, "gtevfbkmef", text)
# print("Replaced text:", new_text)  # Replaced text: This is a test.



# pattern = r"\d+"
# text = "This   is a 0te2st."
# print(re.split(pattern, text))

# pattern = r","
# text = "apple, banana    ,  cherry,date"
# print(re.split(pattern, text))


# Example 1: Match an email address
# pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
# text = "Contact us at support@example.1234 for more info."
# match = re.search(pattern, text)
# if match:
#     print("Email found:", match.group())  # Email found: support@example.com
# else:
#     print("No email matching the pattern found")


# Example 2: Extract dates in YYYY-MM-DD format
# pattern = r"\b\d{4}-\d{2}-\d{2}\b"
# text = "The event is on 2023-08-15. Deadline is 2023-08-01."
# dates = re.findall(pattern, text)
# print("Dates found:", dates)  # Dates found: ['2023-08-15', '2023-08-01']


# Example 3: Validate a phone number (US format)
# pattern = r"^\(\d{3}\) \d{3}-\d{4}$"
# phone_number = "(123) 456-7890"
# print(re.match(pattern, phone_number))
# if re.match(pattern, phone_number):
#     print("Valid phone number")  # Valid phone number
# else:
#     print("Invalid phone number")


# ASSIGNMENT CORRECTION

