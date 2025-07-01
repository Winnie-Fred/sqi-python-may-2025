import re


email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

phone_num_pattern = r"\+234 \d{3} \d{3} \d{4}"

with open("reviews.txt", "r") as f:
    contents = f.read()
    emails = re.findall(email_pattern, contents)

    with open("emails.txt", "w") as f:
        f.write("\n".join(emails))


    phone_nums = re.findall(phone_num_pattern, contents)
    with open("phone_numbers.txt", "w") as f:
        f.write("\n".join(phone_nums))