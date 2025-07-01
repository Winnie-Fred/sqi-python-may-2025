# event = "birthday"

# i = 0

# while i < len(event):
#     char = event[i]
#     print(char)
#     i += 1

# event = "birthday"
# for char in event:
#     print(char)

# yoruba_names = ["Abike", "Adebisi", "Folorunsho", "Kilanko", "Araire", "Desire", "Alubankudi"]

# for yoruba_name in yoruba_names:
# print("something")
# print(yoruba_names)

# for name in yoruba_names:
#     print(name)


# professions = ('teaching', 'law', 'software engineer', 'medicine', 'accounting', 'automobile engineering')
# for profession in professions:
#     print(profession)


# my_dream_job = {"dreamer": "Ms. Molayo", "dream_job": "Data Analyst", "dream_salary": 1_000_000_000}

# for key in my_dream_job:
#     print(key)

# for item in my_dream_job.items():
#     print(item)

# for key, value in my_dream_job.items():
#     print(f"{key} -> {value}")


# states_and_capitals = {"Anambra": "Awka", "Lagos": "Ikeja", "Oyo": "Ibadan", "Osun": "Osogbo", "Ogun": "Abeokuta"}
# for state, capital in states_and_capitals.items():
#     print(f"The capital of {state} is {capital}")

# actions = ["run", "jump", "stop", "walk"]

# for action in actions:
#     if action == "stop":
#         break
#     print(action)

# actions = ["run", "jump", "stop", "walk"]
# for action in actions:
#     if action == "jump":
#         continue
#     print(action)

# print(list(range(35)))
# print(list(range(1, 35)))
# print(list(range(1, 35, 2)))
# print(list(range(2, 35, 2)))
# print(list(range(35, 2, -1)))

# for num in range(35):
#     print(num)

# print all the even numbers between 12 and 20, do not use any if statements

story = "Once upon a time"
# Print every 2nd character from the string story i.e
# O
# c
#
# ...

# for index in range(0, len(story), 2):
#     print(story[index])


# for index in range(0, len(story)):
#     if index % 2 == 0:
#         print(story[index])


# =============================================Assignmnet correction=============================================
# 5, 6, 9
# 5. Write a program that takes a list of numbers (entered as comma-separated values) from the user and removes any duplicate values. Print the new list. Do not use the set() constructor. Use a loop. Example:
# Input: "1, 2, 3, 2, 4, 3"
# Output: [1, 2, 3, 4]

# numbers = input("Enter comma-separated numbers: ").split(",")

# unique_numbers = []

# for number in numbers:
#     number = int(number)
#     if number in unique_numbers:
#         continue
#     unique_numbers.append(number)


# print(unique_numbers)
# numbers = input("Enter comma-separated numbers: ").split(",")

# unique_numbers = []

# for number in numbers:
#     number = int(number)
#     if number not in unique_numbers:
#         unique_numbers.append(number)

# print(unique_numbers)

# 6. Write a program that takes an integer input n from the user and prints the first
# n numbers in the Fibonacci sequence. Example:
# Input: 10
# Output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
# DSA -> Data Structures and Algorithms
# n = int(input("Enter the number of numbers you want in the fibonacci sequence: "))

# fibonacci = [0, 1]

# i = 0
# while i < n - 2:
#     first_num = fibonacci[i]
#     second_num = fibonacci[i+1]
#     next_num = first_num + second_num
#     fibonacci.append(next_num)
#     i += 1

# print(fibonacci)

# fibonacci = [0, 1]

# for i in range(0, n - 2):
#     first_num = fibonacci[i]
#     second_num = fibonacci[i+1]
#     next_num = first_num + second_num
#     fibonacci.append(next_num)

# print(fibonacci)

# 9. Collect a string from the user and use a loop to count the frequency of each character
# in the string. Print each character along with its frequency. Example:
# Input: "hello"
# Output:
# h: 1
# e: 1
# l: 2
# o: 1

# text = input("Enter some text: ").strip().lower()

# occurences = {}

# for char in text:
#     if char in occurences:
#         occurences[char] += 1
#     else:
#         occurences[char] = 1

# print(occurences)


# =============================================Assignmnet correction=============================================


# ENUMERATE
# using while loops
# text = "Tuesday"
# index = 0
# while index < len(text):
#     char = text[index]
#     print(char)
#     index += 1


# text = "Tuesday"
# for index in range(len(text)):
#     char = text[index]
#     print(char)


# colors = ["red", "orange", "purple", "black", "silver", "blue"]
# for index in range(len(colors)):
#     char = colors[index]
#     print(char)

# colors = ["red", "orange", "purple", "black", "silver", "blue"]

# print(list(enumerate(colors)))

# for index, color in enumerate(colors):
#     print(f"Index of {color} is {index}")

# for index, _ in enumerate(colors):
#     print(index)

# sports = ["Basketball", "Volleyball", "Tennis", "Swimming"]

# Output:
# Sports #1 -> Basketball
# Sports #s -> Volleyball
# Sports #1 -> Tennis
# Sports #1 -> Swimming



# for index, sport in enumerate(sports):
#     print(f"Sport #{index + 1} -> {sport}")

# i = 0
# while i <= 10:
#     print(i)
#     i += 1
# else:
#     print("loop has stopped")


# for i in range(11):
#     print(i)
# else:
#     print("loop has stopped")


# sports = ["Basketball", "Volleyball", "Tennis", "Swimming"]

# for i, sport in enumerate(sports):
#     print(f"{i}: {sport}")
#     for j, char in enumerate(sport):
#         print(f"{j}: {char}")


# a) Basketball
# b) Volleyball

# import string
# alphabets = string.ascii_lowercase
# print(alphabets)

# sports = ["Basketball", "Volleyball", "Tennis", "Swimming"] * 100

# print(list(zip(alphabets, sports)))

# for letter, sport in zip(alphabets, sports):
#     print(f"{letter}). {sport}")


# adjectives = ["fierce", "majestic", "playful"]
# animals = ["lion", "eagle", "dolphin"]

# for adjective in adjectives:
#     for animal in animals:
#         print(f"{adjective} {animal}")

# for num in [1, 2, 3]:
#     # print(num)
#     pass

# print("something")


# ===================================ASSIGNMENT===================================
# Use only for loops for the problems below:

# 1. You are given two lists, names and grades. Print them together
names = ['Ken', 'Mia', 'Rose', 'Henry', 'Suzan']
grades = ['A', 'E', 'F', 'C', 'B']

# Expected Output:
# Ken got grade A
# Mia got grade E
# Rose got grade F
# Henry got grade C
# Suzan got grade B

# 2. Print only the items at even indexes
items = ['zero', 'one', 'two', 'three']

# Expected Output:
# 0: zero
# 2: two

# 3 Given two lists of numbers of the same length, print the indices and values of where they differ in a list.
# list1 = [5, 8, 6, 7, 12, 4]
# list2 = [5, 3, 6, 9, 12, 0]

# Expected output:
# [
#   'Index 1: 8 != 3',
#   'Index 3: 7 != 9',
#   'Index 5: 4 != 0',
# ]

# result = []
# print(list(zip(list1, list2)))
# print(list(enumerate(zip(list1, list2))))
# for index, items in enumerate(zip(list1, list2)):
#     if items[0] != items[1]:
#         result.append(f"Index {index}: {items[0]} != {items[1]}")

# print(result)

# OR

# list1 = [5, 8, 6, 7, 12, 4]
# list2 = [5, 3, 6, 9, 12, 0]
# i = 0

# result = []
# while i < len(list1):
#     if list1[i] != list2[i]:
#         result.append(f"Index {i}: {list1[i]} != {list2[i]}")
#     i += 1

# print(result)

# ===================================ASSIGNMENT===================================



# ===================================LIST COMPREHENSION===================================

# Write a for loop to do this. Print a list containing the same items in my_list but all in upper case letters

# my_list = ["drink", "food", "sleep", "read"]

# Output:
# ["DRINK", "FOOD", "SLEEP", "READ"]


# my_list = ["drink", "food", "sleep", "read"]
# my_list_upper = []
# for item in my_list:
#     my_list_upper.append(item.upper())

# print(my_list_upper)


# my_list = ["drink", "food", "sleep", "read"]
# my_list_upper = [item.upper() for item in my_list]
# print(my_list_upper)


# my_list = ["drink", "food", "sleep", "read"]
# len_my_list = []
# for item in my_list:
#     len_my_list.append(len(item))

# my_list = ["drink", "food", "sleep", "read"]
# [5, 4, 5, 4]

# len_my_list = [len(item) for item in my_list]


# list_of_whole_numbers = [43, 45, 87, 12, 3098]
# ['43', '45', '87', '12', '3098']

# list_of_str_numbers = [str(num) for num in list_of_whole_numbers]
# print(list_of_str_numbers)

# animals = ["Hyena", "Zebra", "Ape", "Lion", "Elephant", "Cheetah", "Tiger"]
# # ["1", "1", "1", "0", "2", "2", "1"]

# no_of_e_in_animals = []
# for animal in animals:
#     no_of_e_in_animals.append(str(animal.lower().count("e")))

# print(no_of_e_in_animals)

# animals = ["Hyena", "Zebra", "Ape", "Lion", "Elephant", "Cheetah", "Tiger"]
# no_of_e_in_animals = [str(animal.lower().count("e")) for animal in animals]
# print(no_of_e_in_animals)


# no_of_e_in_animals = []
# for animal in animals:
#     number_of_e = 0
#     for char in animal:
#         # if char == "e" or char == "E":
#         if char in "eE":
#             number_of_e += 1
#     no_of_e_in_animals.append(str(number_of_e))

# print(no_of_e_in_animals)


# numbers = [54, 23, 89, 12, 78, 12]
# print a list of all numbers greater than 30


# numbers = [54, 23, 89, 12, 78, 12]
# # [54, 89, 78]

# nums_greater_than_30 = []
# for num in numbers:
#     if num > 30:
#         nums_greater_than_30.append(num)
# print(nums_greater_than_30)

# numbers = [54, 23, 89, 12, 78, 12]
# nums_greater_than_30 = [num for num in numbers if num > 30]
# print(nums_greater_than_30)

# all even nos between 67 and 102
# even_nos = [num for num in range(67, 103) if num % 2 == 0]
# print(even_nos)


# states = ["Oyo", "Ogun", "Lagos", "Osun", "Anambra"]
# print a list of all the states that start with O, but make the states all lowercase.
# ["oyo", "ogun", "osun"]

# states = ["Oyo", "Ogun", "Lagos", "Osun", "Anambra"]
# states_that_start_with_o = [state.lower() for state in states if state.lower().startswith("o")]
# print(states_that_start_with_o)


# states = ["Oyo", "Ogun", "Lagos", "Osun", "Anambra"]
# # states_that_start_with_o_or_a = [state for state in states if state.startswith("O") or state.startswith("A")]
# # states_that_start_with_o_or_a = [state for state in states if state[0] in "OA"]
# states_that_start_with_o_or_a = [state for state in states if state[0] == "O" or state[0] == "A"]
# print(states_that_start_with_o_or_a)

# nums = [32, 30, 45, 15, 12, 43]
# print a list of all the numbers that are not multiples of 5

# states = ["Oyo", "Ogun", "Lagos", "Osun", "Anambra"]
# print a list of all the states that are not Lagos

# states = ["Oyo", "Ogun", "Lagos", "Osun", "Anambra"]
# not_lagos_states = {state for state in states if state != "Lagos"}

# print(not_lagos_states)

# animals = ["Hyena", "Zebra", "Ape", "Lion", "Elephant", "Cheetah", "Tiger"]
# {"Hyena": 1, "Zebra": 1, "Ape": 1, "Lion": 0, "Elephant": 2, "Cheetah": 2, "Tiger": 1}

# no_of_e_in_animals = {animal: animal.lower().count("e") for animal in animals}
# print(no_of_e_in_animals)


# nums = [45, 23, 67, 12, 43, 89, 20]
# {45: False, 23: False, 67: False, 12: True, 43: False, 89: False, 20: True}
# is_even = {num: num % 2 == 0 for num in nums}
# print(is_even)


# states = ["Oyo", "Ogun", "Lagos", "Osun", "Anambra"]
# not_lagos_states = (state for state in states if state != "Lagos")
# print(list(not_lagos_states))


# states = ["Oyo", "Ogun", "Lagos", "Osun", "Anambra"]
# # [True, True, False, True, False]
# # starts_with_o = all(state.startswith("O") for state in states)
# starts_with_o = any(state.startswith("O") for state in states)
# print(starts_with_o)

# numbers = [3, 23, 45, 67, 23, 1]
# # are all the numbers odd?
# # all_odd = all(num % 2 != 0 for num in numbers)
# all_odd = all([num % 2 != 0 for num in numbers])
# # are_odd = [num % 2 != 0 for num in numbers]
# print(all_odd)
# # print(are_odd)



# are all the letters of this string uppercase, don't use .isupper()
# import string
# uppercase = string.ascii_uppercase

# location = "SQICOLLEGEOFICT"
# # print(location.isupper())
# # all_upper = all(char.isupper() for char in location)
# print([char in uppercase for char in location])
# # all_upper = all(char in uppercase for char in location)
# # print(all_upper)


# Use a list comprehension to create a list of numbers between 1 and 50 that are divisible by 3
# nums_divisible_by_3 = [num for num in range(1, 51) if num % 3 == 0]
# print(nums_divisible_by_3)
# ===================================LIST COMPREHENSION===================================