class Calculator:
    def __call__(self, a, b):
        return a + b

calc = Calculator()
print("Sum:", calc(5, 3))
