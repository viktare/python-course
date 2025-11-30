from car import Car
from battery import Battery

class ElectricCar(Car):

    def __init__(self, make, model, year) -> None:
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        print(f"Electric cars don't have Gas tanks")