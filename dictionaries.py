# names = ["Mrs. Fash", "Lekan", "Omolola"]
# numbers = ["08037178750", "08166263885", "08183632046"]

# names = {"Mrs. Fash", "Lekan", "Omolola"}
# print(type(names))
# names = set()
# print(type(names))


# phone_book = {}
# phone_book = {"Mrs. Fash": "08037178750", 0: "zero", "Lekan": "08166263885", "Omolola": "08183632046"}

# print(phone_book[0])

# phone_book = {"Mrs. Fash": "08037178750", "Lekan": "08166263885", "Omolola": "08183632046"}
# print(phone_book["Lekan"])
# print(phone_book["Winnie"])
# print(phone_book["Mrs. Fash"])

# print("before: ", phone_book)
# phone_book["Molayo"] = "07054319485"
# phone_book["Lekan"] = "07026570964"

# del phone_book["Omolola"]

# print("Mrs. Fash" in phone_book)
# print("Mrs Fash" in phone_book)
# print("Jeff Bezos" in phone_book)

# print(phone_book.keys())
# print(type(phone_book.keys()))
# print(list(phone_book.keys()))
# print("Mrs. Fash" in phone_book.keys())
# print("Mrs. Fash" in phone_book.values())
# print("08183632046" in phone_book.values())
# print(phone_book.items())
# print("08183632046" in phone_book.items())

# del phone_book
# phone_book.clear()
# print(phone_book)  NameError
# print("after:  ", phone_book)

# 1. Create a dictionary called "my_info" with keys "name", "is_male", "age", "complexion". Provide the values for the keys
# 2. Print the dictionary
# 3. Add a key called "height" and assign a float height to it
# 4. Remove the age from the dict
# 5. Change the "name" to another one of your names
# 6. Check if "weight" exists as a key in the dictionary
# 7. Check if False exists as a value in the dictionary
# 8. Get the value of "is_male"
# 9. Print the length of the dictionary
# 10. Print the keys of the dictionary
# 11. Print a LIST of the values of the dictionary
# 12. Print the items of the dictionary
# 13. Clear the dictionary and print it
# 14. Delete the entire dictionary so it no longer exists

# my_info = {"name": "Winnie", "is_male": False, "age": 23, "complexion": "dark"}
# my_info["height"] = 1.45
# del my_info["age"]
# my_info["name"] = "Winifred"
# print("weight" in my_info)
# print("weight" in my_info.keys())
# print(False in my_info.values())
# print(my_info["is_male"])
# print(len(my_info))
# print(my_info.keys())
# print(list(my_info.values()))
# print(my_info.items())
# my_info.clear()
# print(my_info)
# del my_info

# my_info = {"name": "Winnie", "is_male": False, "age": 23, "complexion": "dark"}
# my_info_2 = {"is_male": False, "age": 23, "name": "Winnie", "complexion": "dark"}

# print(my_info == my_info_2)


# ==============================================.GET()==============================================
# yoruba_translator = {
#     "mother": "mama",
#     "mum": "mama",
#     "snake": "ejo",
#     "book": "iwe",
#     "herbalist": "awo",
#     "chair": "aga",
#     "life": "aye",
#     "book": "iwe",
# }

# print(yoruba_translator)

# print(yoruba_translator["herbalist"])

# print(yoruba_translator.get("herbalist"))
 
# print(yoruba_translator.get("air"))  None

# print(yoruba_translator["air"])  KeyError

# print(yoruba_translator.get("air", "Does not exist"))
# print(yoruba_translator.get("chair", "Does not exist"))

# ==============================================.GET()==============================================

# ==============================================.SETDEFAULT==============================================
# yoruba_translator = {
#     "mother": "mama",
#     "mum": "mama",
#     "snake": "ejo",
#     "book": "iwe",
#     "herbalist": "awo",
#     "chair": "aga",
#     "life": "aye",
#     "book": "iwe",
# }
# print(yoruba_translator.setdefault("mummy", "mama"))
# print(yoruba_translator.setdefault("snake", "mama"))
# print(yoruba_translator.setdefault("coat"))
# print(yoruba_translator)

# ==============================================.SETDEFAULT==============================================



# ==============================================.UPDATE()==============================================
# my_dream_car = {
#     "brand": "Lamborghini",
#     "is_electric": False,
#     "manufacture_year": 2025,
# }
# print("before:  ", my_dream_car)
# my_dream_car.update({"is_electric": True})
# my_dream_car["color"] = "yellow"
# my_dream_car.update({
#     "color": "yellow",
#     "max_speed_mph": 221
# })
# my_dream_car.update(color="yellow", max_speed_mph=221)

# print("after:  ", my_dream_car)

# ==============================================.UPDATE()==============================================



# ==============================================REMOVING ITEMS==============================================

# my_dream_house = {
#     "type": "mansion",
#     "location": "Abuja",
#     "no_of_rooms": 24,
#     "color": "white"
# }
# print("before:  ", my_dream_house)

# popped_val = my_dream_house.pop("no_of_rooms")
# print("popped value: ", popped_val)
# del my_dream_house["no_of_rooms"]
# last_item = my_dream_house.popitem()
# print("popped item:", last_item)
# print("after:  ", my_dream_house)


# ==============================================REMOVING ITEMS==============================================


# ==============================================MISCELLANEOUS==============================================
# my_dream_house = {
#     "type": "mansion",
#     "location": "Abuja",
#     "no_of_rooms": 24,
#     "color": "white"
# }
# print(type(my_dream_house))


# person = {
#     ("Lekan", "male"): 30,
#     ("Awwal", "male"): 10,
# }
# person = {
#     "Lekan": (30, 25),
#     "Awwal": (10, 15),
# }
# print(person)

# ==============================================MISCELLANEOUS==============================================

# ==============================================CASTING TO DICT==============================================
# names = ["Mrs. Fash", "Lekan", "Omolola"]
# print(dict(names))

# phone_book = [("Mrs. Fash", "08037178750"), ("Lekan", "08166263885"), ("Omolola", "08183632046")]
# phone_book = (("Mrs. Fash", "08037178750"), ("Lekan", "08166263885"), ("Omolola", "08183632046"))
# phone_book = {("Mrs. Fash", "08037178750"), ("Lekan", "08166263885"), ("Omolola", "08183632046")}
# print(dict(phone_book))

# my_dream_man = dict(is_tall=True, complexion="dark", status="rich")
# print(my_dream_man)

# ==============================================CASTING TO DICT==============================================


# ==============================================.COPY()==============================================

# my_dream_man = {'is_tall': True, 'complexion': 'dark', 'status': 'rich'}
# my_dream_man_copy = my_dream_man.copy()
# print(my_dream_man)
# print(my_dream_man_copy)
# ==============================================.COPY()==============================================



# ==============================================QUIZ CORRECTION==============================================
# 1. Access and print the name of the teacher of "class2".
# school = {
#     "class1": {
#         "students": ["Alice", "Bob"],
#         "teacher": "Mr. Smith"
#     },
#     "class2": {
#         "students": ["Charlie", "David"],
#         "teacher": "Ms. Johnson"
#     }
# }
# print(school["class2"]["teacher"])

# 2. Access and print the second employee in the "Engineering" department.
# company = {
#     "HR": ["Alice", "Bob"],
#     "Engineering": ["Charlie", "David"]
# }
# print(company["Engineering"][1])

# 3. Access and print the name of the second assistant.
# university = {
#     "faculty": {
#         "professors": ["Dr. Smith", "Dr. Brown"],
#         "assistants": ["Ms. Green", "Mr. White"]
#     },
#     "students": ["John", "Jane", "Alice", "Bob"]
# }
# print(university["faculty"]["assistants"][1])

#  4.	Access and print the price of the third fruit.
# store = {
#     "fruits": [
#         {"name": "apple", "price": 0.5},
#         {"name": "banana", "price": 0.2},
#         {"name": "cherry", "price": 1.5}
#     ],
#     "vegetables": [
#         {"name": "carrot", "price": 0.3},
#         {"name": "lettuce", "price": 1.0},
#         {"name": "onion", "price": 0.4}
#     ]
# }
# print(store["fruits"][2]["price"])
# 5. Access and print the second non-fiction book.
# library = {
#     "fiction": ["1984", "To Kill a Mockingbird", "The Great Gatsby"],
#     "non-fiction": ["Sapiens", "Educated", "The Wright Brothers"]
# }
# print(library["non-fiction"][1])

#  6. 	Access and print the age of the first child.
# family = {
#     "parents": ["John", "Jane"],
#     "children": [
#         {"name": "Tom", "age": 5},
#         {"name": "Lucy", "age": 8}
#     ]
# }
# print(family["children"][0]["age"])

# 7. Access and print the name of the second main course.
# restaurant = {
#     "menu": {
#         "appetizers": ["soup", "salad"],
#         "main_courses": ["steak", "pasta"],
#         "desserts": ["cake", "ice cream"]
#     },
#     "staff": ["Chef A", "Chef B", "Waiter X", "Waiter Y"]
# }
# print(restaurant["menu"]["main_courses"][1])

#  8. 	Access and print the department of the user of the first desk.
# workspace = {
#     "desks": [
#         {"user": "Alice", "department": "HR"},
#         {"user": "Bob", "department": "Engineering"}
#     ],
#     "equipment": {"computers": 20, "printers": 10}
# }
# print(workspace["desks"][0]["department"])

#  9. 	Access and print the name of the second designer.
# team = {
#     "developers": ["Dev A", "Dev B"],
#     "designers": ["Designer X", "Designer Y"],
#     "projects": ["Project 1", "Project 2"]
# }
# print(team["designers"][1])

#  10. 	Access and print the second international destination.
# travel = {"domestic": ["Boston", "Chicago"], "international": ["Paris", "Tokyo"], "expenses": 
# {"flights": 1500, "hotels": 2000}}
# print(travel["international"][1])



# ==============================================QUIZ CORRECTION==============================================


# ==============================================ASSIGNMENT CORRECTION==============================================

# 1. Create a dictionary called `student` with keys "name", "age", and "grade", and 
# corresponding values "John", 20, and "A". Access and print the value of "name".

# student = {"name": "John", "age": 20, "grade": "A"}
# print(student["name"])

# 2. Create a dictionary called `product` with keys "name", "price", and "stock", and 
# corresponding values "Laptop", 999.99, and 50. Change the value of "price" to 899.99.
# product = {"name": "Laptop", "price": 999.99, "stock": 50}
# product["price"] = 899.99

# 3. Create a dictionary called `employee` with keys "name" and "position", and corresponding values "Alice" and "Manager". Add a new key "salary" with the value 50000.
# employee = {"name": "Alice", "position": "Manager"}
# employee["salary"] = 50000

# 4. Create a dictionary called `inventory` with keys "apple", "banana", and "orange", and values 10, 5, and 8 respectively. Remove the key "banana".
# inventory = {"apple": 10, "banana": 5, "orange": 8}
# del inventory["banana"]
# inventory.pop("banana")

# 5. Create a dictionary called person with keys "name", "age", and "city", and corresponding values "Bob", 25, and "New York". Use the copy() method to make a copy of the dictionary and call it person_copy.
# person = {"name": "Bob", "age": 25, "city": "New York"}
# person_copy = person.copy()

# 6. Create a nested dictionary called `family` with keys "child1", "child2", and "child3", each containing a dictionary with keys "name" and "age" with appropriate values. Access and print the age of "child2".
# family = {
#     "child1": {
#         "name": "Winifred",
#         "age": 23,
#     },
#     "child2": {
#         "name": "Justin",
#         "age": 22
#     },
#     "child3": {
#         "name": "Augusta",
#         "age": 20
#     }
# }
# print(family["child2"]["age"])

# 7. Create a dictionary called `car` with keys "brand", "model", and "year", and corresponding values "Toyota", "Corolla", and 2020. Access and print the value of "model".
# car = {"brand": "Toyota", "model": "Corolla", "year": 2020}
# print(car["model"])


# 8. Create a dictionary called `settings` with keys "volume", "brightness", and "language", and corresponding values 50, 75, and "English". Change the "language" to "Spanish".
# settings = {"volume": 50, "brightness": 75, "language": "English"}
# settings["language"] = "Spanish"


# 9. Create a dictionary called `scores` with keys "math", "science", and "english", and corresponding values 90, 85, and 88. Remove the key "science".
# scores = {"math": 90, "science": 85, "english": 88}
# del scores["science"]
# scores.pop("science")

# 10. Create a dictionary called `menu` with keys "starter", "main_course", and "dessert", and corresponding values "Soup", "Steak", and "Ice Cream". Check if the key "appetizer" is present in the dictionary.
# menu = {"starter": "soup", "main_course": "steak", "dessert": "ice cream"}
# print("appetizer" in menu)

# 11. Create a dictionary called `config` with keys "theme", "language", and "timezone", and corresponding values "dark", "English", and "UTC". Clear the dictionary.
# config = {"theme": "dark", "language": "English", "timezone": "UTC"}
# config.clear()

#  12.	Create a dictionary called `phone_book` with keys "Alice", "Bob", and 
# "Charlie", and corresponding phone numbers as values. Print the number of 
# items in the dictionary.
# phone_book = {"Alice": "08123344556", "Bob": "09030556547", "Charlie": "0806066454"}
# print(len(phone_book))

#  13. Create a dictionary called `grades` with keys "math", "science", and "history", 
# and corresponding values "A", "B", and "C". Get a LIST of all the keys in the 
# dictionary.
# grades = {"math": "A", "science": "B", "history": "C"}
# print(list(grades.keys()))

#  14. 	Create a dictionary called `employee` with keys "name", "position", and 
# "salary", and corresponding values "David", "Engineer", and 70000. Get a LIST 
# of all the values in the dictionary.
# employee = {"name": "David", "position": "Engineer", "salary": 70000}
# print(employee.values()[0])
# print(type(employee.values()))
# print(list(employee.values())[0])

#  15. 	Create a dictionary called `game` with keys "title", "genre", and "rating", and 
# corresponding values "Minecraft", "Sandbox", and 4.5. Get a LIST of all 
# key-value pairs in the dictionary.
# game = {"title": "Minecraft", "genre": "Sandbox", "rating": 4.5}
# print(list(game.items()))


# ==============================================ASSIGNMENT CORRECTION==============================================

