# #EX1

def display_message():
    print('I am learning about functions in Python')

display_message()


# EX2

def favorite_book(title):
    print(f'One of my favorite books is {title}')

favorite_book('"Rich Ded, Poor Dad"')


#EX3

# Option 1:

def describe_city(city, country = "Unknown"):
    print(f'{city} is in {country}')

describe_city('Reykjavik', 'Iceland')
describe_city("Paris")


# Option 1:

def describe_city(city, country = "Unknown"):
    return (f'{city} is in {country}')

print(describe_city('Reykjavik', 'Iceland'))
print(describe_city("Paris"))


# EX4

import random

def random_1_to_100_num(num):
    if 1 <= num <= 100:
        random_num = random.randint(1, 100)
        if random_num == num:
            print('Success! (same numbers)')
        else:
            print(f'Fail: your number is {num} and the random number is {random_num}')
    else:
        print("Not valid number (should be from 1 tp 100)")


random_1_to_100_num(78)


#EX 5

def make_shirt(size= 'Large', text= 'I love python'):
    print(f"You`r shirt is {size} size, and have a `{text}` message on it")

make_shirt('S', 'Hello!')
# make_shirt(42, 'Hello!')

make_shirt()
make_shirt('medium')
make_shirt('any', 'I love Shirts!')

make_shirt(size=44, text= 'Hello, people!')


#EX 6

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(m_names):
    for name in m_names:
        print(name)

def make_great(m_names):
    for index, name in enumerate(m_names):
        m_names[index] = f'{name} the Great'


make_great(magician_names)
show_magicians(magician_names)


#EX7

import random

# # Initial function:
# def get_random_temp():
#     return random.randint(-10, 40)
# # print(get_random_temp())


# modified function (bonus):
def get_random_temp():
    return random.uniform(-10, 40)
# print(get_random_temp())



# Basic version:

# def main():
#     current_temp = get_random_temp()
#     print(f'The temperature right now is {current_temp} degrees Celsius.')
# main()

# def main():
#     current_temp = get_random_temp()
#     print(f'The temperature right now is {current_temp} degrees Celsius.')
#     if current_temp < 0:
#         print('Brrr, that’s freezing! Wear some extra layers today.')
#     elif current_temp < 16:
#         print("Quite chilly! Don`t forget your coat.")
#     elif current_temp < 24:
#         print('Nice weather.')
#     elif current_temp <32:
#         print('A bit warm, stay hydrated.')
#     else:
#         print('It’s really hot! Stay cool.')
# main()



# 5: Month-Based Seasons (Bonus Version)
def main():
    current_month = int(input("What is curren month number (1-12)? "))
    # print(f'The temperature right now is {current_temp} degrees Celsius.')
    if current_month in [1, 2, 12]:
        print('Brrr, that`s freezing! Wear some extra layers today.')
    elif current_month < 6:
        print("Quite chilly! Don`t forget your coat.")
    elif current_month < 9:
        print('A bit warm, stay hydrated.')
    elif current_month < 12:
        print('Nice weather.')
    else:
        print('Wrong month number!')
main()




