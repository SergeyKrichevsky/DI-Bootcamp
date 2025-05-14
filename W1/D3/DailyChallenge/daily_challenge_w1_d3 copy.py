#CH1

user_word = input('Enter a word ')
chars_dictionary = {}

for index, char in enumerate(user_word):
    if char in chars_dictionary:
        chars_dictionary[char].append(index)
    else:
        chars_dictionary[char] = [index]

print(chars_dictionary)

#better way:

user_word = input('Enter a word ')
chars_dictionary = {}

for index, char in enumerate(user_word):
    if char in chars_dictionary:
        chars_dictionary[char].append(index)
    else:
        chars_dictionary.update({char : [index]})
        # chars_dictionary[char] = [index]

print(chars_dictionary)

#CH2



items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet = "$300"

# Aditional examples of 'items_purchase':

# items_purchase = {"Apple": "$4", "Honey": "$3", "Fan": "$14", "Bananas": "$4", "Pan": "$100", "Spoon": "$2"}
# wallet = "$100"

# items_purchase = {"Phone": "$999", "Speakers": "$300", "Laptop": "$5,000", "PC": "$1200"}
# wallet = "$1"


import re

for key, value in items_purchase.items():
    clean_value = re.sub(r'\D', '', value)
    items_purchase[key] = int(clean_value)

wallet = int(re.sub(r'\D', '', wallet))
# clean_wallet = int(re.sub(r'\D', '', wallet))

affordable_list = []
for key, value in items_purchase.items():
    if value <= wallet:
        affordable_list.append(key)

affordable_list = sorted(affordable_list)

if affordable_list:
    print(affordable_list)
else:
    print('Nothing')









# import re

# items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}

# for key, value in items_purchase.items():
#     clean_value = re.sub(r'\D', '', value)
#     items_purchase[key] = int(clean_value)

# print(items_purchase)
