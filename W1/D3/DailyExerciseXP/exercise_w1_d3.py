#EX1

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

new_dictionary = {}
#print(new_dictionary)

for key, value in zip(keys, values):
    new_dictionary[key] = value

print(new_dictionary)


#EX2

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
#print(family)

ticket_price_infant = 0
ticket_price_child = 10
ticket_price_adult = 15

ticket_prices_by_name ={}
total_cost = 0

for name, age in family.items():
    if age < 3:
        price = ticket_price_infant
    elif age <= 12:
        price = ticket_price_child
    else:
        price = ticket_price_adult
    
    ticket_prices_by_name[name] = f'- ${price}'
    total_cost += price

for name, price in ticket_prices_by_name.items():
    print(f'{name} {price}')

print(f'Total cost: ${total_cost}')


#EX2 (Bonus)

family = {}

def get_valid_age(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

#family[input('Wat is your name? ')] = int(input('Wat is your age? '))
name = input("What is your name? ")
age = get_valid_age("Wat is your age? ")

family[name] = age

while True:
    name = input('Anyone Else ? - Print Their name (leave empty to stop) ')
    if name == '':
        break
    age = get_valid_age(f"What is {name}'s age? ")
    family[name] = age

#print(family)


ticket_price_infant = 0
ticket_price_child = 10
ticket_price_adult = 15

ticket_prices_by_name ={}
total_cost = 0

for name, age in family.items():
    if age < 3:
        price = ticket_price_infant
    elif age <= 12:
        price = ticket_price_child
    else:
        price = ticket_price_adult
    
    ticket_prices_by_name[name] = f'- ${price}'
    total_cost += price

print("\nTicket Summary:")

for name, price in ticket_prices_by_name.items():
    print(f'{name} {price}')

print(f'Total cost: ${total_cost}')




#EX3

brand = {
    'name': 'Zara',
    'creation_date': 1975,
    'creator_name': 'Amancio Ortega Gaona',
    'type_of_clothes': ['men', 'women', 'children', 'home'],
    'international_competitors': ['Gap', 'H&M', 'Benetton'],
    'number_stores': 7000,
    'major_color': {
        'France': 'blue',
        'Spain': 'red',
        'US': ['pink', 'green']
    }
}
print(brand)

brand['number_stores'] = 2

print(f'\nOur clients are: {brand["type_of_clothes"]}')

brand['country_creation'] = 'Spain'

if "international_competitors" in brand:
    brand['international_competitors'].append('Desigual')

brand.pop('creation_date')

print(brand['international_competitors'][-1])

print(brand['major_color']['US'])

print(len(brand))

for key in brand:
    print(key)


#EX3 Bonus:

brand = {
    'name': 'Zara',
    'creation_date': 1975,
    'creator_name': 'Amancio Ortega Gaona',
    'type_of_clothes': ['men', 'women', 'children', 'home'],
    'international_competitors': ['Gap', 'H&M', 'Benetton'],
    'number_stores': 7000,
    'major_color': {
        'France': 'blue',
        'Spain': 'red',
        'US': ['pink', 'green']
    }
}

more_on_zara  = {
    'creation_date': 1975,
    'number_stores': 10000
}

brand.update(more_on_zara)

print('\n')
print(brand)


#EX4

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]


characters_to_indices = {}

for name in users:
    characters_to_indices[name] = users.index(name)

print(characters_to_indices)



indices_to_characters = {}

for name in users:
    indices_to_characters[users.index(name)] = name

print(indices_to_characters)



alphabetically_mapped_to_indices = {}
sorted_users = sorted(users)

for name in sorted_users:
    alphabetically_mapped_to_indices[name] = sorted_users.index(name)

#print(sorted_users)
print(alphabetically_mapped_to_indices)


#EX 4 (Other Method)

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

characters_to_indices = {}
indices_to_characters = {}
alphabetically_mapped_to_indices = {}

for index, name in enumerate(users):
    characters_to_indices[name] = index
print(characters_to_indices)

for index, name in enumerate(users):
    indices_to_characters[index] = name
print(indices_to_characters)


sorted_users = sorted(users)
for index, name in enumerate(sorted_users):
    alphabetically_mapped_to_indices[name] = index
print(alphabetically_mapped_to_indices)


