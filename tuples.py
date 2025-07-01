# celebrities = ("Giveon", "Bovi", "Jenifa", "Tatiana", "Alessia", "Drake", "Olamide")
# print(celebrities)
# print(celebrities[2])
# print(celebrities[2:4])

# even_nos = 2, 800, 24, 56
# print(type(even_nos))

# even_nos = 2,
# print(type(even_nos))

# tuples are ordered
# tuples do not need the round brackets
# tuples are indexed
# tuples are immutable


# celebrities = ("Giveon", "Bovi", "Jenifa", ["Tatiana", "Alessia"], "Drake", "Olamide")
# celebrities[3][1] = "Cara"
# print(celebrities)


# celebrities = ("Giveon", "Bovi", "Jenifa", "Tatiana", "Alessia", "Drake", "Olamide")
# celebrities[-1] = "Baddo"


# celeb = "Idris Elba"
# celeb[2] = "Y"


# celebrities = ("Giveon", "Jenifa", "Bovi", "Jenifa", "Tatiana", "Alessia", "Drake", "Olamide")
# print(celebrities.index("Bovi"))
# # jenifa = "jenifa"
# jenifa = celebrities[1]
# print(jenifa.count("e"))
# print(celebrities.count(jenifa))

# celebrities = ("Giveon", "Jenifa", "Bovi", "Jenifa", "Tatiana", "Alessia", "Drake", "Olamide")
# print(celebrities)


# celebrities = {"Giveon", "Jenifa", "Bovi", "Jenifa", "Tatiana", "Alessia", "Drake", "Olamide"}
# print(celebrities)


# items = ["apple", "orange", "banana"]
# other_items = ["orange", "banana", "apple"]
# print(items == other_items)


# items = {"apple", "orange", "banana"}
# other_items = {"orange", "banana", "apple"}
# print(items == other_items)

# celebrities = ("Giveon", "Jenifa", "Bovi", "Jenifa", "Tatiana", "Alessia", "Drake", "Olamide")
# print(len(celebrities))
# print(type(celebrities))

# celebrities = {"Giveon", "Jenifa", "Bovi", "Jenifa", "Tatiana", "Alessia", "Drake", "Olamide"}
# print(len(celebrities))


# celebrities = ("Giveon", 209.75678, "Jenifa", False, "Bovi", "Jenifa", 23, "Tatiana", None, "Alessia", "Drake", "Olamide")
# print(type(celebrities))
# print(celebrities)


# celebrities = ["Giveon", "Jenifa", "Bovi", "Jenifa", "Tatiana", "Alessia", "Drake", "Olamide"]
# print(type(celebrities))
# celebrities.append("Basketmouth")
# celebrities = tuple(celebrities)
# celebrities.append("Kira Kosarin")
# print(type(celebrities))

# food = ("beans")
# print(type(food))
# num = (4)
# print(type(num))

# food = ("beans",)
# print(type(food))
# num = (4,)
# print(type(num))


# car_brands = ("Toyota", "Mercedes Benz", "Venza", "Lamborghini", "Tasla", "Rangerover")
# car_brands = list(car_brands)
# car_brands.insert(2, "Lexus")
# car_brands = tuple(car_brands)
# print(car_brands)

# car_brands = ("Toyota", "Mercedes Benz", "Venza", "Lamborghini", "Tasla", "Rangerover")
# more_car_brands = ("Lexus", "Bentley", "Ferrari")
# all_brands = car_brands + more_car_brands
# print(car_brands)
# print(more_car_brands)
# print(all_brands)

# more_car_brands = ("Lexus", "Bentley", "Ferrari")
# brands_times_four = more_car_brands * 4
# print(brands_times_four)
# print(more_car_brands)

# more_car_brands = ("Lexus", "Bentley", "Ferrari")
# # more_car_brands = more_car_brands * 4
# more_car_brands *= 4
# print(more_car_brands)

# chocolates = ("Full Bar", "Snickers", "Mars", "Nutella", "Mutella")
# full_bar, snickers, mars, peanut_butter, mutella = chocolates
# print("full_bar", full_bar)
# print("snickers", snickers)
# print("mars", mars)
# print("peanut_butter", peanut_butter)
# print("mutella", mutella)


# full_bar, snickers, mars, peanut_butter, mutella = ("Full Bar", "Snickers", "Mars", "Nutella", "Mutella")
# print("full_bar", full_bar)
# print("snickers", snickers)
# print("mars", mars)
# print("peanut_butter", peanut_butter)
# print("mutella", mutella)


# chocolates = ("Full Bar", "Snickers", "Mars", "Nutella", "Mutella")
# full_bar, snickers, _, peanut_butter, _ = chocolates

# full_bar = chocolates[0]
# snickers = chocolates[1]
# _ = chocolates[2]
# peanut_butter = chocolates[3]
# _ = chocolates[4]

# print("full_bar", full_bar)
# print("snickers", snickers)
# print("mars", _)
# print("peanut_butter", peanut_butter)
# print("mutella", _)


# chocolates = ("Full Bar", "Snickers", "Mars", "Nutella", "Mutella")
# full_bar, snickers, *_ = chocolates

# print(full_bar)
# print(snickers)
# print(_)


# chocolates = ("Full Bar", "Snickers", "Mars", "Nutella", "Mutella")
# full_bar, *_, mutella = chocolates
# print(full_bar)
# print(_)
# print(mutella)


# chocolates = ("Full Bar", "Snickers", "Mars", "Nutella", "Mutella")
# *_, mars, _, _ = chocolates


# full_bar, snickers, mars, peanut_butter, mutella = ("Full Bar", "Snickers", "Nutella", "Mutella")


# Given the tuple record:
# record = ("Jane", (32, "Manager"), ["HR", "Finance"])
# Unpack the tuple to extract the name, the tuple containing age and position, and the list of departments. Print the extracted age and the first department.

# record = ("Jane", (32, "Manager"), ["HR", "Finance"])
# name, age_and_position, depts = record
# age, position = age_and_position
# first_dept, second_dept = depts
# print(age)
# print(first_dept)


# record = ("Jane", (32, "Manager"), ["HR", "Finance"])
# name, (age, position), (first_dept, second_dept) = record
# print(age)
# print(first_dept)

# record = ("Jane", (32, "Manager"), ["HR", "Finance"])
# name, [age, position], [first_dept, second_dept] = record
# print(age)
# print(first_dept)


record = (
    ("Alpha", [
        ("Beta", (
            ["Gamma", ("Delta",)],
            "Epsilon"
        )),
        "Zeta"
    ]),
    ["Eta", ("Theta", ["Iota", ("Kappa",)])]
)

(
    (alpha, [
        (beta, (
            [gamma, (delta,)],
            epsilon
        )),
        zeta
    ]),
    [eta, (theta, [iota, (kappa,)])]
) = record


print(alpha)
print(beta)
print(gamma)
print(delta)
print(epsilon)
print(zeta)
print(eta)
print(theta)
print(iota)
print(kappa)



# record = (
#     "ItemA",
#     ["SubItem1", ("Detail1", "Detail2")],
#     ("ItemB", ["SubItem2", "SubItem3"])
# )

# item_a, (sub_item1, (detail1, detail2)), (item_b, (sub_item2, sub_item3)) = record
# print(item_a)
# print(sub_item1)
# print(detail1)
# print(detail2)
# print(item_b)
# print(sub_item2)
# print(sub_item3)


# record = (
#     "ItemA",
#     ["SubItem1", ("Detail1", "Detail2")],
#     ("ItemB", ["SubItem2", "SubItem3"])
# )

# _, (_, (detail1, detail2)), *_ = record
# print(detail1)
# print(detail2)


# Exercises
# Exercise 1
# Define a 3×3 tuple grid of numbers (like a calculator keypad). Ask the user for a row and column (0-indexed) and print the value at that position. Then ask for a second position and return the sum of the two numbers.

grid = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
# Input: (0,2) and (2,0) → Output: 3 + 7 = 10


# keypad = [
#     [1,   2,    3],
#     [4,   5,    6],
#     [7,   8,    9],
#     ["*", "0", "#"]
# ]



# board = [[""] * 3] * 3

board = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""],
]
print(board)

for row in board:
    print(f"{row[0] or "_"} | {row[1] or "_"} | {row[2] or "_"}")


def get_board_position(keypad_pos):
    row = (keypad_pos - 1) // 3
    col = (keypad_pos - 1) % 3
    return (row, col)

print(get_board_position(8))

# 1. Create a visual representation of the board for the user.
# 2. Collect position where user wants to play and update the board ata that position.

# 0 -> 2
# 1 -> 0
# 2 -> 1

# ASSIGNMENT CORRECTION
# 1. Create a tuple called dimensions with values 10, 20, 30. Unpack the values into variables 
# length, width, and height, and print each variable.
# dimensions = (10, 20, 30)
# length, width, height = dimensions
# print(length)
# print(width)
# print(height)


# 2. Given the tuple coordinates:
# coordinates = (1.5, 2.5, 3.5)
# Unpack the tuple into variables x, y, and z, and print the value of y.
# coordinates = (1.5, 2.5, 3.5)
# _, y, _ = coordinates
# print(y)

# 3. Create a tuple called person with values ("John", 25, "Engineer"). Unpack the values into variables name, age, and profession, and print the value of profession.
# person = ("John", 25, "Engineer")
# name, age, profession = person
# print(profession)


# 4. Given the nested tuple data:
# data = (("Alice", "Bob"), ("Math", "Science"), (90, 85))
# Unpack the first element of data into variables student1 and student2, and print student2.
# data = (("Alice", "Bob"), ("Math", "Science"), (90, 85))
# (student1, student2), *_ = data
# print(student2)


# 5. Create a tuple called colors with values ("red", "green", "blue", "yellow"). Unpack the first two values into variables color1 and color2, and print both variables.
# colors = ("red", "green", "blue", "yellow")
# color1, color2, *_ = colors
# print(color1)
# print(color2)


# 6. Given the tuple record:
# record = ("Jane", (32, "Manager"), ["HR", "Finance"])
# Unpack the tuple to extract the name, the tuple containing age and position, and the list of departments. Print the extracted age and the first department.
# record = ("Jane", (32, "Manager"), ["HR", "Finance"])
# name, details, depts = record
# age, position = details
# print(age)
# dept1, dept2 = depts
# print(dept1)

# record = ("Jane", (32, "Manager"), ["HR", "Finance"])
# _, (age, _), (dept1, _) = record
# print(age)
# print(dept1)

# 7. Create a tuple called triplet with values ("one", "two", "three"). Unpack the tuple into variables and print the value of the second variable.
# triplet = ("one", "two", "three")
# _, second, _ = triplet
# print(second)


# 8. Given the tuple info:
# info = ("product123", ("Electronics", 299.99), (20, 5, 2022))
# Unpack the tuple to get the product ID, category, price, and manufacture date. Print the category and the manufacture year.
# info = ("product123", ("Electronics", 299.99), (20, 5, 2022))
# _, (category, _), (_, _, year) = info
# print(category)
# print(year)

# 9. Create a tuple called nested_tuple with values (("a", "b"), ("c", "d"), ("e", "f")). Unpack the nested tuples into individual variables and print the second value of the third tuple.
# nested_tuple = (("a", "b"), ("c", "d"), ("e", "f"))
# _, _, (_, second_val_tuple_3) = nested_tuple
# print(second_val_tuple_3)

# 10. Given the tuple inventory: inventory = (("apples", 50), ("bananas", 100), ("cherries", 75))
# Unpack the tuple to get each fruit and its corresponding quantity, then print the quantity of bananas.
# inventory = (("apples", 50), ("bananas", 100), ("cherries", 75))
# fruit1, fruit2, fruit3 = inventory
# name, qty = fruit2
# print(qty)

# inventory = (("apples", 50), ("bananas", 100), ("cherries", 75))
# _, (_, qty), _ = inventory
# print(qty)