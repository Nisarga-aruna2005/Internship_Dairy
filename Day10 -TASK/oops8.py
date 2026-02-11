class Library:
    def __init__(self, books):
        self.books = books

    def search(self, title):
        if title in self.books:
            print("Book found:", title)
        else:
            print("Book not found")

lib = Library(["Python", "Java", "C++"])
lib.search("Python")
