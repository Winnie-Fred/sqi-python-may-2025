# Write a Python program named `sum_of_two_digits.py` that takes a string as input from the user. The string will consist of exactly two digits (e.g., "23", "98", "09"). Your program should calculate and output the sum of these two digits.

# Example:

# For input "23", the program should output 5 i.e. (2 + 3).
# For input "98", the program should output 17 i.e. (9 + 8).
# For input "09", the program should output 9 i.e. (0 + 9).

# Assume that the input will always be a string made up of
# exactly two digits.



# digits = input("Enter a number made up of two digits in figures: ")  # 75
# # 76
# # code here
# digit_one = digits[0]
# digit_two = digits[1]


# print(f"First digit  : {digit_one}")
# print(f"Second digit : {digit_two}")

# # sum_of_digits = int(digit_one) + int(digit_two)
# sum_of_digits = sum((int(digit_one), int(digit_two)))
# print(f"Sum of digits: {sum_of_digits}")

# print(f"The sum of {digit_one} and {digit_two} is {sum_of_digits}")


digits = input("Enter a number made up of two digits in figures: ")  # 75
print(f"The sum of {digits[0]} and {digits[1]} is {int(digits[0]) + int(digits[1])}")