#EX1

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

# Step 1: Create cat objects
# cat1 = create the object

cat1 = Cat('Kitty', 1)
cat2 = Cat('Ricky', 2)
cat3 = Cat('Sperviser', 5)
# print(cat1, cat2)
# print(cat1.__dict__)
# print(cat2.__dict__)
# print(cat3.__dict__)
# print(cat1.__dict__, cat2.__dict__)


# Step 2: Create a function to find the oldest cat

def find_oldest_cat(cat1, cat2, cat3):
     return max([cat1, cat2, cat3], key=lambda cat: cat.age)

# print(find_oldest_cat(cat1, cat2, cat3).__dict__)

# def find_oldest_cat(cat1, cat2, cat3):
    # ... code to find and return the oldest cat ...

# Step 3: Print the oldest cat's details

oldest_cat = find_oldest_cat(cat1, cat2, cat3)
print(f'The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.')
# print(f'The oldest cat is {find_oldest_cat(cat1, cat2, cat3).name}, and is {find_oldest_cat(cat1, cat2, cat3).age} years old.')



#EX2
# Create a Dog class with methods for barking and jumping. Instantiate dog objects, call their methods, and compare their sizes.

# Step 1: Create the Dog Class
# Create a class called Dog.
# In the __init__ method, take name and height as parameters and create corresponding attributes.
# Create a bark() method that prints “ goes woof!”.
# Create a jump() method that prints “ jumps cm high!”, where x is height * 2.


class Dog:
    def __init__(self, dog_name, dog_height):
        self.name = dog_name
        self.height = dog_height

    def bark(self):
        print(f'{self.name} goes woof!')
    
    def jump(self):
        print(f'{self.name} jumps {self.height * 2} cm high')
        

# Step 2: Create Dog Objects
# Create davids_dog and sarahs_dog objects with their respective names and heights.

davids_dog = Dog('David`s Dog', 20)
sarahs_dog = Dog('Sarah`s Doggy', 10)
# print(davids_dog)
# print(sarahs_dog)


# Step 3: Print Dog Details and Call Methods
# Print the name and height of each dog.
# Call the bark() and jump() methods for each dog.

print(f'{davids_dog.name} height is {davids_dog.height} cm high')
print(f'{sarahs_dog.name} height is {sarahs_dog.height} cm high')

davids_dog.bark()
davids_dog.jump()
sarahs_dog.bark()
sarahs_dog.jump()

# Step 4: Compare Dog Sizes

def compare_dog_size (dog1, dog2):
    if dog1.height > dog2.height:
        return f'{dog1.name} is {dog1.height - dog2.height} cm taller than {dog2.name}'
    if dog2.height > dog1.height:
        return f'{dog2.name} is {dog2.height - dog1.height} cm taller than {dog1.name}'
    
print(compare_dog_size(davids_dog, sarahs_dog))



# # EX3 Who’s the song producer?
# # Goal: Create a Song class to represent song lyrics and print them.

# # Instructions:
# # Create a Song class with a method to print song lyrics line by line.

# # Step 1: Create the Song Class
# # Create a class called Song.
# # In the __init__ method, take lyrics (a list) as a parameter and create a corresponding attribute.
# # Create a sing_me_a_song() method that prints each element of the lyrics list on a new line.

# class Song:
#     def __init__(self, lyrics: list[str]):
#         self.lyrics = lyrics

#     def sing_me_a_song(self):
#         if not self.lyrics:
#             print("This song has no lyrics.")
#         else:
#             for line in self.lyrics:
#                 print(line)

# stairway = Song(["There's a lady who's sure", "all that glitters is gold", "and she's buying a stairway to heaven"])

# stairway.sing_me_a_song()

# # Testing empty dong check:
# # rain_man = Song([])
# # rain_man.sing_me_a_song()


# # Example:
# # stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"]


# EX4 Afternoon at the Zoo
# Goal:
# Create a Zoo class to manage animals. The class should allow adding animals, displaying them, selling them, and organizing them into alphabetical groups.

# Instructions
# STEP 1: Define the Zoo Class

#1. Create a class called Zoo.

class Zoo:
    def __init__(self, zoo_name: str):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if not new_animal in self.animals:
            self.animals.append(new_animal)
        return self

    def get_animals(self):
        print(self.animals)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        if not self.animals:
            print('No animals to sort. The ZOO is empty!')
        else:
            self.animals = sorted(self.animals)
            self.groups = {}
            for animal in self.animals:
                letter = animal[0]
                if letter in self.groups:
                    self.groups[letter].append(animal)
                else:
                    self.groups[letter] = [animal]
        return self
    
    def get_groups(self):
        # for group in self.groups:
        #     print(group)
        for key, value in self.groups.items():
            print(f'{key}: {value}')


# 2. Implement the __init__() method:
# It takes a string parameter zoo_name, representing the name of the zoo.
# Initialize an empty list called animals to keep track of animal names.



# 3. Add a method add_animal(new_animal):
# This method adds a new animal to the animals list.
# Do not add the animal if it is already in the list.



# 4. Add a method get_animals():
# This method prints all animals currently in the zoo.



# 5. Add a method sell_animal(animal_sold):
# This method checks if a specified animal exists on the animals list and if so, remove from it.



# 6. Add a method sort_animals():
# This method sorts the animals alphabetically.
# It also groups them by the first letter of their name.
# The result should be a dictionary where:
# Each key is a letter.
# Each value is a list of animals that start with that letter.



# Example output:
# {
#    'B': ['Baboon', 'Bear'],
#    'C': ['Cat', 'Cougar'],
#    'G': ['Giraffe'],
#    'L': ['Lion'],
#    'Z': ['Zebra']
# }



# 7. Add a method get_groups():
# This method prints the grouped animals as created by sort_animals().
# Example output:
# B: ['Baboon', 'Bear']
# C: ['Cat', 'Cougar']
# G: ['Giraffe']
# ...


# ==> STEP 1 - Execution function:
# zoo1.sort_animals()
# zoo1.get_groups()
# zoo1.sell_animal('Cat')



# STEP 2: Create a Zoo Object
# Create an instance of the Zoo class and pass a name for the zoo.

di_zoo = Zoo('DI Mini Petting Zoo')


# STEP 3: Call the Zoo Methods
# Use the methods of your Zoo object to test adding, selling, displaying, sorting, and grouping animals.

di_zoo = Zoo('Zoo1')            
di_zoo.add_animal("Cat")
di_zoo.add_animal('Dog')
di_zoo.add_animal('Dog')

di_zoo.add_animal('Anaconda')
for animal in (['Baboon', 'Bear', 'Cat', 'Cougar', 'Giraffe', 'Lion', 'Zebra']):
    di_zoo.add_animal(animal)

di_zoo.get_animals()
di_zoo.sell_animal('Dog')
di_zoo.get_animals()
di_zoo.sort_animals()
di_zoo.get_groups()


# Example (No Internal Logic Provided)
# class Zoo:
#     def __init__(self, zoo_name):
#         pass

#     def add_animal(self, new_animal):
#         pass

#     def get_animals(self):
#         pass

#     def sell_animal(self, animal_sold):
#         pass

#     def sort_animals(self):
#         pass

#     def get_groups(self):
#         pass

# # Step 2: Create a Zoo instance
# ramat_gan_safari = Zoo("Ramat Gan Safari")

# # Step 3: Use the Zoo methods
# ramat_gan_safari.add_animal("Giraffe")
# ramat_gan_safari.add_animal("Bear")
# ramat_gan_safari.add_animal("Baboon")
# ramat_gan_safari.get_animals()
# ramat_gan_safari.sell_animal("Bear")
# ramat_gan_safari.get_animals()
# ramat_gan_safari.sort_animals()
# ramat_gan_safari.get_groups()