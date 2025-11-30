from car import Car
from electric_car import ElectricCar

my_bmw = Car('BMW', 'Serie 1', 2011)
my_tesla = ElectricCar('Tesla', 'S', 2019)

my_bmw.fill_gas_tank()
my_tesla.fill_gas_tank()

my_tesla.battery.describe_battery()

