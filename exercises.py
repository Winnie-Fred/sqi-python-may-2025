# Exercise 1: Student Grades Average
# Description:
# Write a program that:
# Asks the user to input grades (as numbers) for 5 subjects.
# Stores them in a list.
# Calculates and prints the average grade.

# grade_1 = int(input("Enter the first grade: "))
# grade_2 = int(input("Enter the second grade: "))
# grade_3 = int(input("Enter the third grade: "))
# grade_4 = int(input("Enter the fourth grade: "))
# grade_5 = int(input("Enter the fifth grade: "))

# grades = [grade_1, grade_2, grade_3, grade_4, grade_5]

# sum_of_grades = sum(grades)

# no_of_grades = len(grades)

# average = sum_of_grades / no_of_grades

# print(f"The averga egrade is {average}.")

# Exercise 2: Swap First and Last
# Description:
# Create a program that:
# Takes 4 names as comma-separated string input and stores them in a list.
# Swaps the first and last names in the list.
# Prints the updated list.



# WRONG!!!
# names = input("Enter 4 names separated by commas: ").split(",")
# print("before: ", names)
# names[0] = names[3]
# names[3] = names[0]
# print("after:  ", names)


# METHOD 1
# names = input("Enter 4 names separated by commas: ").split(",")
# print("before: ", names)
# temp = names[0]
# names[0] = names[3]
# names[3] = temp
# print("after:  ", names)

# METHOD 2
# names = input("Enter 4 names separated by commas: ").split(",")
# print("before: ", names)
# names[0], names[3] = names[3], names[0]
# print("after:  ", names)


# Exercise 3: 
# Ask the user to input comma-separated numbers.
# Store them in a list.
# Print the median number.

# numbers = input("Enter comma-separated numbers: ").split(",")
# numbers.sort()
# index_median = len(numbers) // 2
# print("numbers:      ", numbers)
# print("index_median: ", index_median)
# median = numbers[index_median]
# print(f"The median is {median}.")


# Exercise 4:
# Repeat This Word
# Description:
# Ask the user for a word and a number.
# Print the word repeated that many times.

# Example Input:
# word: hi  
# count: 4

# Output:
# hihihihi

# word = input("Enter a word: ")
# no_of_times = int(input(f"Enter how many times you want \"{word}\" to be repeated: "))
# print(word * no_of_times)



# sentence = 'I\'m a girl'
# print(sentence)
# sentence = 'I\\m a girl'
# print(sentence)
# file_path = "C:\Users\Dell\Documents\SQI\SQI_PYTHON_MAY_2025"
# story = "Once upon a time, in the land of Oyo. \"I am hungry\", she said"
# print(story)
# story = "Once upon a time, in the land of Oyo. \"I am hungry\", she said"
# color = "black"
# print(f"The color is {{{color}}}")