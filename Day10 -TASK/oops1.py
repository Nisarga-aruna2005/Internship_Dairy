class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)

    def update(self, title, author):
        self.title = title
        self.author = author

    def delete(self):
        self.title = None
        self.author = None
        print("Book details deleted")


b = Book("Python Basics", "John")
b.display()
b.update("Advanced Python", "Mike")
b.display()
b.delete()
