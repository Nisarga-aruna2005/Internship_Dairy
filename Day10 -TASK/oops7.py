class Session:
    def __init__(self):
        self.active = True

    def close(self):
        self.active = False
        print("Session closed")

s = Session()
s.close()
