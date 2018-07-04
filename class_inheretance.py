class Animal():
    def __init__(self):
        print("Animal Created")

    def who_am_i(self):
        print('i am an animal')
    
    def eat(self):
        print('i am eating')

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('dog created')

my_dog = Dog()