# from collections import Counter

# with open("simple_data.csv", "r") as f:
#     contents = f.read()
#     # contents = f.readlines()


# rows = contents.strip().split("\n")
# headers = rows[0]
# rows = rows[1:]
# names = []
# ages = []
# sum_of_ages = 0
# names_and_ages = []
# for row in rows:
#     row_id, name, age, country = row.split(",")
#     names.append(name)
#     age = int(age)
#     ages.append(age)
#     names_and_ages.append({"name": name, "age": age})

# names.sort()
# sum_of_ages = sum(ages)
# print(f"Avg age: {sum_of_ages/len(rows)}")


# age_occurrences = dict(Counter(ages))


# most_occurring_age = list(age_occurrences.keys())[0]
# no_of_occurences_most_occuring_age = list(age_occurrences.values())[0]
# for age, occurence in age_occurrences.items():
#     if occurence > no_of_occurences_most_occuring_age:
#         no_of_occurences_most_occuring_age = occurence
#         most_occurring_age = age

# print("Most occuring age: ", most_occurring_age)

# most_occurring_age_people = []
# for name_age in names_and_ages:
#     name, age = name_age["name"], name_age["age"]
#     if age == most_occurring_age:
#         most_occurring_age_people.append(name)


# print(f"People with the most occuring age: {most_occurring_age_people}")


# from datetime import datetime
# with open("created-with-python.md", "a") as f:
#     f.write(f"""This file was created by Python on {datetime.now()}.
# We are learning how to read from and write to files using Python.""")



# Output
# Line 1: Hello
# Line 2: I am at SQI today
# Line 3: I am a student
# Line 4: I love Python
# Line 5: Python is amazing

# with open("new_file.txt", "r") as f:
#     lines = f.readlines()
#     for idx, line in enumerate(lines, start=1):
#         print(f"Line {idx}: {line.strip()}")


# MANUAL FILE HANDLING
# f = open("new_file.txt", "w")
# f.write("This is new content")
# f.close()



# import math

# print(math.sqrt(25))

# print(math.pow(4, 3))

# print(math.radians(40))

# print(math.sin(math.radians(90)))

# print(math.pi)


import datetime


# print(datetime.datetime.now())

# print(datetime.datetime.now().year)
# print(datetime.datetime.now().month)
# print(datetime.datetime.now().date())
# print(datetime.datetime.now().day)
# print(datetime.datetime.now().hour)
# print(datetime.datetime.now().minute)
# print(datetime.datetime.now().second)



# first_day_in_june = datetime.date(2025, 6, 1)

# one_week = datetime.timedelta(weeks=1)

# one_week_after_june_1 = first_day_in_june + one_week

# print(one_week_after_june_1)


# first_day_in_june = datetime.datetime(2025, 6, 1, 4, 30, 23)

# formatted_june_1 = first_day_in_june.strftime("%d/%m/%Y, %H:%M:%S")

# print(formatted_june_1)
# print(type(formatted_june_1))

# string parse time
# date = "06-25-2025"

# formatted_date = datetime.datetime.strptime(date, "%m-%d-%Y")

# three_days = datetime.timedelta(days=3)

# three_days_ago = formatted_date - three_days
# print(three_days_ago)


# birth_date_str = input("Enter your birth date and month in DD-MM format e.g. 23-05 (23rd of May): ").strip()
# current_year = datetime.datetime.now().year
# birth_date = datetime.datetime.strptime(f"{birth_date_str}-{current_year}", "%d-%m-%Y").date()
# print(birth_date)
# today = datetime.datetime.now().date()
# if birth_date > today:
#     print("It isn't your birthday yet")
# elif birth_date < today:
#     print("Your birthday has passed")
# else:
#     print("Hapy birthday to you 🥳")

# PyPi

# Linux was created Linus Torvalds
# Git was created Linus Torvalds


# pip install requests bs4
# package manager

# pip installs python


# virtual environment

from pathlib import Path
# # c:\Users\Dell\Documents\SQI\SQI_PYTHON_APR\dictionaries.py

with open(Path("c:\Users\Dell\Documents\SQI\SQI_PYTHON_APR\dictionaries.py"), "r", encoding="utf-8") as f:
    contents = f.read()
    print(contents)


