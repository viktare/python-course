class Car:

    def __init__(self, make, model, year) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.full_tank = False

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage <= self.odometer_reading:
            print(f"You can't roll back mileage!")
        self.odometer_reading = mileage
    
    def increment_mileage(self, mileage):
        if mileage <= 0:
            print(f"You can't roll back mileage!")
        self.odometer_reading += mileage

    def fill_gas_tank(self):
        self.full_tank = True
        print(f"Filled the gas tank!")
    