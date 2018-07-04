class Dog():
    #class object attribute 
    species = 'mammal'

    def __init__(self, breed, name, spots):
        #attributes 
        #we take in argument
        #assign it using self.attribute_name
        self.breed = breed
        self.name = name
        self.spots = spots

    #methods 

    def bark(self):
        print('woof my name is {}'.format(self.name))

my_dog = Dog(breed = 'lab', name = 'buster', spots = False)
my_dog.breed

my_dog.bark()


class Circle():
    pi = 3.14

    def __init__(self, radius = 1):
        self.radius = radius

    def get_circumference(self):
        return self.radius * self.pi * 2

my_circle = Circle()

print(my_circle.get_circumference())


