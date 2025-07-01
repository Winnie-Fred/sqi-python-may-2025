# Write a program in a file named `password_strength_checker.py` that takes a string called `password` and prints `True` if the password is strong and `False` otherwise. A strong password:

# Is at least 8 characters long.
# Contains both uppercase and lowercase characters.
# Contains at least one digit.
# Contains at least one special character (e.g., !@#$%^&*()).

# def check_password_strength(password):
#     at_least_8_chars = len(password) >= 8

#     has_upper = any(char.isupper() for char in password)
#     has_lower = any(char.islower() for char in password)
#     has_digit = any(char.isdigit() for char in password)
#     special_chars = '!@#$%^&*()'
#     has_special_char = any(char in special_chars for char in password)
#     print(all([at_least_8_chars, has_upper, has_lower, has_digit, has_special_char]))

# check_password_strength("PASSwoRd1@")
# check_password_strength("p@sswoRd1")
# check_password_strength("psswoRd")


# def check_password_strength(password: str):
#     at_least_8_chars = len(password) >= 8
#     special_chars = '!@#$%^&*()'

#     # has_upper = False
#     # has_lower = False
#     # has_digit = False
#     # has_special_chars = False

#     for char in password:
#         if char.isupper():
#             has_upper = True
#         if char.islower():
#             has_lower = True
#         if char.isdigit():
#             has_digit = True
#         if char in special_chars:
#             has_special_chars = True

#     return all((at_least_8_chars, has_upper, has_lower, has_digit, has_special_chars))

# print(check_password_strength("password@123"))