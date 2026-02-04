class book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def display(self):
        print("TITLE:",self.title)
        print("AUTHOR:",self.author)
        
class issued_book(book):
    def __init__(self,title,author,issued_to,issued_date):
        super().__init__(title,author)
        self.issued_to=issued_to
        self.issued_date=issued_date
    def display_detailes(self):
            self.display()
            print("issued_to:",self.issued_to)
            print("issued_date:",self.issued_date)
obj=issued_book("python","rossan","nisarga","04-02-2026")
obj.display_detailes() 
