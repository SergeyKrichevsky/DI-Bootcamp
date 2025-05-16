# *Args and **Kargs

# *Args (Arguments)

# def say_hello(language, user_name):
#     if language == EN:
#         print(f'Hello, {user_name}')

# say_hello()


# def print_names(*args):
# # def print_names(*names):
#     for name in args:
#         print(f'Hello, {name}')
#     if not args:
#         print('Please add a name to say hello')

# print_names()
# print_names('Sergey', 'Juliana', 'Dolev', 'Sofia')


# **Kwargs (KeyWordsArguments) - with Dictioneries

# def user_info(**kwargs):
#     for info in kwargs.values():
#         print(info)
#     # print(kwargs)

# user_info(name = 'Sergey', age = 43, adress = 'Haifa')    


# Exercise: 

# creata a function called tasks_mamager that exsepts tasks
#and prints "today i need to do: {task}"

# def pass_example (*args):
#     pass

# def tasks_mamager(*tasks):
#     if tasks:
#         for task in tasks:
#             print(f'today i need to do: {task}')
#     else:
#             print('Please pass a task as argument')

# # tasks_mamager()
# tasks_mamager('Eat', 'Learn', 'Mini-Project')


# Using *args and **kwargs togeter

# def party_planner(*args, **kwargs):
#     if args:
#        print('You need to buy: ')
#     for arg in args:
#         print(arg)
#     else:
#         print('There is no food to bay')

#     if kwargs:
#         print('Party details: ')

#         for key, value in kwargs.items():
#             print(f'{key} : \n {value})

#EX: 1 - Call this function and the party details.
#    2 - Call it only thith fuud information
#    3 - Call it only with details

def party_planner(*args, **kwargs):
    if args:
        print('You need to buy: ')
        for arg in args:
            print(arg)
    else:
        print('there is no food to buy' )

    if kwargs:
        print('Party details: ')

        for key, value in kwargs.items():
            print(f' {key} : \n {value}')
    else:
        print('There are no details about this party')


#party_planner(('Bread', 'Milk')(adress = 'Haifa', cost = 200))
# party_planner('Bread', 'Milk', adress = 'Haifa', time = '7PM', cost = 200)
# party_planner('Bread', 'Milk')
party_planner(adress = "haifa", cast = 200, cost2 = [200, 'ILS'], tuple = {1: 200, 2: 300})

# party_planner('Bread', adress = 'Haifa', 'Milk', cost = 200)
# party_planner(adress = "haifa", cast = list(200 'Ils'))



