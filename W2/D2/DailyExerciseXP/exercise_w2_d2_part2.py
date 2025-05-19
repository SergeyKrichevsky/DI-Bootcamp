# EX3

import random

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f'{self.name} is barking'
    
    def run_speed(self):
        return f'{self.name} run speed is: {self.weight / self.age}'
    
    def fight(self, other_dog):
        a = self.run_speed() * self.weight
        b = other_dog.run_speed() * other_dog.weight
        if a == b:
            return f'It seems like a Tie between {self.name} and {other_dog.name}'
        elif a > b:
            return f'{self.name} won the fight against {other_dog.name}'
        else:
            return f'{other_dog.name} won the fight against {self.name}'
        


class PetDog(Dog):
    '''def __init__(self, name, age, weight, trained = False)'''
    def __init__(self, name, age, weight, trained = False):
        super().__init__(name, age, weight)
        self.trained = trained

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        '''*args on this method is a list of dog instances.
        prints “ all play together”'''
        names_of_dog_friends = []
        for dog in args:
            names_of_dog_friends.append(dog.name)
        print(f'{", ".join(names_of_dog_friends)} all play together')
        # print(f'{", ".join(args)} all play togeter') # - accordinf to the example in exercize, but against exercize discription:
        # Implement a play(*args) method that prints “ all play together”.
        # *args on this method is a list of dog instances.
    def do_a_trick(self):
        tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
        if not self.trained:
            print(f'{self.name} is not trained to do tricks')
        else:
            index = random.randint(0, len(tricks) -1)
            print(f'{self.name} {tricks[index]}')



pitbul_1 = Dog('Pitbul', 5, 20)
chihuahua_1 = Dog('Chihuahua', 3, 2)
labrador_1 = Dog('Labrador', 4, 15)

list_of_dogs = []
list_of_dogs.append(pitbul_1)
list_of_dogs.append(chihuahua_1)
list_of_dogs.append(labrador_1)
# for dog in list_of_dogs:
#     print(dog.name)


my_dog = PetDog("Fido", 2, 20)

# my_dog.play("Buddy", "Max") # - accordinf to the example in exercize, but against exercize discription:
# Implement a play(*args) method that prints “ all play together”.
# *args on this method is a list of dog instances.
my_dog.play(*list_of_dogs)

my_dog.do_a_trick()
my_dog.train()
my_dog.do_a_trick()
print('')


# EX4

class Person:
    def __init__(self, first_name, age, last_name = ''):
        self.first_name = first_name
        self.age = age
        self.last_name = last_name

    def is_18(self):
        if self.age >= 18:
            return True
        else:
            return False

    # def is_18(self, member):
    #     if member.age >= 18:
    #         return True
    #     else:
    #         return False
        

class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
        new_person = Person(first_name, age)
        new_person.last_name = self.last_name
        self.members.append(new_person)

    def check_majority(self, first_name):
        for member in self.members:
            if member.first_name == first_name:
                if member.is_18():                
                    print(f'{first_name} you are over 18, your parents Jane and John accept that you will go out with your friends')
                else:
                    print(f"{first_name} Sorry, you are not allowed to go out with your friends.")
            
    def family_presentation(self):
        print(f"{self.last_name} Family members:")
        for member in self.members:
            print(f'{member.first_name} - {member.age} years old')

    
my_family = Family('Krichevsky')
my_family.born("Sergey", 43)
my_family.born('Yuri', 51)
my_family.born('Andrey', 51)
my_family.born('Sasha', 77)
my_family.born('Galina', 72)
my_family.born('Baby', 15)

# for member in my_family.members:
#     print(member.first_name)

my_family.check_majority('Sergey')
my_family.check_majority('Baby')
# for member in my_family.members:
#     print(member.is_18(member))

print('')
my_family.family_presentation()

