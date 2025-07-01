class spacecraft:
    def __init__(self, name:str, fuel:int):
        self.name = name
        self.fuel = fuel

    def launch(self):
        print(f"Launching {self.name}")
        self.fuel -= 50
        if self.fuel < 50:
            print("Not enough fuel to run")
        return 
        


class Cargoship(spacecraft):
    def __init__(self, name, fuel, cargo_weight):
        super().__init__(name, fuel)
        self.cargo_weight = cargo_weight

    def launch(self):
        print(f"Launching {self.name}")
        print(f"Launching consumes extra fuel depending on cargo")
        self.fuel = self.fuel - (50 + (self.cargo_weight * 2))
        return f"Fuel after lauch = 200 - (50 + 30*2) = {self.fuel}"
        

    def refuel(self, amount):
        self.amount = amount
        self.fuel += amount
        if amount <=0 :
            print(f"You cannot refuel with negative amount {amount}")
        return f"{self.name} Hauler with {amount} units. Fuel is now {self.fuel}"
    
class passengership(spacecraft):
    def __init__(self, name:str, fuel: int, passenger_count: int):
        super().__init__(name, fuel)
        self.passenger_count = passenger_count

    def launch(self):
        print(f"Launching {self.name}")
        print(f"Launching consumes extra fuel depending on cargo")
        self.fuel -= 50
        if self.passenger_count > 100:
            print("Too many perssenger! Cannot Launch")
        return f"Fuel after lauch = {self.fuel} - 50 = {self.fuel}"
    

    def refuel(self, amount):
        self.amount = amount
        self.fuel += amount
        if self.amount <= 0:
            print(f"Cannot Refuel with negative amount {amount}")
        return f"{self.name} with {amount} units. Fuel is now {self.fuel}"
    






# # SAMPLE EXECUTION
# # Create objects
cargo_ship = Cargoship("Galactic Hauler", 200, 30)
passenger_ship = passengership("Star Voyager", 100, 80)

# # Attempt to launch both ships
print(cargo_ship.launch())
# # Output: Launching Galactic Hauler with cargo!
# # Fuel after launch: 200 - (50 + 30*2) = 90

print(passenger_ship.launch())
# # Output: Launching Star Voyager!
# # Fuel after launch: 100 - 50 = 50


# # Refuel both ships
print(cargo_ship.refuel(50))
# # Output: Refueled Galactic Hauler with 50 units. Fuel is now 140.


print(passenger_ship.refuel(30))
# # Output: Refueled Star Voyager with 30 units. Fuel is now 80.


# # Launch again after refueling
print(cargo_ship.launch())
# # Output: Launching Galactic Hauler with cargo!
# # Fuel after launch: 140 - (50 + 30*2) = 30


print(passenger_ship.launch())
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
# # Output: Not enough fuel to launch with cargo.