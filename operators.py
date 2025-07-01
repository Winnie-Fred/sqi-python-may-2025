# ==============================================ARITHMETIC OPERATORS ==============================================
# num1 = 45
# num2 = 34
# # addition operator
# print(num1 + num2)  # polymorphic -> its function depends on the operands


# num1 = "45"
# num2 = "34"
# print(num1 + num2)  # concatenation operator


# num1 = "45"
# num2 = 34
# print(num1 + num2)  # TypeError  

# year = 2025
# print(year - 2002)
# year = 2025
# year_of_birth = 2002
# print(year - year_of_birth)

# print(2025 - 2002)


# first_num = 34
# second_num = 2

# print(first_num / second_num)  # float division

# # print(second_num / 0)

# num1 = 23
# num2 = 5
# print(num1 / num2)
# print(num1 // num2)

# print(11 / 2)  # 5.5
# print(11 // 2)  # 5

# print(11 % 2)  # 1

# print(53 // 4)  # 13
# print(53 % 4)  # 1


# print(29 % 5)  # 4

# print(10 % 2 == 0)
# print(15 % 2 == 0)

# # check if 15 is a multiple of 3

# print(15 % 3 == 0)
# print(15 % 3 != 0)

# print(5 * 2)  # 10
# print(5 ** 2)  # 25

# # find the square root of 25
# print(25 ** (1/2))


# no_of_apples = 45  # assignment operator
# print(no_of_apples)

# ==============================================ARITHMETIC OPERATORS ==============================================



# ==============================================ASSIGNMENT OPERATORS ==============================================
# number = 98
# number += 2
# print(number)
# number = number + 2
# print(number)


# houses_in_lekki = 4
# houses_in_abuja = 2
# houses_in_lekki += houses_in_abuja
# # print(houses_in_lekki)
# print(houses_in_abuja)



# distance = 12
# step = 2
# # distance = distance + step
# distance += step
# print(distance)


# total = 54
# total += 1
# print(total)


# savings = 4500
# expenses = 2000
# savings -= expenses
# print(savings)

# total_price = 34
# total_price -= 1
# print(total_price)



# number = 4
# parts = 2
# number /= parts
# number = number / parts
# print(number)
# print(parts)

# number = 86
# number *= 3
# print(number)

# number = 86
# number **= 3
# print(number)


# number = 86
# number //= 3
# print(number)  # 28


# number = 86
# number %= 3
# print(number)  # 2

# number = 86
# print(number %= 3)  # wrong!!
# print(number)  # 2


# print(num = 79)  # wrong!!
# ==============================================ASSIGNMENT OPERATORS ==============================================




# ==============================================COMPARISON OPERATORS ==============================================
# print(10 > 5)
# print(10 < 5)
# print(10 <= 5)
# print(10 < 5 or 10 == 5)

# print(4 != 4.0)

# print("James" == "John")
# print("James" == "James")
# print("James" == "james".capitalize())
# ==============================================COMPARISON OPERATORS ==============================================




# ==============================================LOGICAL OPERATORS ==============================================
# print(34 > 21 and 78 < 45)
# print(34 > 21 or 78 < 45)
# print(not(True))
# print(not(False))

# print(not(not(34 > 21) or not(78 < 45)))

# print(not(4 == 4))
# print(4 != 4)
# ==============================================LOGICAL OPERATORS ==============================================


# ==============================================IDENTITY OPERATORS ==============================================
# interning


# CPython

# None

# beverages = ["milo", "ovaltine", "bournvita", "cowbell choco"]
# python gotcha
# beverages_copy = beverages  # not a true copy, creates a reference
# print(beverages)
# print(beverages_copy)

# beverages_copy.append("milk")
# print(beverages)
# print(beverages_copy)

# print(beverages is beverages_copy)

# print(id(beverages))
# print(id(beverages_copy))
# print(id(beverages) == id(beverages_copy))


# beverages = ["milo", "ovaltine", "bournvita", "cowbell choco"]
# python gotcha
# beverages_copy = beverages.copy()  # not a true copy, creates a reference
# print(beverages)
# print(beverages_copy)

# beverages_copy.append("milk")
# print(beverages)
# print(beverages_copy)

# print(beverages is beverages_copy)
# print(beverages is not beverages_copy)
# print(not(beverages is beverages_copy))

# print(id(beverages))
# print(id(beverages_copy))
# print(id(beverages) == id(beverages_copy))

# ==============================================IDENTITY OPERATORS ==============================================





# ==============================================MEMBERSHIP OPERATORS ==============================================
# beverages = ["milo", "ovaltine", "bournvita", "cowbell choco"]
# print("ovaltine" in beverages)

# # print("milk" in beverages)
# print("milk" not in beverages)

# game = "Minecraft"
# print("ine" in game)
# print("INE" in game)
# ==============================================MEMBERSHIP OPERATORS ==============================================



# print((6 + 3) - (6 + 3))

# print(5 + 2 ** 3)
