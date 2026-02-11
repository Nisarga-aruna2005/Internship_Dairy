class Cart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def display(self):
        print("Cart items:", self.items)

c = Cart()
c.add("Shoes")
c.add("Shirt")
c.display()
