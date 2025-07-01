# name = input("What is your name? ")
# print(f"Hello, {name}")

# favorite_food = input("Enter your favorite food: ")
# print(f"Your favorite food is {favorite_food}")

# print("End of file")

# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")
# print(f"Good morning {first_name} {last_name}")


# ask the user for their year of birth and tell them how old they are

# year_of_birth = input("Enter your year of birth: ")
# current_year = 2025
# age = current_year - int(year_of_birth)
# print(f"You are {age} years old")


# year_of_birth = int(input("Enter your year of birth: "))
# current_year = 2025
# age = current_year - year_of_birth
# print(f"You are {age} years old")


# year_of_birth = int(input("Enter your year of birth: "))
# print(f"You are {2025 - year_of_birth} years old")


# print(f"You are {2025 - int(input("Enter your year of birth: "))} years old")


# from datetime import datetime

# year_of_birth = input("Enter your year of birth: ")
# current_year = datetime.now().year
# age = current_year - int(year_of_birth)
# print(f"You are {age} years old")


# from datetime import datetime
# print(datetime.today())
# print(datetime.today().year)
# print(datetime.today().month)
# print(datetime.today().day)
# print(datetime.today().hour)
# print(datetime.today().minute)
# print(datetime.today().second)


# ASSIGNMENT CORRECTION
# 1. Write a program that asks the user for their name and then greets them with their 
# name: Print a greeting message that includes the user's name in the format "Hello, {name}!".
# name = input("Enter your name: ")
# print(f"Hello, {name}!")


# 2. Ask the user for their birth year and calculate their age. Print the user's age in the 
# format “You are {age} years old.”.
# from datetime import datetime

# birth_year = int(input("What year were you born: "))
# age = datetime.now().year - birth_year
# print(f"You are {age} years old.")


# 3. Ask the user for their favourite color. Print a statement that includes the color in the format “Your favorite color is {favourite_color}.”.
# favourite_color = input("What is your favorite color? ")
# print(f"Your favorite color is {favourite_color}.")

# 4. Ask the user to input some text and check if it is a palindrome. A palindrome is a word, phrase, or sequence that reads the same backwards as forwards, e.g. `madam` or `nurses run` or `121`.
# Print a statement in the format “It is {is_palindrome} that {text} is a palindrome.”. `is_palindrome` is either `True` or `False`.
# text = input("Enter some text: ")
# print(text.lower().replace(" ", ""))
# print(text[::-1].lower().replace(" ", ""))
# print(text)
# cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
# print(cleaned_text)

# is_palindrome = text.lower().replace(" ", "") == text[::-1].lower().replace(" ", "")
# print(f"It is {is_palindrome} that {text} is a palindrome.")

# 5. Create a program that asks the user to input a password and checks if it meets certain criteria (at least 8 characters and not more than 30 characters).
# Print a statement in the format “It is {is_valid} that the password fulfils the criteria.”. `is_valid` is either `True` or `False`.
# Bonus point if you can hide the password input from displaying on the screen as clear text.

# from getpass import getpass

# import getpass
# tkinter, pygame


# password = getpass.getpass("Enter your password: ")
# password = getpass("Enter your password: ")
# is_valid = 8 <= len(password) <= 30
# is_valid = len(password) >= 8 and len(password) <= 30
# print(f"It is {is_valid} that the password fulfils the criteria.")



# 6. Write a program that asks the user for their weight (in kilograms) and height (in meters) and calculates their Body Mass Index (BMI). Calculate the BMI using the formula BMI = weight / (height ** 2). Round the BMI to 2 decimal places. Print a statement in the format “Your BMI is {BMI}”.
# weight = float(input("Enter your weight in kg: "))
# height = float(input("Enter your height in meters: "))
# bmi = round(weight / (height ** 2), 2)
# print(f"Your BMI is {bmi}")