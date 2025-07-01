# Print "I love Python" 10 times


# i = 1

# while i <= 10:
#     print(f"{i}). I love Python")
#     i += 1


# i = 20
# while i < 41:
#     print(i)
#     i += 1


# num = 40
# while num >= 20:
#     print(num)
#     num -= 1

# count all the even numbers from 7 to 50

# i = 7
# while i <= 50:
#     print(i+1)
#     i += 2

# i = 7
# while i <= 50:
#     print("something")
#     if i % 2 == 0:
#         print(i)
#     i += 1

# print all the numbers that are multiples of 5 between 1 and 200


# Count from 1 to 50

# i = 1
# while i < 51:
#     print(i)
#     i += 1



# Count all the odd numbers from 1 to 67
# i = 1
# while i < 68:
#     print(i)
#     i += 2

# Count all the odd numbers from 2 to 67
# i = 2
# while i < 68:
#     print(i + 1)
#     i += 2 

# i = 2
# while i < 68:
#     if i % 2 != 0:
#         print(i)
#     i += 1


# print the numbers that are both multiples of 3 and 5 between 69 and 203
# i = 69
# while i <= 203:
#     if i % 15 == 0:
#         print(i)
#     i += 1



# print a list of the numbers that are both multiples of 3 and 5 between 69 and 203
# i = 69
# while i <= 203:
#     multiples_of_15 = []
#     if i % 15 == 0:
#         multiples_of_15.append(i)
#     i += 1


# print(multiples_of_15)

# while loop exercises

# count from 1 to 50, and print a comma separated string of the numbers
# your output will look like:
# "1, 2, 3, 4, ..., 45, 46, 47, 48, 49, 50"

# numbers = []
# i = 1
# while i <= 50:
#     numbers.append(str(i))
#     i += 1


# print(numbers)
# print(", ".join(numbers))


# count from 1 to 50, and print a comma separated string of the numbers
# don't use a list


# numbers = ""
# i = 1
# while i <= 50:
#     numbers += str(i)
#     if i < 50:
#         numbers += ", "
#     i += 1


# print(numbers)
# names = "Awwal, Lekan"
# print(names)
# # add Omolola 
# # add Molayo
# # names = names + ", Omolola"
# names += ", Omolola"
# names += ", Molayo"
# print(names)

# Print numbers from 1 to 10, but skip number 5
# Expected Output:
# 1
# 2
# 3
# 4
# 6
# 7
# 8
# 9
# 10

# i = 1
# while i <= 10:
#     if i != 5:
#         print(i)
#     i += 1


# Print a square of stars
# Ask the user to enter a number
# Example 1:
# Input: 3

# Output:
# ***
# ***
# ***

# Example 2:
# Input: 5

# Output:
# *****
# *****
# *****
# *****
# *****


# 1. Collect the number from the user
# 2. Multiply the * by the number the user enters
# 3. Repeat that `length` times


# length = int(input("Enter a number: "))
# i = 1
# while i <= length: 
#     print("*" * length)
#     i += 1


# Print a rectangle of area length X breadth
# ask the user to provide length and breadth
# Example:
# Input:
# Length: 5
# Breadth: 4
# *****
# *****
# *****
# *****


# 1. Collect the length and breadth of the rectangle
# 2. Print `length`` stars
# 3. Repeat number 2 `breadth`` times

# length = int(input("Enter the length of the rectangle: "))
# breadth = int(input("Enter the breadth of the rectangle: "))

# i = 1
# while i <= breadth:
#     print("*" * length)
#     i += 1



# Print "1" ten times on the same line using a while loop
# Expected Output:
# 1111111111

# result = ""
# i = 1
# while i <= 10:
#     result += "1"
#     i += 1

# print(result)


# result = []
# i = 1
# while i <= 10:
#     result.append("1")
#     i += 1

# print("".join(result))


# break and cointinue
# Print numbers from 1 to 10, but skip number 5
# Expected Output:
# 1
# 2
# 3
# 4
# 6
# 7
# 8
# 9
# 10

# i = 0
# while i < 10:
#     i += 1
#     if i == 5:
#         continue
#     print(i)



# print all even numbers form 1 to 20

# i = 1
# while i <= 20:
#     i += 1
#     if i % 2 != 0:
#         continue
#     print(i)


# print all the numbers from 5 to 20, but stop once you reach a multiple of 15

# i = 5
# while i <= 20:
#     if i % 15 == 0:
#         break
#     print(i)
#     i += 1


# how to loop through strings, lists with while loops
# name = "Winnie"

# print(name[0])  # 0
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])
# print(name[5])  # 5

# i = 0
# # while i <= len(name) - 1:
# while i < len(name):
#     char = name[i]
#     print(char)
#     i += 1

# name = "Omolola"

# i = 0
# while i < len(name):
#     char = name[i]
#     print(char)
#     i += 1


# ATM withdrawal simulation


# directions = ["up", "down", "left", "right"]

# i = 0
# while i < len(directions):
#     direction = directions[i]
#     print(direction)
#     i += 1



# items = ("cap", "shoe", "basket")
# i = 0
# while i < len(items):
#     item = items[i]
#     print(item)
#     i += 1



# series = ["Wednesday", "Umbrella Academy", "Vampire Diaries", "Stranger Things", "Blacklist", "Blindspot", "Prison Break"]

# Output:
# Series 1: Wednesday
# Series 2: Umbrella Academy
# Series 3: Vampire Diaries
# Series 4: Stranger Things
# Series 5: Blacklist
# Series 6: Blindspot
# Series 7: Prison Break

# Output:
# The series at index 0 is Wednesday
# The series at index 1 is Umbrella Academy

# i = 0
# while i < len(series):
#     print(f"Series {i+1}: {series[i]}")
#     i += 1


# i = 0
# while i < len(series):
#     print(f"The series at index {i}: {series[i]}")
#     i += 1


# series = ["Wednesday", "Umbrella Academy", "Vampire Diaries", "Stranger Things", "Blacklist", "Blindspot", "Prison Break"]

# Output:
# The series at index 0 is Wednesday
# The series at index 1 is Umbrella Academy
# The series at index 2 is Vampire Diaries
# The series at index 3 is Stranger Things
# The series at index 4 is Blacklist
# The series at index 5 is Blindspot
# The series at index 6 is Prison Break


# i = 0
# while i < len(series):
#     print(f"The series at index {i} is {series[i]}")
#     i += 1


# count = 0
# while True:
#     print("something")
#     count += 1
#     if count == 5:
#         break





# print the first 10 multiples of 5, don't include 50 anywhere in your code.

# count = 0
# i = 5
# while count < 10:
#     if i % 5 == 0:
#         print(i)
#         count += 1
#     i += 1


# count = 0
# i = 5
# while True:
#     if i % 5 == 0:
#         print(i)
#         count += 1
#     if count == 10:
#         break
#     i += 1

    

# Assignment: Print a list of the first 12 multiples of 3 starting from 3

# Write a program that simulates an ATM withdrawal process. The user should enter their 
# balance and then enter withdrawal amounts until they decide to stop. Ensure the user does
# not withdraw more than their balance.
# Sample Input and Output:
# Enter your balance: 500
# Enter withdrawal amount: 100
# Remaining balance: 400
# Do you want to make another withdrawal? (yes/no): yes
# Enter withdrawal amount: 50
# Remaining balance: 350
# Do you want to make another withdrawal? (yes/no): no
# Final balance: 350

# balance = int(input("Enter your balance: "))
# while True:
#     withdrawal_amount = int(input("Enter withdrawal amount: "))
#     if withdrawal_amount > balance:
#         print("Insufficient funds!")
#         continue

#     balance -= withdrawal_amount
#     print(f"Remaining balance: {balance}")

#     continue_withdrawal = input("Do you want to make another withdrawal? (yes/no): ").strip().lower()

#     if continue_withdrawal == "yes":
#         continue
#     print(f"Final balance: {balance}")
#     break


# balance = int(input("Enter your balance: "))
# main_loop = True
# while main_loop:
#     withdrawal_amount = int(input("Enter withdrawal amount: "))
#     if withdrawal_amount > balance:
#         print("Insufficient funds!")
#         continue

#     balance -= withdrawal_amount
#     print(f"Remaining balance: {balance}")

#     keep_asking = True
#     while keep_asking:
#         continue_withdrawal = input("Do you want to make another withdrawal? (yes/no): ").strip().lower()

#         if continue_withdrawal == "yes":
#             keep_asking = False
#             continue
#         if continue_withdrawal == "no":
#             print(f"Final balance: {balance}")
#             main_loop = False
#             break
#         print("Invalid input")
        


# 2. Write a program that simulates a grocery store checkout. The user should enter the prices of items until they decide to stop. The program should calculate and display the total cost.
# Sample Input and Output:
# Enter item price: 2.99
# Enter another item? (yes/no): yes
# Enter item price: 5.49
# Enter another item? (yes/no): no
# Total cost: 8.48


# total_cost = 0
# while True:
#     item_price = float(input("Enter item price: "))
#     total_cost += item_price

#     another_item = input("Enter another item? (yes/no): ").strip().lower()
#     if another_item == "yes":
#         continue
#     print(f"Total cost: {total_cost}")
#     break 

# 3. Write a program that continuously prompts the user to enter a password until they enter a valid one. A valid password must be at least 8 characters long and have a maximum of 25 characters.
# Sample Input and Output:
# Enter password: hello
# Password must be at least 8 characters long and have a maximum of 25 characters.
# Enter password: mysecretpasswordisasecret
# Password accepted.


# while True:
#     password = input("Enter password: ").strip()
#     if 8 <= len(password) <= 25:
#         print("Password accepted")
#         break
#     print("Password must be at least 8 characters long and have a maximum of 25 characters.")



# 5. Write a program that tracks the inventory of items in a store. The user should be able 
# to add or remove items and the program should display the current inventory after each
# operation. The program stops when the user decides to exit.
# The current store inventory is {‘eggs’: 40, ‘fish’: 200, ‘bread’: 343, ‘yam’:2}
# Sample Input and Output:
# Enter operation (add/remove/exit): add
# Enter item: eggs
# Enter quantity: 10
# Current inventory: {'eggs': 50, 'fish': 200, 'bread': 343, 'yam': 2}
# Enter operation (add/remove/exit): remove
# Enter item: fish
# Enter quantity: 50
# Current inventory: {'eggs': 50, 'fish': 150, 'bread': 343, 'yam': 2}
# Enter operation (add/remove/exit): exit


# inventory = {"eggs": 40, "fish": 200, "bread": 343, "yam":2}

# while True:
#     operation = input("Enter operation (add/remove/exit): ").strip().lower()

#     if operation == "exit":
#         print("Bye")
#         break

#     item = input("Enter item: ").strip().lower()
#     quantity = int(input("Enter quantity: "))

#     if operation == "add":
#         inventory[item] += quantity
#     elif operation == "remove":
#         if item in inventory:
#             inventory[item] -= quantity
#         else:
#             print(f"{item} not in inventory")
#     else:
#         print("Invalid operation")
#         continue
#     print(f"Current inventory: {inventory}")


# Assignment: Print a list of the first 12 multiples of 3 starting from 3
# i = 3
# count = 0
# multiples_of_3 = []
# while True:
#     if i % 3 == 0:
#         count += 1
#         multiples_of_3.append(i)
#     if count == 12:
#         break
#     i += 1
# print(multiples_of_3)

# i = 3
# count = 0
# multiples_of_3 = []

# while count < 12:
#     if i % 3 == 0:
#         multiples_of_3.append(i)
#         count += 1
#     i += 1
# print(multiples_of_3)

# 1. Write a program that uses a while loop to print numbers from 1 to 10.

# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# 2. Write a program that takes an integer n from the user and calculates the sum of all 
# natural numbers up to n using a while loop.
# n = int(input("Enter a number: "))

# num = 1
# total = 0
# result = []
# while num <= n:
#     total += num
#     result.append(str(num))
#     num += 1

# print(f"{' + '.join(result)} = {total}")
# 1+2+3+4+5=15


# 3. Write a program that generates a random secret number between 1 and 50. Use a while loop to allow 
# the user to guess the number with a maximum of 5 attempts. Provide hints if the guess is too high or too low. E.g. if the secret num is 35, and the user guesses 42, their guess is too high. If they guess lower than 35, their guess is too low.

# import random

# secret_num = random.randint(1, 50)
# attempts = 5
# while attempts > 0:
#     guess = int(input("Guess the secret number: "))
#     if guess < 1 or guess > 50:
#         print(f"The secret number is between 1 and 50")
#         continue

#     if guess == secret_num:
#         print("Congratulations 👏. You guessed the number correctly!!!")
#         break
    
#     attempts -= 1

#     if guess < secret_num:
#         print(f"You guessed too low. You have {attempts} attempts left.")
#     elif guess > secret_num:
#         print(f"You guessed too high. You have {attempts} attempts left.")
# else:
#     print(f"The secret number is {secret_num}")


# 4. Write a program that keeps asking the user for a password until they enter the correct one. The correct password is `secret`.

# CORRECT_PASSWORD = "secret"
# while True:
#     password = input("Enter the password: ").strip()
#     if password != CORRECT_PASSWORD:
#         print("Incorrect password")
#         continue
#     print("Password accepted")
#     break

# CORRECT_PASSWORD = "secret"
# password = ''
# while password != CORRECT_PASSWORD:
#     password = input("Enter the password: ").strip()
#     if password == CORRECT_PASSWORD:
#         print("Password accepted")
#         break
#     print("Invalid password")





# 5. Write a program that takes an integer input from the user and uses a while loop to print a countdown from that number to zero.

# countdown = int(input("Enter the countdown number: "))
# while countdown >= 1:
#     print(countdown)
#     countdown -= 1
# else:
#     print("Blast off!")

# 6. Write a program that takes an integer n from the user and uses a while loop to print all even numbers from 1 to n.
# n = int(input("Enter a number: "))
# i = 2
# while i <= n:
#     if i % 2 == 0:
#         print(i)
#     i += 1


# 7. Write a program that takes two integers, base and exponent, from the user and uses a while loop to calculate base raised to the power of exponent.
# Sample Input:
# Enter the base: 2
# Enter the exponent: 3
# Output:
# 2 raised to the power of 3 is 8
# Sample Input:
# Enter the base: 5
# Enter the exponent: 4
# Output:
# 5 raised to the power of 4 is 625

# base = int(input("Enter the base: "))
# exponent = int(input("Enter the exponent: "))
# i = 1
# result = 1
# while i <= exponent:
#     result *= base
#     i += 1

# print(f"{base} raised to the power of {exponent} is {result}")


# 8. Write a program that takes a string input from the user and uses a while loop to count the number of vowels (a, e, i, o, u) in the string.
# hello

# text = input("Enter some text: ").strip().lower()

# index = 0
# no_of_vowels = 0
# while index < len(text):
#     char = text[index]
#     if char in "aeiou":
#         no_of_vowels += 1
#     index += 1

# print(f"The number of vowels is {no_of_vowels}")


# 9. Write a program that takes a string input from the user and uses a while loop to reverse the string.
# text = "python"
# python -> nohtyp
# print(text[0])
# print(text[1])
# print(text[2])
# print(text[3])
# print(text[4])
# print(text[5])
# print(text[5])
# print(text[4])
# print(text[3])
# print(text[2])
# print(text[1])
# print(text[0])
# text = input("Enter some text: ").strip()
# index = len(text) - 1
# while index >= 0:
#     char = text[index]
#     print(char)
#     index -= 1

# index = 0
# text = input("Enter some text: ").strip()
# reversed_text = ""
# while index < len(text):
#     char = text[index]
#     reversed_text = char + reversed_text
#     index += 1

# print(reversed_text)

# hello

# 10. Write a program that takes comma-separated integers from the user, converts that
# to a tuple and uses a while loop to find the minimum value in the tuple.
# numbers = tuple(input("Enter comma-separated numbers: ").split(","))
# print(numbers)

# minimum = int(numbers[0])
# index = 1
# while index < len(numbers):
#     number = int(numbers[index])
#     if number < minimum:
#         minimum = number
#     index += 1

# print(f"The minumum number is {minimum}")

# 11. Write a program that takes a string input from the user and uses a while loop to count
# the occurrences of each character, storing the counts in a dictionary.
# Sample Input:
# Enter a string: Hello
# Sample Output:
# {‘h’: 1, ‘e’: 1, ‘l’: 2, ‘o’: 1}
# lekan
# {'l': 1, 'e': 1, 'k': 1, 'a': 1, 'n': 1}
# winnie
# {'w': 1, 'i': 2, 'n': 2, 'e': 1}

# 1. Go through each character
# 2. If it is not already in the occurences dict, add it and set it to 1
# 3. But if it is already there, then you want to increase the number of occurences for that character by 1

# text = input("Enter some text: ")
# occurences = {}
# index = 0
# while index < len(text):
#     char = text[index]
#     if char in occurences:
#         occurences[char] += 1
#     else:
#         occurences[char] = 1
#     index += 1

# print(occurences)