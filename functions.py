# def my_func():
#     print("This code is running from my_func()")

# my_func()

# def greet(name):
#     print(f"Good morning, {name}")


# my_name = "Winnie"
# greet(my_name)


# def add_2_nums(a, b):
#     print(f"{a} + {b} = {a+b}")

# result = add_2_nums(3, 6)
# print(result)


# def add_2_nums(a, b):
#     return f"{a} + {b} = {a+b}"

# result = add_2_nums(3, 6)
# print(result)

# def add_2_nums(a, b):
#     return f"{a} + {b} = {a+b}"

# result = add_2_nums(3, 6)
# print(result)



# Write a function raise_to_power(base, exponent) that prints the result of base raised to the power of exponent
# my_name = "Winifred"
# my_name_upper = my_name.upper()
# print(my_name_upper)

# def greet(name, time_of_day):
#     return f"Good {time_of_day}, {name}!"

# greeting = greet("Winnie", "morning")
# print(greeting)


# Write a function multiply_nums(num1, num2) that returns the result of multiplying num1 by num2.
# After, print the result of the function

# def multiply_nums(num1, num2):
#     return num1 * num2

# print(multiply_nums(4, 5))


# Write a function that checks if an email address contains "@", ends with ".com" and has at least 8 chard
# If all these are not satsified, the function should return False
# Otherwise, return True 

# def validate_email_address(email: str):
#     has_at_symbol = False
#     ends_with_dot_com = False
#     has_at_least_8_chars = False
#     if "@" in email:
#         has_at_symbol = True
#     if email.endswith(".com"):
#         ends_with_dot_com = True
#     if len(email) >= 8:
#         has_at_least_8_chars = True
#     return has_at_symbol and ends_with_dot_com and has_at_least_8_chars

# print(validate_email_address("winnie@gmail.com"))


# def validate_email_address(email: str):

#     if "@" not in email:
#         return False
    
#     if not email.endswith(".com"):
#         return False
    
#     if len(email) < 8:
#         return False
#     return True

# print(validate_email_address("winniegmail.com"))


# def greet():
#     print("Running from inside greet() func")

# print("Running before greet() call")
# greet()
# print("Running after greet() call")


# Output
# Running before greet() call
# Running form inside greet() func
# Running after greet() call



# Write a function called square_num(num) that returns the square of num
# Print the result

# def square_num(num):
#     # return num * num
#     return num ** 2

# print(square_num(12))


# Write a function that returns True if num is even, otherwise, return False
# Print the result 

# # BEGINNER
# def is_even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False

# print(is_even(13))

# # INTERMEDIATE

# def is_even(num):
#     if num % 2 == 0:
#         return True
#     return False

# print(is_even(13))


# ADVANCED

# def is_even(num):
#     return num % 2 == 0

# print(is_even(13))

# def is_even(num):
#     print(num % 2 == 0)

# print(is_even(13))


# def collect_user_details(first_name, last_name, age, password, confirm_password):

#     return first_name, last_name, age, password, confirm_password

# first_name = input("Enter your first name: ").strip()
# last_name = input(":Enter your last name: ").strip()
# age = int(input("Enter your age: "))
# password = input("Enter your password: ").strip()
# confirm_password = input("Confirm your password: ").strip()
# print(collect_user_details(first_name, last_name, age, password, confirm_password))

# SIGN USERS UP
# 1. Collect the user's details
# 2. Validate the details
# 3. Add them to the fake_db and display a success message

# def collect_user_details():
#     first_name = input("Enter your first name: ").strip()
#     last_name = input("Enter your last name: ").strip()
#     age = int(input("Enter your age: "))
#     password = input("Enter your password: ").strip()
#     confirm_password = input("Confirm your password: ").strip()

#     return first_name, last_name, age, password, confirm_password


# def validate_user_details(first_name, last_name, age, password, confirm_password):
#     if not first_name:
#         print("First name cannot be blank")
#         return False
#     if not last_name:
#         print("Last name cannot be blank")
#         return False
#     if age < 1:
#         print("Age must be positive")
#         return False
#     if not password:
#         print("Password cannot be balnk")
#         return False
#     if not confirm_password:
#         print("Confirm Password cannot be balnk")
#         return False
#     if password != confirm_password:
#         print("Passwords don't match")
#         return False
#     return True
    

# fake_db = []
# def populate_fake_db(first_name, last_name, age, password):
#     fake_db.append({"first_name": first_name, "last_name": last_name, "age": age, "password": password})
    # print(f"{first_name} {last_name} registered successsfully")
    


# while True:
#     first_name, last_name, age, password, confirm_password = collect_user_details()
#     details_are_valid = validate_user_details(first_name, last_name, age, password, confirm_password)
#     if details_are_valid:
#         populate_fake_db(first_name, last_name, age, password)
#     continue_registering = input("Do you want to register another user? (Y/N): ").strip().lower()

#     if continue_registering != "y":
#         # First name: ______, Last name: _______
#         # First name: ______, Last name: _______
#         # First name: ______, Last name: _______
#         # First name: ______, Last name: _______
        # for user in fake_db:
        #     print(f"First name: {user["first_name"]}, Last name: {user["last_name"]}, Age: {user["age"]}")
#         break


# def greet(time_of_day, name="Anonymous"):
#     # return f"Good {time_of_day}, {name}🌻"
#     pass

# print(greet(name="Winnie", time_of_day="morning"))


# *args and **kwargs

# def print_nums(num1, num2, num3):
#     print(num1)
#     print(num2)
#     print(num3)


# print_nums(3, 5, 12)


# def print_nums(*nums):
#     for num in nums:
#         print(num)


# print_nums(3, 5, 12, 34, 768, 1567283, 562, 8992, 1038)


# def add_all_nums(*nums):
#     return sum(nums)


# print(add_all_nums(3, 5, 12, 34, 768, 1567283, 562, 8992, 1038))

# 1578697


# def greet_everyone(*names):
#     for name in names:
#         print(f"Hello, {name} 👋")

# greet_everyone("Winnie", "Awwal", "Lekan", "Molayo", "Omolola")


# Take in an arbitrary number of names and using a list comprehension, turn them all to uppercase
# Your function shoudl return a list of all the names uppercased.

# def uppercase_all_names(*names):
#     return [name.upper() for name in names]

# print(uppercase_all_names("Winnie", "Awwal", "Lekan", "Molayo", "Omolola"))
# ["WINNIE", "AWWAL", "LEKAN", "MOLAYO", "OMOLOLA"]


# Take in an arbitrary number of numbers and using a list comprehension, return a tuple of only the numbers that are greater than 50.

# def filter_out_nums_less_than_50(favorite_num, *nums):
#     print(f"my fave num is {favorite_num}")
#     return tuple([num for num in nums if num > 50])

# print(filter_out_nums_less_than_50(45, 89, 12, 43, 90))
# (89, 90)


# **kwargs
# def states_and_their_capitals(location, **states_and_capitals):
#     print(f"I am currently at {location}")
#     for state, capital in states_and_capitals.items():
#         print(f"The capital of {state} is {capital}")

# # states_and_their_capitals("SQI", oyo="Ibadan", osun="Osogbo", ogun="Abeokuta", ondo="Akure")
# states_and_capitals = {
#     "Oyo": "Ibadan",
#     "Osun": "Osogbo",
#     "ogun": "Abeokuta",
#     "ondo": "Akure",
# }
# states_and_their_capitals("SQI", **states_and_capitals)

# def power(base, exponent):
#     if exponent == 0:  # Base case
#         return 1
#     else:
#         return base * power(base, exponent - 1)  # Recursive call

# power(2, 3)
# 2 * power(2, 2)
# 2 * 2 * power(2, 1)
# 2 * 2 * 2 * power(2, 0)
# 2 * 2 * 2 * 1
# 8

# print(power(2, 1000))


# import random
# print("080" + str(random.randrange(1000000, 9999999)))


# name = "Winnie"

# def my_func():
#     global name
#     name = "Omolola"
#     print(f"Name inside my_func: {name}")

# print(f"Name before func call: {name}")
# my_func()
# print(f"Name after func call: {name}")



# color = "red"

# def some_func(name):
#     """
#     Some func
#     """
#     print(name)
#     print(color)

# some_func("Winnie")

# print(name)


# def add_nums(num1: int, num2: int) -> int:
#     """
#     Add nums num1 and num2 together.
#     Return the result.

#     num1: int
#     num2: int
#     Returns:
#     int
#     """
#     return num1 + num2

# print(add_nums(5, 8))

# help(add_nums)

# Write a function is_alliteration(two_word_string) that takes a two-word string and returns True if both words begin with the same letter.
# is_alliteration(‘Levelheaded llama’) —> True
# is_alliteration(‘Crazy Kangaroo’) –> False


# def is_alliteration(two_word_string: str):
#     word1, word2 = two_word_string.lower().split()
#     first_letter_word_1 = word1[0]
#     second_letter_word_2 = word2[0]
#     return first_letter_word_1 == second_letter_word_2

# print(is_alliteration("Levelheaded Llama"))
# print(is_alliteration("Silicon Valley"))

# def is_alliteration(two_word_string: str):
#     word1, word2 = two_word_string.lower().split()
#     return word1[0] == word2[0]



# ASSIGNMENT CORRECTION
# 1. Write a function sum_numbers(a, b) that returns the sum of two numbers.

# def sum_numbers(a, b):
#     return a + b

# print(sum_numbers(34, 21))
# print(sum_numbers(4, 2))


# 2. Write a function is_even(n) that returns True if n is even and False if n is odd.
# def is_even(n):
#     return n % 2 == 0

# print(is_even(16))
# 3. Write a function is_prime(n) that returns True if n is a prime number and False otherwise.
# def is_prime(n):
#     if n <= 1:
#         return False
    
#     for i in range(2, (int(n ** 0.5) + 1)):
#         if n % i == 0:
#             return False
#     return True

# print(is_prime(4))

# 4. Using the is_prime(n) function from number 3, write a function that asks a user for an input n and returns all the prime numbers up to n.
# def primes_up_to_n(number):
#     return [num for num in range(number+1) if is_prime(num)]

# print(primes_up_to_n(int(input("Enter a number: "))))


# def first_n_prime_numbers(number):
#     first_n_primes = []
#     num = 2
#     while len(first_n_primes) < number:
#         if is_prime(num):
#             first_n_primes.append(num)
#         num += 1
#     return first_n_primes

# print(first_n_prime_numbers(100))

# 5. Write a function lesser_of_two_evens(a, b) that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd.

# def lesser_of_two_evens(a, b):
#     if a % 2 == 0 and b % 2 == 0:
#         return min(a, b)
#     return max(a, b)

# print(lesser_of_two_evens(3, 5))  # 5
# print(lesser_of_two_evens(12, 16))  # 12
# print(lesser_of_two_evens(12, 27))  # 27


# 6. Write a function is_alliteration(two_word_string) that takes a two-word string  and returns True if both words begin with the same letter.
# is_alliteration(‘Levelheaded llama’) —> True
# is_alliteration(‘Crazy Kangaroo’) –> False
# def is_alliteration(two_word_string):


# 7. Write a function old_macdonald(name) that capitalizes the first and fourth letters of a name
# old_macdonald(‘macdonald’) —> MacDonald
# Note: ‘macdonald’.capitalize() returns Macdonald, not MacDonald.
# def old_macdonald(name: str):
#     return name[0].upper() + name[1:3] + name[3].upper() + name[4:]
# print(old_macdonald("macdonald"))
# print(old_macdonald("macmahon"))

# def old_macdonald(name: str):
#     return name[0:3].capitalize() + name[3:].capitalize()

# print(old_macdonald("macdonald"))
# print(old_macdonald("macmahon"))


# 8. Write a function spy_game(list_of_ints) that takes in a list of integers and returns True if it contains 007 in order.
# spy_game([1, 2, 4, 0, 0, 7, 5]) —> True
# spy_game([1, 0, 2, 4, 0, 5, 7]) —> True
# spy_game([1, 7, 2, 0, 4, 5, 0]) —> False

# [1, 0, 2, 4, 0, 5, 7]
# [0, 0, 7]
# [1, 0, 2, 4, 0, 5, 89, 12, 23, 0, 5, 2, 7, 23, 0, 12, 45, 78, 0, 8990, 23, 7]
# [0, 0, 0, 7, 0, 0, 7]
# [0, 1, 2, 3, 4, 5, 6]
# 0 -> 2 (+2)
# 1 -> 3 (+2)
# 2 -> 4 (+2)
# def spy_game(list_of_ints):
#     filtered_list = [num for num in list_of_ints if num in [0, 7]] 
#     i = 0
#     while i <= len(list_of_ints) - 3:
#     # while i < len(list_of_ints):
#         triple = filtered_list[i:i+3]
#         if triple == [0, 0, 7]:
#             return True
#         i += 1
#     return False

# print(spy_game([1, 2, 4, 0, 0, 7, 5]))
# print(spy_game([1, 0, 2, 4, 0, 5, 7]))
# print(spy_game([1, 7, 2, 0, 4, 5, 0]))

# def spy_game(list_of_ints):
#     pattern = [0, 0, 7]
#     for num in list_of_ints:
#         if pattern and num == pattern[0]:
#             pattern.pop(0)
#     return not pattern

# print(spy_game([1, 2, 4, 0, 0, 7, 5]))
# print(spy_game([1, 0, 2, 4, 0, 5, 7]))
# print(spy_game([1, 7, 2, 0, 4, 5, 0]))


# def spy_game(list_of_ints):
#     pattern = [0, 0, 7]
#     for num in list_of_ints:
#         if num == pattern[0]:
#             pattern.pop(0)
#         if not pattern:
#             return True
#     return False
# print(spy_game([1, 2, 4, 0, 0, 7, 5]))
# print(spy_game([1, 0, 2, 4, 0, 5, 7]))
# print(spy_game([1, 7, 2, 0, 4, 5, 0]))

# 9. Write a function vol(radius) that computes the volume of a sphere given its radius.
# def vol(radius):
#     return round((4/3) * (22/7) * (radius ** 3), 2)

# print(vol(3))

# 10. Write a function range_check(num, low, high) that checks whether a number is in a given range (inclusive of high and low).
# def range_check(num, low, high):
#     return low <= num <= high
#     # return low <= num and num <= high
#     # return num in range(low, high+1)

# print(range_check(200, 5, 67)) # -> True


# 11. Write a function upper_lower(text) that accepts a string and calculates the number of uppercase letters and lowercase letters.

# 5, 9
# Number of uppercase: 5, Number of lowercase: 9
# def upper_lower(text: str):
#     uppercase = 0
#     lowercase = 0
#     for char in text:
#         if char.isupper():
#             uppercase += 1
#         elif char.islower():
#             lowercase += 1
#     # return uppercase, lowercase
#     return f"Number of uppercase: {uppercase}, Number of lowercase: {lowercase}"

# print(upper_lower("HeLLO You"))


# 12. Write a function unique_list(list_items) that takes in a list and returns a new list with unique elements of the first list. Do not use the set() constructor.
# def unique_list(list_items):
#     unique = []
#     for item in list_items:
#         if item not in unique:
#             unique.append(item)
#     return unique

# print(unique_list([45, 89, "heyy", "heyy", True, False, 45, False]))
# # [45, 89, "heyy", True, False]


# 13.	Write a function multiply(list_items) to multiply all the numbers in a list.
# Sample List: [1, 2, 3, -4]
# Expected output: -24
# def multiply(list_items):
#     result = 1
#     for num in list_items:
#         result *= num
#     return result

# print(multiply([1, 2, 3, -4]))

# def multiply(list_items):
#     result = list_items[0]
#     for num in list_items[1:]:
#         result *= num
#     return result

# print(multiply([1, 2, 3, -4]))


# 14. Write a function is_pangram(text) to check whether a string is a pangram or not. 
# Note: A pangram is a word or sentence that contains every letter of the alphabet at  
# least once. For example: “The quick brown fox jumps over the lazy dog”.
# Hint: Import and use the string module.
# import string
# letters = string.ascii_lowercase

# def is_pangram(text: str):
#     text = text.lower()
#     for letter in letters:
#         if letter not in text:
#             return False
#     return True

# print(is_pangram("The quick brown fox jumps over the lazy dog"))
# print(is_pangram("The quick brown fox"))

# import string
# letters = string.ascii_lowercase
# def is_pangram(text: str):
#     text = text.lower()
#     return set(letters).issubset(text)
#     # return set(letters) <= set(text)

# print(is_pangram("The quick brown fox jumps over the lazy dog"))
# print(is_pangram("The quick brown fox"))
# print(is_pangram("Pack my box with five dozen liquor jugs"))


# 15. 	Write a function are_anagrams(s1, s2) that checks if two strings are anagrams of each
# other. a word, phrase, or name formed by rearranging the letters of another, such as
# spar, formed from rasp.

# def get_char_occurences(text):
#     occurences = {}
#     for char in text:
#         if char in occurences:
#             occurences[char] += 1
#         else:
#             occurences[char] = 1
#     return occurences

# # get_char_occurences("hello") # -> {'h': 1, 'e': 1, 'l': 2, 'o': 1} 

# def are_anagrams(s1: str, s2: str):
#     s1, s2 = s1.lower().replace(" ", ""), s2.lower().replace(" ", "")
#     s1_occurences = get_char_occurences(s1)
#     s2_occurences = get_char_occurences(s2)
#     return s1_occurences == s2_occurences

# print(are_anagrams("spar", "rasp"))
# print(are_anagrams("spar", "raps"))
# print(are_anagrams("angle", "angela"))
# print(are_anagrams("a gentleman", "elegant man"))
# print(are_anagrams("adultery", "true lady"))
# print(are_anagrams("Eleven plus two", "Twelve plus one"))
# print(are_anagrams("Tom Marvolo Riddle", "I am Lord Voldemort"))
# print(are_anagrams("The Morse Code", "Here Come dots"))

# def are_anagrams(s1: str, s2: str):
#     return sorted(s1.lower().replace(" ", "")) == sorted(s2.lower().replace(" ", ""))

# print(are_anagrams("spar", "rasp"))
# print(are_anagrams("spar", "raps"))
# print(are_anagrams("angle", "angela"))
# print(are_anagrams("a gentleman", "elegant man"))
# print(are_anagrams("adultery", "true lady"))
# print(are_anagrams("Eleven plus two", "Twelve plus one"))
# print(are_anagrams("Tom Marvolo Riddle", "I am Lord Voldemort"))
# print(are_anagrams("The Morse Code", "Here Come dots"))


# def sort_string(text: str):
#     # text_list = list(text)
#     # text_list.sort(key=str.lower)
#     # print(text_list)
#     # return "".join(text_list)
#     return "".join(sorted(text, key=str.lower))

# print(sort_string("Hello")) # -> "ehllo"



# 16. 	Write a function calculate_bmi(weight, height) that calculates the Body Mass Index 
# (BMI) given weight in kilograms and height in meters.
# def calculate_bmi(weight, height):
    # return round(weight / (height ** 2), 2)
    
# print(calculate_bmi(75, 1.75))


# def calculate_bmi(weight, height):
#     bmi = round(weight / (height ** 2), 2)
#     if bmi < 18.5:
#         return "You are underweight"
#     if 18.5 <= bmi <= 24.9:
#         return "Your weight is healthy"
#     if 25 <= bmi <= 29.9:
#         return "You are overweight"
#     if bmi >= 30:
#         return "You are obese"
    
# print(calculate_bmi(75, 1.75))
# print(calculate_bmi(175, 1.4))

# 17. Write a function calculate_simple_interest(principal, rate, time) that calculates the 
# simple interest given principal amount, interest rate, and time (in years).
# def calculate_simple_interest(principal, rate, time):
#     return (principal * rate * time) / 100


# Ask the user to enter a color
# Pass this color into a function get_hex_code(color)
# if they enter red, return "The hex code is #FF0000", 
# if they enter blue, return "The hex code is #0000FF", 
# if they enter green, return "The hex code is #008000", 
# if they enter white, return "The hex code is #FFFFFF", 
# if they enter black, return "The hex code is #000000"
# Finally, call the function and print the result.


# def get_hex_code(color):
#     if color == "red":
#         return "The hex code is #FF0000"
#     if color == "blue":
#         return "The hex code is #0000FF"
#     if color == "green":
#         return "The hex code is #008000"
#     if color == "white":
#         return "The hex code is #FFFFFF"
#     if color == "black":
#         return "The hex code is #000000"
#     return "Unsupported color entered"

# print(get_hex_code(input("Enter a color: ").strip().lower()))

# color_hex_code_map = {"red": "#FF0000", "blue": "#0000FF", "green": "#008000", "white": "#FFFFFF", "black": "#000000"}

# def get_hex_code(color):
#     if color in color_hex_code_map:
#         return f"The hex code is {color_hex_code_map[color]}"
#     return "Unsupported color entered"

# print(get_hex_code(input("Enter a color: ").strip().lower()))


# color_hex_code_map = {"red": "#FF0000", "blue": "#0000FF", "green": "#008000", "white": "#FFFFFF", "black": "#000000"}

# def get_hex_code(color):
#     return color_hex_code_map.get(color, "Unsupported color entered")

# print(get_hex_code(input("Enter a color: ").strip().lower()))

# color_hex_code_map = {"red": "#FF0000", "blue": "#0000FF", "green": "#008000", "white": "#FFFFFF", "black": "#000000"}

# def get_hex_code(color):
#     code = color_hex_code_map.get(color)
#     if code is not None:
#         return f"The hex code is {code}"
#     return "Unsupported color entered"

# print(get_hex_code(input("Enter a color: ").strip().lower()))
