# is_raining = False

# if is_raining:
#     print("Carry an umbrella")
# else:
#     print("Enjoy the outdoors")


# num1 = 5
# num2 = 12

# print(num1 > num2)

# if num1 > num2:
#     print("num1 is greater than num2")
# else:
#     print("num1 is not greater than num2")


# num1 = 5
# num2 = 12


# if num1 > num2:
#     print("num1 is greater than num2")
# elif num1 < num2:
#     print("num1 is less than num2")
# else:
#     print("num1 is equal to num2")

# num1 = 5
# num2 = 12


# if num1 > num2:
#     print("num1 is greater than num2")
# elif num1 < num2:
#     print("num1 is less than num2")
# elif num1 == num2:
#     print("num1 is equal to num2")


# Exercise 1
# Ask the user to enter a number and print True if the number is even, otherwise, print False

# number = int(input("Enter a number to check if it is even: "))

# if number % 2 == 0:
#     print(True)    
# else:
#     print(False)    


# Exercise 2
# Ask the user to enter what day it is today, if they enter Wednesday, print "You are correct",
# otheriwse, print, "Today is Wednesday, not `day`"

# today = input("What day is it today?: ")
# if today == "Wednesday":
#     print("You are correct")
# else:
#     print(f"Today is Wednesday, not {today}")



# Ask the user to enter a positive number and print True if the number is even, otherwise, print False.
# If the number is negative, print "Enter a positive number"


# number = int(input("Enter a number to check if it is even: "))

# if number % 2 == 0 and number > 0:
#     print("Positive even number")
# elif number % 2 != 0 and number > 0:
#     print("Positive odd number")
# else:
#     print("Negative number")

# number = int(input("Enter a number to check if it is even: "))


# if number < 0:
#     print("Negative number")
# elif number % 2 == 0:
#     print("Positive even number")
# elif number % 2 != 0:
#     print("Positive odd number")


# Ask the user for a number, 
# if the number is a multiple of 5, print "It is a multiple of 5",
# otherwise, print("It is not a multipole of 5")

# num = int(input("Enter a number: "))
# if num % 5 == 0:
#     print("It is a multiple of 5")
# else:
#     print("It is not a multiple of 5")


# Ask the user for a number, 
# if the number is a multiple of 3 and 5, print "It is a multiple of  3 and 5",
# otherwise, print("It is not a multipole of 3 and 5")

# number = int(input("Enter a number: "))

# if number % 3 == 0 and number % 5 == 0:
# # if number % 15 == 0:
#     print("It is a multiple of 3 and 5")
# else:
#     print("It is not a multiple of 3 and 5")


# If the number is amultiple of both 3 and 5, print It is a multiple of both 3 and 5
# If the number is only a multiple of 3, print "It is a multiple of 3"
# If the number is only a multiple of 5, print "It is a multiple of 5"

# number = int(input("Enter a number: "))

# # if number % 3 == 0 and number % 5 == 0:
# if number % 15 == 0:
#     print("It is a multiple of 3 and 5")
# elif number % 3 == 0:
#     print("It is a multiple of only 3")
# elif number % 5 == 0:
#     print("It is a multiple of only 5")
# else:
#     print("It is not a mutiple of 3, 5 or 15")




# truthy and falsy values in conditional statements

# Assuming the user may enter invalid chars (i.e. not just alphabets and/or spaces)

# name = input("Enter your name: ").strip()

# import string

# allowed_chars = set(string.ascii_letters)
# allowed_chars.add(" ")
# print(allowed_chars)
# name_chars = set(name)
# print(name_chars)

# if not name:
#     print(f"Good morning, Anonymous 🌻")
# elif name_chars.issubset(allowed_chars):
#     print(f"Good morning, {name} 🌻")
# else:
#     print(f"Invalid chars in name, enter only alphabets and spaces")




# Assuming the user only enters valid chars (i.e. alphabets and/or spaces)
# name = input("Enter your name: ").strip()
# if not name:
#     print("Good morning, Anonymous 🌻")
# else:
#     print(f"Good morning, {name} 🌻")


# has_umbrella = False
# has_raincoat = False

# if the user has an umbrella, then print "You are protected from the rain"
# if the user has a raincoat, then print "You are protected from the rain"
# If the user has both, print "You are WELL protected from the rain"
# If the user has none, print "You are NOT protected from the rain"

# DRY -> Don't Repeat Yourself

# if has_umbrella and has_raincoat:
#     print("You are WELL protected from the rain")
# elif has_umbrella or has_raincoat:
#     print("You are protected form the rain")
# else:
#     print("you are not protected from the rain")


# ternary operator

# is_raining = False

# if is_raining:
#     print("Carry an umbrella")
# else:
#     print("Enjoy the outdoors")

# is_raining = False

# print("Carry an umbrella") if is_raining else print("Enjoy the outdoors")

# print("Carry an umbrella" if is_raining else "Enjoy the outdoors")



# is_raining = False

# if is_raining:
# advice = "Carry an umbrella"
# else:
#     advice = "Enjoy the outdoors"

# print(advice)


# is_raining = False

# advice = "Carry an umbrella" if is_raining else "Enjoy the outdoors"
# print(advice)



# SILICON VALLEY

# FAANG -> Facebook, Amazon, Apple, Netflix, Google


# ASSIGNMENT CORRECTION
# 1. Collect two numbers as input from the user and assign as variables, a and b, write an if 
# statement that prints "a and b are both positive" if both a and b are positive, prints 
# "Only one is positive" if one of them is positive, and prints "Neither is positive" if 
# neither is positive.
# 2. Collect three numbers x, y and z as a comma separated string input from the user and print "Increasing order" if they are in STRICTLY increasing order, "Decreasing order" if they are in STRICTLY decreasing order, and "Neither" otherwise.
# Write a program that reads a string called `palindrome` supplied through user input and checks if it is a palindrome. Print "Is a palindrome" if it is, otherwise print "Not a palindrome".
# 4. You have three variables: x, y, and z collected as 3 separate inputs from the user. Write an if statement that checks if exactly two out of the three variables are equal and prints "Two are equal" if this is true. Otherwise, print "All different" or "All same" accordingly.
# x = input("Enter the value of x: ").strip()
# y = input("Enter the value of y: ").strip()
# z = input("Enter the value of z: ").strip()

# # if x == y and y == z:
# if x == y == z:
#     print("All equal")
# elif x == y or y == z or x == z:
#     print("Two are equal")
# else:
#     print("All different")

# 5. Given three angles angle1, angle2, and angle3 collected as 3 separate inputs from the user, use if statements to check if they can form a valid triangle. Print "Valid triangle" if the sum of the angles is 180 degrees and all angles are greater than 0. Otherwise, print "Invalid triangle".
# angle1 = float(input("Enter the value of angle1: "))
# angle2 = float(input("Enter the value of angle2: "))
# angle3 = float(input("Enter the value of angle3: "))

# if (angle1 + angle2 + angle3 == 180) and (angle1 > 0 and angle2 > 0 and angle3 > 0):
#     print("Valid triangle")
# else:
#     print("Invalid triangle")

# 6. You have a single character variable `ch` supplied through user input. Write an if statement that prints "Vowel" if ch is a vowel (a, e, i, o, u, both uppercase and lowercase), and "Consonant" otherwise. 

# ch = input("Enter a single alphabetic character: ").strip().lower()
# # if ch in ('a', 'e', 'i', 'o', 'u'):
# if ch in 'aeiou':
#     print("Vowel")
# else:
#     print("Consonant")


# # Assume that the user can enter more than one non-alphabetic character
# ch = input("Enter a single alphabetic character: ").strip().lower()

# if len(ch) != 1:
#     print("Enter only a single chasracter")
# elif not ch.isalpha():
#     print("Enter only alphabetic characters")
# # elif ch in ('a', 'e', 'i', 'o', 'u'):
# elif ch in 'aeiou':
#     print("Vowel")
# else:
#     print("Consonant")


# 7. Given a comma separated string input from the user of three colors color1, color2, and color3, write an if statement to check if all three colors are primary colors (red, blue, yellow). Print "All primary colors" if they are, otherwise print "Not all primary colors".

# colors = input("Enter three colors separated by commas: ").lower().split(",")

# color1, color2, color3 = colors
# color1, color2, color3 = color1.strip(), color2.strip(), color3.strip()
# primary_colors = {"red", "blue", "yellow"}
# all_colors = {color1, color2, color3}

# if all_colors == primary_colors:
#     print("All primary colors")
# else:
#     print("Not all primary colors")


# OR
# colors = input("Enter three colors separated by commas: ").lower().split(",")

# color1, color2, color3 = colors
# color1, color2, color3 = color1.strip(), color2.strip(), color3.strip()
# primary_colors = ["red", "blue", "yellow"]
# all_colors = [color1, color2, color3]

# if sorted(all_colors) == sorted(primary_colors):
#     print("All primary colors")
# else:
#     print("Not all primary colors")


# 8. You have a variable `mode` supplied by the user which can be "manual", "automatic", or "off". Write an if statement that prints "Manual mode activated" if mode is "manual", "Automatic mode activated" if mode is "automatic", and "System is off" if mode is "off".
# mode = input("Enter a mode, choose form manual, automatic or off: ").strip().upper()

# if mode == "MANUAL":
#     print('Manual mode activated')
# elif mode == "AUTOMATIC":
#     print('Automatic mode activated')
# elif mode == "OFF":
#     print('System is off')
# else:
#     print("Invalid mode")

# 9. Given a string `message` entered by the user, use if statements to check if the message contains any of the words "urgent", "important", or "immediate". If it contains any of these words, print "High priority message". Otherwise, print "Normal message".
# message = input("Enter a message: ").lower()

# if "urgent" in message or "immediate" in message or "important" in message:
#     print("High priority message")
# else:
#     print("Normal message")


# 10.	You have two variables, status1 and status2, provided through user input, each of 
# which can be "active", “inactive", or "pending". Write an if statement to print 
# "Both active" if both statuses are "active", "One active" if exactly one is "active",
# and "None active" if neither is "active".
# 11. 	Given a string `filename` supplied by the user, write an if statement to check if the
# filename ends with “.jpg", ".png", or ".gif". Print "Image file" if it does, otherwise
# print "Not an image file".
# filename = input("Enter a filename: ").strip()

# # # if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".gif"):
# if filename.lower().endswith((".jpg", ".gif", ".png")):
#     print(f"{filename} is an image file")
# else:
#     print(f"{filename} is not an image file")



# 12. 	You have a variable `access_level` provided through user input which can be "admin",
# "user", or "guest". Write an if statement that prints "Full access" if access_level is
# "admin", "Limited access" if it is "user", and "No access" if it is "guest".

# access_level = input("Enter your access level: ").strip().lower()

# if access_level == "admin":
#     print("Full access")
# elif access_level == "user":
#     print("Limited access")
# elif access_level == "guest":
#     print("No access")
# else:
#     print("Invalid access level")


# 13. 	Given a string `email` collected from the user, write an if statement to check if the
# email contains both "@" and 	"." characters. Print "Valid email" if it does, otherwise
# print "Invalid email".

# email = input("Enter the email address: ")

# # python gotcha
# if "@" in email and "." in email:
#     print("Valid email address")
# else:
#     print("Invalid email address")

# 14. You have a variable `day` provided by user input which can be any day of the week 
# (e.g., "Monday", "Tuesday", 	etc.). Write an if statement that prints "Weekend" if the
# day is "Saturday" or "Sunday", and "Weekday" if it is any other day.
# day = input("Enter the day of the week: ").strip().capitalize()

# weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# if day == "Saturday" or day == "Sunday":
#     print("Weekend")
# elif day in weekdays:
#     print("Weekday")
# else:
#     print("Not a day of the week")

# 15. Write a program that takes three numbers (num1, num2, num3) as a comma-separated string 
# input from the user and prints the greatest number. Use conditional statements
# to determine which number is the greatest. Bonus point if you can do it without `else` 
# statements.

# num1, num2, num3 = input("Enter three numbers separated by commas: ").split(",")
# num1, num2, num3 = float(num1), float(num2), float(num3)

# if num1 >= num2 and num1 >= num3:
#     print(f"{num1} is the greatest")
# elif num2 >= num1 and num2 >= num3:
#     print(f"{num2} is the greatest")
# else:
#     print(f"{num3} is the greatest")

# OR
# num1, num2, num3 = input("Enter three numbers separated by commas: ").split(",")
# num1, num2, num3 = float(num1), float(num2), float(num3)

# greatest = num1

# if num2 > greatest:
#     greatest = num2
 
# if num3 > greatest:
#     greatest = num3

# print(f"{greatest} is the greatest")