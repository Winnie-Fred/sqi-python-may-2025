
# 1. Access and print the name of the teacher of "class2".
school = {
    "class1": {
        "students": ["Alice", "Bob"],
        "teacher": "Mr. Smith"
    },
    "class2": {
        "students": ["Charlie", "David"],
        "teacher": "Ms. Johnson"
    }
}
print("1. ",school["class2"]["teacher"])
# 2. Access and print the second employee in the "Engineering" department.
company = {
    "HR": ["Alice", "Bob"],
    "Engineering": ["Charlie", "David"]
}
print("2. ",company["Engineering"][1])
# 3. Access and print the name of the second assistant.
university = {
    "faculty": {
        "professors": ["Dr. Smith", "Dr. Brown"],
        "assistants": ["Ms. Green", "Mr. White"]
    },
    "students": ["John", "Jane", "Alice", "Bob"]
}
print("3. ",university["faculty"]["assistants"][1])
#  4.	Access and print the price of the third fruit.
store = {
    "fruits": [
        {"name": "apple", "price": 0.5},
        {"name": "banana", "price": 0.2},
        {"name": "cherry", "price": 1.5}
    ],
    "vegetables": [
        {"name": "carrot", "price": 0.3},
        {"name": "lettuce", "price": 1.0},
        {"name": "onion", "price": 0.4}
    ]
}
print("4. ",store["fruits"][2]["price"])
#  5. 	Access and print the second non-fiction book.
library = {
    "fiction": ["1984", "To Kill a Mockingbird", "The Great Gatsby"],
    "non-fiction": ["Sapiens", "Educated", "The Wright Brothers"]
}
print("5. ",library["non-fiction"][1])
#  6. 	Access and print the age of the first child.
family = {
    "parents": ["John", "Jane"],
    "children": [
        {"name": "Tom", "age": 5},
        {"name": "Lucy", "age": 8}
    ]
}
print("6. ",family["children"][0]["age"])

#  7.	Access and print the name of the second main course.
restaurant = {
    "menu": {
        "appetizers": ["soup", "salad"],
        "main_courses": ["steak", "pasta"],
        "desserts": ["cake", "ice cream"]
    },
    "staff": ["Chef A", "Chef B", "Waiter X", "Waiter Y"]
}
print("7. ",restaurant["menu"]["main_courses"][1])
#  8. 	Access and print the department of the user of the first desk.
workspace = {
    "desks": [
        {"user": "Alice", "department": "HR"},
        {"user": "Bob", "department": "Engineering"}
    ],
    "equipment": {"computers": 20, "printers": 10}
}
print("8. ",workspace["desks"][0]["department"])

#  9. 	Access and print the name of the second designer.
team = {
    "developers": ["Dev A", "Dev B"],
    "designers": ["Designer X", "Designer Y"],
    "projects": ["Project 1", "Project 2"]
}
print("9. ",team["designers"][1])
#  10. 	Access and print the second international destination.
travel = {
    "domestic": ["Boston", "Chicago"], 
    "international": ["Paris", "Tokyo"], 
    "expenses": {"flights": 1500, "hotels": 2000}
}
print("10. ",travel["international"][1])
