

# EX1

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
#1

class Siamese(Cat):
    pass


bengal_1 = Bengal('Bengal #1', 2)
chartreux_1 = Chartreux('Chartreux #1', 5)
siamese_1 = Siamese('Siamese #1', 3)

all_cats = [bengal_1, chartreux_1, siamese_1]

# for cat in all_cats:
#     print(f'Cats name is: {cat.name}. Its {cat.age} years old')

sara_pets = Pets(all_cats)
sara_pets.walk()


# EX2

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f'{self.name} is barking'
    
    def run_speed(self):
        return self.weight / self.age * 10
    
    def fight(self, other_dog):
        a = self.run_speed() * self.weight
        b = other_dog.run_speed() * other_dog.weight
        if a == b:
            return f'It seems like a Tie between {self.name} and {other_dog.name}'
        elif a > b:
            return f'{self.name} won the fight against {other_dog.name}'
        else:
            return f'{other_dog.name} won the fight against {self.name}'
        

pitbul_1 = Dog('Pitbul', 5, 20)
chihuahua_1 = Dog('Chihuahua', 3, 2)
labrador_1 = Dog('Labrador', 4, 15)

print(pitbul_1.bark())
print(chihuahua_1.bark())
print(labrador_1.bark())
print('')

print(pitbul_1.run_speed())
print(chihuahua_1.run_speed())
print(labrador_1.run_speed())
print('')

print(pitbul_1.fight(pitbul_1))
print(chihuahua_1.fight(pitbul_1))
print(labrador_1.fight(pitbul_1))
print('')


