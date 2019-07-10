class Supply:
    def __init__(self, brand, cost):
        self.brand = brand
        self.cost = cost

    def calculate_price(self):
        if self.cost <= 0:
            raise ValueError('Cost must be more than 0 to calculate price!')
        return self.cost * 2.5

    def __str__(self):
        return "Brand: " + self.brand + \
               " | Cost: " + str(self.cost)


class Pen(Supply):
    color = 'N/A'

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color
