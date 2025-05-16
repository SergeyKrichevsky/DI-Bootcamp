# SEQUENCES AND COLLECTIONS IN PYTHON 
# Collections - (list, tupples, dictioneries)
# orginizing, storing and retrieving data

## dtring method:
# temp_str += char #adds char to the end of the string

# LISTS
# USE CASES: to store and organize data that can be changed, ordered by undex.
# The most "flexible callection

# creating a list - [] aquare brackets

# methods
# append()
# extand()
# remove()
# pop()
# sort()

# methods that creates a new list
# sorted()
# split()

#ex"
# tasks = input('enter a task seperated by coma: ')
# task_list = tasks.split(', ')
# print(task_list)

list_1 = [1,2,3,4,5]
list_2 = [6,7,8,9,10]

list_3 = [list_1, list_2]
print(list_3)

list_3 = [*list_1, *list_2] # - UnPacking the list
print(list_3)


# TUPPLES
# # creating a tupple - () round brackets - minimum 2 elements!

# use cases:
# useful if you want to store info that should`nt be change: 
# password list,adresses, coordinates, id numbers

# can easily access (by index)

x, y =(4, 6)

coorinates = (x, y)
print(coorinates)
print(coorinates[1])

adresses = ("Haifa", 'TLV', 'Ramat Gan')
print(adresses)
      
      
# SETS
# неупорядоченная коллекция уникальных элементов
# ❌ Не допускает дубликатов (если попытаться добавить повторяющийся элемент — он будет проигнорирован)
# ❌ Неупорядоченное — порядок элементов не гарантирован и может меняться
# ❌ Не индексируется — нельзя получить элемент по индексу, как в списке
# ✅ Главное: хранит только уникальные элементы и не гарантирует порядок

# use cases: useful for data that you don`t want to have duplicated (IDs...)
# finding a common element between different collections

fruits = {'apple', 'banana', 'tomato', 'pineapple'}
vegitables = {'brocoli', 'carrot', 'potato', 'tomato'} 

common = fruits.intersection(vegitables)

# cammon = fruits.intercection(vegitables)
print(common)


# DICTIONARIES
# use cases: when we need logical assosiation between the data and the lable

# creating: {'a': X, 'b': y}

users = {"alice": {"age": 25, "email": ["alice@example.com", "alice@gmail.com"]},
         "bob": {"age": 30, "email": "bob@example.com"}}


users.update({'John': {"age": 20, "email": "john@example.com"}})
print(users)

print(users['bob']['email'])
print(users['alice']['email'][1])


twoD_list = [['', '', ''],
             ['', '', ''],
             ['', '', '']]

twoD_list[0][0] = 'x'
print(twoD_list[0][0])


