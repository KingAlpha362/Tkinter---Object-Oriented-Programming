class Dog:
    
    def add_one(self, x):
        return x + 1
        
    def bark(self):
        print("Woof!")

my_dog = Dog()
my_dog.bark()
print(my_dog.add_one(5))

print(type(my_dog))