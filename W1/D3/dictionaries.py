# #DICTIONARIES

# #Reminder of previously learnd Sequences:

# #Lists example:
# shoping_list = ["milk", "eggs", 'bread']
# shoping_list.append("butter")
# shoping_list.remove("eggs")
# shoping_list[0] # refers to "milk"


# #Dictionary:
# #students = {"Name": John", "age": "age", "major": "computer science"}
# students = {'Name': 'John', 'age': 20, 'major': 'computer science'}   
# print(students)

# students['age'] = 21
# print(students)

# my_dog = {
#   'name': 'Rufus',
#   'age': 4,
#   'good_dog': True
# }

# rick_dict = {
#     'first_name':'Rick',
#     'last_name':'Sanchez'
# }

# print(rick_dict['last_name'])


# a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}

# for key, value in a_dict.items():
#     print(key, "->", value)

# rick_dict['last_name'] = 'SUNCHEZ_2'
# rick_dict['age'] =70
# rick_dict['heir_color'] = 'white'

# print(rick_dict)
# print(rick_dict['last_name'])
# print(rick_dict['age'])
# print('\n')

# del rick_dict['heir_color']

# # Dictionaries and lists

# shirts = [
#   {
#     'name': 'Awesome T-shirt 3000',
#     'size': 'S',
#     'price': 20
#   },
#   {
#     'name': 'Awesome T-shirt 3000',
#     'size': 'M',
#     'price': 25
#   },
#   {
#     'name': 'Awesome T-shirt 3000',
#     'size': 'L',
#     'price': 30
#   },
# ]


# for shirt in shirts:
#     print(shirt['size'])
# print('\n')


# sample_dict = { 
#    "class":{ 
#       "student":{ 
#          "name":"Mike",
#          "marks":{ 
#             "physics":70,
#             "history":80
#          }
#       }
#    }
# }



# # user_a = {
# #     'first_name': 'Bob',
# #     'last_name': 'Ross', #STOP HERE, EXPLAIN
# #     'age': 53, #EXPLAIN DATA TYPES AS VALUES
# #     'address': 'Tel Aviv', #STOP HERE EXPLAIN ACESSING DATA
# #     'hobbies': ['painting', 'guitar'], #STOP HERE EXPLAIN DATA TYPES: DICTS AND LISTS
# #     'pets': [('Rufus', 9), ('Garfield', 8), ('Katty', 6)], #EXPLAIN LIST OF OTHER DATA TYPES (EX.:TUPPLES) 
# #     'family': {'partner':{
# #         'first_name': 'Lior', 
# #         'last_name': 'Alon', 
# #         'age': 50
# #         },




# # 'sports': ['volleyball', 'soccer']
# #         },
# #     }
# # }
# # #print(user_a['first_name'])
# # #print(user_a['hobbies'][1])
# # #print(user_a['pets'][2][0])

# # # for pet in user_a['pets']:
# # #     print(pet[0])

# # # print(user_a['family']['partner']['last_name'])
# # # print(user_a['family']['children']['sports'][0])
# # # print(user_a['family'])


# # user_a['first_name'] = 'John'

# # user_a['pets'][2][0] = 'Garfield_2'

# # print(user_a)


# rick_dict = {
#     'first_name':'Rick',
#     'last_name':'Sanchez'
# }
# print(rick_dict.items())
# print(rick_dict.keys())
# print(rick_dict.values())



# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"

# }
# keys_to_remove = ["name", "salary"]

# print(sample_dict)
# # del sample_dict['name']
# # del sample_dict['salary']

# for key in keys_to_remove:
#     del sample_dict[key]

# print(sample_dict)


# for item in enumerate('abcd'):
#     print(item)


# for (index_count, letter) in enumerate('abcd'):
#     print('At index {} the letter is {}'.format(index_count, letter))

# list1 = [1,2,3]
# list2 = ['a','b','c']
# list3 = [1.1, 2.2, 3.3, 4.4, 5.5]

# for item in zip(list1, list2, list3): # only go as far it is possible
#     print(item)

# for i in range(1, 3):
#     print(i)
# else:
#     print('The for loop is over')


# x = 0
# while x < 2:
#     print(f'x is {x}')
#     x += 1
# else:
#     print('x is bigger than 2')


# for letter in 'Leonardo':
#     if letter == 'a':
#         break
#     print(letter, end='') # end='' renders each letter next to the other


# while True:
#     s = input('Enter something : ')
#     if s == 'quit':
#         break
#     print('Length of the string is', len(s))
# print('Done')

# for letter in 'Leonardo':
#     if letter == 'o':
#         continue
#     print(letter, end='') # dont execute for 'o' letter
# # >> Lenard

# while True:
#     s = input('Enter something : ')
#     if s == 'quit':
#         break
#     if len(s) < 3:
#         print('Too small')
#         continue
#     print('Input is of sufficient length')


# for item in [1,2,3]:
#     # comment
#     pass # to avoid the error

# print('Finish the script')


# my_number = '1234'
# my_list = []

# my_list = [num for num in my_number]
# print(my_list)


# # A. The basic way of appending an element into a list
# my_number = '1234'
# my_list = []

# for num in my_number:
#     my_list.append(num)
# print(my_list)

# >> ['1', '2', '3', '4']

# # B. The list comprehension way
# my_number = '1234'
# my_list = []

# my_list = [num for num in my_number]
# print(my_list)

# >> ['1', '2', '3', '4']


# C. The basic way of appending an element into a list with Nested Loop
# my_list = []

# for i in [2, 3, 4]:
#     for j in [100, 200, 300]:
#         my_list.append(i*j)

# print(my_list)

# >> [200, 400, 600, 300, 600, 900, 400, 800, 1200]


# D. The list comprehension way
# my_list = []
# my_list = [(i*j) for i in [2, 3, 4] for j in [100, 200, 300]]
# print(my_list)

# >> [200, 400, 600, 300, 600, 900, 400, 800, 1200]

# # E. Dictionary comprehension
# # dictionary = {key: value for var in iterable}
# family_age = {'Lea': 12, 'Mark': 25, 'George': 50}

# new_year = 1

# new_family_age = {name: age+new_year for (name, age) in family_age.items()}

# print(new_family_age)

# #>> {'Lea': 13, 'Mark': 26, 'George': 51}


