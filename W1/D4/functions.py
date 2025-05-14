#FUNCTIONS
#syntax

# def func_name():
#     '''describe what this function does (prints aphrase on the consol)''' #doc strings
#     print('I am a function ')

# func_name()
# print(func_name.__doc__) #prints the dog string
# print(print.__doc__)
# print(len.__doc__)

# create function called greetings that prinys 'hello' in your mother toung# then call the function and run the file

# def greetengs():
#     '''prints hello in russian'''
#     print('Привет!' ) 

# greetengs()

# Passing arguments to function
# def greetengs(language):
#     '''prints hello in potuguese or russian'''
#     if language == "PT":
#         print('Ola')
#     elif language == "RU":
#         print('Привет!' ) 
#     elif language == "HE":
#         print('שלום! ')

# greetengs('HE')

# 'Hello Sunshone'.replace('Hello', 'Hi')

# def greetengs(language, user_name):
#     '''prints hello in potuguese or russian'''
#     if language == "PT":
#         print(f'Ola ', {user_name}, '!')
#     elif language == "RU":
#         print(f'Привет', user_name, '!') 
#     elif language == "HE":
#         print(f'שלום ', user_name, '!')
#     else:
#         print("Undefined Language")

# # keyword arguments
# greetengs(user_name= 'Сергей', language= 'RU')
# # greetengs('RU', 'Сергей')


# Default arguments:

# def greetengs(language = 'RU', user_name = 'Сергей'):
#     '''prints hello in potuguese or russian'''
#     if language == "PT":
#         print(f'Ola ', {user_name}, '!')
#     elif language == "RU":
#         print(f'Привет', {user_name}, '!') 
#     elif language == "HE":
#         print(f'שלום ', {user_name}, '!')
#     else:
#         print("Undefined Language")

# # keyword arguments
# # greetengs(user_name= 'Сергей', language= 'RU')
# # greetengs('RU', 'Сергей')
# greetengs()
# greetengs('PT')


# create a function called country that receives a country name as argument
# and print the capital of that country/ Make the country name agrument default
# Nabu (star wars planet). Uts capital is Theed

# def capital_function(country = 'Nabu'):
#     ''''''
#     if country == 'England':
#         print(f'London is the capital of, {country}')
#     elif country == 'France':
#         print(f'Paris is the capital of, {country}')
#     elif country == 'Nabu':
#         print(f'Theen is the capital of, {country}')
#     else:
#         print(f'Not defined')

# capital_function('England')
# capital_function('France')
# capital_function()

# return keyword

# def calculation(num1, num2):
#     result = num1 + num2
#     return result # also stops the function

# print(calculation(5, 4))

# calculation_resoult = calculation(5, 4)
# print(calculation_resoult)
# print(calculation_resoult + 10)

countries = ['Brazil', 'Israel', 'China']

def country_info(countries):
    for country in countries:
        print(f'hello {countries}')
        if country == 'Israel':
            return country #stops on 'Israel"
        
print(country_info(countries))

# Scopes
# global scope
    # local scope: intendent block (if statements, a loop, a function...)

# Variables defined (and exist) inside different scpes
# Can be called to other scope:

# global_war = 100

# def calculation(a, b):
#     addition = a+b
#     substruction = a-b
#     global_war = 50 # different variable (from global scope)
#     return addition, substruction

# aditional, substraction = calculation(5, 7)
# print(aditional,  substraction)
# print(global_war)




global_war_1 = 100

def calculation(a, b):
    addition = a+b
    substruction = a-b
    #global global_war_1
    global_war_1 = 50
    return addition, substruction, global_war_1

aditional, substraction, global_war_1 = calculation(5, 7)
print(aditional,  substraction, global_war_1)
print(global_war_1)


