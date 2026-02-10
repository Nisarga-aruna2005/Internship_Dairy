from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
       pass
    def sleep(self):
        print("Animal sleeps")
class Dog(Animal):
    def sound1(self):
        print("Dog barcks")
class Cat(Animal):
    def sound(self):
        print("Cat Meows")



obj2=Cat()
obj2.sound()
obj2.sleep()