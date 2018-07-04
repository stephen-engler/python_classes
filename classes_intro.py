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
        print('woof')

my_dog = Dog(breed = 'lab', name = 'buster', spots = False)
my_dog.breed

my_dog.bark()



