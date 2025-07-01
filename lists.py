# Collections:
# Lists
# Tuples
# Sets
# Dictionaries


# jollof_rice_shopping_list = ["rice", "tomato paste", "groundnut oil", "spices", "chicken", "margarine", "green beans", "rice"]

# print(jollof_rice_shopping_list)

# print(jollof_rice_shopping_list[3])

# print(jollof_rice_shopping_list[3][2])
# print("spices"[2])


# Lists are ordered
# Lists are indexed
# Lists are mutable
# lists allow duplicate values

# print("before: ", jollof_rice_shopping_list)
# jollof_rice_shopping_list[4] = "meat"
# jollof_rice_shopping_list.append("onions")

# jollof_rice_shopping_list.remove("green beans")



# jollof_rice_shopping_list.remove("green")

# print("after:  ", jollof_rice_shopping_list)

# ingredient = "chicken"
# ingredient[0] = "h"


# jollof_rice_shopping_list = ["rice", "tomato paste", "groundnut oil", "spices", "chicken", "margarine", "green beans", "rice"]
# jollof_rice_shopping_list.remove("green beans")



# jollof_rice_shopping_list = ["rice", "tomato paste", "groundnut oil", "spices", "chicken", "margarine", "green beans", "rice"]


# print("before: ", jollof_rice_shopping_list)
# jollof_rice_shopping_list.remove("chicken")  # list methods work in place
# jollof_rice_shopping_list.append("onions")
# print("Rice" in jollof_rice_shopping_list)

# jollof_rice_shopping_list.insert(4, "crayfish")
# jollof_rice_shopping_list.insert(2, "curry")

# print("after:  ", jollof_rice_shopping_list)


# day_of_the_week = "Tuesday"
# day_of_the_week_upper = day_of_the_week.upper()
# print(day_of_the_week)
# print(day_of_the_week_upper)


# Lists are ordered
# Lists are indexed
# Lists are mutable
# lists allow duplicate values



# Create a list called `sports` that contains "Basketball", "Volleyball", "Tennis", "Golf"
# Print how many items are in the list
# Add "Baseball" to the end of the list
# Remove "Volleyball" from the list
# Print the "ball" in "Basketball"
# Add "Hockey" inbetween "Tennis" and "Golf"
# Check if "Rugby" is in the list
# Print the 2nd item in the list


# sports = ["Basketball", "Volleyball", "Tennis", "Golf"]
# print(len(sports))
# sports.append("Baseball")
# # print("Sade".upper())
# sports.remove("Volleyball")
# print(sports[0][6:])
# sports.insert(2, "Hockey")
# print(sports)
# print("Rugby" in sports)
# print(sports[1])


# sports = ["Basketball", "Volleyball", "Tennis", "Golf"]
# print(sports[0:3])
# print(sports[0:1])
# sports[0:3] = ["Rugby"]
# sports[0] = "Rugby"
# sports[0] = ["Rugby"]
# print(sports)


# numbers = [98, 23, 67.8, 12, 7.6]

# numbers[1:4] = [2]
# numbers[1:2] = [20]
# numbers[1:2] = [2]

# numbers[3] = 10

# print(numbers)


# numbers = [98, 23, 67.8, 12, 7.6]
# print(numbers[-1])
# print(type(numbers))


# my_list = ["Hey", 9, True, 12, 2.5, None]
# print(my_list)

# my_dict = {"tomato": 7800, "onions": 2300}

# my_tuple = ("John", "Mary", "Hilda", "Timmy")
# my_list = list(my_tuple)
# print(my_list)


# data = ("John", "Mary", "Hilda", "Timmy")
# print(type(data))
# data = list(data)
# print(type(data))
# print(data)

# brand = "Gucci"
# print(list(brand))

# sentence = "I love Teslas"
# print(sentence.split(" "))
# sentence = list(sentence)
# print(sentence)

# depts = ["Data Science", "Data Analysis", "Software Engineering"]

# # other_depts = ["UI/UX", "Graphics Design", "AI"]
# other_depts = ("UI/UX", "Graphics Design", "AI")

# depts.extend(other_depts)
# # other_depts.extend(depts)
# print(depts)  # ["Data Science", "Data Analysis", "Software Engineering"]
# print(other_depts)  # ["UI/UX", "Graphics Design", "AI", "Data Science", "Data Analysis", "Software Engineering"]



# depts = ["Data Science", "Data Analysis", "Software Engineering"]
# other_depts = ["UI/UX", "Graphics Design", "AI"]
# # all_depts = depts + other_depts
# # print(all_depts)
# print(depts + other_depts)



# sqi_depts = ["UI/UX", "Graphics Design", "AI"]
# sqi_depts.remove("AI")
# del sqi_depts[2]
# del sqi_depts
# print(sqi_depts)  # NameError

# sqi_depts.pop(2)
# print(sqi_depts)


# sqi_depts = ["UI/UX", "AI", "Graphics Design", "AI"]
# print("before: ", sqi_depts)
# sqi_depts.remove("AI")
# del sqi_depts[3]
# popped_item = sqi_depts.pop(3)
# popped_item = sqi_depts.pop()
# popped_item = sqi_depts.pop(0)
# print("after:  ", sqi_depts)
# print(popped_item)


# sqi_depts = ["UI/UX", "AI", "Graphics Design", "AI"]
# del sqi_depts
# print(sqi_depts)

# num = 5
# del num
# print(num)


# depts = ["Data Science", "Data Analysis", "Software Engineering"]
# depts.clear()
# print(depts)

# depts = ["Data Science", "Data Analysis", "Software Engineering"]
# depts = []
# print(depts)


# depts = ["Data Science", "Data Analysis", "Software Engineering"]
# # depts.sort()
# depts.sort(reverse=False)
# # depts.sort(reverse=True)
# print(depts)

# fruits = ["Apple", "Grape", "orange", "banana"]
# # ["Apple", "banana", "Grape", "orange"]
# # fruits.sort()  # case sensitive sort
# fruits.sort(key=str.lower)  # case-insensitve sort
# print(fruits)


# fruits = ["Apple", "Grape", 12, "orange", "banana"]
# fruits.sort()
# print(fruits)

# fruits = ["Apple", "Grape", 12, "orange", "banana"]
# ["banana", "orange", 12, "Grape", "Apple"]
# print("before: ", fruits)
# fruits.reverse()
# print("after:  ", fruits)


# fruits = ["Apple", "Grape", 12, "orange", "banana"]
# fruits = fruits[::-1]
# print(fruits)

# colors = ["red", "violet", "rebecca purple", "cyan", "white"]
# colors_copy = colors  # reference
# print("before colors     ", colors)
# print("before colors_copy", colors_copy)


# colors.append("black")
# print("after colors      ", colors)
# print("after colors_copy ", colors_copy)


# colors = ["red", "violet", "rebecca purple", "cyan", "white"]
# colors_copy = colors.copy()  # true copy
# print("before colors     ", colors)
# print("before colors_copy", colors_copy)


# colors.append("black")
# print("after colors      ", colors)
# print("after colors_copy ", colors_copy)

# import copy
# nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# nums_copy = copy.copy(nums)  # copies only outer elements
# nums_copy = copy.deepcopy(nums)  # copy nested elements

# nums = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(nums[1][1])
# print(nums[0][2])
# print(nums[-1][-3])
# print(nums[1][0:2])


# nested_list = [
#     ["Alice", "Bob"],
#     [10, 20, 30],
#     [True, False]
# ]
# print(nested_list[1][1] + nested_list[1][2])
# print(nested_list[0][0][2:])
# Alibob
# print(nested_list[0][0][0:3] + nested_list[0][1][0:])
# nested_list[2][1] = 20
# print(nested_list)

# nested_list[2][0] = int(nested_list[2][0])
# print(nested_list)