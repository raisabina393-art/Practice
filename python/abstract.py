from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Cat(Animal):
    def sound(self):
        print("Meow")

cat = Cat()
cat.sound()
