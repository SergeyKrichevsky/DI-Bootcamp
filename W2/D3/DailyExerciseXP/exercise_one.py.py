class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return f'{self.amount} {self.currency}s'

    def __int__(self):
        return int(self.amount)

    def __repr__(self):
        return f'{self.amount} {self.currency}'
    
    def __add__(self, other):
        if isinstance(other, int):
            return self.amount + other
        elif isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            return self.amount + other.amount
        else:
            raise TypeError("Unsupported operand type(s) for +")
        
    def __iadd__(self, other):
        if isinstance(other, int):
            self.amount += other
        elif isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            self.amount += other.amount
        else:
            raise TypeError("Unsupported operand type(s) for +=")
        return self



c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

#the comment is the expected output
# print(str(c1))
print(str(c1))
# '5 dollars'

print(int(c1))
# print(int(c1))
# # 5

repr(c1)
# # '5 dollars'

print(c1 + 5)
# # 10

print(c1 + c2)
# # 15

print(c1) 
# # 5 dollars

c1 += 5
print(c1)
# # 10 dollars

c1 += c2
print(c1)
# # 20 dollars

# print(c1 + c3)
# # TypeError: Cannot add between Currency type <dollar> and <shekel>


# EX2
print("=" * 50) 
print("*" * 50)

import func

func.sum_2_numbers(10, 15)


# EX3
print("=" * 50) 
print("*" * 50)

import string
import random

all_latters = ''
all_latters = string.ascii_lowercase + string.ascii_uppercase
# print(all_latters)

my_string = ''

for i in range(5):
    my_string += all_latters[random.randint(0, len(all_latters)) -1]

print(my_string)


# EX4
print("=" * 50) 
print("*" * 50)

from datetime import datetime


now = datetime.now()
print(now.date())


# EX5
print("=" * 50) 
print("*" * 50)

next_jan1 = datetime(now.year + 1, 1, 1)
# print(next_jan1)
delta = next_jan1 - now
print(f"Time left until January 1st: {delta}")


# EX 6
print("=" * 50) 
print("*" * 50)

def live_length_in_minuts(birth_time):
    birth = datetime.strptime(birth_time, "%Y-%m-%d %H:%M")
    now = datetime.now()
    delta = now - birth
    minutes = int(delta.total_seconds()//60)
    print(f"You have lived for {minutes} minutes.")

live_length_in_minuts("1995-05-20 12:00")


# EX 7
print("=" * 50) 
print("*" * 50)

from faker import Faker

# Testing faker:
# fake = Faker()
# print(fake.name())
# print(fake.address())
# print(fake.language_code())


users_list = []

def fake_users_generator(number_of_users):
    '''fake_users_generator(number_of_users):'''
    faker = Faker()
    for i in range(0, number_of_users):
        user = {
            "name": faker.name(),
            "address": faker.address(),
            "language_code": faker.language_code()
        }
        users_list.append(user)

fake_users_generator(6)

for user in users_list:
    print(user)

