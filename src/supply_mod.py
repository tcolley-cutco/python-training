from Supply import Pen, Supply
from test_packages.Car import Car
from test_packages.Person import Person

paper = Supply("Xerox", 0)
red_pen = Pen('Bic', .99)
print(paper.cost)

price = 0.0
try:
    price = paper.calculate_price()
except ValueError:
    print("The cost was 0! Defaulting to no price.")
print(price)

car = Car("Honda", "Blue")
person = Person("Jimmy", 34)