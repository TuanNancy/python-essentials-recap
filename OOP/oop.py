# class = ban thiet ke

class Dog:
    def __init__(self, name, age): # ham khoi tao
        self.name = name
        self.age = age
    def bark(self):
        print(f"{self.name}: gau gau!")

#object = vat the tao ra tu ban thiet ke
dog1 = Dog("Rex", 3)
dog2 = Dog("Buddy", 5)

dog1.bark()
print(dog2.name)



# Class cha
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} đang ăn")

    def speak(self):
        print(f"{self.name}: ????")
# Class con — kế thừa từ Animal
class Dog(Animal):
    def bark(self):
        print(f"{self.name}: Gâu gâu!")
    def speak(self):
        super().speak() # kế thừa từ Animal
        print(f"{self.name}: toi la dog, hihi!")

class Cat(Animal):
    def meow(self):
        print(f"{self.name}: Meo meo!")

dog = Dog("Milo")
dog.eat()    # Milo đang ăn   ← kế thừa từ Animal
dog.bark()   # Milo: Gâu gâu! ← của Dog
dog.speak()   # Milo: ???


cat = Cat("Kitty")
cat.eat()    # Kitty đang ăn  ← kế thừa từ Animal
cat.meow()   # Kitty: Meo meo!
cat.speak()   # Kitty: ???
