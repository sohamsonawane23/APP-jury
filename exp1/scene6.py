print("soham sonawane")
class Car:
    def __init__(self, make, model, fuel_type, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_type = fuel_type
        self.fuel_capacity = fuel_capacity
        self.fuel_level = 0

    def refuel(self, amount):
        if self.fuel_type == "Electric":
            print(f"{self.make} {self.model} is electric and does not use fuel.")
        else:
            self.fuel_level += amount
            if self.fuel_level > self.fuel_capacity:
                self.fuel_level = self.fuel_capacity
            print(f"Refueled {amount} liters. Current fuel level: {self.fuel_level} liters.")

    def start(self):
        if self.fuel_level > 0 or self.fuel_type == "Electric":
            print(f"{self.make} {self.model} started.")
        else:
            print(f"{self.make} {self.model} cannot start. Fuel is empty.")


class ElectricCar(Car):
    def __init__(self, make, model, battery_capacity):
        super().__init__(make, model, "Electric", battery_capacity)
        self.battery_level = 0

    def refuel(self, amount):
        # Overriding refuel to simulate recharging battery
        self.battery_level += amount
        if self.battery_level > self.fuel_capacity:
            self.battery_level = self.fuel_capacity
        print(f"Recharged {amount} kWh. Current battery level: {self.battery_level} kWh.")

    def start(self):
        if self.battery_level > 0:
            print(f"{self.make} {self.model} (Electric) started silently!")
        else:
            print(f"{self.make} {self.model} (Electric) cannot start. Battery is empty.")


# Demonstration
car1 = Car("Toyota", "Corolla", "Gasoline", 50)
car1.refuel(30)
car1.start()

print()

car2 = ElectricCar("Tesla", "Model 3", 75)
car2.refuel(40)
car2.start()
