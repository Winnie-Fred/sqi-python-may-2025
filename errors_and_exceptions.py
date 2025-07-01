# Ask the user for their age
# If they enter a negative age, keep asking till they enter a valid age
# When you have a valid age, tell them what year they were born

# from datetime import datetime

# current_year = datetime.now().year
# while True:
#     try:
#         age = int(input("Enter your age: "))
#     except ValueError:
#         print("Enter a valid number")
#     except Exception:
#         print("Something went wrong")
#     else:
#         if age < 1:
#             print("Negative ages are not allowed")
#             continue
#         print(f"You were born in {current_year - age}")
#         break

# class NegativeAgeError(Exception):
#     def __init__(self, message):
#         self.message = message
#         super().__init__(self.message)


# from datetime import datetime

# current_year = datetime.now().year
# def calculate_birth_year():
#     while True:
#         try:
#             age = int(input("Enter your age: "))
#         except ValueError:
#             print("Enter a valid number")
#         except Exception:
#             print("Something went wrong")
#         else:
#             if age < 1:
#                 raise NegativeAgeError("Negative ages are not allowed")
#             print(f"You were born in {current_year - age}")
#             break


# try:
#     calculate_birth_year()
# except NegativeAgeError as e:
#     print(f"Negative age entered: {e}")


# Write a function divide(num1, num2) and returns the result of the division

# def divide(num1, num2):
#     try:
#         result = float(num1) / float(num2)
#     except ZeroDivisionError as e:
#         return f"Cannot divide by zero: {e}"
#     except ValueError as e:
#         return f"num1 and num2 must be numbers: {e}"
#     except TypeError as e:
#         return f"num1 and num2 must be numbers: {e}"
#     finally:
#         print("This block will always run")
#     return f"The result is {result}"

# print(divide("4", "23whbdujenfd"))


# 1. Define a custom exception called NegativeNumberError.
# Write a function check_positive(number) that raises 
# NegativeNumberError if the input number is negative.
# Catch the exception when calling the function.

# class NegativeNumberError(Exception):
#     def __init__(self, num):
#         self.message = f"{num} is negative"
#         super().__init__(self.message)

# def check_positive(number: float):
#     if number < 0:
#         raise NegativeNumberError(number)
#     return None

# try:
#     check_positive(-3)
# except NegativeNumberError as e:
#     print(e)


# 2. Handle Multiple Exceptions:
# Write a function safe_divide(a, b) that performs division.
# Handle ZeroDivisionError if the divisor is zero.
# Handle TypeError if the inputs are not numbers.
# Handle ValueError if the inputs are not convertible to floats.


# def safe_divide(a, b):
#     try:
#         result = float(a) / float(b)
#     except ZeroDivisionError as e:
#         print(f"Divisor cannot be zero: {e}")
#     except TypeError as e:
#         print(f"a and b must both be numbers: {e}")
#     except ValueError as e:
#         print(f"a and b must both be numbers: {e}")
#     else:
#         print(result)

# def safe_divide(a, b):
#     try:
#         result = float(a) / float(b)
#     except ZeroDivisionError as e:
#         return f"Divisor cannot be zero: {e}"
#     except TypeError as e:
#         return f"TypeError: a and b must both be numbers: {e}"
#     except ValueError as e:
#         return f"ValueError: a and b must both be numbers: {e}"
#     return result

    
# print(safe_divide(16, [8]))
# print(safe_divide(16, "gvwbhdmkl,"))
# print(safe_divide(16, 0))