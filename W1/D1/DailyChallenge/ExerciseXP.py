#EX1

greeting = 'Hello world\n'
print(greeting * 4)

#EX2

print((99 ** 3)*8)

#EX3

# false (5 < 3)
# true (3 == 3)
# false (3 == "3")
# Error("3" > 3)
# false ("Hello" == "hello")

#EX4

computer_brand = 'Castom_Desktop'
print(f'I have a {computer_brand} computer')

#EX5

name = "Sergey"
age = 43
shoe_size = 42
info= (
    f'Hi!\n'
    f'My name is {name}.\n'
    f"I'm {age} years old.\n"
    f'I wear size {shoe_size} shoes'
)

print(f'{info}\n')


#EX6

a = 55
b = 7

if a > b:
    print(greeting)
else:
    print('No greeting this time')

#EX7

number7 = int(input('Enter a number > '))
if number7%2 == 0:
    print(f'{number7} is an Even number')
else:
    print(f'{number7} is an Odd number')

#EX8

user_name = input('What is your name? ')
if user_name == name:
    print('Cool! You and I are namesakes! :-)')
else:
    print('Nice to meet you!')

#EX9

user_height = int(input("What is your height in centimeters ? "))
if user_height > 145:
    print('You are tall enough to ride! ')
else:
    print('Sorry, you are not tall enough to ride.')

