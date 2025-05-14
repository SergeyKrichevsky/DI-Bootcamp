#CH1 (of week1 day 3)
# 3. Expected Output:

# For the input “dodo”, the output should be: {"d": [0, 2], "o": [1, 3]}.
# For the input “froggy”, the output should be: {"f": [0], "r": [1], "o": [2], "g": [3, 4], "y": [5]}.
# For the input “grapes”, the output should be: {"g": [0], "r": [1], "a": [2], "p": [3], "e": [4], "s": [5]}.


# user_word = input('enter a word ')
# user_word = 'dodo'

# out_dict = {}
# for char in user_word:
#     out_dict.update({char : })


# user_word = input('Enter a word ')
# chars_dictionary = {}

# for index, char in enumerate(user_word):
#     if char in chars_dictionary:
#         chars_dictionary[char].append(index)
#     else:
#         chars_dictionary.update({char : [index]})
#         # chars_dictionary[char] = [index]

# print(chars_dictionary)



# user_word = input('Enter a word ')
# chars_dictionary = {}

# for index, char in enumerate(user_word):
#     if char in chars_dictionary:
#         chars_dictionary[char].append(index)
#     else:
#         chars_dictionary.update({char : [index]})
#         # chars_dictionary[char] = [index]

# print(chars_dictionary)


#CH2

items_purchase = {"Water": "$1"
                  , "Bread": "$3"
                  , "TV": "$1,000"
                  , "Fertilizer": "$20"}

wallet = "$300"
basquet = []

# Aditional examples of 'items_purchase':

# items_purchase = {"Apple": "$4", "Honey": "$3", "Fan": "$14", "Bananas": "$4", "Pan": "$100", "Spoon": "$2"}
# wallet = "$100"

# items_purchase = {"Phone": "$999", "Speakers": "$300", "Laptop": "$5,000", "PC": "$1200"}
# wallet = "$1"

wallet = int(wallet.replace('$', '').replace(',', ''))

for item_name, price in items_purchase.items():
    price = int(price.replace('$', '').replace(',', ''))
    #print(price)
    price = int(price)

    if price < wallet:
        basquet.append(item_name)
    else:
        continue
        
if basquet:
    basquet = sorted(basquet)
    print(basquet)
else:
    print("Nothing")

    