class Parent:
    def speak(self):
        print(f'Perent is speaking')

class Child(Parent):
    pass

class Grandchild(Child):
    pass

obj1 = Child()
obj1.speak()

obj2 = Grandchild()
obj2.speak()



class Animal:
    def __init__(self, name, family, legs):
        self.name = name
        self.family = family
        self.legs = legs
        # self.full_name = name + ' ' +family
        self.full_name = f'{name} {family}'

        # id_num = 0
        # self.id_number = id_num
        # self.id_number += 1


#EX:
# add two other attributes specifically to the Dog class: trained (boolean), age (int)
# user the super().__init__() to do so
# create an instance of Dog after that and analyse what change

class Dog(Animal):
    def __init__(self, name, family, legs, trained, age):
        super().__init__(name, family, legs)
        self.trained = trained
        self.age = age

    def bark(self):
        print(f'A {self.name} is barking')

    def sleep(self):
        return f'{self.name} is sleeping fron a Dog Class'
              
# dog_1 = Dog('Dog', 'Canidae', 4, True, 11)
# dog_1.bark()
# dog_1.bark()
# dog_1.bark()

# Create a Cat class that inherit from Animal.
# create a mathod get_crazy that prints 
# "a self.name is running with its self.legs legs in full poewer"

class Cat(Animal):
    def __init__(self, name, family, legs, friendly, nick_name):
        super().__init__(name, family, legs)
        self.friendly = friendly
        self.nick_name = nick_name

    def get_crazy(self):
        print(f'A {self.name} is running with its {self.legs} legs in full poewer')



class Alien:
    def __init__(self, personal_name, planet):
        self.personal_name = personal_name
        self.planet = planet

    def fly(self):
        return f'{self.name} is flying around'
    
    def sleep(self):
        return f'{self.name} is sleeping fron a Alien Class'
    
    def make_sound(self):
        return f'{self.name} is making a sound from Alien'
    


class AlienDog(Dog, Alien):
    def __init__(self, name, family, legs, personal_name, planet):
        Dog.__init__(self, name, family, legs)
        Alien.__init__(self, personal_name, planet)
    


lion = Animal('Lion', 'Falidae', 4)
print(lion.__dict__)

dog_1 = Dog('Dog', 'Canidae', 4, True, 11)
dog_1.bark()

# cat_1 = Cat('Cat', 'Falidae', 4, True, 'Pyssy')
# cat_1.get_crazy()

# aliendog1 = AlienDog('Dog', 'Canide', 4, 'Raxi', 'Saturn')

# # if we want to call the method in some specific parent class 
# # (not by order of inheritance) we can do:
# print(dog)...


#EX:
# add two other attributes specifically to the Dog class: trained (boolean), age (int)
# user the super().__init__() to do so
# create an instance of Dog after that and analyse what changed

