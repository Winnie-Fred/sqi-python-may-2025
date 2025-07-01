"""
This module will explain strings to SQI 2025 MAy COHORT
"""

# Create a variable `text` that contains "today is Monday"
# Capitalize the text.
# Turn the text to lowercase
# Turn the text to uppercase
# Check if text starts with "T" regardless of the case of `text`
# Check if text ends with "Day" regardless of the case of `text`


# text = "today is Monday"
# print(text.capitalize())
# print(text.lower())
# print(text.upper())
# print(text.upper().startswith("T"))

# print(text.upper().endswith("Day".upper())) 
# print(text.upper().endswith("DAY")) 
# print(text.upper())
# print("Day".upper())

# tuple_t = ("T", "t")
# print(text.startswith(tuple_t))
# print(text.startswith(("T", "t")))


# name = "Omolola"
# print(name.lower().startswith("o"))



# my_list = ["Joy", "Happiness", "Sadness", "Charity", "Peace", "Chaos"]

# my_tuple = ("TV", "Radio", "Fryer", "Washing Machine", "Jug")

# # print(my_list[2])
# # print(my_tuple)

# # my_list.append("Serenity")
# my_tuple.append("Serenity")
# print(my_list)

# split, join, count, find, index, islower, isupper, strip, replace


# greeting = "Hello Hello"
# print(greeting.count("l"))
# print(greeting.count("z"))
# print(greeting.lower().count("h"))
# print(greeting.count("Hello"))




# magic_phrase = "abracadabra"
# # print(len(magic_phrase))  # 11
# print(magic_phrase.count("abra"))  # 2
# print(magic_phrase.count("ab"))  # 2


# text = "abababa"
# print(text.count("ab"))
# print(text.count("ba"))
# print(text.count("aba"))


# text = "today is Monday"
# uppercase = text.upper()
# print(uppercase)
# print(text)

# text = "today is Monday"
# text = text.upper()  # 
# print(text)



# text = "abababa"
# print(text.find("b")) 
# print(text.find("a", 2)) 
# print(text.find("b", 2)) 


# text = "today is Monday"
# print(text.find("Monday")) 
# print(text.find("day"))
# print(text.find("day", 5))
# print(text.find("Tuesday")) 
# print(text.find("wegvhnmf,")) 


# text = "today is Monday"
# print(text.index("today"))
# print(text.index("is"))
# print(text.index("Tuesday"))


# name = "Molayo"
# print(name.islower())
# print(name.isupper())
# print(name.upper().isupper())
# name = "molayo"
# print(name.upper().isupper())
# print(name.isupper())
# print(name.islower())


# story = "\tOnce upon a time  "
# print(story.lstrip())
# print(story.rstrip())
# print(story.strip())


# story = "***Once upon a time***********"
# print(story.lstrip("*"))
# print(story.rstrip("*"))
# print(story.strip("*"))

# story = "***Once upon a time***********"
# story = "   Once upon a time "
# print(story.replace(" ", ""))
# print(story.upper().replace("O", "P"))
# print(story.replace("time", "day").replace("upon", "UPON"))
# print(story.replace("Z", "P"))


# story = "Once upon a time"
# print(story.split())
# story = "Once*upon*a*time"
# print(story.split())
# print(story.split("*"))

# movies = "Love in every word, Beauty in Black, My Siblings and I, Black Diamond, Mission Impossible"
# print(movies.split(", "))

# games = ["CandyCrush", "KillerBean", "DreamLeague", "LoveParadise", "SubwaySurf", "Watchdog"]

# print("".join(games))
# print(" ".join(games))
# print(", ".join(games))

# 17 - 44



# pep 8 -> style guide for Python


# docstring -> documentation string


# !!!!BAD
"""
a  = 6
b  = 4
print(a + b)  # add a and b together
"""

# ASSIGNMENT CORRECTION
# 17. Convert a string “James John Kennedy” called “names” to a list using the string 
# .split() method. Store the result in a list called “names_list”
# names = "James John Kennedy"
# print(names.split())

# 18. You have a list of cities called cities_list containing ['New York', 'Los Angeles', 
# 'Chicago']. Convert this list into a single string where each city is separated by a 
# semicolon and a space. Store the result in a string called cities_string.
# cities_list = ['New York', 'Los Angeles', 'Chicago']
# print("; ".join(cities_list))


# 19. Create a string variable sentence with the value "the quick brown fox jumps over the 
# lazy dog". Capitalize the first letter of the string and 
# print the result.
# sentence = "the quick brown fox jumps over the lazy dog"
# print(sentence.capitalize())


# 20. Create a string variable book_title with the value "to kill a mockingbird". Capitalize 
# the first letter of each word and print the result.
# book_title = "to kill a mockingbird"
# print(book_title.title())

# 21. Create a string variable text with the value "hello world". Count the number of 
# occurrences of the letter 'o' and print the result.
# text = "hello world"
# print(text.count("o"))

# 22. Create a string variable filename with the value "document.txt". Check if the string 
# starts with "doc" and print the result.
# filename = "document.txt"
# print(filename.startswith("doc"))

# 23. Create a string variable url with the value "https://www.example.com". Check if the 
# string ends with ".com" and print the result.
# url = "https://www.example.com"
# print(url.endswith(".com"))

# 24. Create a string variable phrase with the value "find the needle in the haystack". Find 
# the position of the word "needle" and print the result.
# phrase = "find the needle in the haystack"
# print(phrase.find("needle"))

# 25. Create a string variable template with the value "Hello, {}. Welcome to {}.". Use the 
# format() method to replace the placeholders with "Alice" and "Wonderland" and print the 
# Result. Bonus point if you can do it with the f-string and concatenation methods also.

# template = "Hello, {}. Welcome to {}."
# name = "Alice"
# place = "Wonderland"

# print(template.format(name, place))
# print(f"Hello, {name}. Welcome to {place}.")
# print("Hello, " + name + ". Welcome to " + place + ".")




# num = 8
# print(f"before: {type(num)}")
# num = str(num)
# print(f"after:  {type(num)}")

# num = 8
# second_num = 7
# print(num + second_num)

# age = 5
# is_student = True
# name = "Awwal"
# height = 4.65

# Use f-string, .format() and concatenation to compose the sentence below:
# I am Awwal. It is True that I am a student. I am 5 years old, my height is 4.65m

# print(f"I am {name}. It is {is_student} that I am a student. I am {age} years old, my height is {height}m")
# print("I am {}. It is {} that I am a student. I am {} years old, my height is {}m".format(name, is_student, age, height))
# # print("I am {2}. It is {0} that I am a student. I am {1} years old, my height is {3}m".format(is_student, age, name, height))
# print("I am " + name + ". It is " + str(is_student) + " that I am a student. I am " + str(age) + " years old, my height is " + str(height) + "m")



# temperature = 29.5
# is_raining = False
# no_of_cats = 7
# name = "Zainab"
# mood = "happy"
# location = "Lagos"
# TASK: Using all three methods — f-string, .format(), and concatenation — compose the following sentence:
# "Hello, my name is Zainab. I live in Lagos and I have 7 cats. It is False that it is raining today, and the temperature is 29.5°C. I am feeling happy."

# sentence = f"Hello, my name is {name}. I live in {location} and I have {no_of_cats} cats. It is {is_raining} that it is raining today, and the temperature is {temperature}°C. I am feeling {mood}."
# print(sentence)
# template = "Hello, my name is {}. I live in {} and I have {} cats. It is {} that it is raining today, and the temperature is {}°C. I am feeling {}."
# sentence = template.format(name, location, no_of_cats, is_raining, temperature, mood)
# print(sentence)

# sentence = "Hello, my name is " + name +  ". I live in " + location + " and I have " + str(no_of_cats) + " cats. It is " + str(is_raining) + " that it is raining today, and the temperature is " + str(temperature) + "°C. I am feeling " + mood + "."
# print(sentence)



# 26.	Create a string variable `quote` with the value "To be or not to be". Find the position 
# of the word "not" and print the result.
# quote = "To be or not to be"
# print(quote.find("not"))
# print(quote.index("not"))


# quote = "To be or not to be"
# print(quote.find("wsdvbhenfmk"))  # -1
# print(quote.index("wsdvbhenfmk"))  # Error


# 27. Create a string variable word with the value "hello". Check if all characters in the 
# string are lowercase and print the result.
# word = "hello"
# print(word.islower())


# 28. Create a string variable shout with the value "HELLO". Check if all characters in the 
# string are uppercase and print the result.
# shout = "HELLO"
# print(shout.isupper())


# 29. Create a string variable mixed_case with the value "PyThOn". Convert all characters to 
# lowercase and print the result.
# mixed_case = "PyThOn"
# print(mixed_case.lower())


# 30. Create a string variable mixed_case with the value "PyThOn". Convert all characters to 
# uppercase and print the result.
# mixed_case = "PyThOn"
# print(mixed_case.upper())


# 31. Create a string variable padded_text with the value " hello ". Remove leading whitespace and 
# print the result.
# padded_text = " hello "
# print(padded_text.lstrip())

# 32. 	Create a string variable padded_text with the value " hello ". Remove trailing whitespace and 
# print the result.
# padded_text = " hello "
# print(padded_text.rstrip())


# 33. Create a string variable padded_text with the value " hello ". Remove both leading and trailing 
# whitespace and print the result.
# padded_text = " hello "
# print(padded_text.strip())


# 34. Create a string variable greeting with the value "Hello, World!". Replace "World" with "Alice" 
# and print the result.
# greeting =  "Hello, World!"
# print(greeting.replace("World", "Alice"))


# 35. Given the string course_name = "Introduction to Python", use slicing to print:
# The word "Introduction".
# course_name = "Introduction to Python"
# print(course_name[:12])
# The word "Python".
# print(course_name[16:])
# print(course_name[-6:])


# 36. Given the string quote = "To be or not to be, that is the question.", use slicing to print:
# The substring "To be or not to be".
# The substring "that is the question".
# quote = "To be or not to be, that is the question."
# print(quote[:18])
# print(quote[20:-1])

# 37. Given the string phrase = "A journey of a thousand miles begins with a single step", use 
# slicing to print:
# The last 5 characters.
# All characters except the last 7.
# phrase = "A journey of a thousand miles begins with a single step"
# print(phrase[-5:])
# print(phrase[:-7])

# 38. Given the string alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ", use slicing to print:
# Every second letter (A, C, E, ...).
# Every third letter starting from the first letter (A, D, G, ...).
# alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# print(alphabet[0::2])
# print(alphabet[::3])

# 39. Given the string word = "tenet", use slicing to:
# Reverse the string and print the result.
# word = "tenet"
# print(word[::-1])


# 40. Given the string sentence = "Learning Python is fun and rewarding!", use slicing to print:
# Characters from index 9 to 19. (Python is f)
# Every second character from index 0 to 10. (Lann y)
# Every third character from the beginning to the end. (LrnPh  nnrai!)
# sentence = "Learning Python is fun and rewarding!"
# print(sentence[9:20])
# print(sentence[0:11:2])
# print(sentence[0::3])


# 41. Given the string programming_language = "JavaScript", use slicing to:
# Print the first character.
# Print the last character.
# programming_language = "JavaScript"
# print(programming_language[0:1])
# print(programming_language[-1:])

# 42. Given the string data = "DataScience", use slicing to:
# Print the substring "Science".
# data = "DataScience"
# print(data[4:])

# 43. Given the string greeting = "Good Morning!", use slicing to:
# Print every second character.
# greeting = "Good Morning!"
# print(greeting[::2])

# 44. Given the string name = "Alexander", use slicing to:
# Print the first three characters concatenated with the last three characters.
# name = "Alexander"
# print(name[:3] + name[-3:])

# Practice
# 1. Format the following sentence using f-string, .format(), and concatenation:
# "Welcome to Mars! This planet is 237 million years old. It is True that it is friendly to visitors. Gravity here is 3.721 m/s²."
# planet = "Mars"
# age = 237
# is_friendly = True
# gravity = 3.721


# 2. Format the following sentence using all three styles:
# "You are watching Inception. Your seat number is 45. It is false that this is a premium seat. The ticket costs $12.99."
# movie = "Inception"
# ticket_price = 12.99
# seat_number = 45
# is_premium = False


# 3. Compose this sentence using all three formatting styles:
# "Sweet Crumbs is located in Downtown. We have 150 cakes today, each priced at $5.75 on average. It is True that we sell chocolate cakes."
# bakery_name = "Sweet Crumbs"
# num_cakes = 150
# average_price = 5.75
# has_chocolate = True
# location = "Downtown"



# 4. Create this sentence using all three formatting methods:
# "Last night at Moonlight Arena, Aria Blaze performed 18 songs over 2.5 hours. It is True that the concert was live."
# artist = "Aria Blaze"
# duration = 2.5
# num_songs = 18
# was_live = True
# venue = "Moonlight Arena"


# 5. Format the following sentence using f-string, .format(), and concatenation:
# "Meet Whiskers, a 2-year-old cat weighing 3.9 kg. It is True that Whiskers is vaccinated."
# pet_name = "Whiskers"
# pet_type = "cat"
# weight = 3.9
# age = 2
# vaccinated = True


# num = 5673897647839
# print(type(num))

# phone_num = 9_030_556_547
# phone_num = "09030556547"
# print(phone_num)

# diameter = 98.34
# print(type(diameter))

# num_1 = 6
# num_2 = 2
# print(num_1 / num_2)


# num = 70000
# print(7e-4)


# BOOLEANS
# bool -> George Bool
# is_happy = True
# print(is_happy)
# print(type(is_happy))

# young = False
# print(young)
# print(type(young))


# print(10 > 6)
# print(0 > 1)
# print(0 < 12)
# print(12 == 12)
# print(12 == 12.0)
# print(12 <= 15)
# print(15 >= 100)



# is_young = True
# is_beautiful = False
# is_light = True

# print(is_young and is_beautiful and is_light)
# print(is_young and is_beautiful or is_light)


# be_personally_invited = True
# purchased_expensive_ticket = False

# print(be_personally_invited and purchased_expensive_ticket)
# print(be_personally_invited or purchased_expensive_ticket)



# print(int(False))
# print(int(True))



# truthy and falsy values

# position = "CEO"
# print(bool(position))
# position = " "
# print(bool(position))
# position = ""
# print(bool(position))


# age = 12
# print(bool(age))
# age = 0
# print(bool(age))
# age = -21
# print(bool(age))



# radius = 43.23
# print(bool(radius))
# radius = 0.0
# print(bool(radius))
# radius = 0.000000000000000000000000001
# print(bool(radius))
# radius = -98.231
# print(bool(radius))


# is_on = True
# print(bool(is_on))
# is_on = False
# print(bool(is_on))


# means_of_transport = ["car", "bus", "keke", "bike", "lorry", "boat", "ship", "aircraft", "broom"]
# print(bool(means_of_transport))
# means_of_transport = [""]
# print(len(means_of_transport))
# print(bool(means_of_transport))
# means_of_transport = []
# print(bool(means_of_transport))
# means_of_transport = [[]]
# print(bool(means_of_transport))

# print(bool(()))
# print(bool(("radio", "fan")))

# print(bool(None))

# print(isinstance(4.0, int))
# print(isinstance(True, int))
# print(isinstance(True, bool))
# print(isinstance([1, 2, 3], list))
# print("Word1", "Word2", sep="%")


# means_of_transport = ["car", "bus", "keke", "bike", "lorry", "boat", "ship", "aircraft", "broom"]

# unpacking

# car, bus, tricycle, bicycle, lorry, boat, ship, plane, broom = means_of_transport
# print("car", car)
# print("bus", bus)
# print("tricycle", tricycle)
# print("bicycle", bicycle)
# print("lorry", lorry)
# print("boat", boat)
# print("ship", ship)
# print("plane", plane)
# print("broom", broom)



# awwal, lekan, fash, molayo, lola = "Awwal", "Olamilekan", "Mrs. Fash", "Molayo", "Omolola"
# print("awwal:", awwal)
# print("lekan:", lekan)
# print("fash:", fash)
# print("molayo:", molayo)
# print("lola:", lola)


# names = ("Awwal", "Olamilekan", "Mrs. Fash", "Molayo", "Omolola", "Winnie")
# print(type(names))


# car = "Nissan",
# print(type(car))



# person = winnie = chinaza = "Winnie"
# print(person)
# print(winnie)
# print(chinaza)


# name = "Leka"
# if name == "Lekan":
#     print("Lekan, good morning")
# else:
#     print("good morning, Anonymous")


num = 4
print(float(num))

num1 = 5
num2 = 3.2
print(num1 + num2)


# ASSIGNMENT
# 11 - 16
