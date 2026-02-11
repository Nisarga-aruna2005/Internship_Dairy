class User:
    def __init__(self, username):
        self.username = username

    def display(self):
        print("User:", self.username)

u = User("Nisarga")
u.display()
