# OOP: OBJECT ORIENTED PROGRAMMING

# WHAT IS AN OBJECT?
# WHAT IS A CLASS

# HOW TO CREATE A CLASS

# class Dog:
#     pass 

class Dog:
    
    def __init__(self, name, color, breed, age): #Any tipe of variables
        # print('creating object')
        self.name = name
        self.color = color
        self.breed = breed
        self.age = age

    # How to create methods of the class
    # ACTIONS, CHANGES
    def bark(self):
        print(f'{self.name} is barking')
        # pass

    def walk(self, meters):
        print(f'{self.name} is walking {meters} meters')

    def birthday(self):
        self.age += 1
        return self # The Idea of OOP
    
    def rename (self, name):
        self.name = name
        return self
        # pass # To not get an "Error" (= 'I`ll write the code later`)


# An Instanse (or object) of class Dog is created:
# shelter_dog = Dog()

# Creating atributes to the instance:
# shelter_dog.color = 'Black'
# print(shelter_dog.color)

# pitbull = Dog()
# print(pitbull.color)

# Creating the instances of dog after creating  the __ini__() method:
shelter_dog = Dog('Rex', 'Black', 'shelter', 5)#
# print(shelter_dog.__dict__)

# Create 2 objects (instanses) of the call Dog

pitbul_dog = Dog('Rocky', 'Brown', 'Pitbul', 1)
chihuahua = Dog('Pearl', 'White', 'Chihuahua', 2)

# pitbul_dog.bark()
# my_name = 'Sergey'
# my_name.upper() # for str

# print(pitbul_dog.__dict__) # {'name': 'Rocky', 'color': 'Brown', 'breed': 'Pitbul', 'age': 1}
# print(chihuahua.__dict__)
# print(pitbul_dog) # <__main__.Dog object at 0x0000022017518A50>
# print(pitbul_dog.name, pitbul_dog.color, pitbul_dog.age) # Rocky Brown 1

my_dogs = [shelter_dog, pitbul_dog]
# print(my_dogs) # memory addressed

# for dog in my_dogs:
#     print(dog.name)
          
# print(type(pitbul_dog))


# print(help(str))

#?
# my_dogs_objects = [obj for obj in globals().values() if isinstance(obj, Dog)]
# print(my_dogs_objects)
#?

# for dog in my_dogs:
#     dog.bark()


# EX:
# Create a method called walk() that prints: dog name is walking
# for dog in my_dogs:
#     dog.walk()

# pitbul_dog.walk(200)

# print(shelter_dog.age)
# shelter_dog.birthday()
# print(shelter_dog.age)

# print(pitbul_dog.name)
# pitbul_dog.rename('Max')
# print(pitbul_dog.name)

