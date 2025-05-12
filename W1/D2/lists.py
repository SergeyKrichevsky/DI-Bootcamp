
#LISTS

#A list is a siquence of elements

#Syntax
#some_list = list('item 1') #to convert other qequance into list
#['i', 't', 'e', 'm', ' ', '1']
#other_list = ['item 1'] #the best way to create an empty list
#['item 1']
#print(some_list)
#print(other_list)

#print(len(some_list))

#print(some_list[1])

#my_list = []

#methods for list
#my_list.append('A')
#print(my_list)

#my_list.extend(['B', 'C', 'D'])
#print(my_list)

#create an empty list called names and add 4 names of your favorite characters 
#of some show

#names = []
#names.append('Dovakin')
#print(names)
#names.append('Alduin')
#print(names)
#names.extend(['Jarl', 'Ulrich', 'Astrid'])
#print(names)

num_list = list(range(1,8))
print(num_list)
print(num_list[2:6])
print(num_list[:6])

copied_list = num_list[:]
print(copied_list)

copied_list = num_list.copy()
print(copied_list)

#other methods:
#  - insert(where, what)
#  - remove(wahat) removes the first occurence of the element
# -  deliting some element:

del num_list[3]
print(num_list)

#pop() by default deletes (takes out) the last element
poped_el = num_list.pop()
print(num_list)
print(poped_el)

# sorted() - create new list - sort in order
fruits = ['Banana', 'orange', 'lime', 'apple']
sorted_fruits = sorted(fruits)
print(sorted_fruits)
print(fruits)
# sort() - change the original list
fruits.sort()
print(fruits)

# index(element) - returns you the index of it`s element
list = [5, 10, 15, 20, 25, 50, 20] 
# find the value 20 in the list if it`s present, replace it with 200.
# only the first
# use index method

#print(list)
#index_20 = list.index(20)
#list.insert(index_20, 200)
#print(f'New updated list:', list)

if 20 in list:
    inex_found = list.index(20)
    list.insert(inex_found, 200)
    list.remove(20)
    print(list)
else:
    print('element not found')

