# class Person:
#     def __init__(self, name, height, complexion, is_male, age):
#         self.full_name = name
#         self.height = height
#         self.complexion = complexion
#         self.is_male = is_male
#         self.age = age


#     def introduce_yourself(self):
#         gender_statement = "I am male" if self.is_male else "I am female"
#         return f"My name is {self.full_name}. {gender_statement}. I am {self.height}m tall. I am {self.complexion} in complexion. I am {self.age} years old."


#     def sing(self, song):
#         return f"{self.full_name} sings {song}"


# molayo = Person("Molayo Mercy", 1.54, "dark", False, 27)
# print(molayo)
# print(molayo.full_name)
# print(molayo.is_male)
# print(molayo.introduce_yourself())
# print(molayo.sing("Heartbreak Anniversary"))
# lekan = Person("Lekan Oyewole", 1.62, "light", True, 30)
# print(lekan)
# print(lekan.full_name)
# print(lekan.is_male)
# print(lekan.introduce_yourself())
# print(lekan.sing("Perfect"))


# Create a class called `Book`.
# The class has the following attributes or properties - title, author, no_of_pages, genre, is_published (True or False)
# The class can print_info() which returns all the necessary info about that particular book
# Then create two different books and call their print_info()
# Also print their title and their author.


# class Book:
#     def __init__(self, title, author, no_of_pages, genre, is_published):
#         self.title = title
#         self.author = author
#         self.no_of_pages = no_of_pages
#         self.genre = genre
#         self.is_published = is_published

#     def print_info(self):
#         print(f"Title: {self.title}")
#         print(f"Author: {self.author}")
#         print(f"Number of pages: {self.no_of_pages}")
#         print(f"Genre: {self.genre}")
#         published = "Yes" if self.is_published else "No"
#         print(f"Is published: {published}")

    
# book1 = Book("Title of Book 1", "Author of Book 1", 23, "fiction", True)
# book2 = Book("Title of Book 2", "Author of Book 2", 200, "Mystery", False)
# book3 = Book("Title of Book 3", "Author of Book 3", 567, "History", False)
# book4 = Book("Title of Book 4", "Author of Book 4", 65, "Adventure", True)

# book1.print_info()
# book2.print_info()
# book3.print_info()
# book4.print_info()

# print(book1.title)
# print(book2.title)
# print(book3.title)
# print(book4.title)

# print(book1.author)
# print(book2.author)
# print(book3.author)
# print(book4.author)


# Forms
# Attendance - Full Name, Time In, Time Out, Signature
# Job Application - Full Name, Resume URL, LinkedIn URL, GitHub URL



# from datetime import datetime, time

# class AttendanceRecord:
#     def __init__(self, full_name: str, time_in: datetime, time_out: datetime, signature: str):
#         self.full_name = full_name
#         self.time_in = time_in
#         self.time_out = time_out
#         self.signature = signature

#     def __str__(self):
#         return f"{self.full_name} | {self.time_in} | {self.time_out} | {self.signature}"


# class AttendancePage:
#     def __init__(self, records: list[AttendanceRecord], page_no: int):
#         self.records = records
#         self.page_number = page_no

#     def __str__(self):
#         header = f"Page {self.page_number}\nFull Name | Time In | Time Out | Signature\n"
#         str_records = [str(record) for record in self.records]
#         return header + "\n".join(str_records)

# class AttendanceBook:
#     def __init__(self, pages: list[AttendancePage]):
#         self.pages = pages

#     def __str__(self):
#         book_pages = [str(page) for page in self.pages]
#         book_pages = "\n".join(book_pages)
#         return f"SQI PYTHON MAY 2025 ATTENDANCE\n{book_pages}"
    
#     def find_late_comers(self, start_time: datetime, end_time: datetime):
#         late_comers = []
#         for page in self.pages:
#             for record in page.records:
#                 if start_time.date() <= record.time_in.date() <= end_time.date():
#                     time_in = record.time_in.time()
#                     if time_in > time(8, 30):
#                         late_comers.append(record.full_name)
#         return late_comers



# record1 = AttendanceRecord("Awwal Abdulwahab", datetime(2025, 6, 18, 8, 10), datetime(2025, 6, 18, 10, 35), "awwal")
# record2 = AttendanceRecord("Omolola Muhammed", datetime(2025, 6, 18, 8, 29), datetime(2025, 6, 18, 3, 47), "lola")
# record3 = AttendanceRecord("Molayo Elemese", datetime(2025, 6, 18, 8, 43), datetime(2025, 6, 18, 4, 25), "mercy")
# record4 = AttendanceRecord("Lekan Oyewole", datetime(2025, 6, 18, 8, 20), datetime(2025, 6, 18, 1, 12), "lekan")

# page1 = AttendancePage([record1, record2], 1)
# page2 = AttendancePage([record3, record4], 100)

# sqi_python_may_2025_attendance = AttendanceBook([page1, page2])

# # print(sqi_python_may_2025_attendance)
# print(sqi_python_may_2025_attendance.find_late_comers(datetime(2025, 6, 1), datetime(2025, 6, 30)))


# Create a class called CartItem.
# A CartItem has a name, a price, and a quantity
# Also create a class called Cart
# A cart is a list of CartItems
# A cart can print the total price of CartItems in it

# Ex
# class CartItem:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#     def total_price(self):
#         return self.price * self.quantity
    
# class Cart:
#     def __init__(self, cart_items: list[CartItem]):
#         self.cart_items = cart_items

#     def total(self):
#         total_price_cart = 0
#         for cart_item in self.cart_items:
#             total_price_cart += cart_item.total_price()
#         return total_price_cart
    

# cart_item1 = CartItem("eggs", 250, 4)
# cart_item2 = CartItem("bread", 1200, 6)
# print(cart_item1.total_price()) # -> 1000
# print(cart_item2.total_price()) # -> 7200
# cart = Cart([cart_item1, cart_item2])
# print(cart.total()) # -> 8200


# class CartItem:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity

    
# class Cart:
#     def __init__(self, cart_items: list[CartItem]):
#         self.cart_items = cart_items

#     def total(self):
#         total_price_cart = 0
#         for cart_item in self.cart_items:
#             total_price = cart_item.price * cart_item.quantity
#             total_price_cart += total_price
#         return total_price_cart

# cart_item1 = CartItem("eggs", 250, 4)
# cart_item2 = CartItem("bread", 1200, 6)
# cart = Cart([cart_item1, cart_item2])
# print(cart.total()) # -> 8200

# PI = 22/7

# class Circle:

#     PI = 3.14

#     def __init__(self, radius=12):
#         self.radius = radius

#     @property
#     def diameter(self):
#         return self.radius * 2
    
#     def show_pi(self):
#         # return self.PI
#         return Circle.PI
    
# circle = Circle(3)
# circle2 = Circle(5)
# circle3 = Circle()
# # print(circle.diameter())
# # print(circle.diameter)
# # print(circle.PI)
# # print(circle2.PI)
# # print(PI)
# print(circle3.show_pi())
# print(circle3.radius)
# print(circle3.diameter)
# print(circle.show_pi())
# print(circle2.show_pi())


# ASSIGNMENT CORRECTION
# Fill in the Line class methods to accept coordinates as a pair of tuples and 
# return the slope and distance of the line. Look up the formulas for finding the distance and slope of a line.


# class Line:
#     def __init__(self, coor1, coor2): 
#         self.x1, self.y1 = coor1
#         self.x2, self.y2 = coor2

#     def distance(self):
#         return (((self.x2 - self.x1) ** 2) + ((self.y2 - self.y1) ** 2)) ** 0.5

#     def slope(self):
#         return (self.y2 - self.y1) / (self.x2 - self.x1)

# # EXAMPLE EXECUTION

# coordinatel = (3,2)
# coordinate2 = (8,10)

# line_1 = Line(coordinatel, coordinate2)

# print(line_1.distance())  # 9.433981132056603
# print(line_1.slope())  # 1.6


# 2. Fill in the class
# class Cylinder:

#     PI = 3.14   

#     def __init__(self, height=1, radius=1):
#         self.height = height
#         self.radius = radius

#     def volume(self):
#         return Cylinder.PI * (self.radius ** 2) * self.height

#     def surface_area(self):
#         return (2 * Cylinder.PI * self.radius) * (self.radius + self.height)

# # EXAMPLE EXECUTION

# cylinder = Cylinder(2,3)
# print(cylinder.volume())  # 56.52
# print(cylinder.surface_area())  # 94.2



# class Person:
#     def __init__(self, name, height, complexion, is_male, age):
#         self.full_name = name
#         self.height = height
#         self.complexion = complexion
#         self.is_male = is_male
#         self.age = age


#     def introduce_yourself(self):
#         gender_statement = "I am male" if self.is_male else "I am female"
#         return f"My name is {self.full_name}. {gender_statement}. I am {self.height}m tall. I am {self.complexion} in complexion. I am {self.age} years old."

# class Employee(Person):

#     def __init__(self, name, height, complexion, is_male, age, salary):
#         super().__init__(name, height, complexion, is_male, age)
#         self.salary = salary

#     # def __init__(self, full_name):
#     #     self.full_name = full_name


#     def work(self):
#         return f"{self.full_name} is working! Employee receives ₦{self.salary} monthly"
    
#     def introduce_yourself(self):
#         introduction = super().introduce_yourself()
#         return f"Employee Introduction: {introduction}"


# person = Person("Molayo Mercy", 1.54, "dark", False, 27)
# employee = Employee("Lekan Oyewole", 1.62, "light", True, 30, 780_000)

# print(issubclass(Person, Employee))
# print(issubclass(Employee, Person))
# print(person.introduce_yourself())
# print(employee.introduce_yourself())
# print(employee.work())

# print(isinstance(person, Person))
# print(isinstance(employee, Person))
# print(isinstance(person, Employee))

# print(isinstance(4.0, int))



# class Animal:
#     def __init__(self, name: str, type: str, has_legs: bool, has_wings: bool, age: int, sound: str):
#         self.name = name
#         self.type = type
#         self.has_legs = has_legs
#         self.has_wings = has_wings
#         self.age = age
#         self.sound = sound
#         self.article = "an" if self.name.lower().startswith(("a", "e", "i", "o", "u")) else "a"

#     def speak(self, speech):
#         return f"{self.sound}! {self.name} says {speech}"
    
#     def get_info(self):
#         return f"My name is {self.name}. I am {self.article} {self.type}"
    
#     def make_sound(self):
#         return f"{self.article} {self.type}, {self.name} says {self.sound}"
    

# class Dog(Animal):
#     def __init__(self, name, age, breed):
#         super().__init__(name, "dog", True, False, age, "woof")
#         self.breed = breed

#     def guard(self, owner):
#         self.something = "Something"
#         return f"I am {self.name}. I am guarding {owner}"
    
#     def make_sound(self):
#         print(f"from make_sound method:, {self.something}")
#         return f"A dog, {self.name} says Woof"
    

# smart = Dog("Smart", 4, "German Shepherd")
# smart.guard("Winnie")
# smart.make_sound()

# fido = Animal("Fido", "cat", True, False, 3, "meow")
# kion = Animal("Kion", "lion", True, False, 5, "GGRRRROOOAAARRR!")
# smart = Dog("Smart", 4, "German Shepherd")

# animals = [fido, kion]
# print(fido.speak("I haven't been fed"))
# print(kion.speak("Feed me"))
# for animal in animals:
#     print(animal.get_info())
#     print(animal.make_sound())



# class Device:
#     def operate(self):
#         print("Operating the device")

# class SmartPhone:
#     def operate(self):
#         print("Operating the smartphone")

# class Fridge:
#     def operate(self):
#         print("Operating the fridge")

# class Blender:
#     def operate(self):
#         print("Operating the blender")


# device = Device()
# smartphone = SmartPhone()
# fridge = Fridge()
# blender = Blender()

# devices = [device, smartphone, fridge, blender]

# devices = [Device(), SmartPhone(), Fridge(), Blender()]

# for device in devices:
#     device.operate()

# class Book:
#     def __init__(self, title, author, no_of_pages, is_published, is_fiction):
#         self.title = title
#         self.author = author
#         self.is_published = is_published
#         self.is_fiction = is_fiction
#         self.no_of_pages = no_of_pages

#     def publish(self):
#         self.is_published = True

#     def __repr__(self):
#         return f'Book(title="{self.title}", author="{self.author}", no_of_pages={self.no_of_pages}, is_fiction={self.is_fiction}, is_published={self.is_published}'
    
#     # def __str__(self):
#     #     return f"{self.title} by {self.author}"
    
#     def __len__(self):
#         return self.no_of_pages
    

# book = Book("And then there were None", "Agatha Christie", 345, False, True)
# book = Book(title="And then there were None", author="Agatha Christie", no_of_pages=345, is_fiction=False, is_published=True)
# book.publish()
# print(book.is_published)
# print(str(book))
# print(repr(book))
# print(len(book))

# book = Book(title="And then there were None", author="Agatha Christie", no_of_pages=345, is_fiction=False, is_published=True)
# book.author = "AGATHA CHRISTIE"
# book.no_of_pages = 780
# print(str(book))
# print(repr(book))

# class LightBulb:
#     def __init__(self, is_on):
#         self.is_on = is_on

#     def press_switch(self):
#         self.is_on = not self.is_on

# light_bulb = LightBulb(True)
# light_bulb.press_switch()
# print(light_bulb.is_on)  # False
# light_bulb.press_switch()  
# print(light_bulb.is_on)  # True
# light_bulb.press_switch()  
# light_bulb.press_switch()  
# print(light_bulb.is_on)  # True



# BONUS EXERCISE
# 🎮 Exercise: 
# You are building a simple game. Create different types of game characters.

# Step 1 — Create a base class
# Create a class called GameCharacter that has:

# Attributes:

# name (string)

# health (integer)

# attack_power (integer)

# A method attack(target) that reduces the target's health by self.attack_power.

# class GameCharacter:
#     def __init__(self, name: str, health: int, attack_power: int):
#         self.name = name
#         self.health = health
#         self.attack_power = attack_power

#     def attack(self, target):
#         if target.name == self.name:
#             print(f"{self.name} cannot attack themself")
#             return
#         print(f"{self.name} attacks {target.name}")
#         target.health -= self.attack_power
#         print(f"{target.name}'s health is now {target.health}")


# # Step 2 — Create subclasses
# # 1️⃣ Warrior

# class Warrior(GameCharacter):
#     def __init__(self, name, health, attack_power, armor):
#         super().__init__(name, health, attack_power)
#         self.armor = armor

#     def attack(self, target):
#         target.health -= 10
#         super().attack(target)
    
    

# # Has an extra attribute: armor (integer)

# # Override attack(target) so that it deals extra 10 damage.

# # 2️⃣ Mage

# class Mage(GameCharacter):
#     def __init__(self, name, health, attack_power, mana):
#         super().__init__(name, health, attack_power)
#         self.mana = mana

#     def attack(self, target):
#         if self.mana < 5:
#             print("Not enough mana to attack")
#             return
#         super().attack(target)
#         self.mana -= 5

# Has an extra attribute: mana (integer)

# Override attack(target) so that it uses 5 mana each time it attacks. If mana is less than 5, print "Not enough mana to attack".

# Step 3 — Create objects
# Create one Warrior and one Mage.

# Let them attack each other a few times.

# Print the health and other attributes after each attack.



# warrior = Warrior(name="Thor", health=100, attack_power=10, armor=20)
# mage = Mage(name="Merlin", health=100, attack_power=10, mana=10)
# warrior.attack(mage)
# # Output:
# # Thor attacks Merlin!
# # Merlin's health is now 80
# mage.attack(warrior)
# # Output:
# # Merlin attacks Thor!
# # Thor's health is now 90
# mage.attack(warrior)
# # Merlin attacks Thor!
# # Thor's health is now 80
# mage.attack(warrior)
# # Not enough mana to attack
# print(warrior.health)  # 80
# print(mage.health)  # 80
# print(mage.mana)  # 0

# gaius health 80, mana 30
# merlin health 100 mana 5
# merlin health 90 mana 5
# gaius health 80, mana 25

# merlin health 80 mana 5
# gaius health 80, mana 20

# gaius health 60, mana 20
# merlin health 80 mana 0


# merlin = Mage(name="Merlin", health=100, attack_power=20, mana=10)
# gaius = Mage(name="Gaius", health=100, attack_power=10, mana=30)

# merlin.attack(gaius)
# # Merlin attacks Gaius
# # gauis health is now 80
# gaius.attack(merlin)
# # Gaius attacks Merlin
# # merlin health is now 90
# gaius.attack(gaius)
# # Gaius cannot attack themself
# gaius.attack(merlin)
# # Gaius attacks Merlin
# # Merlin health is now 80
# merlin.attack(gaius)
# # Merlin attacks Gaius
# # Gaius health is now 60
# merlin.attack(gaius)
# # Not enough mana to attack


# ASSIGNMENT
# Space Mission
# You are building a simple simulation of a space mission. There are different types of spacecraft.

# 1. Create a base class
# Create a class called Spacecraft with:
# Attributes:
# name (string)
# fuel (integer)

# Methods:
# launch() — prints "Launching {name}!"
# Reduces fuel by 50 units.
# If not enough fuel, print "Not enough fuel to launch."

# refuel(amount) — adds amount to fuel.


# 2. Create subclasses
# CargoShip
# Has an additional attribute: cargo_weight (integer)
# Override launch() — launching consumes extra fuel depending on cargo:
# total fuel reduction = 50 + (cargo_weight * 2)

# PassengerShip
# Has an additional attribute: passenger_count (integer)
# Override launch() — if passenger_count > 100, print "Too many passengers. Cannot launch."
# Otherwise, launch normally (reduce fuel by 50 units)

# Handle negative refuel amounts.


# # SAMPLE EXECUTION
# # Create objects
# cargo_ship = CargoShip("Galactic Hauler", 200, 30)
# passenger_ship = PassengerShip("Star Voyager", 100, 80)

# # Attempt to launch both ships
# cargo_ship.launch()
# # Output: Launching Galactic Hauler with cargo!
# # Fuel after launch: 200 - (50 + 30*2) = 90

# passenger_ship.launch()
# # Output: Launching Star Voyager!
# # Fuel after launch: 100 - 50 = 50

# # Refuel both ships
# cargo_ship.refuel(50)
# # Output: Refueled Galactic Hauler with 50 units. Fuel is now 140.

# passenger_ship.refuel(30)
# # Output: Refueled Star Voyager with 30 units. Fuel is now 80.

# # Launch again after refueling
# cargo_ship.launch()
# # Output: Launching Galactic Hauler with cargo!
# # Fuel after launch: 140 - (50 + 30*2) = 30

# passenger_ship.launch()
# # Output: Launching Star Voyager!
# # Fuel after launch: 80 - 50 = 30

# # Try to refuel with invalid amount
# cargo_ship.refuel(-10)
# # Output: Cannot refuel with negative amount.

# # Test PassengerShip with too many passengers
# passenger_ship.passenger_count = 120
# passenger_ship.launch()
# # Output: Too many passengers. Cannot launch.

# # Try to launch cargo ship with low fuel
# cargo_ship.launch()
# # Output: Not enough fuel to launch.



# ASSIGNMENT CORRECTION


class InsufficientFundsError(Exception):
    def __init__(self, amount, balance):
        self.message = f"Insufficient Funds Error. You need {amount - balance} more to complete that transaction."
        super().__init__(self.message)

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance
        print("Init method running")
    
    @property
    def balance(self):
        return self._format_currency(self._balance)

    def __str__(self):
        return f"""Account owner: {self.owner}
Account balance: {self._format_currency(self._balance)}"""
    
    def _format_currency(self, amount):
        return f"₦{amount:,.2f}"

    def _validate_amount(self, amount):
        if amount < 1:
            print("Cannot deposit a negative amount")
            return False
        return True

    def deposit(self, amount):
        if not self._validate_amount(amount):
            return
        self._balance += amount
        return "Deposit accepted"

    def withdraw(self, amount):
        if not self._validate_amount(amount):
            return
        if amount > self._balance:
            raise InsufficientFundsError(amount, self._balance)
        self._balance -= amount
        return "Withdrawal accepted"


# #1. Instantiate the class
acct1 = Account('Winnie', 100)

# #2. Print the object
print(acct1)
# # Output:
# # Account owner: Winnie
# # Account balance: $100

# #3. Show the account owner attribute
print(acct1.owner)  # Winnie

# #4. Show the account balance attribute 
print(acct1.balance)  # ₦100.00

# #5. Make a series of deposits and withdrawals 
print(acct1.deposit(50))  # Output: Deposit Accepted

print(acct1.withdraw(15))  # Output: Withdrawal Accepted

# #6. Make a withdrawal that exceeds the available balance 
try:
    print(acct1.withdraw(500))
except InsufficientFundsError as e:
    print(e)

print(acct1.balance)  # ₦135.00
print(acct1._balance)  # ₦135



# You are building a simple simulation of a space mission. There are different types of spacecraft.

# 1. Create a base class
# Create a class called Spacecraft with:
# Attributes:
# name (string)
# fuel (integer)

# Methods:
# launch() — prints "Launching {name}!"
# Reduces fuel by 50 units.
# If not enough fuel, print "Not enough fuel to launch."

# refuel(amount) — adds amount to fuel.

# class Spacecraft:
#     def __init__(self, name: str, fuel: int):
#         self.name = name
#         self.fuel = fuel

#     def is_fuel_enough(self):
#         if self.fuel < 50:
#             print("Not enough fuel to launch.")
#             return False
#         return True
        
#     def launch(self):
#         if not self.is_fuel_enough():
#             return
#         new_fuel = self.fuel - 50 
#         print(f"Launching {self.name}!")
#         print(f"Fuel after launch: {self.fuel} - 50 = {new_fuel}")
#         self.fuel = new_fuel

#     def refuel(self, amount):
#         if amount < 1:
#             print("Cannot refuel with negative amount.")
#             return
#         self.fuel += amount
#         print(f"Refueled {self.name} with {amount} units. Fuel is now {self.fuel}.")

        

# # 2. Create subclasses
# # CargoShip
# # Has an additional attribute: cargo_weight (integer)
# # Override launch() — launching consumes extra fuel depending on cargo:
# # total fuel reduction = 50 + (cargo_weight * 2)


# class CargoShip(Spacecraft):
#     def __init__(self, name: str, fuel: int, cargo_weight: int):
#         super().__init__(name, fuel)
#         self.cargo_weight = cargo_weight

#     def launch(self):
#         if not self.is_fuel_enough():
#             return
#         new_fuel = self.fuel - (50 + (self.cargo_weight * 2))
#         print(f"Launching {self.name} with cargo!")
#         print(f"Fuel after launch: {self.fuel} - 50 + ({self.cargo_weight} * 2) = {new_fuel}")
#         self.fuel = new_fuel

# # PassengerShip
# # Has an additional attribute: passenger_count (integer)
# # Override launch() — if passenger_count > 100, print "Too many passengers. Cannot launch."
# # Otherwise, launch normally (reduce fuel by 50 units)

# # 3. Handle negative refuel amounts.

# class PassengerShip(Spacecraft):
#     def __init__(self, name: str, fuel: int, passenger_count: int):
#         super().__init__(name, fuel)
#         self.passenger_count = passenger_count

#     def launch(self):
#         if self.passenger_count > 100:
#             print("Too many passengers. Cannot launch.")
#             return
#         return super().launch()


# # SAMPLE EXECUTION
# # Create objects
# cargo_ship = CargoShip("Galactic Hauler", 200, 30)
# passenger_ship = PassengerShip("Star Voyager", 100, 80)

# # Attempt to launch both ships
# cargo_ship.launch()
# # Output: Launching Galactic Hauler with cargo!
# # Fuel after launch: 200 - (50 + 30*2) = 90

# passenger_ship.launch()
# # Output: Launching Star Voyager!
# # Fuel after launch: 100 - 50 = 50

# # Refuel both ships
# cargo_ship.refuel(50)
# # Output: Refueled Galactic Hauler with 50 units. Fuel is now 140.

# passenger_ship.refuel(30)
# # Output: Refueled Star Voyager with 30 units. Fuel is now 80.

# # Launch again after refueling
# cargo_ship.launch()
# # Output: Launching Galactic Hauler with cargo!
# # Fuel after launch: 140 - (50 + 30*2) = 30

# passenger_ship.launch()
# # Output: Launching Star Voyager!
# # Fuel after launch: 80 - 50 = 30

# # Try to refuel with invalid amount
# cargo_ship.refuel(-10)
# # Output: Cannot refuel with negative amount.

# # Test PassengerShip with too many passengers
# passenger_ship.passenger_count = 120
# passenger_ship.launch()
# # Output: Too many passengers. Cannot launch.

# # Try to launch cargo ship with low fuel
# cargo_ship.launch()
# # Output: Not enough fuel to launch.

