class Mobile:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print(self.name, ":", self.price)


m1 = Mobile("Phone A", 20000)
m2 = Mobile("Phone B", 25000)

m1.display()
m2.display()